# -*- coding: utf-8 -*-
"""
delete_bucket 操作：删除存储桶
对齐 coscli rb 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client


def delete_bucket(args, parsed_globals):
    """删除存储桶"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    force = args.get("force", False)

    try:
        if force:
            print("正在清空存储桶 %s ..." % bucket)
            _clear_bucket(client, bucket)

        client.delete_bucket(Bucket=bucket)
        print("存储桶删除成功: %s" % bucket)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))


def _clear_bucket(client, bucket):
    """
    清空存储桶中的所有对象和未完成的分片上传。
    按照 coscli rb --force 的行为：
    1. 删除所有普通对象
    2. 删除所有版本对象和删除标记
    3. 清理所有未完成的分片上传
    """
    # 1. 删除所有普通对象
    deleted_objects = 0
    marker = ""
    while True:
        response = client.list_objects(
            Bucket=bucket,
            Marker=marker,
            MaxKeys=1000,
        )
        if "Contents" in response:
            objects = [{"Key": obj["Key"]} for obj in response["Contents"]]
            if objects:
                client.delete_objects(
                    Bucket=bucket,
                    Delete={"Object": objects, "Quiet": "true"},
                )
                deleted_objects += len(objects)

        if response.get("IsTruncated") == "true":
            marker = response.get("NextMarker", "")
        else:
            break

    if deleted_objects > 0:
        print("  已删除 %d 个对象" % deleted_objects)

    # 2. 删除所有版本对象和删除标记（如果开启了版本控制）
    deleted_versions = 0
    key_marker = ""
    version_id_marker = ""
    while True:
        try:
            response = client.list_objects_versions(
                Bucket=bucket,
                KeyMarker=key_marker,
                VersionIdMarker=version_id_marker,
                MaxKeys=1000,
            )
            objects = []
            if "Version" in response:
                versions = response["Version"]
                if not isinstance(versions, list):
                    versions = [versions]
                for v in versions:
                    objects.append({"Key": v["Key"], "VersionId": v["VersionId"]})

            if "DeleteMarker" in response:
                markers = response["DeleteMarker"]
                if not isinstance(markers, list):
                    markers = [markers]
                for m in markers:
                    objects.append({"Key": m["Key"], "VersionId": m["VersionId"]})

            if objects:
                client.delete_objects(
                    Bucket=bucket,
                    Delete={"Object": objects, "Quiet": "true"},
                )
                deleted_versions += len(objects)

            if response.get("IsTruncated") == "true":
                key_marker = response.get("NextKeyMarker", "")
                version_id_marker = response.get("NextVersionIdMarker", "")
            else:
                break
        except CosServiceError:
            # 如果未开启版本控制，忽略错误
            break

    if deleted_versions > 0:
        print("  已删除 %d 个版本对象" % deleted_versions)

    # 3. 清理未完成的分片上传
    aborted = 0
    key_marker = ""
    upload_id_marker = ""
    while True:
        response = client.list_multipart_uploads(
            Bucket=bucket,
            KeyMarker=key_marker,
            UploadIdMarker=upload_id_marker,
            MaxUploads=1000,
        )
        uploads = response.get("Upload", [])
        if not isinstance(uploads, list):
            uploads = [uploads]

        for upload in uploads:
            if not upload:
                continue
            client.abort_multipart_upload(
                Bucket=bucket,
                Key=upload["Key"],
                UploadId=upload["UploadId"],
            )
            aborted += 1

        if response.get("IsTruncated") == "true":
            key_marker = response.get("NextKeyMarker", "")
            upload_id_marker = response.get("NextUploadIdMarker", "")
        else:
            break

    if aborted > 0:
        print("  已清理 %d 个未完成的分片上传" % aborted)