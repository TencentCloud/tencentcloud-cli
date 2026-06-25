# -*- coding: utf-8 -*-
"""
文档处理模块

提供数据万象文档处理功能的 CLI 命令，包括：
- 同步文档预览（转图片下载到本地）
- HTML 文档预览（获取预览 URL）
- 异步文档转码任务（提交 + 查询 + 列出）
"""
import os

from .ci_helpers import init_cos_client, handle_cos_error, print_result, save_response_to_file


def doc_preview(args, parsed_globals):
    """同步文档预览（转为图片）

    将 COS 上的文档（PDF/Word/Excel/PPT 等）转为图片并下载到本地。

    Args:
        args:
            - bucket: 存储桶名称
            - key: 文档在 COS 上的对象键
            - page: (可选) 预览页码，从 1 开始，默认 1
            - src_type: (可选) 源文件类型，如 pdf/docx/xlsx/pptx
            - image_type: (可选) 输出图片类型 png/jpg，默认 png
            - dsttype: (可选) 输出格式 png/jpg/pdf，默认 png
            - output: (可选) 本地保存路径
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        kwargs = {
            "Bucket": args["bucket"],
            "Key": args["key"],
        }

        page = args.get("page") or "1"
        kwargs["Page"] = int(page)

        if args.get("src_type"):
            kwargs["SrcType"] = args["src_type"]
        if args.get("image_type"):
            kwargs["ImageParams"] = "imageMogr2/format/" + args["image_type"]
        if args.get("dsttype"):
            kwargs["DstType"] = args["dsttype"]

        response = client.ci_doc_preview_process(**kwargs)

        # 确定输出路径
        ext = args.get("dsttype") or args.get("image_type") or "png"
        base = os.path.splitext(os.path.basename(args["key"]))[0]
        default_name = f"{base}_page{page}.{ext}"
        output = args.get("local_path") or default_name

        total_bytes = save_response_to_file(response, output)

        print_result({
            "Status": "Success",
            "Output": os.path.abspath(output),
            "ContentType": response.get("Content-Type", ""),
            "ContentLength": str(total_bytes),
            "Page": page,
            "TotalPage": response.get("X-Total-Page", ""),
            "TotalSheet": response.get("X-Total-Sheet", ""),
        }, response)
    except Exception as e:
        handle_cos_error(e)


def doc_preview_html(args, parsed_globals):
    """HTML 文档在线预览

    获取文档的 HTML 预览内容，保存为本地 HTML 文件。

    Args:
        args:
            - bucket: 存储桶名称
            - key: 文档在 COS 上的对象键
            - src_type: (可选) 源文件类型
            - output: (可选) 保存 HTML 内容到本地的路径，默认自动生成
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        kwargs = {
            "Bucket": args["bucket"],
            "Key": args["key"],
        }

        if args.get("src_type"):
            kwargs["SrcType"] = args["src_type"]

        response = client.ci_doc_preview_html_process(**kwargs)

        # 确定输出路径：未指定时自动生成
        if args.get("local_path"):
            output = args["local_path"]
        else:
            base = os.path.splitext(os.path.basename(args["key"]))[0]
            output = f"{base}_preview.html"

        total_bytes = save_response_to_file(response, output)
        print_result({
            "Status": "Success",
            "Output": os.path.abspath(output),
            "ContentType": "text/html",
            "ContentLength": str(total_bytes),
        }, response)
    except Exception as e:
        handle_cos_error(e)


def doc_job_submit(args, parsed_globals):
    """提交异步文档转码任务

    将文档转码为指定格式（图片/PDF 等），结果存储到 COS。

    Args:
        args:
            - bucket: 存储桶名称
            - key: 文档在 COS 上的对象键
            - output_bucket: (可选) 输出存储桶，默认同 bucket
            - output_key: 输出文件的 COS 对象键
            - src_type: (可选) 源文件类型
            - tgt_type: (可选) 目标文件类型 png/jpg/pdf，默认 png
            - start_page: (可选) 起始页码，默认 1
            - end_page: (可选) 结束页码，默认 -1（所有页）
            - sheet_id: (可选) Sheet 编号（Excel 文件）
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        doc_process = {}
        if args.get("src_type"):
            doc_process["SrcType"] = args["src_type"]
        doc_process["TgtType"] = args.get("tgt_type") or "png"
        if args.get("start_page"):
            doc_process["StartPage"] = int(args["start_page"])
        if args.get("end_page"):
            doc_process["EndPage"] = int(args["end_page"])
        if args.get("sheet_id"):
            doc_process["SheetId"] = int(args["sheet_id"])

        kwargs = {
            "Bucket": args["bucket"],
            "InputObject": args["key"],
            "OutputBucket": args.get("output_bucket") or args["bucket"],
            "OutputRegion": parsed_globals.get("region") or "ap-guangzhou",
            "OutputObject": args["output_key"],
        }

        if doc_process.get("SrcType"):
            kwargs["SrcType"] = doc_process["SrcType"]
        if doc_process.get("TgtType"):
            kwargs["TgtType"] = doc_process["TgtType"]
        if doc_process.get("StartPage"):
            kwargs["StartPage"] = doc_process["StartPage"]
        if doc_process.get("EndPage"):
            kwargs["EndPage"] = doc_process["EndPage"]
        if doc_process.get("SheetId"):
            kwargs["SheetId"] = doc_process["SheetId"]

        response = client.ci_create_doc_job(**kwargs)
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def doc_job_query(args, parsed_globals):
    """查询异步文档转码任务

    Args:
        args:
            - bucket: 存储桶名称
            - job_id: 任务 ID
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        response = client.ci_get_doc_job(
            Bucket=args["bucket"],
            JobID=args["job_id"],
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def doc_job_list(args, parsed_globals):
    """列出异步文档转码任务

    Args:
        args:
            - bucket: 存储桶名称
            - size: (可选) 每页数量，默认 10
            - page: (可选) 页码，默认 1
            - status: (可选) 任务状态过滤 All/Submitted/Running/Success/Failed/Pause/Cancel
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        kwargs = {
            "Bucket": args["bucket"],
        }
        if args.get("size"):
            kwargs["Size"] = int(args["size"])
        if args.get("page"):
            kwargs["Page"] = int(args["page"])
        if args.get("status"):
            kwargs["States"] = args["status"]

        response = client.ci_list_doc_jobs(**kwargs)
        print_result(response)
    except Exception as e:
        handle_cos_error(e)
