---
type: always
---

# 规则：utils.py 工具函数参考

## 概述

`utils.py` 是 cos 插件的工具模块，提供凭据解析、客户端初始化、文件过滤、格式化、对象列举等通用功能。**所有命令文件必须从 `utils.py` 导入所需工具函数，禁止在命令文件中重复实现这些功能。**

---

## 客户端相关

### `init_cos_client(parsed_globals) → (client, region)`

标准 COS 客户端初始化，内部调用 `parse_global_arg` 处理凭据优先级。

```python
from .utils import init_cos_client

client, region = init_cos_client(parsed_globals)
# client: CosS3Client 实例
# region: 地域字符串，如 "ap-guangzhou"
```

### `parse_global_arg(parsed_globals) → dict`

解析全局参数，填充凭据（secretId/secretKey/token/region/endpoint）。通常不需要直接调用，`init_cos_client` 内部已调用。

---

## 文件过滤

### `match_filters(name, include, exclude) → bool`

根据 include/exclude 模式过滤文件名，返回 True 表示文件应被处理。

```python
from .utils import match_filters

# include="*.txt", exclude="*.log"
if not match_filters(rel_path, include, exclude):
    skip_count += 1
    continue
```

---

## 元数据解析

### `parse_meta(meta_str) → dict`

解析自定义元数据字符串，格式为 `key1=value1#key2=value2`，key 自动加 `x-cos-meta-` 前缀。

```python
from .utils import parse_meta

metadata = parse_meta("author=test#version=1.0")
# → {"x-cos-meta-author": "test", "x-cos-meta-version": "1.0"}
```

---

## COS key 构造

### `build_cos_key(prefix, rel_path) → str`

根据前缀和相对路径构造 COS 对象键。

```python
from .utils import build_cos_key

build_cos_key("", "dir/file.txt")       # → "dir/file.txt"
build_cos_key("backup", "dir/file.txt") # → "backup/dir/file.txt"
build_cos_key("backup/", "dir/file.txt")# → "backup/dir/file.txt"
```

---

## 对象列举

### `list_all_objects(client, bucket, prefix="") → dict`

列出存储桶中指定前缀下的所有对象（**跳过 `/` 结尾的目录标记**），自动处理分页。

```python
from .utils import list_all_objects

# 返回: {key: {"Size": int, "ETag": str, "LastModified": str, "StorageClass": str}}
cos_objects = list_all_objects(client, bucket, "prefix/")
```

### `list_all_objects_with_dirs(client, bucket, prefix="") → dict`

列出存储桶中指定前缀下的所有对象（**包含 `/` 结尾的目录标记**），自动处理分页。

```python
from .utils import list_all_objects_with_dirs

# 返回: {key: {"Size": int, "ETag": str, "LastModified": str, "StorageClass": str, "IsDir": bool}}
cos_all_objects = list_all_objects_with_dirs(client, bucket, "prefix/")
```

**使用场景**：
- `list_all_objects`：同步上传时比较 COS 上的文件（不需要目录对象）
- `list_all_objects_with_dirs`：同步删除多余文件时（需要包含目录对象）

---

## 本地文件列举

### `list_local_files(local_dir) → dict`

递归列出本地目录下的所有文件（不含目录）。

```python
from .utils import list_local_files

# 返回: {rel_path: {"Size": int, "FullPath": str}}
# rel_path 使用 "/" 分隔（跨平台统一）
local_files = list_local_files("/local/dir")
```

---

## 格式化工具

### `format_size(size_bytes) → str`

格式化文件大小为人类可读的字符串。

```python
from .utils import format_size

format_size(1024)           # → "1.00 KB"
format_size(1024 * 1024)    # → "1.00 MB"
format_size(1024 ** 3)      # → "1.00 GB"
```

---

## 进度监控

### `TransferProgressMonitor(op_type)`

批量传输进度监控器，详见 `03-transfer-and-progress.md`。

```python
from .utils import TransferProgressMonitor

monitor = TransferProgressMonitor("upload")  # op_type: upload/download/copy/move
monitor.start()
# ... 传输操作 ...
monitor.stop(log_file=log_file)
```

---

## 禁止在命令文件中重复实现的功能

以下功能已在 `utils.py` 中实现，**禁止**在命令文件中重复实现：

```python
# ❌ 禁止：重复实现文件大小格式化
def format_size(size):  # 禁止
    ...

# ❌ 禁止：重复实现对象列举
def list_objects(client, bucket, prefix):  # 禁止
    ...

# ❌ 禁止：重复实现元数据解析
def parse_meta(meta_str):  # 禁止
    ...

# ❌ 禁止：重复实现过滤逻辑
def match_pattern(name, pattern):  # 禁止
    ...
```
