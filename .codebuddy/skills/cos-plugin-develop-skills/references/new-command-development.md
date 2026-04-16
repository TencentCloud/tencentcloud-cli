# Skill：新命令开发完整流程

## 概述

本 Skill 描述在 tccli cos 插件中开发一个新命令（action）的完整步骤。根据命令类型选择对应模板。

---

## Step 1：确定命令类型

根据命令特征选择模板：

| 类型 | 特征 | 参考命令文件 |
|---|---|---|
| **简单操作** | 单次 SDK 调用，无文件传输，无进度监控 | `create_bucket.py`, `signurl_object.py`, `head_object.py` |
| **单文件传输** | 单文件上传/下载，需进度监控 + 重试 | `upload_object.py`（单文件分支）、`download_object.py`（单文件分支） |
| **批量传输** | 多文件并发传输，需 ThreadPoolExecutor + 进度监控 | `upload_object.py`（recursive 分支）、`sync_upload_object.py` |
| **三元组命令** | get/put/delete 三个函数写在同一文件 | `tagging_object.py`、`acl_object.py` |

---

## Step 2：创建命令实现文件

在 `tccli/plugins/cos/` 下创建 `<command_name>.py`，按固定结构编写。

### Skill 1：简单操作模板（以 head 为例）

```python
# -*- coding: utf-8 -*-
"""
head 操作：查询 COS 对象元信息
对齐 coscli stat 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client


def head_object(args, parsed_globals):
    """查询 COS 对象元信息"""
    client, region = init_cos_client(parsed_globals)

    # ① 读取必填参数（直接用 []）
    bucket = args["bucket"]
    cos_key = args["cos_key"]
    # ② 读取可选参数（用 .get() or default 防止 None）
    version_id = args.get("version_id", "") or ""

    try:
        kwargs = {"Bucket": bucket, "Key": cos_key}
        if version_id:
            kwargs["VersionId"] = version_id

        response = client.head_object(**kwargs)

        print("Content-Type: %s" % response.get("Content-Type", ""))
        print("Content-Length: %s" % response.get("Content-Length", ""))
        print("Last-Modified: %s" % response.get("Last-Modified", ""))
        print("ETag: %s" % response.get("ETag", ""))

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
    except Exception as e:
        print("Error: %s" % str(e))
```

### Skill 2：单文件传输模板（以 upload 单文件为例）

```python
# -*- coding: utf-8 -*-
"""
upload 操作：上传本地文件到 COS
对齐 coscli cp (本地->COS) 命令
- thread_num: 单文件分块上传并发线程数（传给 SDK 的 MAXThread）
"""
import os
from qcloud_cos import CosServiceError
from .utils import init_cos_client, TransferProgressMonitor


def _upload_single(client, bucket, local_path, cos_key,
                   thread_num, part_size, rate_limiting, retry=3, log_file=""):
    """上传单个文件"""
    file_size = os.path.getsize(local_path)
    monitor = TransferProgressMonitor("upload")
    monitor.set_scan_info(1, file_size)
    monitor.start()

    progress_cb, file_id = monitor.create_progress_callback(file_size)
    last_err = None
    for attempt in range(max(1, retry + 1)):
        try:
            kwargs = {
                "Bucket": bucket,
                "LocalFilePath": local_path,
                "Key": cos_key,
                "PartSize": part_size,
                "MAXThread": thread_num,
                "progress_callback": progress_cb,
            }
            if rate_limiting:
                kwargs["TrafficLimit"] = str(int(rate_limiting) * 1024 * 1024 * 8)
            client.upload_file(**kwargs)
            monitor.update_ok(file_size, file_id)
            last_err = None
            break
        except CosServiceError as e:
            last_err = e
            if attempt < retry:
                # 重试前必须重置 progress_callback，避免进度累加错误
                progress_cb, file_id = monitor.create_progress_callback(file_size)

    if last_err is not None:
        err_reason = "%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code())
        monitor.update_err(file_id,
                           src_path=local_path,
                           dest_path="cos://%s/%s" % (bucket, cos_key),
                           reason=err_reason,
                           request_id=last_err.get_request_id())
    monitor.stop(log_file=log_file)
    if last_err is not None:
        raise last_err
```

### Skill 3：批量传输模板（以 sync_upload 为例）

```python
# -*- coding: utf-8 -*-
"""
sync_upload 操作：本地 -> COS 同步上传
对齐 coscli sync (本地->COS) 命令
- thread_num: 单文件分块上传并发线程数（传给 SDK 的 MAXThread）
- routines: 文件间并发数（同时上传的文件数）
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from qcloud_cos import CosServiceError
from .utils import (init_cos_client, match_filters, build_cos_key,
                    list_all_objects, list_local_files, TransferProgressMonitor)


def sync_upload_object(args, parsed_globals):
    """同步上传：本地目录 -> COS"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    local_path = args["local_path"]
    cos_prefix = args.get("cos_key", "") or ""
    include = args.get("include", "") or ""
    exclude = args.get("exclude", "") or ""
    routines = args.get("routines", 3) or 3
    retry = args.get("retry", 3)
    if retry is None:
        retry = 3
    retry = int(retry)
    log_file = args.get("log_file", "") or ""

    try:
        if not os.path.isdir(local_path):
            print("Error: 本地路径不是目录: %s" % local_path)
            return

        # 1. 扫描阶段：收集任务列表，使用 match_filters 过滤
        local_files = list_local_files(local_path)
        cos_objects = list_all_objects(client, bucket, cos_prefix)

        monitor = TransferProgressMonitor("upload")
        monitor.start()

        tasks = []
        total_size = 0
        skip_count = 0
        skip_size = 0
        for rel_path, file_info in local_files.items():
            if not match_filters(rel_path, include, exclude):
                skip_count += 1
                continue
            cos_key = build_cos_key(cos_prefix, rel_path)
            # 增量同步：大小一致则跳过
            if cos_key in cos_objects and cos_objects[cos_key]["Size"] == file_info["Size"]:
                skip_count += 1
                skip_size += file_info["Size"]
                continue
            total_size += file_info["Size"]
            tasks.append((file_info, cos_key))

        monitor.set_scan_info(len(tasks) + skip_count, total_size + skip_size)
        for _ in range(skip_count):
            monitor.update_skip(skip_size // skip_count if skip_count > 0 else 0)

        # 2. 定义单任务执行函数（含重试）
        def _do_upload(file_info, cos_key):
            last_err = None
            progress_cb, file_id = monitor.create_progress_callback(file_info["Size"])
            for attempt in range(max(1, retry + 1)):
                try:
                    client.upload_file(
                        Bucket=bucket,
                        LocalFilePath=file_info["FullPath"],
                        Key=cos_key,
                        progress_callback=progress_cb,
                    )
                    monitor.update_ok(file_info["Size"], file_id)
                    last_err = None
                    break
                except CosServiceError as e:
                    last_err = e
                    if attempt < retry:
                        progress_cb, file_id = monitor.create_progress_callback(file_info["Size"])
            if last_err is not None:
                monitor.update_err(file_id,
                                   src_path=file_info["FullPath"],
                                   dest_path="cos://%s/%s" % (bucket, cos_key),
                                   reason="%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code()),
                                   request_id=last_err.get_request_id())

        # 3. 线程池并发执行，routines 控制文件间并发
        if tasks:
            max_workers = min(routines, len(tasks))
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = [executor.submit(_do_upload, fi, ck) for fi, ck in tasks]
                for future in as_completed(futures):
                    future.result()

        # 4. 停止进度监控
        monitor.stop(log_file=log_file)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
    except Exception as e:
        print("Error: %s" % str(e))
```

### Skill 4：三元组命令模板（以 tagging 为例）

将 get/put/delete 三个函数写在同一文件，共用 `init_cos_client`：

```python
# -*- coding: utf-8 -*-
"""
tagging 操作：获取/设置/删除对象标签
对齐 coscli get/put/delete object tagging 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client


def get_object_tagging(args, parsed_globals):
    """获取对象标签"""
    client, region = init_cos_client(parsed_globals)
    bucket = args["bucket"]
    cos_key = args["cos_key"]
    try:
        response = client.get_object_tagging(Bucket=bucket, Key=cos_key)
        tags = response.get("TagSet", {}).get("Tag", [])
        if not isinstance(tags, list):
            tags = [tags]
        print("对象标签: cos://%s/%s" % (bucket, cos_key))
        print("-" * 50)
        for tag in tags:
            print("  %s = %s" % (tag.get("Key", ""), tag.get("Value", "")))
    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))


def put_object_tagging(args, parsed_globals):
    """设置对象标签"""
    client, region = init_cos_client(parsed_globals)
    bucket = args["bucket"]
    cos_key = args["cos_key"]
    tags_str = args["tags"]
    try:
        tag_list = []
        for pair in tags_str.split(","):
            pair = pair.strip()
            if "=" in pair:
                k, v = pair.split("=", 1)
                tag_list.append({"Key": k.strip(), "Value": v.strip()})
        client.put_object_tagging(
            Bucket=bucket, Key=cos_key,
            Tagging={"TagSet": {"Tag": tag_list}},
        )
        print("标签设置成功: cos://%s/%s" % (bucket, cos_key))
    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))


def delete_object_tagging(args, parsed_globals):
    """删除对象标签"""
    client, region = init_cos_client(parsed_globals)
    bucket = args["bucket"]
    cos_key = args["cos_key"]
    try:
        client.delete_object_tagging(Bucket=bucket, Key=cos_key)
        print("标签删除成功: cos://%s/%s" % (bucket, cos_key))
    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
```

在 `__init__.py` 中分别 import 三个函数：

```python
from .tagging_object import get_object_tagging, put_object_tagging, delete_object_tagging
```

---

## Step 3：在 `__init__.py` 中注册命令

### 3.1 顶部添加 import

```python
# 简单命令（一个文件一个函数）
from .head_object import head_object

# 三元组命令（同一文件多个函数）
from .tagging_object import get_object_tagging, put_object_tagging, delete_object_tagging
```

### 3.2 在 `_spec["actions"]` 中添加 action

```python
"actions": {
    # ... 已有命令 ...
    "head": {
        "name": "查询对象元信息",
        "document": "查询 COS 对象的元数据信息，包括大小、类型、修改时间、ETag 等",
        "input": "headRequest",
        "output": "headResponse",
        "action_caller": head_object,
    },
    # 三元组命令分别注册
    "get_object_tagging": {
        "name": "获取对象标签",
        "document": "获取 COS 对象的标签信息",
        "input": "getObjectTaggingRequest",
        "output": "getObjectTaggingResponse",
        "action_caller": get_object_tagging,
    },
    "put_object_tagging": {
        "name": "设置对象标签",
        "document": "设置 COS 对象的标签",
        "input": "putObjectTaggingRequest",
        "output": "putObjectTaggingResponse",
        "action_caller": put_object_tagging,
    },
    "delete_object_tagging": {
        "name": "删除对象标签",
        "document": "删除 COS 对象的标签",
        "input": "deleteObjectTaggingRequest",
        "output": "deleteObjectTaggingResponse",
        "action_caller": delete_object_tagging,
    },
}
```

### 3.3 在 `_spec["objects"]` 中添加 Request/Response 定义

```python
"objects": {
    # ... 已有对象 ...
    "headRequest": {
        "members": [
            {"name": "bucket", "member": "string", "type": "string", "required": True,
             "document": "存储桶名称，格式如 my-bucket-1250000000"},
            {"name": "cos_key", "member": "string", "type": "string", "required": True,
             "document": "要查询的对象键（Key）"},
            {"name": "version_id", "member": "string", "type": "string", "required": False,
             "document": "指定查询的对象版本 ID（开启版本控制时使用）"},
        ],
    },
    "headResponse": {
        "members": [],   # 统一为空列表，输出由函数自行 print
    },
}
```

### 3.4 `_spec` 参数类型规范

| 参数类型 | `"type"` 值 | 说明 |
|---|---|---|
| 字符串 | `"string"` | 最常用 |
| 整数 | `"integer"` | 如 `thread_num`、`routines` |
| 布尔值 | `"boolean"` | 如 `recursive`、`force` |
| 浮点数 | `"float"` | 如 `rate_limiting` |

**注意**：以下全局参数由 tccli 框架自动注入，**禁止**在 `_spec["objects"]` 中声明：
`secretId`、`secretKey`、`token`、`region`、`endpoint`、`profile`

---

## Step 4：编写单元测试

**核心原则：**
1. **只 mock `qcloud_cos` SDK 方法和 `init_cos_client`**，禁止产生真实的外部服务调用
2. `utils.match_filters`、`utils.build_cos_key` 等纯逻辑函数**不需要 mock**，让其正常执行
3. 每个命令必须覆盖：参数缺失、SDK 调用失败、成功路径、各重要参数组合

### 测试文件结构

```python
# tests/test_cos_plugin.py
import pytest
from unittest.mock import patch, MagicMock
from tccli.plugins.cos.head_object import head_object

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
    def test_head_success(self, mock_init_client):
        """成功获取对象元信息"""
        mock_client = MagicMock()
        mock_init_client.return_value = (mock_client, "ap-guangzhou")
        mock_client.head_object.return_value = {
            "Content-Length": "1024",
            "Content-Type": "text/plain",
        }
        args = {"bucket": "test-bucket-1250000000", "cos_key": "test/file.txt"}
        head_object(args, MOCK_GLOBALS)
        mock_client.head_object.assert_called_once_with(
            Bucket="test-bucket-1250000000",
            Key="test/file.txt",
        )

    @patch("tccli.plugins.cos.head_object.init_cos_client")
    def test_head_with_version_id(self, mock_init_client):
        """带 version_id 可选参数"""
        mock_client = MagicMock()
        mock_init_client.return_value = (mock_client, "ap-guangzhou")
        mock_client.head_object.return_value = {"Content-Length": "1024"}
        args = {"bucket": "test-bucket-1250000000", "cos_key": "test/file.txt",
                "version_id": "v1234"}
        head_object(args, MOCK_GLOBALS)
        mock_client.head_object.assert_called_once_with(
            Bucket="test-bucket-1250000000",
            Key="test/file.txt",
            VersionId="v1234",
        )

    @patch("tccli.plugins.cos.head_object.init_cos_client")
    def test_head_sdk_error(self, mock_init_client):
        """SDK 调用失败，错误通过 print 输出，不抛出异常"""
        from qcloud_cos import CosServiceError
        mock_client = MagicMock()
        mock_init_client.return_value = (mock_client, "ap-guangzhou")
        mock_client.head_object.side_effect = CosServiceError(
            "GET", "NoSuchKey", 404, "NoSuchKey", "Object not found", "req-123"
        )
        args = {"bucket": "test-bucket-1250000000", "cos_key": "not-exist.txt"}
        # 不应抛出异常，错误通过 print 输出
        head_object(args, MOCK_GLOBALS)
```

### 打桩边界原则

| 调用类型 | 是否 mock | 说明 |
|---|---|---|
| `qcloud_cos.CosS3Client` 的所有方法 | ✅ 必须 mock | 会产生真实 HTTP 请求 |
| `utils.init_cos_client` | ✅ 通常 mock | 避免真实凭据校验 |
| `utils.match_filters`、`utils.build_cos_key` 等纯逻辑函数 | ❌ 不 mock | 纯本地逻辑，正常执行 |
| `utils.list_all_objects`、`utils.list_local_files` | 视情况 | 若内部有 SDK 调用则 mock |

### 覆盖率要求

每个命令的测试用例必须覆盖以下所有分支：

| 分支类型 | 是否必须 |
|---|---|
| SDK 调用失败（CosServiceError） | ✅ |
| 成功路径 | ✅ |
| 各重要可选参数（version_id、storage_class 等） | ✅ |
| 本地路径不存在（传输命令） | ✅ |
| 重试逻辑（传输命令） | ✅ |

---

## Step 5：参数规范与错误处理

### 参数读取规范

```python
# ① 必填参数：直接用 []，缺失时由框架报错
bucket = args["bucket"]
cos_key = args["cos_key"]

# ② 可选参数：必须提供默认值并处理 None（用 or 运算符）
include = args.get("include", "") or ""
exclude = args.get("exclude", "") or ""
thread_num = args.get("thread_num", 5) or 5
routines = args.get("routines", 3) or 3
part_size = args.get("part_size", 20) or 20
rate_limiting = args.get("rate_limiting", 0) or 0
log_file = args.get("log_file", "") or ""

# ③ 数值型参数需显式 int() 转换（框架可能传入字符串）
retry = args.get("retry", 3)
if retry is None:
    retry = 3
retry = int(retry)
# 或简写：retry = int(args.get("retry", 3) or 3)
```

### 常用参数默认值

| 参数 | 默认值 | 说明 |
|---|---|---|
| `thread_num` | 5 | 单文件分片并发线程数 |
| `routines` | 3 | 文件间并发数 |
| `part_size` | 20 | 分片大小（MB） |
| `rate_limiting` | 0 | 限速（MB/s），0 不限速 |
| `retry` | 3 | 失败重试次数 |
| `recursive` | False | 是否递归操作 |
| `force` | False | 是否跳过确认 |
| `delete_extra` | False | 是否删除目标端多余文件 |

### 标准错误处理模式

```python
try:
    client.some_operation(...)
    print("操作成功: ...")
except CosServiceError as e:
    print("Error: %s (Code: %s, RequestId: %s)" % (
        e.get_error_msg(), e.get_error_code(), e.get_request_id()))
except Exception as e:
    print("Error: %s" % str(e))
```

---

## Step 6：验证

```bash
# 语法检查
python3 -c "import ast; ast.parse(open('tccli/plugins/cos/<command_name>.py').read())"

# 帮助文档验证
tccli cos <action_key> --help

# 实际调用测试
tccli cos <action_key> --bucket my-bucket-1250000000 --cos_key test/file.txt

# 运行单测
pytest tests/test_cos_plugin.py -v
```
