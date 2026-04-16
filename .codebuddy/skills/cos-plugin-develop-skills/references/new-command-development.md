# Skill：新命令开发完整流程

## 概述

本 Skill 描述在 tccli cos 插件中开发一个新命令（action）的完整步骤，以一个假设的 `head`（查询对象元信息）命令为例。

---

## Step 1：确定命令类型

根据命令特征选择模板：

| 类型 | 特征 | 参考命令文件 |
|---|---|---|
| **简单操作** | 单个对象，无批量，无进度监控 | `create_bucket.py`, `signurl_object.py`, `head_object.py` |
| **批量传输操作** | 多文件，需 TransferProgressMonitor + 线程池 | `upload_object.py`, `download_object.py`, `copy_object.py` |
| **同步操作** | 增量比较 + 批量传输 | `sync_upload_object.py`, `sync_download_object.py`, `sync_copy_object.py` |

---

## Step 2：创建命令文件

在 `tccli/plugins/cos/` 下创建 `<name>_object.py`（或 `<name>_bucket.py`），按固定结构编写：

### 简单操作模板（以 head 为例）

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

    bucket = args["bucket"]
    cos_key = args["cos_key"]
    version_id = args.get("version_id", "") or ""

    try:
        kwargs = {"Bucket": bucket, "Key": cos_key}
        if version_id:
            kwargs["VersionId"] = version_id

        response = client.head_object(**kwargs)

        # 输出结果
        print("Content-Type: %s" % response.get("Content-Type", ""))
        print("Content-Length: %s" % response.get("Content-Length", ""))
        print("Last-Modified: %s" % response.get("Last-Modified", ""))
        print("ETag: %s" % response.get("ETag", ""))

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
```

### 批量传输操作模板（以 upload 为例）

```python
# -*- coding: utf-8 -*-
"""
upload 操作：上传本地文件到 COS
"""
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from qcloud_cos import CosServiceError
from .utils import init_cos_client, match_filters, parse_meta, TransferProgressMonitor


def upload_object(args, parsed_globals):
    """上传本地文件到 COS"""
    client, region = init_cos_client(parsed_globals)

    # ① 读取所有参数（带默认值）
    bucket = args["bucket"]
    local_path = args["local_path"]
    cos_key = args["cos_key"]
    recursive = args.get("recursive", False)
    include = args.get("include", "") or ""
    exclude = args.get("exclude", "") or ""
    thread_num = args.get("thread_num", 5) or 5
    routines = args.get("routines", 3) or 3
    part_size = args.get("part_size", 20) or 20
    rate_limiting = args.get("rate_limiting", 0) or 0
    retry = int(args.get("retry", 3) or 3)
    log_file = args.get("log_file", "") or ""

    try:
        if recursive and os.path.isdir(local_path):
            _upload_directory(client, bucket, local_path, cos_key, include, exclude,
                              thread_num, routines, part_size, rate_limiting, retry, log_file)
        else:
            if not os.path.isfile(local_path):
                print("Error: 本地文件不存在或不是文件: %s" % local_path)
                return
            _upload_single(client, bucket, local_path, cos_key,
                           thread_num, part_size, rate_limiting, retry, log_file)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
    except Exception as e:
        print("Error: %s" % str(e))
```

---

## Step 3：在 `__init__.py` 中注册命令

### 3.1 导入函数

在 `__init__.py` 顶部的 import 区域添加：

```python
from .head_object import head_object
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
        "members": [],
    },
}
```

---

## Step 4：参数规范

### 必填参数（required: True）

- `bucket`：存储桶名称，格式如 `my-bucket-1250000000`
- 操作目标（`cos_key`、`local_path` 等）

### 可选参数（required: False）

- 过滤参数：`include`、`exclude`（支持通配符，如 `*.txt`）
- 并发参数：`thread_num`（单文件分片并发，默认 5）、`routines`（文件间并发，默认 3）
- 传输参数：`part_size`（分片大小 MB，默认 20）、`rate_limiting`（限速 MB/s，0 不限速）
- 重试参数：`retry`（失败重试次数，默认 3）
- 日志参数：`log_file`（失败日志文件路径）

### 参数读取规范

```python
# 所有可选参数必须提供默认值，并处理 None 的情况
thread_num = args.get("thread_num", 5) or 5
routines = args.get("routines", 3) or 3
# retry 两种等价写法均可：
retry = int(args.get("retry", 3) or 3)  # 简写形式
# 或展开形式：
# retry = args.get("retry", 3)
# if retry is None:
#     retry = 3
# retry = int(retry)
include = args.get("include", "") or ""
exclude = args.get("exclude", "") or ""
```

---

## Step 5：错误处理规范

### 标准错误处理模式

```python
try:
    # 业务逻辑
    client.some_operation(...)
    print("操作成功: ...")

except CosServiceError as e:
    # COS 服务错误（含 HTTP 状态码、错误码、RequestId）
    print("Error: %s (Code: %s, RequestId: %s)" % (
        e.get_error_msg(), e.get_error_code(), e.get_request_id()))
except Exception as e:
    # 其他异常（网络错误、本地文件错误等）
    print("Error: %s" % str(e))
```

### 批量操作错误记录

批量操作中，单个文件失败不中断整体流程，通过 `monitor.update_err()` 记录：

```python
except CosServiceError as e:
    err_reason = "%s (Code: %s)" % (e.get_error_msg(), e.get_error_code())
    monitor.update_err(
        src_path="cos://%s/%s" % (bucket, cos_key),
        dest_path=local_path,
        reason=err_reason,
        request_id=e.get_request_id()
    )
```

---

## Step 6：全局参数说明

以下全局参数由 tccli 框架自动注入到 `parsed_globals` 中，命令函数通过 `init_cos_client(parsed_globals)` 使用：

| 参数 | 说明 | 来源优先级 |
|---|---|---|
| `secretId` | 腾讯云 SecretId | 命令行 > 环境变量 > 配置文件 |
| `secretKey` | 腾讯云 SecretKey | 命令行 > 环境变量 > 配置文件 |
| `token` | 临时密钥 Token | 命令行 > 环境变量 > 配置文件 |
| `region` | 地域（如 ap-guangzhou） | 命令行 > 环境变量 > 配置文件 |
| `endpoint` | 自定义 endpoint | 命令行参数 |
| `profile` | 配置文件 profile 名 | 命令行参数，默认 "default" |

**注意**：命令函数的参数签名固定为 `def xxx(args, parsed_globals)`，不可更改。
