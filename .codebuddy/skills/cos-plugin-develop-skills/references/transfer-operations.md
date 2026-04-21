# Skill：文件传输操作与 TransferProgressMonitor

## 概述

`TransferProgressMonitor` 是批量文件传输（上传、下载、复制、同步）的核心进度监控器，定义在 `utils.py` 中，对齐 coscli 的 `FileProcessMonitor`。

---

## TransferProgressMonitor 完整字段说明

```python
class TransferProgressMonitor:
    op_type        # 操作类型: "upload" / "download" / "copy" / "move"
    total_num      # 扫描到的总文件数（含跳过）
    total_size     # 扫描到的总大小（字节）
    ok_num         # 成功处理的文件数
    skip_num       # 跳过的文件数（同步时大小一致）
    err_num        # 失败的文件数
    deal_size      # 已处理的总大小（含跳过）
    transfer_size  # 实际传输的大小（通过 progress_callback 实时更新）
    skip_size      # 跳过的总大小
```

---

## 标准使用模式

### 单文件传输

```python
def _upload_single(client, bucket, local_path, cos_key, thread_num, part_size, rate_limiting, retry=3, log_file=""):
    monitor = TransferProgressMonitor("upload")
    file_size = os.path.getsize(local_path)
    monitor.set_scan_info(1, file_size)   # 设置总数和总大小
    monitor.start()                        # 启动进度条刷新线程

    progress_cb, file_id = monitor.create_progress_callback(file_size)
    last_err = None
    for attempt in range(max(1, retry + 1)):
        try:
            client.upload_file(
                Bucket=bucket,
                LocalFilePath=local_path,
                Key=cos_key,
                PartSize=part_size,
                MAXThread=thread_num,
                progress_callback=progress_cb,
            )
            monitor.update_ok(file_size, file_id)  # 成功
            last_err = None
            break
        except CosServiceError as e:
            last_err = e
            if attempt < retry:
                # 重置进度，准备重试
                progress_cb, file_id = monitor.create_progress_callback(file_size)

    if last_err is not None:
        err_reason = "%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code())
        monitor.update_err(
            file_id,
            src_path=local_path,
            dest_path="cos://%s/%s" % (bucket, cos_key),
            reason=err_reason,
            request_id=last_err.get_request_id()
        )

    monitor.stop(log_file=log_file)  # 停止进度条，输出最终结果，写失败日志
    if last_err is not None:
        raise last_err
```

### 批量文件传输（线程池）

```python
def _upload_directory(client, bucket, local_dir, cos_prefix, include, exclude,
                      thread_num, routines, part_size, rate_limiting, retry=3, log_file=""):
    monitor = TransferProgressMonitor("upload")
    monitor.start()

    # ① 先扫描收集所有任务
    tasks = []
    total_size = 0
    skip_count = 0
    for root, dirs, files in os.walk(local_dir):
        for filename in files:
            full_path = os.path.join(root, filename)
            rel_path = os.path.relpath(full_path, local_dir).replace(os.sep, "/")

            if not match_filters(rel_path, include, exclude):
                skip_count += 1
                continue

            cos_key = build_cos_key(cos_prefix, rel_path)
            file_size = os.path.getsize(full_path)
            total_size += file_size
            tasks.append((full_path, cos_key, file_size))

    # ② 设置扫描结果
    monitor.set_scan_info(len(tasks) + skip_count, total_size)
    for _ in range(skip_count):
        monitor.update_skip(0)

    # ③ 定义单文件任务函数
    def _do_upload(full_path, cos_key, file_size):
        last_err = None
        progress_cb, file_id = monitor.create_progress_callback(file_size)
        for attempt in range(max(1, retry + 1)):
            try:
                client.upload_file(
                    Bucket=bucket,
                    LocalFilePath=full_path,
                    Key=cos_key,
                    PartSize=part_size,
                    MAXThread=thread_num,
                    progress_callback=progress_cb,
                )
                monitor.update_ok(file_size, file_id)
                last_err = None
                break
            except CosServiceError as e:
                last_err = e
                if attempt < retry:
                    progress_cb, file_id = monitor.create_progress_callback(file_size)
        if last_err is not None:
            err_reason = "%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code())
            monitor.update_err(file_id,
                               src_path=full_path,
                               dest_path="cos://%s/%s" % (bucket, cos_key),
                               reason=err_reason,
                               request_id=last_err.get_request_id())

    # ④ 线程池并发执行，routines 控制文件间并发数
    if tasks:
        max_workers = min(routines, len(tasks))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(_do_upload, fp, ck, fs) for fp, ck, fs in tasks]
            for future in as_completed(futures):
                future.result()

    monitor.stop(log_file=log_file)
```

---

## monitor 方法说明

| 方法 | 说明 | 调用时机 |
|---|---|---|
| `set_scan_info(total_num, total_size)` | 设置总文件数和总大小 | 扫描完成后，start() 之后 |
| `start()` | 启动进度条刷新线程 | 开始传输前 |
| `update_ok(size, file_id=None)` | 记录成功 | 单文件传输成功后 |
| `update_skip(size)` | 记录跳过 | 同步时文件已存在且大小一致 |
| `update_err(file_id, src_path, dest_path, reason, request_id)` | 记录失败 | 单文件传输失败后 |
| `create_progress_callback(file_size)` | 创建分片进度回调 | 每次传输前（重试时需重新创建） |
| `stop(log_file=None)` | 停止进度条，输出最终结果 | 所有文件传输完成后 |

---

## 同步操作模式（增量比较）

同步操作对齐 **coscli sync** 的跳过逻辑：通过 `utils.py` 提供的统一判断函数实现，禁止使用"大小相同即跳过"的简化逻辑。

### 跳过规则（优先级从高到低）

| 参数 | 判断方式 | 说明 |
|---|---|---|
| `--ignore-existing` | 目标存在即跳过 | 不做任何内容比较，仅判断对象是否存在 |
| `--update` | 按 `Last-Modified` 对比 | 目标 `Last-Modified` >= 源 `Last-Modified`（或本地 mtime）则跳过 |
| （默认） | CRC64 比较 | 对比 COS HEAD 的 `x-cos-hash-crc64ecma` 与对端 CRC64；相等则跳过 |

**目标不存在** → 一律不跳过（无论是否指定上述参数）。

### sync 专用工具函数（位于 utils.py）

| 函数 | 用途 |
|---|---|
| `calculate_local_crc64(file_path)` | 计算本地文件 CRC64（ECMA-182），返回字符串；未装 crcmod 或失败返回 `None` |
| `get_object_head(client, bucket, cos_key)` | 封装 `head_object`，对象不存在或异常时返回 `None` |
| `parse_http_time(time_str)` | 解析 RFC1123/RFC3339 时间字符串为 Unix 时间戳 |
| `should_skip_sync_upload(client, bucket, cos_key, local_full_path, local_mtime, ignore_existing, update)` | sync_upload 跳过判定 |
| `should_skip_sync_download(client, bucket, cos_key, cos_head_info, local_full_path, ignore_existing, update)` | sync_download 跳过判定 |
| `should_skip_sync_copy(client, src_bucket, src_key, dest_bucket, dest_key, ignore_existing, update)` | sync_copy 跳过判定 |

### sync_upload 示例

```python
from .utils import (list_local_files, list_all_objects, build_cos_key,
                    match_filters, should_skip_sync_upload)

local_files = list_local_files(local_path)                 # 含 "MTime" 字段
cos_objects = list_all_objects(client, bucket, cos_prefix)

for rel_path, file_info in local_files.items():
    if not match_filters(rel_path, include, exclude):
        skip_count += 1
        continue

    cos_key = build_cos_key(cos_prefix, rel_path)

    # ✅ 正确：对齐 coscli sync 的跳过逻辑（CRC64 / update / ignore-existing）
    if cos_key in cos_objects and should_skip_sync_upload(
            client, bucket, cos_key,
            file_info["FullPath"], file_info.get("MTime", 0),
            ignore_existing=ignore_existing, update=update):
        skip_count += 1
        skip_size += file_info["Size"]
        continue

    # ❌ 错误：通过大小比较判断（coscli 并不这么做，且同名不同内容时会误跳过）
    # if cos_key in cos_objects and cos_objects[cos_key]["Size"] == file_info["Size"]:
    #     continue

    tasks.append((file_info, cos_key))
```

### sync_download 示例

```python
from .utils import should_skip_sync_download

local_file = os.path.join(local_path, rel_key.replace("/", os.sep))
if rel_key in local_files and should_skip_sync_download(
        client, bucket, cos_key, obj_info, local_file,
        ignore_existing=ignore_existing, update=update):
    skip_count += 1
    skip_size += obj_info["Size"]
    continue
```

### sync_copy 示例

```python
from .utils import should_skip_sync_copy

if dest_key in dest_objects and should_skip_sync_copy(
        client, bucket, src_key, dest_bucket, dest_key,
        ignore_existing=ignore_existing, update=update):
    skip_count += 1
    skip_size += obj_info["Size"]
    continue
```

### 参数规范（`_spec`）

所有三个 sync 命令（sync_upload / sync_download / sync_copy）都必须在 Request 中声明：

```python
{"name": "ignore_existing", "member": "bool", "type": "bool", "required": False,
 "document": "目标已存在即跳过，默认 false。与 --update 互斥，优先级高于 --update"},
{"name": "update", "member": "bool", "type": "bool", "required": False,
 "document": "仅在源比目标新时更新（按 Last-Modified 比较），默认 false。未指定 --ignore-existing 和 --update 时使用 CRC64 校验判断是否跳过"},
```

### 依赖说明

CRC64 计算依赖 `crcmod`（项目已使用）：

```
pip install crcmod
```

`calculate_local_crc64` 在未安装 `crcmod` 时返回 `None`，此时 `should_skip_sync_*` 会回退为"不跳过"（即重新传输），行为保底安全。

---

## 限速参数转换

COS SDK 的 `TrafficLimit` 参数单位为 bit/s，需要从 MB/s 转换：

```python
if rate_limiting:
    kwargs["TrafficLimit"] = str(int(rate_limiting) * 1024 * 1024 * 8)
```

---

## 元数据解析

使用 `utils.parse_meta()` 解析自定义元数据字符串：

```python
from .utils import parse_meta

# 输入格式: "key1=value1#key2=value2"
metadata = parse_meta(meta)
# 输出: {"x-cos-meta-key1": "value1", "x-cos-meta-key2": "value2"}

if metadata:
    kwargs["Metadata"] = metadata
```

---

## 过滤规则

使用 `utils.match_filters()` 进行 include/exclude 过滤：

```python
from .utils import match_filters

# 返回 True 表示文件应被处理，False 表示跳过
if not match_filters(rel_path, include, exclude):
    skip_count += 1
    continue
```

---

## COS key 构造

使用 `utils.build_cos_key()` 根据前缀和相对路径构造 COS 对象键：

```python
from .utils import build_cos_key

# prefix="" + rel_path="dir/file.txt" → "dir/file.txt"
# prefix="backup" + rel_path="dir/file.txt" → "backup/dir/file.txt"
# prefix="backup/" + rel_path="dir/file.txt" → "backup/dir/file.txt"
cos_key = build_cos_key(cos_prefix, rel_path)
```

---

## 删除多余文件（同步操作）

同步操作中，`delete_extra=True` 时删除目标端多余文件，需区分目录对象和普通文件：

```python
if delete_extra:
    from .utils import list_all_objects_with_dirs
    # 使用 list_all_objects_with_dirs 获取包含目录对象的完整列表
    cos_all_objects = list_all_objects_with_dirs(client, bucket, cos_prefix)
    deleted = 0
    for cos_key, obj_info in cos_all_objects.items():
        rel_key = cos_key[len(cos_prefix):].lstrip("/") if cos_prefix else cos_key
        if obj_info.get("IsDir"):
            # 目录对象：检查本地是否存在对应目录
            dir_rel = rel_key.rstrip("/")
            if dir_rel and not os.path.isdir(os.path.join(local_path, dir_rel.replace("/", os.sep))):
                client.delete_object(Bucket=bucket, Key=cos_key)
                deleted += 1
        else:
            # 普通文件：检查本地是否存在
            if rel_key not in local_files:
                client.delete_object(Bucket=bucket, Key=cos_key)
                deleted += 1
    if deleted > 0:
        print("已删除目标端多余文件: %d" % deleted)
```
