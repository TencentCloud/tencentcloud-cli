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
