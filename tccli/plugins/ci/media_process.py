# -*- coding: utf-8 -*-
"""
媒体处理模块

提供数据万象媒体处理全部功能的 CLI 命令，包括：

同步处理：
- video_snapshot:   视频同步截帧
- media_info:       获取媒体文件信息

异步任务：
- media_job_submit: 创建媒体处理异步任务（转码、截帧、动图、拼接、智能封面等）
- media_job_query:  查询媒体处理任务
- media_job_list:   列出媒体处理任务
- media_job_cancel: 取消媒体处理任务

所有异步媒体处理通过统一的 ci_create_media_jobs 接口，
通过 Tag 区分不同类型：
  Transcode, Snapshot, Animation, Concat, SmartCover,
  VideoProcess, VideoMontage, VoiceSeparate, SDRtoHDR,
  DigitalWatermark, ExtractDigitalWatermark, SuperResolution,
  VideoTag, Segment, QualityEstimate, SegmentVideoBody,
  MediaInfo, SoundHound, NoiseReduction, StreamExtract
"""
import json
import os
import xml.etree.ElementTree as ET

from .ci_helpers import init_cos_client, handle_cos_error, print_result, save_response_to_file


# =====================================================================
# 同步处理
# =====================================================================

def video_snapshot(args, parsed_globals):
    """视频同步截帧

    调用 SDK 的 get_snapshot 方法，同步获取视频在指定时间点的截图。
    返回截图的二进制流，直接写入本地文件。

    Args:
        args: 命令参数字典
            - bucket: 存储桶名称
            - key: 视频在 COS 上的对象键
            - snapshot_time: 截帧时间点（秒，支持小数如 1.5）
            - width: (可选) 截图宽度（像素），范围 [0,4096]，默认 0 表示原始宽度
            - height: (可选) 截图高度（像素），范围 [0,4096]，默认 0 表示原始高度
            - format: (可选) 截图格式，jpg 或 png，默认 jpg
            - mode: (可选) 截帧方式，exactframe(精确帧) 或 keyframe(最近关键帧)
            - rotate: (可选) 旋转方式，auto(自动旋转) 或 off(不旋转)
            - local_path: (可选) 截图保存到本地的路径
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]
        key = args["key"]
        time_point = args["snapshot_time"]

        # 构建可选参数
        kwargs = {}
        fmt = args.get("format") or "jpg"
        kwargs["Format"] = fmt

        width = args.get("width")
        if width is not None and width != "":
            kwargs["Width"] = int(width)

        height = args.get("height")
        if height is not None and height != "":
            kwargs["Height"] = int(height)

        mode = args.get("mode")
        if mode is not None and mode != "":
            kwargs["Mode"] = mode

        rotate = args.get("rotate")
        if rotate is not None and rotate != "":
            kwargs["Rotate"] = rotate

        # 使用 SDK 原生的 get_snapshot 方法
        response = client.get_snapshot(
            Bucket=bucket,
            Key=key,
            Time=str(time_point),
            **kwargs,
        )

        # 确定输出路径
        default_name = os.path.splitext(os.path.basename(key))[0] + "_snapshot." + fmt
        output = args.get("local_path") or default_name

        total_bytes = save_response_to_file(response, output)

        print_result({
            "Status": "Success",
            "Output": os.path.abspath(output),
            "ContentType": response.get("Content-Type", ""),
            "ContentLength": str(total_bytes),
            "SnapshotTime": str(time_point),
        }, response)
    except Exception as e:
        handle_cos_error(e)


def _xml_to_dict(element):
    """递归将 XML Element 转换为 dict

    处理规则：
    - 叶子节点：tag -> text
    - 非叶子节点：tag -> {children dict}
    - 同名多节点：tag -> [values list]

    Args:
        element: xml.etree.ElementTree.Element

    Returns:
        dict: XML 结构的字典表示
    """
    result = {}
    for child in element:
        # 去除命名空间前缀（如有）
        tag = child.tag
        if "}" in tag:
            tag = tag.split("}", 1)[1]

        if len(child) > 0:
            value = _xml_to_dict(child)
        else:
            value = child.text or ""

        # 处理同名多节点
        if tag in result:
            if not isinstance(result[tag], list):
                result[tag] = [result[tag]]
            result[tag].append(value)
        else:
            result[tag] = value

    return result


def media_info(args, parsed_globals):
    """获取媒体文件信息

    调用 SDK 的 get_media_info 方法获取媒体文件的详细信息。
    SDK 直接返回解析好的 dict 结构。

    输出内容包括：
    - MediaInfo.Format: 容器格式（FormatName、Duration、Bitrate、Size 等）
    - MediaInfo.Stream.Video: 视频流信息（CodecName、Width、Height、Fps 等）
    - MediaInfo.Stream.Audio: 音频流信息（CodecName、SampleRate、Channel 等）
    - MediaInfo.Stream.Subtitle: 字幕流信息（如有）

    Args:
        args: 命令参数字典
            - bucket: 存储桶名称
            - key: 媒体文件在 COS 上的对象键
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        # 使用 SDK 原生的 get_media_info 方法
        response = client.get_media_info(
            Bucket=args["bucket"],
            Key=args["key"],
        )

        print_result(response)
    except Exception as e:
        handle_cos_error(e)


# =====================================================================
# 异步任务
# =====================================================================

def media_job_submit(args, parsed_globals):
    """创建媒体处理异步任务

    通过 Tag 区分不同的处理类型（转码、截帧、动图等）。
    操作参数通过 JSON 字符串传入。

    Args:
        args:
            - bucket: 存储桶名称
            - key: 输入文件的 COS 对象键
            - tag: 任务类型标签，如 Transcode/Snapshot/Animation 等
            - operation: 操作参数 JSON 字符串
            - output_bucket: (可选) 输出存储桶
            - output_key: (可选) 输出文件的 COS 对象键
            - output_region: (可选) 输出区域
            - queue_id: (可选) 队列 ID
            - callback: (可选) 回调 URL
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]
        tag = args["tag"]

        # 构建操作参数
        operation = {}
        if args.get("operation"):
            operation = json.loads(args["operation"])

        # 如果指定了 output_key，构建 Output 节点
        if args.get("output_key"):
            operation["Output"] = {
                "Bucket": args.get("output_bucket") or bucket,
                "Region": args.get("output_region") or parsed_globals.get("region") or "ap-guangzhou",
                "Object": args["output_key"],
            }

        kwargs = {
            "Tag": tag,
            "Input": {"Object": args["key"]},
            "Operation": operation,
        }

        if args.get("queue_id"):
            kwargs["QueueId"] = args["queue_id"]
        if args.get("callback"):
            kwargs["CallBack"] = args["callback"]

        response = client.ci_create_media_jobs(
            Bucket=bucket,
            Jobs=kwargs,
            ContentType='application/xml',
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def media_job_query(args, parsed_globals):
    """查询媒体处理任务

    Args:
        args:
            - bucket: 存储桶名称
            - job_id: 任务 ID
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        response = client.ci_get_media_jobs(
            Bucket=args["bucket"],
            JobIDs=args["job_id"],
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def media_job_list(args, parsed_globals):
    """列出媒体处理任务

    Args:
        args:
            - bucket: 存储桶名称
            - tag: 任务类型标签
            - queue_id: (可选) 队列 ID
            - status: (可选) 任务状态 All/Submitted/Running/Success/Failed/Pause/Cancel
            - size: (可选) 每页数量，默认 10
            - next_token: (可选) 翻页标记
            - order_by_time: (可选) 排序方式 Desc/Asc
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        kwargs = {
            "Bucket": args["bucket"],
            "Tag": args["tag"],
        }

        if args.get("queue_id"):
            kwargs["QueueId"] = args["queue_id"]
        if args.get("status"):
            kwargs["States"] = args["status"]
        if args.get("size"):
            kwargs["Size"] = int(args["size"])
        if args.get("next_token"):
            kwargs["NextToken"] = args["next_token"]
        if args.get("order_by_time"):
            kwargs["OrderByTime"] = args["order_by_time"]

        response = client.ci_list_media_jobs(**kwargs)
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


def media_job_cancel(args, parsed_globals):
    """取消媒体处理任务

    Args:
        args:
            - bucket: 存储桶名称
            - job_id: 任务 ID
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        response = client.ci_cancel_jobs(
            Bucket=args["bucket"],
            JobID=args["job_id"],
        )
        print_result(response)
    except Exception as e:
        handle_cos_error(e)
