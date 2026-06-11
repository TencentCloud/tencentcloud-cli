# -*- coding: utf-8 -*-
"""
内容审核模块

提供数据万象内容审核功能的 CLI 命令，包括：
- 图片审核（同步批量）
- 视频审核（提交 + 查询）
- 音频审核（提交 + 查询）
- 文本审核（提交 + 查询）
- 文档审核（提交 + 查询）
- 网页审核（提交 + 查询）
- 直播审核（提交 + 取消）
- 病毒检测（提交 + 查询）
- 举报不良内容
"""
from .ci_helpers import init_cos_client, handle_cos_error, print_result


def _parse_detect_type(detect_type_str):
    """将逗号分隔的审核类型字符串转为 SDK 要求的整数位掩码

    SDK DetectType 是一个整数位掩码：
      CiDetectType.PORN = 1
      CiDetectType.TERRORIST = 2
      CiDetectType.POLITICS = 4
      CiDetectType.ADS = 8

    也接受直接传数字。
    """
    type_map = {
        "porn": 1,
        "terrorist": 2,
        "terrorism": 2,
        "politics": 4,
        "ads": 8,
    }
    if not detect_type_str:
        return None  # 不设置，让 SDK 使用默认值

    # 如果是纯数字，直接返回
    try:
        return int(detect_type_str)
    except ValueError:
        pass

    result = 0
    for part in detect_type_str.replace("|", ",").split(","):
        part = part.strip().lower()
        if part in type_map:
            result |= type_map[part]
    return result if result > 0 else None


# ---------------------------------------------------------------------------
# 图片审核
# ---------------------------------------------------------------------------

def auditing_image(args, parsed_globals):
    """图片批量审核（同步）

    ci_auditing_image_batch(self, Bucket, Input, DetectType=None, BizType=None, ...)
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]

        # 构建审核输入列表
        inputs = []
        keys = args.get("key")
        if keys:
            for k in keys.split(","):
                k = k.strip()
                if k:
                    inputs.append({"Object": k})

        urls = args.get("url")
        if urls:
            for u in urls.split(","):
                u = u.strip()
                if u:
                    inputs.append({"Url": u})

        if not inputs:
            raise ValueError("必须指定 key 或 url 参数")

        kwargs = {
            "Bucket": bucket,
            "Input": inputs,
        }

        detect_type = _parse_detect_type(args.get("detect_type"))
        if detect_type is not None:
            kwargs["DetectType"] = detect_type

        biz_type = args.get("biz_type")
        if biz_type:
            kwargs["BizType"] = biz_type

        response = client.ci_auditing_image_batch(**kwargs)
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 视频审核
# ---------------------------------------------------------------------------

def auditing_video_submit(args, parsed_globals):
    """提交视频审核任务

    ci_auditing_video_submit(self, Bucket, Key, DetectType=None, Url=None,
                             Callback=None, Mode='Interval', Count=100, BizType=None, ...)
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]

        kwargs = {"Bucket": bucket}

        # Key 是位置参数，必须提供（可以为空字符串，用 Url 替代）
        key = args.get("key") or ""
        kwargs["Key"] = key

        if args.get("url"):
            kwargs["Url"] = args["url"]

        detect_type = _parse_detect_type(args.get("detect_type"))
        if detect_type is not None:
            kwargs["DetectType"] = detect_type

        if args.get("biz_type"):
            kwargs["BizType"] = args["biz_type"]
        if args.get("snapshot_mode"):
            kwargs["Mode"] = args["snapshot_mode"]
        if args.get("snapshot_count"):
            kwargs["Count"] = int(args["snapshot_count"])

        response = client.ci_auditing_video_submit(**kwargs)
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def auditing_video_query(args, parsed_globals):
    """查询视频审核任务结果"""
    try:
        client = init_cos_client(parsed_globals)
        response = client.ci_auditing_video_query(
            Bucket=args["bucket"],
            JobID=args["job_id"],
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 音频审核
# ---------------------------------------------------------------------------

def auditing_audio_submit(args, parsed_globals):
    """提交音频审核任务

    ci_auditing_audio_submit(self, Bucket, Key, DetectType=None, Url=None,
                             BizType=None, ...)
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]

        kwargs = {"Bucket": bucket}

        # Key 是位置参数
        key = args.get("key") or ""
        kwargs["Key"] = key

        if args.get("url"):
            kwargs["Url"] = args["url"]

        detect_type = _parse_detect_type(args.get("detect_type"))
        if detect_type is not None:
            kwargs["DetectType"] = detect_type

        if args.get("biz_type"):
            kwargs["BizType"] = args["biz_type"]

        response = client.ci_auditing_audio_submit(**kwargs)
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def auditing_audio_query(args, parsed_globals):
    """查询音频审核任务结果"""
    try:
        client = init_cos_client(parsed_globals)
        response = client.ci_auditing_audio_query(
            Bucket=args["bucket"],
            JobID=args["job_id"],
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 文本审核
# ---------------------------------------------------------------------------

def auditing_text_submit(args, parsed_globals):
    """提交文本审核任务

    ci_auditing_text_submit(self, Bucket, Key=None, DetectType=None,
                            Content=None, Callback=None, BizType=None, Url=None, ...)
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]

        kwargs = {"Bucket": bucket}

        if args.get("key"):
            kwargs["Key"] = args["key"]
        if args.get("url"):
            kwargs["Url"] = args["url"]
        if args.get("content"):
            # SDK 要求 Content 是 bytes 类型
            content = args["content"]
            if isinstance(content, str):
                content = content.encode("utf-8")
            kwargs["Content"] = content

        if not (args.get("key") or args.get("url") or args.get("content")):
            raise ValueError("必须指定 key、url 或 content 参数")

        detect_type = _parse_detect_type(args.get("detect_type"))
        if detect_type is not None:
            kwargs["DetectType"] = detect_type

        if args.get("biz_type"):
            kwargs["BizType"] = args["biz_type"]

        response = client.ci_auditing_text_submit(**kwargs)
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def auditing_text_query(args, parsed_globals):
    """查询文本审核任务结果"""
    try:
        client = init_cos_client(parsed_globals)
        response = client.ci_auditing_text_query(
            Bucket=args["bucket"],
            JobID=args["job_id"],
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 文档审核
# ---------------------------------------------------------------------------

def auditing_document_submit(args, parsed_globals):
    """提交文档审核任务

    ci_auditing_document_submit(self, Bucket, Url=None, DetectType=None,
                                Key=None, Type=None, BizType=None, ...)
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]

        kwargs = {"Bucket": bucket}

        if args.get("key"):
            kwargs["Key"] = args["key"]
        if args.get("url"):
            kwargs["Url"] = args["url"]

        if not (args.get("key") or args.get("url")):
            raise ValueError("必须指定 key 或 url 参数")

        if args.get("doc_type"):
            kwargs["Type"] = args["doc_type"]

        detect_type = _parse_detect_type(args.get("detect_type"))
        if detect_type is not None:
            kwargs["DetectType"] = detect_type

        if args.get("biz_type"):
            kwargs["BizType"] = args["biz_type"]

        response = client.ci_auditing_document_submit(**kwargs)
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def auditing_document_query(args, parsed_globals):
    """查询文档审核任务结果"""
    try:
        client = init_cos_client(parsed_globals)
        response = client.ci_auditing_document_query(
            Bucket=args["bucket"],
            JobID=args["job_id"],
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 网页审核
# ---------------------------------------------------------------------------

def auditing_webpage_submit(args, parsed_globals):
    """提交网页审核任务

    ci_auditing_html_submit(self, Bucket, Url, DetectType=None,
                            ReturnHighlightHtml=False, BizType=None, ...)
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]

        kwargs = {
            "Bucket": bucket,
            "Url": args["url"],
        }

        detect_type = _parse_detect_type(args.get("detect_type"))
        if detect_type is not None:
            kwargs["DetectType"] = detect_type

        if args.get("biz_type"):
            kwargs["BizType"] = args["biz_type"]

        response = client.ci_auditing_html_submit(**kwargs)
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def auditing_webpage_query(args, parsed_globals):
    """查询网页审核任务结果"""
    try:
        client = init_cos_client(parsed_globals)
        response = client.ci_auditing_html_query(
            Bucket=args["bucket"],
            JobID=args["job_id"],
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 直播审核
# ---------------------------------------------------------------------------

def auditing_live_submit(args, parsed_globals):
    """提交直播审核任务"""
    try:
        client = init_cos_client(parsed_globals)
        kwargs = {
            "Bucket": args["bucket"],
            "Url": args["url"],
        }
        if args.get("biz_type"):
            kwargs["BizType"] = args["biz_type"]
        if args.get("callback"):
            kwargs["Callback"] = args["callback"]
        response = client.ci_auditing_live_video_submit(**kwargs)
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def auditing_live_cancel(args, parsed_globals):
    """取消直播审核任务"""
    try:
        client = init_cos_client(parsed_globals)
        response = client.ci_auditing_live_video_cancle(
            Bucket=args["bucket"],
            JobID=args["job_id"],
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 病毒检测
# ---------------------------------------------------------------------------

def auditing_virus_submit(args, parsed_globals):
    """提交病毒检测任务

    ci_auditing_virus_submit(self, Bucket, Key=None, Url=None, Callback=None, ...)
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]

        kwargs = {"Bucket": bucket}

        if args.get("key"):
            kwargs["Key"] = args["key"]
        if args.get("url"):
            kwargs["Url"] = args["url"]

        if not (args.get("key") or args.get("url")):
            raise ValueError("必须指定 key 或 url 参数")

        response = client.ci_auditing_virus_submit(**kwargs)
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def auditing_virus_query(args, parsed_globals):
    """查询病毒检测任务结果"""
    try:
        client = init_cos_client(parsed_globals)
        response = client.ci_auditing_virus_query(
            Bucket=args["bucket"],
            JobID=args["job_id"],
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 审核结果反馈
# ---------------------------------------------------------------------------

def auditing_report_badcase(args, parsed_globals):
    """审核结果反馈

    ci_auditing_report_badcase(self, Bucket, ContentType, Label,
                               SuggestedLabel, Text=None, Url=None, ...)
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]

        kwargs = {
            "Bucket": bucket,
            "ContentType": int(args["content_type"]),
            "Label": args["label"],
            "SuggestedLabel": args.get("suggestion_label") or "Block",
        }

        if args.get("url"):
            kwargs["Url"] = args["url"]
        if args.get("text"):
            kwargs["Text"] = args["text"]

        response = client.ci_auditing_report_badcase(**kwargs)
        print_result(response)
    except Exception as e:
        handle_cos_error(e)
