# -*- coding: utf-8 -*-
"""
文件处理模块

提供数据万象文件处理功能的 CLI 命令，包括：
- 同步文件哈希计算
- 异步文件哈希计算（提交 + 查询）
- 文件解压缩
- 文件压缩
- 压缩包预览
- 查询文件处理任务
"""
import os

from .ci_helpers import init_cos_client, handle_cos_error, print_result, save_response_to_file


def file_hash(args, parsed_globals):
    """同步计算文件哈希值

    file_hash(self, Bucket, Key, Type, AddToHeader=False, ...)
    """
    try:
        client = init_cos_client(parsed_globals)

        response = client.file_hash(
            Bucket=args["bucket"],
            Key=args["key"],
            Type=args["hash_type"],
            AddToHeader=(
                args.get("add_to_header", "").lower() == "true"
                if args.get("add_to_header") else False
            ),
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def file_hash_job_submit(args, parsed_globals):
    """提交异步文件哈希计算任务

    ci_create_file_hash_job(self, Bucket, InputObject, FileHashCodeConfig,
                            QueueId=None, CallBack=None, ...)
    """
    try:
        client = init_cos_client(parsed_globals)

        hash_config = {
            "Type": args["hash_type"],
        }
        if args.get("add_to_header") and args["add_to_header"].lower() == "true":
            hash_config["AddToHeader"] = "true"

        response = client.ci_create_file_hash_job(
            Bucket=args["bucket"],
            InputObject=args["key"],
            FileHashCodeConfig=hash_config,
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def file_uncompress_submit(args, parsed_globals):
    """提交文件解压缩任务

    ci_create_file_uncompress_job(self, Bucket, InputObject, OutputBucket,
                                  OutputRegion, FileUncompressConfig, ...)
    """
    try:
        client = init_cos_client(parsed_globals)

        uncompress_config = {}
        if args.get("password"):
            uncompress_config["UnCompressKey"] = args["password"]
        if args.get("output_prefix"):
            uncompress_config["Prefix"] = args["output_prefix"]

        response = client.ci_create_file_uncompress_job(
            Bucket=args["bucket"],
            InputObject=args["key"],
            OutputBucket=args.get("output_bucket") or args["bucket"],
            OutputRegion=parsed_globals.get("region") or "ap-guangzhou",
            FileUncompressConfig=uncompress_config,
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def file_compress_submit(args, parsed_globals):
    """提交文件压缩任务

    ci_create_file_compress_job(self, Bucket, OutputBucket, OutputRegion,
                                OutputObject, FileCompressConfig, ...)
    """
    try:
        client = init_cos_client(parsed_globals)

        key_list = [k.strip() for k in args["keys"].split(",") if k.strip()]

        compress_config = {
            "Flatten": "0",
            "Format": args.get("compress_format") or "zip",
            "Key": key_list,
        }
        if args.get("prefix"):
            compress_config["Prefix"] = args["prefix"]

        response = client.ci_create_file_compress_job(
            Bucket=args["bucket"],
            OutputBucket=args["bucket"],
            OutputRegion=parsed_globals.get("region") or "ap-guangzhou",
            OutputObject=args["output_key"],
            FileCompressConfig=compress_config,
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def file_zip_preview(args, parsed_globals):
    """预览压缩包内容（列出文件列表）"""
    try:
        client = init_cos_client(parsed_globals)

        response = client.ci_file_zip_preview(
            Bucket=args["bucket"],
            Key=args["key"],
            NeedHeader=True,
        )
        # ci_file_zip_preview 支持 NeedHeader，返回 (headers, data) 元组
        if isinstance(response, tuple):
            resp_headers, data = response
            print_result(data, resp_headers)
        else:
            print_result(response)
    except Exception as e:
        handle_cos_error(e)


def file_process_jobs_query(args, parsed_globals):
    """查询文件处理任务"""
    try:
        client = init_cos_client(parsed_globals)

        response = client.ci_get_file_process_jobs(
            Bucket=args["bucket"],
            JobIDs=args["job_id"],
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)
