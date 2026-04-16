---
type: always
---

# 规则：项目结构与代码组织

## 目录职责

```
tccli/plugins/cos/
├── __init__.py          # 插件入口：_spec 定义（actions/objects）+ 所有函数 import
├── utils.py             # 工具模块：init_cos_client、TransferProgressMonitor、match_filters 等
├── upload_object.py     # 上传命令（单文件 + recursive 批量）
├── download_object.py   # 下载命令（单文件 + recursive 批量）
├── copy_object.py       # 复制命令（单文件 + recursive 批量）
├── move_object.py       # 移动命令（= copy + delete）
├── sync_upload_object.py    # 同步上传（增量比较 + 批量传输）
├── sync_download_object.py  # 同步下载
├── sync_copy_object.py      # 同步复制
├── delete_object.py     # 删除命令（单文件 + recursive 批量）
├── list_object.py       # 列出对象
├── head_object.py       # 查询对象元信息
├── acl_object.py        # ACL 操作（get/put）
├── tagging_object.py    # 标签操作（get/put/delete）
├── signurl_object.py    # 生成预签名 URL
├── create_bucket.py     # 创建存储桶
└── delete_bucket.py     # 删除存储桶
```

## 命令文件固定结构

每个 `tccli/plugins/cos/<name>.py` 文件必须按以下顺序组织：

```python
# -*- coding: utf-8 -*-
"""
<command> 操作：<一句话描述>
对齐 coscli <对应命令> 命令
"""
# 1. import 块
from qcloud_cos import CosServiceError
from .utils import init_cos_client  # 及其他需要的工具函数

# 2. 命令函数（签名固定）
def command_name(args, parsed_globals):
    """函数文档字符串"""
    client, region = init_cos_client(parsed_globals)
    # ① 读取必填参数
    # ② 读取可选参数（带默认值，处理 None）
    # ③ 参数校验（本地路径存在性等）
    # ④ 调用 COS SDK
    # ⑤ 输出结果

# 3. 私有辅助函数（可选，复杂逻辑抽取）
def _do_single_upload(...):
    ...
def _do_batch_upload(...):
    ...
```

## `__init__.py` 注册规范

### actions 定义

```python
"actions": {
    "<action_key>": {
        "name": "<命令中文名>",
        "document": "<命令描述>",
        "input": "<action_key>Request",
        "output": "<action_key>Response",
        "action_caller": <function_name>,  # 直接引用函数对象，不加引号
    },
}
```

### objects 定义

```python
"objects": {
    "<action_key>Request": {
        "members": [
            {"name": "bucket", "member": "string", "type": "string", "required": True,
             "document": "存储桶名称，格式如 my-bucket-1250000000"},
            {"name": "cos_key", "member": "string", "type": "string", "required": True,
             "document": "<参数说明>"},
            {"name": "optional_param", "member": "string", "type": "string", "required": False,
             "document": "<参数说明，包含默认值>"},
        ],
    },
    "<action_key>Response": {
        "members": [],   # 统一为空列表，输出由函数自行 print
    },
}
```

### 参数类型规范

| 参数类型 | `"type"` 值 | 示例 |
|---|---|---|
| 字符串 | `"string"` | `bucket`、`cos_key`、`include` |
| 整数 | `"integer"` | `thread_num`、`routines`、`part_size` |
| 布尔值 | `"boolean"` | `recursive`、`force`、`delete_extra` |
| 浮点数 | `"float"` | `rate_limiting` |

**禁止**在 `_spec["objects"]` 中声明以下全局参数（由 tccli 框架自动注入）：
`secretId`、`secretKey`、`token`、`region`、`endpoint`、`profile`

---

# 规则：客户端初始化与参数处理

## 客户端初始化规范

**所有命令函数必须通过 `init_cos_client(parsed_globals)` 初始化客户端**，禁止直接使用 `parsed_globals` 中的原始凭据构造 COS 客户端。

```python
# ✅ 正确
def upload_object(args, parsed_globals):
    client, region = init_cos_client(parsed_globals)

# ❌ 错误：直接使用原始凭据
def upload_object(args, parsed_globals):
    from qcloud_cos import CosConfig, CosS3Client
    config = CosConfig(SecretId=parsed_globals["secretId"], ...)  # 禁止
```

## 凭据优先级（由 parse_global_arg 自动处理）

```
命令行参数 > 环境变量 > tccli 配置文件（~/.tccli/<profile>.credential）
```

环境变量名：
- `TENCENTCLOUD_SECRET_ID`
- `TENCENTCLOUD_SECRET_KEY`
- `TENCENTCLOUD_TOKEN`
- `TENCENTCLOUD_REGION`

## 参数读取规范

### 必填参数

```python
# 直接通过 key 访问，缺失时会抛出 KeyError（由框架处理）
bucket = args["bucket"]
cos_key = args["cos_key"]
local_path = args["local_path"]
```

### 可选参数（必须提供默认值并处理 None）

```python
# ✅ 正确：提供默认值并处理 None（用 or 运算符）
recursive = args.get("recursive", False)
include = args.get("include", "") or ""
exclude = args.get("exclude", "") or ""
thread_num = args.get("thread_num", 5) or 5
routines = args.get("routines", 3) or 3
part_size = args.get("part_size", 20) or 20
rate_limiting = args.get("rate_limiting", 0) or 0
log_file = args.get("log_file", "") or ""

# retry 需要额外的 int() 转换（框架可能传入字符串），两种写法均可
retry = args.get("retry", 3)
if retry is None:
    retry = 3
retry = int(retry)
# 或简写为：
retry = int(args.get("retry", 3) or 3)

# ❌ 错误：不处理 None 的情况
thread_num = args.get("thread_num", 5)  # 若用户传入 None 会导致后续错误
```

## 常用参数默认值规范

| 参数 | 默认值 | 说明 |
|---|---|---|
| `thread_num` | 5 | 单文件分片并发线程数 |
| `routines` | 3 | 文件间并发数 |
| `part_size` | 20 | 分片大小（MB） |
| `rate_limiting` | 0 | 限速（MB/s），0 表示不限速 |
| `retry` | 3 | 失败重试次数 |
| `recursive` | False | 是否递归操作 |
| `force` | False | 是否跳过确认 |
| `delete_extra` | False | 是否删除目标端多余文件 |
| `include` | "" | 包含过滤模式 |
| `exclude` | "" | 排除过滤模式 |
| `log_file` | "" | 失败日志文件路径 |

## 限速参数转换

COS SDK 的 `TrafficLimit` 单位为 bit/s，需从 MB/s 转换：

```python
# ✅ 正确：MB/s → bit/s
if rate_limiting:
    kwargs["TrafficLimit"] = str(int(rate_limiting) * 1024 * 1024 * 8)
```

## 元数据参数解析

自定义元数据格式为 `key1=value1#key2=value2`，使用 `parse_meta()` 解析：

```python
from .utils import parse_meta

meta = args.get("meta", "") or ""
metadata = parse_meta(meta)
# 输出: {"x-cos-meta-key1": "value1", "x-cos-meta-key2": "value2"}

if metadata:
    kwargs["Metadata"] = metadata
```

## 存储类型参数

存储类型（`storage_class`）直接传给 COS SDK，有效值：

```
STANDARD          # 标准存储（默认）
STANDARD_IA       # 低频存储
ARCHIVE           # 归档存储
DEEP_ARCHIVE      # 深度归档存储
INTELLIGENT_TIERING  # 智能分层存储
MAZ_STANDARD      # 多 AZ 标准存储
MAZ_STANDARD_IA   # 多 AZ 低频存储
```

```python
storage_class = args.get("storage_class", "") or ""
if storage_class:
    kwargs["StorageClass"] = storage_class
```

## 版本控制参数

```python
version_id = args.get("version_id", "") or ""
if version_id:
    kwargs["VersionId"] = version_id
```

## 跨地域操作

复制/移动操作（copy/move/sync_copy）涉及跨地域时，`CopySource` 中必须指定源地域：

```python
def copy_object(args, parsed_globals):
    client, region = init_cos_client(parsed_globals)  # 使用源地域客户端执行 copy

    dest_region = args.get("dest_region", region) or region

    # copy 操作统一使用源地域 client，CopySource 中指定源地域
    # SDK 会自动处理跨地域请求，无需创建目标地域客户端
    source = {
        "Bucket": bucket,
        "Key": cos_key,
        "Region": region,   # 必须指定源地域
    }
    client.copy(Bucket=dest_bucket, Key=dest_key, CopySource=source)
```

## 复制操作的 CopySource 构造

```python
source = {
    "Bucket": bucket,      # 源存储桶
    "Key": cos_key,        # 源对象键
    "Region": region,      # 源地域（跨地域复制时必须指定）
}
kwargs = {
    "Bucket": dest_bucket,
    "Key": dest_key,
    "CopySource": source,
}
# 修改元数据时需要指定 MetadataDirective
if metadata:
    kwargs["Metadata"] = metadata
    kwargs["MetadataDirective"] = "Replaced"  # 或 "CopyStatus" = "Replaced"（单文件复制）
```
