---
type: always
---

# 规则：文件传输与进度监控

## TransferProgressMonitor 使用规范

**所有批量传输操作（上传、下载、复制、同步）必须使用 `TransferProgressMonitor`**，禁止直接打印进度信息。

```python
from .utils import TransferProgressMonitor

# ✅ 正确：使用 TransferProgressMonitor
monitor = TransferProgressMonitor("upload")
monitor.start()
# ... 传输操作 ...
monitor.stop(log_file=log_file)

# ❌ 错误：直接打印进度
print("上传进度: %d/%d" % (i, total))  # 禁止
```

## 标准批量传输流程

```
① 创建 monitor = TransferProgressMonitor(op_type)
② monitor.start()  # 启动进度条线程
③ 扫描收集所有任务（tasks）
④ monitor.set_scan_info(total_num, total_size)  # 设置总数和总大小
⑤ 对跳过的文件调用 monitor.update_skip(size)
⑥ 线程池并发执行任务
   - 成功：monitor.update_ok(size, file_id)
   - 失败：monitor.update_err(file_id, src_path, dest_path, reason, request_id)
⑦ monitor.stop(log_file=log_file)  # 停止进度条，输出最终结果
```

## progress_callback 使用规范

**使用 SDK 的分片传输（upload_file/download_file）时必须传入 progress_callback**，以实现实时进度更新：

```python
# ✅ 正确：使用 progress_callback
progress_cb, file_id = monitor.create_progress_callback(file_size)
client.upload_file(
    Bucket=bucket,
    LocalFilePath=local_path,
    Key=cos_key,
    progress_callback=progress_cb,  # 必须传入
)
monitor.update_ok(file_size, file_id)  # 传入 file_id

# ❌ 错误：不传 progress_callback
client.upload_file(Bucket=bucket, LocalFilePath=local_path, Key=cos_key)
monitor.update_ok(file_size)  # 不传 file_id，进度不准确
```

## 重试时必须重置 progress_callback

```python
progress_cb, file_id = monitor.create_progress_callback(file_size)
for attempt in range(max(1, retry + 1)):
    try:
        client.upload_file(..., progress_callback=progress_cb)
        monitor.update_ok(file_size, file_id)
        break
    except CosServiceError as e:
        last_err = e
        if attempt < retry:
            # ✅ 重试前必须重置 progress_callback，避免进度累加错误
            progress_cb, file_id = monitor.create_progress_callback(file_size)
```

## 线程池并发规范

```python
# ✅ 正确：使用 ThreadPoolExecutor，routines 控制并发数，as_completed 必须在 with 块内
if tasks:
    max_workers = min(routines, len(tasks))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(_do_task, *task) for task in tasks]
        for future in as_completed(futures):
            future.result()  # 等待所有任务完成，传播异常

# ❌ 错误：不限制并发数
with ThreadPoolExecutor() as executor:  # 禁止：可能创建过多线程
    ...

# ❌ 错误：as_completed 在 with 块外（线程池已关闭，异常位置不准确）
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = [executor.submit(_do_task, *task) for task in tasks]
for future in as_completed(futures):  # 禁止：with 块已退出
    future.result()
```

## 空目录处理

上传/下载/复制时需要处理空目录（COS 上以 `/` 结尾的空对象）：

```python
# 上传时：在 COS 上创建空目录标记
for dir_key in empty_dir_keys:
    try:
        client.put_object(Bucket=bucket, Key=dir_key, Body=b"")
        monitor.update_ok(0)
    except CosServiceError as e:
        monitor.update_err(src_path=dir_key,
                           reason="创建空目录失败: %s" % e.get_error_msg(),
                           request_id=e.get_request_id())

# 下载时：在本地创建对应目录
for local_subdir in empty_local_dirs:
    if local_subdir and not os.path.exists(local_subdir):
        os.makedirs(local_subdir, exist_ok=True)
    monitor.update_ok(0)
```

## 同步操作增量判断规范

同步操作通过比较文件大小判断是否需要传输（对齐 coscli sync 行为）：

```python
# ✅ 正确：通过大小比较判断是否跳过
if cos_key in cos_objects and cos_objects[cos_key]["Size"] == file_info["Size"]:
    skip_count += 1
    skip_size += file_info["Size"]
    continue  # 跳过，不加入 tasks

# ❌ 错误：通过 ETag 或 MD5 比较（性能差，且不对齐 coscli 行为）
```

## 删除多余文件规范

同步操作中 `delete_extra=True` 时，删除目标端多余文件：

```python
if delete_extra:
    # 使用 list_all_objects_with_dirs 获取包含目录对象的完整列表
    from .utils import list_all_objects_with_dirs
    cos_all_objects = list_all_objects_with_dirs(client, bucket, cos_prefix)
    deleted = 0
    for cos_key, obj_info in cos_all_objects.items():
        rel_key = cos_key[len(cos_prefix):].lstrip("/") if cos_prefix else cos_key
        if obj_info.get("IsDir"):
            dir_rel = rel_key.rstrip("/")
            if dir_rel and not os.path.isdir(os.path.join(local_path, dir_rel.replace("/", os.sep))):
                client.delete_object(Bucket=bucket, Key=cos_key)
                deleted += 1
        else:
            if rel_key not in local_files:
                client.delete_object(Bucket=bucket, Key=cos_key)
                deleted += 1
    if deleted > 0:
        print("已删除目标端多余文件: %d" % deleted)
```

## 失败日志规范

`monitor.stop(log_file=log_file)` 会自动将失败记录写入日志文件（结构化格式）：

```
# upload 失败日志
# 生成时间: 2024-01-01 12:00:00
# 执行耗时: 10.5s
# 失败总数: 2

[1]
  Time      : 2024-01-01 12:00:05
  Source    : /local/path/file.txt
  Dest      : cos://bucket/key/file.txt
  Reason    : NoSuchBucket (Code: NoSuchBucket)
  RequestId : NjYxMjM0NTY...
```

**`log_file` 为空字符串时不写日志**，这是正常行为，不需要额外判断。
