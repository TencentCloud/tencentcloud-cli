# -*- coding: utf-8 -*-
"""
delete 操作：删除 COS 上的文件
对齐 coscli rm 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client, match_filters, list_all_objects_with_dirs, TransferProgressMonitor


def delete_object(args, parsed_globals):
    """删除 COS 上的文件"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    cos_key = args["cos_key"]
    recursive = args.get("recursive", False)
    force = args.get("force", False)
    include = args.get("include", "") or ""
    exclude = args.get("exclude", "") or ""
    version_id = args.get("version_id", "") or ""
    retry = args.get("retry", 3)
    if retry is None:
        retry = 3
    retry = int(retry)
    log_file = args.get("log_file", "") or ""

    try:
        if recursive:
            _delete_by_prefix(client, bucket, cos_key, include, exclude, force, retry, log_file)
        else:
            kwargs = {"Bucket": bucket, "Key": cos_key}
            if version_id:
                kwargs["VersionId"] = version_id

            client.delete_object(**kwargs)
            print("删除成功: cos://%s/%s" % (bucket, cos_key))

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))


def _delete_by_prefix(client, bucket, prefix, include, exclude, force, retry=3, log_file=""):
    """递归删除指定前缀下的所有对象（含 / 结尾的空目录对象）"""
    # 收集所有待删除对象（含空目录）
    all_objects = list_all_objects_with_dirs(client, bucket, prefix)
    file_keys = []      # 普通文件
    dir_keys = []       # / 结尾的空目录对象
    skip_count = 0

    for key, obj_info in all_objects.items():
        rel_key = key[len(prefix):].lstrip("/") if prefix else key

        if obj_info.get("IsDir"):
            dir_rel = rel_key.rstrip("/") if rel_key else key.rstrip("/").split("/")[-1]
            if not match_filters(dir_rel, include, exclude):
                skip_count += 1
                continue
            dir_keys.append(key)
            continue

        if not match_filters(rel_key, include, exclude):
            skip_count += 1
            continue

        file_keys.append(key)

    total_count = len(file_keys) + len(dir_keys)
    if total_count == 0:
        print("没有匹配的对象需要删除")
        return

    # 非 force 模式下提示确认
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

    monitor = TransferProgressMonitor("delete")
    monitor.set_scan_info(total_count + skip_count, 0)
    for _ in range(skip_count):
        monitor.update_skip(0)
    monitor.start()

    # 删除普通文件（批量删除，每次最多 1000 个，含重试）
    for i in range(0, len(file_keys), 1000):
        batch_keys = file_keys[i:i + 1000]
        last_err = None
        for attempt in range(max(1, retry + 1)):
            try:
                client.delete_objects(
                    Bucket=bucket,
                    Delete={"Object": [{"Key": k} for k in batch_keys], "Quiet": "true"},
                )
                for k in batch_keys:
                    monitor.update_ok(0)
                last_err = None
                break
            except CosServiceError as e:
                last_err = e
        if last_err is not None:
            err_reason = "%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code())
            for k in batch_keys:
                monitor.update_err(src_path="cos://%s/%s" % (bucket, k),
                                   reason=err_reason,
                                   request_id=last_err.get_request_id())

    # 删除空目录对象（逐个删除，含重试）
    for key in dir_keys:
        last_err = None
        for attempt in range(max(1, retry + 1)):
            try:
                client.delete_object(Bucket=bucket, Key=key)
                monitor.update_ok(0)
                last_err = None
                break
            except CosServiceError as e:
                last_err = e
        if last_err is not None:
            err_reason = "%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code())
            monitor.update_err(src_path="cos://%s/%s" % (bucket, key),
                               reason=err_reason,
                               request_id=last_err.get_request_id())

    monitor.stop(log_file=log_file)