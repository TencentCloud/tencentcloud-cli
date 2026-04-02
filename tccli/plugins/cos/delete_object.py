# -*- coding: utf-8 -*-
"""
delete 操作：删除 COS 上的文件
对齐 coscli rm 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client, match_filters


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

    try:
        if recursive:
            _delete_by_prefix(client, bucket, cos_key, include, exclude, force)
        else:
            kwargs = {"Bucket": bucket, "Key": cos_key}
            if version_id:
                kwargs["VersionId"] = version_id

            client.delete_object(**kwargs)
            print("删除成功: cos://%s/%s" % (bucket, cos_key))

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))


def _delete_by_prefix(client, bucket, prefix, include, exclude, force):
    """递归删除指定前缀下的所有对象"""
    objects_to_delete = []
    marker = ""

    while True:
        response = client.list_objects(
            Bucket=bucket,
            Prefix=prefix,
            Marker=marker,
            MaxKeys=1000,
        )

        if "Contents" in response:
            for content in response["Contents"]:
                key = content["Key"]
                rel_key = key[len(prefix):].lstrip("/") if prefix else key

                if not match_filters(rel_key, include, exclude):
                    continue

                objects_to_delete.append({"Key": key})

        if response.get("IsTruncated") == "true":
            marker = response.get("NextMarker", "")
        else:
            break

    if not objects_to_delete:
        print("没有匹配的对象需要删除")
        return

    # 非 force 模式下提示确认
    if not force:
        print("即将删除 %d 个对象 (前缀: cos://%s/%s)" % (len(objects_to_delete), bucket, prefix))
        print("提示: 使用 --force true 跳过确认")
        try:
            confirm = input("确认删除? (y/N): ").strip().lower()
            if confirm != "y":
                print("已取消删除")
                return
        except (EOFError, KeyboardInterrupt):
            print("\n已取消删除")
            return

    # 批量删除（每次最多 1000 个）
    deleted = 0
    for i in range(0, len(objects_to_delete), 1000):
        batch = objects_to_delete[i:i + 1000]
        client.delete_objects(
            Bucket=bucket,
            Delete={"Object": batch, "Quiet": "true"},
        )
        deleted += len(batch)

    print("删除完成: 共删除 %d 个对象" % deleted)