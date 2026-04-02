# -*- coding: utf-8 -*-
"""
restore 操作：恢复归档存储类型的 COS 对象
对齐 coscli restore 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client, match_filters


def restore_object(args, parsed_globals):
    """恢复归档存储类型的 COS 对象"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    cos_key = args["cos_key"]
    days = args.get("days", 7) or 7
    tier = args.get("tier", "Standard") or "Standard"
    recursive = args.get("recursive", False)
    include = args.get("include", "") or ""
    exclude = args.get("exclude", "") or ""

    try:
        if recursive:
            _restore_by_prefix(client, bucket, cos_key, days, tier, include, exclude)
        else:
            client.restore_object(
                Bucket=bucket,
                Key=cos_key,
                RestoreRequest={
                    "Days": days,
                    "CASJobParameters": {
                        "Tier": tier,
                    },
                },
            )
            print("恢复请求已提交: cos://%s/%s" % (bucket, cos_key))
            print("恢复天数: %d, 恢复模式: %s" % (days, tier))

    except CosServiceError as e:
        if e.get_error_code() == "RestoreAlreadyInProgress":
            print("恢复进行中: cos://%s/%s" % (bucket, cos_key))
        else:
            print("Error: %s (Code: %s, RequestId: %s)" % (
                e.get_error_msg(), e.get_error_code(), e.get_request_id()))


def _restore_by_prefix(client, bucket, prefix, days, tier, include, exclude):
    """递归恢复指定前缀下的所有归档对象"""
    restored = 0
    skipped = 0
    failed = 0
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
                if key.endswith("/"):
                    continue

                storage_class = content.get("StorageClass", "STANDARD")
                # 只恢复归档类型的对象
                if storage_class not in ("ARCHIVE", "DEEP_ARCHIVE"):
                    skipped += 1
                    continue

                rel_key = key[len(prefix):].lstrip("/") if prefix else key

                # include/exclude 过滤
                if not match_filters(rel_key, include, exclude):
                    skipped += 1
                    continue

                try:
                    client.restore_object(
                        Bucket=bucket,
                        Key=key,
                        RestoreRequest={
                            "Days": days,
                            "CASJobParameters": {
                                "Tier": tier,
                            },
                        },
                    )
                    restored += 1
                    print("已提交恢复: cos://%s/%s" % (bucket, key))
                except CosServiceError as e:
                    if e.get_error_code() == "RestoreAlreadyInProgress":
                        print("恢复进行中: cos://%s/%s" % (bucket, key))
                        skipped += 1
                    else:
                        failed += 1
                        print("恢复失败: %s (%s)" % (key, e.get_error_msg()))

        if response.get("IsTruncated") == "true":
            marker = response.get("NextMarker", "")
        else:
            break

    print("\n恢复完成: 提交 %d, 跳过 %d, 失败 %d" % (restored, skipped, failed))