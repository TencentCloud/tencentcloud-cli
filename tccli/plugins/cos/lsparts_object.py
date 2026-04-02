# -*- coding: utf-8 -*-
"""
lsparts 操作：列出未完成的分片上传
对齐 coscli lsparts 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client


def lsparts_object(args, parsed_globals):
    """列出存储桶中未完成的分片上传"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    prefix = args.get("prefix", "") or ""

    try:
        key_marker = ""
        upload_id_marker = ""
        total = 0

        print("%-60s  %-40s  %-25s" % ("Key", "UploadId", "Initiated"))
        print("-" * 130)

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
                upload_id = upload.get("UploadId", "")
                initiated = upload.get("Initiated", "")
                total += 1
                print("%-60s  %-40s  %-25s" % (key, upload_id, initiated))

            if response.get("IsTruncated") == "true":
                key_marker = response.get("NextKeyMarker", "")
                upload_id_marker = response.get("NextUploadIdMarker", "")
            else:
                break

        if total == 0:
            print("没有未完成的分片上传")
        else:
            print("\n共 %d 个未完成的分片上传" % total)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))