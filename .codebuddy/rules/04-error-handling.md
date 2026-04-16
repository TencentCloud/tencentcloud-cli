---
type: always
---

# 规则：错误处理与输出规范

## 错误处理原则

**所有命令函数必须捕获 `CosServiceError` 和 `Exception`，通过 `print()` 输出错误信息，不得让异常向上传播（除非是批量操作中的单文件失败）。**

## 标准错误处理模式

### 简单操作（单文件/单桶）

```python
try:
    client.some_operation(...)
    print("操作成功: ...")

except CosServiceError as e:
    # COS 服务错误：包含 HTTP 状态码、错误码、RequestId
    print("Error: %s (Code: %s, RequestId: %s)" % (
        e.get_error_msg(), e.get_error_code(), e.get_request_id()))
except Exception as e:
    # 其他异常：网络错误、本地文件错误、参数错误等
    print("Error: %s" % str(e))
```

### 批量操作（单文件失败不中断整体）

```python
def _do_upload(full_path, cos_key, file_size):
    last_err = None
    progress_cb, file_id = monitor.create_progress_callback(file_size)  # 必须在循环外初始化
    for attempt in range(max(1, retry + 1)):
        try:
            client.upload_file(..., progress_callback=progress_cb)
            monitor.update_ok(file_size, file_id)
            last_err = None
            break
        except CosServiceError as e:
            last_err = e
            if attempt < retry:
                progress_cb, file_id = monitor.create_progress_callback(file_size)  # 重试前重置

    if last_err is not None:
        # 记录失败，不抛出异常（不中断其他文件的传输）
        err_reason = "%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code())
        monitor.update_err(
            file_id,
            src_path=full_path,
            dest_path="cos://%s/%s" % (bucket, cos_key),
            reason=err_reason,
            request_id=last_err.get_request_id()
        )
```

## CosServiceError 方法

| 方法 | 说明 | 示例输出 |
|---|---|---|
| `e.get_error_msg()` | 错误描述 | `"NoSuchBucket"` |
| `e.get_error_code()` | 错误码 | `"NoSuchBucket"` |
| `e.get_request_id()` | 请求 ID | `"NjYxMjM0NTY..."` |
| `e.get_status_code()` | HTTP 状态码 | `404` |

## 输出规范

### 成功输出

```python
# 简单操作成功
print("存储桶创建成功: %s (Region: %s, ACL: %s)" % (bucket, region, acl))
print("删除成功: cos://%s/%s" % (bucket, cos_key))
print("预签名 URL: %s" % url)

# 批量操作成功（由 monitor.stop() 自动输出）
# Succeed: Total num: 10, size: 100.00 MB. OK num: 10, OK size: 100.00 MB, Progress: 100.0%
# AvgSpeed: 10.00 MB/s, Elapsed: 10.0s
```

### 错误输出

```python
# 标准错误格式（必须包含 Code 和 RequestId）
print("Error: %s (Code: %s, RequestId: %s)" % (
    e.get_error_msg(), e.get_error_code(), e.get_request_id()))

# 参数错误（本地路径不存在等）
print("Error: 本地文件不存在: %s" % local_path)
print("Error: 指定路径不是文件: %s（如需上传目录请使用 --recursive true）" % local_path)
```

## 参数校验规范

在调用 COS SDK 之前，必须校验本地路径的有效性：

```python
# 上传时校验本地路径
if recursive and os.path.isdir(local_path):
    _upload_directory(...)
else:
    if not os.path.exists(local_path):
        print("Error: 本地文件不存在: %s" % local_path)
        return
    if not os.path.isfile(local_path):
        print("Error: 指定路径不是文件: %s（如需上传目录请使用 --recursive true）" % local_path)
        return
    _upload_single(...)

# 同步上传时校验本地路径是目录
if not os.path.isdir(local_path):
    print("Error: 本地路径不是目录: %s" % local_path)
    return
```

## 删除操作的确认提示

递归删除时，非 `force` 模式下必须提示用户确认：

```python
if not force:
    print("即将删除 %d 个对象（文件: %d，文件夹: %d，前缀: cos://%s/%s）" % (
        total_count, len(file_keys), len(dir_keys), bucket, prefix))
    print("提示: 使用 --force true 跳过确认")
    try:
        confirm = input("确认删除? (y/N): ").strip().lower()
        if confirm != "y":
            print("已取消删除")
            return
    except (EOFError, KeyboardInterrupt):
        print("\n已取消删除")
        return
```

## 禁止的错误处理方式

```python
# ❌ 禁止：使用 sys.exit() 退出
import sys
sys.exit(1)

# ❌ 禁止：使用 raise 向上传播（简单操作中）
raise CosServiceError(...)

# ❌ 禁止：静默忽略错误
try:
    client.some_operation(...)
except:
    pass  # 禁止

# ❌ 禁止：使用 logging 模块（应使用 print）
import logging
logging.error("...")  # 禁止
```

---

# 规则：单元测试规范

## 测试框架

```python
import pytest
from unittest.mock import patch, MagicMock
```

## 核心原则

1. **只 mock `qcloud_cos` SDK 方法和 `init_cos_client`**，禁止产生真实的外部服务调用
2. `utils.match_filters`、`utils.build_cos_key` 等纯逻辑函数**不需要 mock**，让其正常执行
3. 每个命令必须覆盖：SDK 调用失败、成功路径、各重要参数组合

## 标准测试结构

```python
# 标准测试全局参数（不依赖真实凭据）
MOCK_GLOBALS = {
    "secretId": "test-secret-id",
    "secretKey": "test-secret-key",
    "token": None,
    "region": "ap-guangzhou",
    "endpoint": None,
    "profile": "default",
}


class TestHeadObject:

    @patch("tccli.plugins.cos.head_object.init_cos_client")
    def test_success(self, mock_init_client):
        """成功路径"""
        mock_client = MagicMock()
        mock_init_client.return_value = (mock_client, "ap-guangzhou")
        mock_client.head_object.return_value = {"Content-Length": "1024"}
        args = {"bucket": "test-bucket-1250000000", "cos_key": "test/file.txt"}
        head_object(args, MOCK_GLOBALS)
        mock_client.head_object.assert_called_once()

    @patch("tccli.plugins.cos.head_object.init_cos_client")
    def test_sdk_error(self, mock_init_client):
        """SDK 调用失败，不抛出异常"""
        from qcloud_cos import CosServiceError
        mock_client = MagicMock()
        mock_init_client.return_value = (mock_client, "ap-guangzhou")
        mock_client.head_object.side_effect = CosServiceError(
            "GET", "NoSuchKey", 404, "NoSuchKey", "Object not found", "req-123"
        )
        args = {"bucket": "test-bucket-1250000000", "cos_key": "not-exist.txt"}
        head_object(args, MOCK_GLOBALS)  # 不应抛出异常
```

## 打桩边界原则

| 调用类型 | 是否 mock | 说明 |
|---|---|---|
| `qcloud_cos.CosS3Client` 的所有方法 | ✅ 必须 mock | 会产生真实 HTTP 请求 |
| `utils.init_cos_client` | ✅ 通常 mock | 避免真实凭据校验 |
| `utils.match_filters`、`utils.build_cos_key` 等纯逻辑函数 | ❌ 不 mock | 纯本地逻辑，正常执行 |
| `utils.list_all_objects`、`utils.list_local_files` | 视情况 | 若内部有 SDK 调用则 mock |

## 覆盖率要求

每个命令的测试用例必须覆盖以下所有分支：

| 分支类型 | 是否必须 |
|---|---|
| SDK 调用失败（CosServiceError） | ✅ |
| 成功路径 | ✅ |
| 各重要可选参数（version_id、storage_class 等） | ✅ |
| 本地路径不存在（传输命令） | ✅ |
| 重试逻辑（传输命令） | ✅ |
