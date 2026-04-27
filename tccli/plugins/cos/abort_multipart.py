# -*- coding: utf-8 -*-
"""
abort 操作：清理未完成的分片上传
对齐 coscli abort 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client


def abort_multipart(args, parsed_globals):
    """清理存储桶中未完成的分片上传"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    prefix = args.get("prefix", "") or ""
    upload_id = args.get("upload_id", "") or ""

    try:
        # 如果指定了 upload_id，则直接取消指定的分片上传
        if upload_id:
            cos_key = args.get("cos_key", "") or ""
            if not cos_key:
                print("Error: 指定 upload_id 时必须同时指定 cos_key")
                return
            client.abort_multipart_upload(
                Bucket=bucket,
                Key=cos_key,
                UploadId=upload_id,
            )
            print("已取消分片上传: cos://%s/%s (UploadId: %s)" % (bucket, cos_key, upload_id))
            return

        # 否则列出并清理所有未完成的分片上传
        key_marker = ""
        upload_id_marker = ""
        aborted = 0

        while True:
            response = client.list_multipart_uploads(
                Bucket=bucket,
                Prefix=prefix,
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
                key = upload.get("Key", "")
                uid = upload.get("UploadId", "")
                initiated = upload.get("Initiated", "")

                client.abort_multipart_upload(
                    Bucket=bucket,
                    Key=key,
                    UploadId=uid,
                )
                aborted += 1
                print("已取消: cos://%s/%s (UploadId: %s, Initiated: %s)" % (bucket, key, uid, initiated))

            if response.get("IsTruncated") == "true":
                key_marker = response.get("NextKeyMarker", "")
                upload_id_marker = response.get("NextUploadIdMarker", "")
            else:
                break

        if aborted == 0:
            print("没有未完成的分片上传")
        else:
            print("\n共清理 %d 个未完成的分片上传" % aborted)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))