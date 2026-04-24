# encoding: utf-8
"""
CI (Cloud Infinite / 数据万象) 命令行工具插件

将数据万象的全部功能集成到 TCCLI 中，包括六大类：

一、图片处理：
  - image_process:         图片下载时处理
  - image_process_saveas:  图片云上处理另存
  - image_upload_process:  图片上传时处理
  - image_info:            获取图片基本信息
  - image_exif_info:       获取图片 EXIF 信息
  - image_ave_color:       获取图片主色调
  - image_inspect:         异常图片检测
  - image_style_add:       添加图片样式
  - image_style_get:       查询图片样式
  - image_style_delete:    删除图片样式

二、内容审核：
  - auditing_image:              图片批量审核（同步）
  - auditing_video_submit:       提交视频审核
  - auditing_video_query:        查询视频审核结果
  - auditing_audio_submit:       提交音频审核
  - auditing_audio_query:        查询音频审核结果
  - auditing_text_submit:        提交文本审核
  - auditing_text_query:         查询文本审核结果
  - auditing_document_submit:    提交文档审核
  - auditing_document_query:     查询文档审核结果
  - auditing_webpage_submit:     提交网页审核
  - auditing_webpage_query:      查询网页审核结果
  - auditing_live_submit:        提交直播审核
  - auditing_live_cancel:        取消直播审核
  - auditing_virus_submit:       提交病毒检测
  - auditing_virus_query:        查询病毒检测结果
  - auditing_report_badcase:     举报不良内容

三、媒体处理：
  - video_snapshot:        视频同步截帧
  - media_info:            获取媒体文件信息
  - media_job_submit:      创建媒体处理异步任务
  - media_job_query:       查询媒体处理任务
  - media_job_list:        列出媒体处理任务
  - media_job_cancel:      取消媒体处理任务

四、内容识别：
  - ai_image_coloring:     AI 图片上色
  - ai_enhance_image:      AI 图片增强
  - ai_image_crop:         AI 智能裁剪
  - ai_image_repair:       AI 图片修复
  - ai_detect_face:        AI 人脸检测
  - ai_face_effect:        AI 人脸特效
  - ai_body_recognition:   AI 人体识别
  - ai_id_card_ocr:        身份证 OCR 识别
  - ai_license_rec:        行驶证/驾驶证识别
  - ai_game_rec:           游戏场景识别
  - ocr_process:           通用 OCR 文字识别
  - detect_label:          图片标签识别
  - detect_car:            车辆识别
  - assess_quality:        图片质量评估
  - qrcode_detect:         二维码识别
  - qrcode_generate:       二维码生成
  - super_resolution:      图片超分辨率
  - goods_matting:         商品抠图
  - pic_matting:           通用抠图
  - portrait_matting:      人像抠图

五、文档处理：
  - doc_preview:           同步文档预览（转图片）
  - doc_preview_html:      HTML 文档在线预览
  - doc_job_submit:        提交异步文档转码任务
  - doc_job_query:         查询异步文档转码任务
  - doc_job_list:          列出异步文档转码任务

六、文件处理：
  - file_hash:             同步计算文件哈希
  - file_hash_job_submit:  提交异步哈希计算任务
  - file_uncompress_submit:提交文件解压缩任务
  - file_compress_submit:  提交文件压缩任务
  - file_zip_preview:      预览压缩包内容
  - file_process_jobs_query: 查询文件处理任务
"""

# ---- 图片处理（含基础处理 + EXIF/主色调/异常图片检测/样式管理）----
from .image_process import (
    image_process, image_info,
    image_process_saveas, image_upload_process,
    image_exif_info, image_ave_color, image_inspect,
    image_style_add, image_style_get, image_style_delete,
)

# ---- 媒体处理（含同步截帧/媒体信息 + 异步任务）----
from .media_process import (
    video_snapshot, media_info,
    media_job_submit, media_job_query,
    media_job_list, media_job_cancel,
)

# ---- 内容审核 ----
from .auditing import (
    auditing_image,
    auditing_video_submit, auditing_video_query,
    auditing_audio_submit, auditing_audio_query,
    auditing_text_submit, auditing_text_query,
    auditing_document_submit, auditing_document_query,
    auditing_webpage_submit, auditing_webpage_query,
    auditing_live_submit, auditing_live_cancel,
    auditing_virus_submit, auditing_virus_query,
    auditing_report_badcase,
)

# ---- 内容识别（AI）----
from .ai_recognition import (
    ai_image_coloring, ai_enhance_image, ai_image_crop, ai_image_repair,
    ai_detect_face, ai_face_effect, ai_body_recognition,
    ai_id_card_ocr, ai_license_rec, ai_game_rec,
    ocr_process, detect_label, detect_car, assess_quality,
    qrcode_detect, qrcode_generate, super_resolution,
    goods_matting, pic_matting, portrait_matting,
)

# ---- 文档处理 ----
from .doc_process import (
    doc_preview, doc_preview_html,
    doc_job_submit, doc_job_query, doc_job_list,
)

# ---- 文件处理 ----
from .file_process import (
    file_hash, file_hash_job_submit,
    file_uncompress_submit, file_compress_submit,
    file_zip_preview, file_process_jobs_query,
)

service_name = "ci"
service_version = "2021-02-24"

# =====================================================================
# 辅助函数：构建 Request/Response 参数成员
# =====================================================================

def _member(name, required=False, doc=""):
    """构建参数成员定义的快捷函数"""
    return {
        "name": name,
        "member": "string",
        "type": "string",
        "required": required,
        "document": doc,
    }


def _bucket(doc="存储桶名称，格式如 my-bucket-1250000000"):
    return _member("bucket", required=True, doc=doc)


def _key(doc="COS 对象键"):
    return _member("key", required=True, doc=doc)


def _optional_key(doc="COS 对象键"):
    return _member("key", required=False, doc=doc)


def _output(doc="本地保存路径"):
    return _member("local_path", required=False, doc=doc)


def _job_id(doc="任务 ID"):
    return _member("job_id", required=True, doc=doc)


# =====================================================================
# _spec 定义
# =====================================================================

_spec = {
    "metadata": {
        "serviceShortName": service_name,
        "apiVersion": service_version,
        "description": "CI (Cloud Infinite / 数据万象) 全功能命令行工具",
    },
    "actions": {
        # ==============================================================
        # 一、图片处理
        # ==============================================================
        "image_process": {
            "name": "图片下载时处理",
            "document": "对COS上的图片进行实时处理并下载到本地（原图不变）。"
                        "支持所有数据万象处理规则：缩放、裁剪、旋转、格式转换、水印等。"
                        "多步处理可使用管道操作符 | 连接。"
                        "rule参考：https://cloud.tencent.com/document/product/460/6924",
            "input": "image_processRequest",
            "output": "image_processResponse",
            "action_caller": image_process,
        },
        "image_process_saveas": {
            "name": "图片云上处理另存",
            "document": "对COS上已有的图片进行处理，结果另存为新的对象（原图不变）。"
                        "rule参考：https://cloud.tencent.com/document/product/460/6924",
            "input": "image_process_saveasRequest",
            "output": "image_process_saveasResponse",
            "action_caller": image_process_saveas,
        },
        "image_upload_process": {
            "name": "图片上传时处理",
            "document": "将本地图片上传到COS，上传的同时进行图片处理并保存结果。"
                        "rule参考：https://cloud.tencent.com/document/product/460/6924",
            "input": "image_upload_processRequest",
            "output": "image_upload_processResponse",
            "action_caller": image_upload_process,
        },
        "image_info": {
            "name": "获取图片信息",
            "document": "获取COS上图片的基本信息，包括格式、尺寸、大小等",
            "input": "image_infoRequest",
            "output": "image_infoResponse",
            "action_caller": image_info,
        },

        # ---- 图片处理补充 ----
        "image_exif_info": {
            "name": "获取图片 EXIF 信息",
            "document": "获取COS上图片的EXIF元数据（拍摄设备、时间、GPS等）",
            "input": "image_exif_infoRequest",
            "output": "image_exif_infoResponse",
            "action_caller": image_exif_info,
        },
        "image_ave_color": {
            "name": "获取图片主色调",
            "document": "获取COS上图片的平均主色调（十六进制颜色值）",
            "input": "image_ave_colorRequest",
            "output": "image_ave_colorResponse",
            "action_caller": image_ave_color,
        },
        "image_inspect": {
            "name": "异常图片检测",
            "document": "检测COS上图片中是否隐含其他类型的可疑文件（如在图片格式中嵌入视频或其他文件）。"
                        "API参考：https://cloud.tencent.com/document/product/460/75997",
            "input": "image_inspectRequest",
            "output": "image_inspectResponse",
            "action_caller": image_inspect,
        },
        "image_style_add": {
            "name": "添加图片样式",
            "document": "为存储桶添加图片处理样式，以便后续通过样式名称快速应用处理规则",
            "input": "image_style_addRequest",
            "output": "image_style_addResponse",
            "action_caller": image_style_add,
        },
        "image_style_get": {
            "name": "查询图片样式",
            "document": "查询存储桶已设置的图片处理样式列表",
            "input": "image_style_getRequest",
            "output": "image_style_getResponse",
            "action_caller": image_style_get,
        },
        "image_style_delete": {
            "name": "删除图片样式",
            "document": "删除存储桶已有的图片处理样式",
            "input": "image_style_deleteRequest",
            "output": "image_style_deleteResponse",
            "action_caller": image_style_delete,
        },

        # ==============================================================
        # 二、内容审核
        # ==============================================================
        "auditing_image": {
            "name": "图片批量审核",
            "document": "对一张或多张图片进行内容审核（同步），支持检测涉黄、涉政、广告等违规内容。"
                        "API参考：https://cloud.tencent.com/document/product/460/37318",
            "input": "auditing_imageRequest",
            "output": "auditing_imageResponse",
            "action_caller": auditing_image,
        },
        "auditing_video_submit": {
            "name": "提交视频审核",
            "document": "提交视频内容审核异步任务，审核结果通过查询接口获取。"
                        "支持截帧审核和音频审核。",
            "input": "auditing_video_submitRequest",
            "output": "auditing_video_submitResponse",
            "action_caller": auditing_video_submit,
        },
        "auditing_video_query": {
            "name": "查询视频审核结果",
            "document": "查询视频审核异步任务的结果",
            "input": "auditing_video_queryRequest",
            "output": "auditing_video_queryResponse",
            "action_caller": auditing_video_query,
        },
        "auditing_audio_submit": {
            "name": "提交音频审核",
            "document": "提交音频内容审核异步任务",
            "input": "auditing_audio_submitRequest",
            "output": "auditing_audio_submitResponse",
            "action_caller": auditing_audio_submit,
        },
        "auditing_audio_query": {
            "name": "查询音频审核结果",
            "document": "查询音频审核异步任务的结果",
            "input": "auditing_audio_queryRequest",
            "output": "auditing_audio_queryResponse",
            "action_caller": auditing_audio_query,
        },
        "auditing_text_submit": {
            "name": "提交文本审核",
            "document": "提交文本内容审核异步任务，支持COS对象、URL和直接文本内容",
            "input": "auditing_text_submitRequest",
            "output": "auditing_text_submitResponse",
            "action_caller": auditing_text_submit,
        },
        "auditing_text_query": {
            "name": "查询文本审核结果",
            "document": "查询文本审核异步任务的结果",
            "input": "auditing_text_queryRequest",
            "output": "auditing_text_queryResponse",
            "action_caller": auditing_text_query,
        },
        "auditing_document_submit": {
            "name": "提交文档审核",
            "document": "提交文档内容审核异步任务，支持PDF/Word/Excel/PPT等格式",
            "input": "auditing_document_submitRequest",
            "output": "auditing_document_submitResponse",
            "action_caller": auditing_document_submit,
        },
        "auditing_document_query": {
            "name": "查询文档审核结果",
            "document": "查询文档审核异步任务的结果",
            "input": "auditing_document_queryRequest",
            "output": "auditing_document_queryResponse",
            "action_caller": auditing_document_query,
        },
        "auditing_webpage_submit": {
            "name": "提交网页审核",
            "document": "提交网页内容审核异步任务",
            "input": "auditing_webpage_submitRequest",
            "output": "auditing_webpage_submitResponse",
            "action_caller": auditing_webpage_submit,
        },
        "auditing_webpage_query": {
            "name": "查询网页审核结果",
            "document": "查询网页审核异步任务的结果",
            "input": "auditing_webpage_queryRequest",
            "output": "auditing_webpage_queryResponse",
            "action_caller": auditing_webpage_query,
        },
        "auditing_live_submit": {
            "name": "提交直播审核",
            "document": "提交直播流内容审核任务，支持RTMP/HLS/FLV直播流",
            "input": "auditing_live_submitRequest",
            "output": "auditing_live_submitResponse",
            "action_caller": auditing_live_submit,
        },
        "auditing_live_cancel": {
            "name": "取消直播审核",
            "document": "取消正在进行的直播流审核任务",
            "input": "auditing_live_cancelRequest",
            "output": "auditing_live_cancelResponse",
            "action_caller": auditing_live_cancel,
        },
        "auditing_virus_submit": {
            "name": "提交病毒检测",
            "document": "提交文件病毒检测任务",
            "input": "auditing_virus_submitRequest",
            "output": "auditing_virus_submitResponse",
            "action_caller": auditing_virus_submit,
        },
        "auditing_virus_query": {
            "name": "查询病毒检测结果",
            "document": "查询病毒检测任务的结果",
            "input": "auditing_virus_queryRequest",
            "output": "auditing_virus_queryResponse",
            "action_caller": auditing_virus_query,
        },
        "auditing_report_badcase": {
            "name": "审核结果反馈",
            "document": "审核结果反馈，用于反馈审核漏检",
            "input": "auditing_report_badcaseRequest",
            "output": "auditing_report_badcaseResponse",
            "action_caller": auditing_report_badcase,
        },

        # ==============================================================
        # 三、媒体处理
        # ==============================================================
        "video_snapshot": {
            "name": "视频同步截帧",
            "document": "对COS上的视频文件进行同步截帧，获取指定时间点的画面截图并下载到本地。"
                        "API参考：https://cloud.tencent.com/document/product/460/49283",
            "input": "video_snapshotRequest",
            "output": "video_snapshotResponse",
            "action_caller": video_snapshot,
        },
        "media_info": {
            "name": "获取媒体信息",
            "document": "获取COS上媒体文件（视频/音频）的详细信息。"
                        "API参考：https://cloud.tencent.com/document/product/460/49284",
            "input": "media_infoRequest",
            "output": "media_infoResponse",
            "action_caller": media_info,
        },
        "media_job_submit": {
            "name": "创建媒体处理任务",
            "document": "创建异步媒体处理任务，支持转码、截帧、动图、拼接、智能封面等。"
                        "通过 tag 参数指定任务类型：Transcode/Snapshot/Animation/Concat/"
                        "SmartCover/VideoProcess/VideoMontage/VoiceSeparate/SDRtoHDR/"
                        "DigitalWatermark/SuperResolution/VideoTag 等。"
                        "操作参数通过 operation（JSON字符串）传入。",
            "input": "media_job_submitRequest",
            "output": "media_job_submitResponse",
            "action_caller": media_job_submit,
        },
        "media_job_query": {
            "name": "查询媒体处理任务",
            "document": "查询指定的媒体处理异步任务的状态和结果",
            "input": "media_job_queryRequest",
            "output": "media_job_queryResponse",
            "action_caller": media_job_query,
        },
        "media_job_list": {
            "name": "列出媒体处理任务",
            "document": "列出指定类型的媒体处理任务列表",
            "input": "media_job_listRequest",
            "output": "media_job_listResponse",
            "action_caller": media_job_list,
        },
        "media_job_cancel": {
            "name": "取消媒体处理任务",
            "document": "取消指定的媒体处理异步任务",
            "input": "media_job_cancelRequest",
            "output": "media_job_cancelResponse",
            "action_caller": media_job_cancel,
        },

        # ==============================================================
        # 四、内容识别（AI）
        # ==============================================================
        "ai_image_coloring": {
            "name": "AI 图片上色",
            "document": "将黑白图片进行智能上色，支持 COS 对象或外部 URL",
            "input": "ai_image_coloringRequest",
            "output": "ai_image_coloringResponse",
            "action_caller": ai_image_coloring,
        },
        "ai_enhance_image": {
            "name": "AI 图片增强",
            "document": "对图片进行清晰度增强和去噪处理",
            "input": "ai_enhance_imageRequest",
            "output": "ai_enhance_imageResponse",
            "action_caller": ai_enhance_image,
        },
        "ai_image_crop": {
            "name": "AI 智能裁剪",
            "document": "基于 AI 识别图片主体，自动进行智能裁剪",
            "input": "ai_image_cropRequest",
            "output": "ai_image_cropResponse",
            "action_caller": ai_image_crop,
        },
        "ai_image_repair": {
            "name": "AI 图片修复",
            "document": "对图片进行智能修复，去除遮挡物",
            "input": "ai_image_repairRequest",
            "output": "ai_image_repairResponse",
            "action_caller": ai_image_repair,
        },
        "ai_detect_face": {
            "name": "AI 人脸检测",
            "document": "检测图片中的人脸位置和属性信息",
            "input": "ai_detect_faceRequest",
            "output": "ai_detect_faceResponse",
            "action_caller": ai_detect_face,
        },
        "ai_face_effect": {
            "name": "AI 人脸特效",
            "document": "对图片中的人脸进行特效处理（年龄变换、性别转换等）",
            "input": "ai_face_effectRequest",
            "output": "ai_face_effectResponse",
            "action_caller": ai_face_effect,
        },
        "ai_body_recognition": {
            "name": "AI 人体识别",
            "document": "检测图片中的人体位置",
            "input": "ai_body_recognitionRequest",
            "output": "ai_body_recognitionResponse",
            "action_caller": ai_body_recognition,
        },
        "ai_id_card_ocr": {
            "name": "身份证 OCR 识别",
            "document": "识别身份证正面/背面信息",
            "input": "ai_id_card_ocrRequest",
            "output": "ai_id_card_ocrResponse",
            "action_caller": ai_id_card_ocr,
        },
        "ai_license_rec": {
            "name": "行驶证/驾驶证识别",
            "document": "识别行驶证或驾驶证信息",
            "input": "ai_license_recRequest",
            "output": "ai_license_recResponse",
            "action_caller": ai_license_rec,
        },
        "ai_game_rec": {
            "name": "游戏场景识别",
            "document": "识别游戏场景截图的内容",
            "input": "ai_game_recRequest",
            "output": "ai_game_recResponse",
            "action_caller": ai_game_rec,
        },
        "ocr_process": {
            "name": "通用 OCR 文字识别",
            "document": "识别图片或PDF中的文字内容",
            "input": "ocr_processRequest",
            "output": "ocr_processResponse",
            "action_caller": ocr_process,
        },
        "detect_label": {
            "name": "图片标签识别",
            "document": "识别图片中的内容标签（场景、物品等）",
            "input": "detect_labelRequest",
            "output": "detect_labelResponse",
            "action_caller": detect_label,
        },
        "detect_car": {
            "name": "车辆识别",
            "document": "识别图片中的车辆品牌、型号、颜色等信息",
            "input": "detect_carRequest",
            "output": "detect_carResponse",
            "action_caller": detect_car,
        },
        "assess_quality": {
            "name": "图片质量评估",
            "document": "评估图片的美学质量分数",
            "input": "assess_qualityRequest",
            "output": "assess_qualityResponse",
            "action_caller": assess_quality,
        },
        "qrcode_detect": {
            "name": "二维码识别",
            "document": "识别图片中的二维码/条形码内容",
            "input": "qrcode_detectRequest",
            "output": "qrcode_detectResponse",
            "action_caller": qrcode_detect,
        },
        "qrcode_generate": {
            "name": "二维码生成",
            "document": "根据文本内容生成二维码图片",
            "input": "qrcode_generateRequest",
            "output": "qrcode_generateResponse",
            "action_caller": qrcode_generate,
        },
        "super_resolution": {
            "name": "图片超分辨率",
            "document": "将图片放大并提升清晰度",
            "input": "super_resolutionRequest",
            "output": "super_resolutionResponse",
            "action_caller": super_resolution,
        },
        "goods_matting": {
            "name": "商品抠图",
            "document": "自动识别并抠出图片中的商品主体",
            "input": "goods_mattingRequest",
            "output": "goods_mattingResponse",
            "action_caller": goods_matting,
        },
        "pic_matting": {
            "name": "通用抠图",
            "document": "自动识别并抠出图片前景主体",
            "input": "pic_mattingRequest",
            "output": "pic_mattingResponse",
            "action_caller": pic_matting,
        },
        "portrait_matting": {
            "name": "人像抠图",
            "document": "自动识别并抠出图片中的人像",
            "input": "portrait_mattingRequest",
            "output": "portrait_mattingResponse",
            "action_caller": portrait_matting,
        },

        # ==============================================================
        # 五、文档处理
        # ==============================================================
        "doc_preview": {
            "name": "同步文档预览",
            "document": "将文档（PDF/Word/Excel/PPT等）同步转为图片并下载到本地",
            "input": "doc_previewRequest",
            "output": "doc_previewResponse",
            "action_caller": doc_preview,
        },
        "doc_preview_html": {
            "name": "HTML 文档在线预览",
            "document": "获取文档的 HTML 预览内容",
            "input": "doc_preview_htmlRequest",
            "output": "doc_preview_htmlResponse",
            "action_caller": doc_preview_html,
        },
        "doc_job_submit": {
            "name": "提交文档转码任务",
            "document": "提交异步文档转码任务，将文档转为图片或PDF",
            "input": "doc_job_submitRequest",
            "output": "doc_job_submitResponse",
            "action_caller": doc_job_submit,
        },
        "doc_job_query": {
            "name": "查询文档转码任务",
            "document": "查询异步文档转码任务的状态和结果",
            "input": "doc_job_queryRequest",
            "output": "doc_job_queryResponse",
            "action_caller": doc_job_query,
        },
        "doc_job_list": {
            "name": "列出文档转码任务",
            "document": "列出异步文档转码任务列表",
            "input": "doc_job_listRequest",
            "output": "doc_job_listResponse",
            "action_caller": doc_job_list,
        },

        # ==============================================================
        # 六、文件处理
        # ==============================================================
        "file_hash": {
            "name": "同步计算文件哈希",
            "document": "同步计算COS上文件的哈希值（MD5/SHA1/SHA256）",
            "input": "file_hashRequest",
            "output": "file_hashResponse",
            "action_caller": file_hash,
        },
        "file_hash_job_submit": {
            "name": "提交异步哈希计算任务",
            "document": "提交异步文件哈希计算任务",
            "input": "file_hash_job_submitRequest",
            "output": "file_hash_job_submitResponse",
            "action_caller": file_hash_job_submit,
        },
        "file_uncompress_submit": {
            "name": "提交文件解压缩任务",
            "document": "提交COS上压缩文件的解压缩任务",
            "input": "file_uncompress_submitRequest",
            "output": "file_uncompress_submitResponse",
            "action_caller": file_uncompress_submit,
        },
        "file_compress_submit": {
            "name": "提交文件压缩任务",
            "document": "将COS上的多个文件压缩为一个压缩包",
            "input": "file_compress_submitRequest",
            "output": "file_compress_submitResponse",
            "action_caller": file_compress_submit,
        },
        "file_zip_preview": {
            "name": "预览压缩包内容",
            "document": "列出COS上压缩包内的文件列表",
            "input": "file_zip_previewRequest",
            "output": "file_zip_previewResponse",
            "action_caller": file_zip_preview,
        },
        "file_process_jobs_query": {
            "name": "查询文件处理任务",
            "document": "查询文件处理（哈希/压缩/解压）任务的状态和结果",
            "input": "file_process_jobs_queryRequest",
            "output": "file_process_jobs_queryResponse",
            "action_caller": file_process_jobs_query,
        },
    },

    "objects": {

        # ==============================================================
        # 图片处理
        # ==============================================================
        "image_processRequest": {
            "members": [
                _bucket(),
                _key(doc="图片在COS上的对象键（Key）"),
                _member("rule", required=True, doc="数据万象处理规则，如 imageView2/2/w/800/h/600"),
                _output(doc="处理后的图片保存到本地的路径，默认保存到当前目录"),
            ],
        },
        "image_processResponse": {
            "members": [
                _member("Status", doc="操作状态，成功返回 Success"),
                _member("Output", doc="处理后图片保存的本地路径"),
                _member("ContentType", doc="处理后图片的 Content-Type"),
                _member("ContentLength", doc="处理后图片的大小（字节）"),
            ],
        },
        "image_process_saveasRequest": {
            "members": [
                _bucket(),
                _key(doc="原图在COS上的对象键"),
                _member("rule", required=True, doc="数据万象处理规则"),
                _member("savekey", required=True, doc="处理后图片在COS上的存储路径"),
            ],
        },
        "image_process_saveasResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("RequestId", doc="请求ID"),
                _member("OriginalImage", doc="原图信息（Format、Width、Height）"),
                _member("ProcessedImages", doc="处理后的图片信息列表"),
            ],
        },
        "image_upload_processRequest": {
            "members": [
                _bucket(),
                _member("local", required=True, doc="本地图片文件路径"),
                _key(doc="上传到COS的对象键（原图存储路径）"),
                _member("rule", required=True, doc="数据万象处理规则"),
                _member("savekey", required=False, doc="处理后图片的存储路径，默认与 key 相同（覆盖原图）"),
            ],
        },
        "image_upload_processResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("RequestId", doc="请求ID"),
                _member("OriginalImage", doc="原图信息"),
                _member("ProcessedImages", doc="处理后的图片信息列表"),
            ],
        },
        "image_infoRequest": {
            "members": [_bucket(), _key(doc="图片在COS上的对象键")],
        },
        "image_infoResponse": {
            "members": [
                _member("format", doc="图片格式"),
                _member("width", doc="图片宽度（像素）"),
                _member("height", doc="图片高度（像素）"),
                _member("size", doc="图片大小（字节）"),
            ],
        },
        "image_exif_infoRequest": {
            "members": [_bucket(), _key(doc="图片在COS上的对象键")],
        },
        "image_exif_infoResponse": {"members": []},

        "image_ave_colorRequest": {
            "members": [_bucket(), _key(doc="图片在COS上的对象键")],
        },
        "image_ave_colorResponse": {"members": []},

        "image_inspectRequest": {
            "members": [_bucket(), _key(doc="图片在COS上的对象键")],
        },
        "image_inspectResponse": {
            "members": [
                _member("picSize", doc="检测的原图大小（Bytes）"),
                _member("picType", doc="检测的原图类型（如 jpg、png）"),
                _member("suspicious", doc="是否检测到图片格式以外的文件（true/false）"),
                _member("suspiciousBeginByte", doc="可疑文件起始字节位置（Bytes）"),
                _member("suspiciousEndByte", doc="可疑文件末尾字节位置（Bytes）"),
                _member("suspiciousSize", doc="可疑文件大小"),
                _member("suspiciousType", doc="可疑文件类型（如 MPEG-TS）"),
            ],
        },

        "image_style_addRequest": {
            "members": [
                _bucket(),
                _member("style_name", required=True, doc="样式名称"),
                _member("style_body", required=True, doc="样式内容（处理规则）"),
            ],
        },
        "image_style_addResponse": {"members": []},

        "image_style_getRequest": {
            "members": [
                _bucket(),
                _member("style_name", doc="样式名称，不指定则列出所有"),
            ],
        },
        "image_style_getResponse": {"members": []},

        "image_style_deleteRequest": {
            "members": [
                _bucket(),
                _member("style_name", required=True, doc="样式名称"),
            ],
        },
        "image_style_deleteResponse": {"members": []},


        # ==============================================================
        # 媒体处理
        # ==============================================================
        "video_snapshotRequest": {
            "members": [
                _bucket(),
                _key(doc="视频在COS上的对象键"),
                _member("snapshot_time", required=True, doc="截帧时间点，单位为秒（支持小数，如 1.5）"),
                _member("width", doc="截图宽度（像素），范围[0,4096]，默认0表示原始宽度"),
                _member("height", doc="截图高度（像素），范围[0,4096]，默认0表示原始高度"),
                _member("format", doc="截图格式，支持 jpg/png，默认 jpg"),
                _member("mode", doc="截帧方式：exactframe(精确帧,默认) 或 keyframe(最近关键帧)"),
                _member("rotate", doc="旋转方式：auto(自动旋转,默认) 或 off(不旋转)"),
                _output(doc="截图保存到本地的路径，默认保存到当前目录"),
            ],
        },
        "video_snapshotResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("Output", doc="截图保存的本地路径"),
                _member("ContentType", doc="截图的 Content-Type"),
                _member("ContentLength", doc="截图的大小（字节）"),
                _member("SnapshotTime", doc="截帧时间点"),
            ],
        },
        "media_infoRequest": {
            "members": [_bucket(), _key(doc="媒体文件在COS上的对象键")],
        },
        "media_infoResponse": {
            "members": [
                _member("Format", doc="容器格式信息"),
                _member("Video", doc="视频流信息"),
                _member("Audio", doc="音频流信息"),
            ],
        },
        "media_job_submitRequest": {
            "members": [
                _bucket(),
                _key(doc="输入文件的COS对象键"),
                _member("tag", required=True,
                        doc="任务类型标签：Transcode/Snapshot/Animation/Concat/"
                            "SmartCover/VideoProcess/VideoMontage/VoiceSeparate/"
                            "SDRtoHDR/DigitalWatermark/SuperResolution/VideoTag等"),
                _member("operation", doc="操作参数JSON字符串"),
                _member("output_bucket", doc="输出存储桶"),
                _member("output_key", doc="输出文件的COS对象键"),
                _member("output_region", doc="输出区域"),
                _member("queue_id", doc="队列ID"),
                _member("callback", doc="回调URL"),
            ],
        },
        "media_job_submitResponse": {"members": []},

        "media_job_queryRequest": {
            "members": [_bucket(), _job_id(doc="媒体处理任务ID")],
        },
        "media_job_queryResponse": {"members": []},

        "media_job_listRequest": {
            "members": [
                _bucket(),
                _member("tag", required=True, doc="任务类型标签"),
                _member("queue_id", doc="队列ID"),
                _member("status", doc="任务状态 All/Submitted/Running/Success/Failed/Pause/Cancel"),
                _member("size", doc="每页数量，默认10"),
                _member("next_token", doc="翻页标记"),
                _member("order_by_time", doc="排序方式 Desc/Asc"),
            ],
        },
        "media_job_listResponse": {"members": []},

        "media_job_cancelRequest": {
            "members": [_bucket(), _job_id(doc="媒体处理任务ID")],
        },
        "media_job_cancelResponse": {"members": []},


        # ==============================================================
        # 内容审核
        # ==============================================================
        "auditing_imageRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键，多个用逗号分隔"),
                _member("url", doc="外部图片URL，多个用逗号分隔"),
                _member("detect_type", doc="审核类型，如 porn,ads,politics,terrorism"),
                _member("biz_type", doc="审核策略ID"),
            ],
        },
        "auditing_imageResponse": {"members": []},

        "auditing_video_submitRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部视频URL"),
                _member("detect_type", doc="审核类型"),
                _member("biz_type", doc="审核策略ID"),
                _member("snapshot_mode", doc="截帧模式 Interval/Average/KeyFrame"),
                _member("snapshot_count", doc="截帧数量"),
            ],
        },
        "auditing_video_submitResponse": {"members": []},

        "auditing_video_queryRequest": {
            "members": [_bucket(), _job_id(doc="审核任务ID")],
        },
        "auditing_video_queryResponse": {"members": []},

        "auditing_audio_submitRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部音频URL"),
                _member("detect_type", doc="审核类型"),
                _member("biz_type", doc="审核策略ID"),
            ],
        },
        "auditing_audio_submitResponse": {"members": []},

        "auditing_audio_queryRequest": {
            "members": [_bucket(), _job_id(doc="审核任务ID")],
        },
        "auditing_audio_queryResponse": {"members": []},

        "auditing_text_submitRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部文本URL"),
                _member("content", doc="纯文本内容（Base64编码）"),
                _member("detect_type", doc="审核类型"),
                _member("biz_type", doc="审核策略ID"),
            ],
        },
        "auditing_text_submitResponse": {"members": []},

        "auditing_text_queryRequest": {
            "members": [_bucket(), _job_id(doc="审核任务ID")],
        },
        "auditing_text_queryResponse": {"members": []},

        "auditing_document_submitRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部文档URL"),
                _member("doc_type", doc="文档类型 pdf/docx/pptx/xlsx等"),
                _member("detect_type", doc="审核类型"),
                _member("biz_type", doc="审核策略ID"),
            ],
        },
        "auditing_document_submitResponse": {"members": []},

        "auditing_document_queryRequest": {
            "members": [_bucket(), _job_id(doc="审核任务ID")],
        },
        "auditing_document_queryResponse": {"members": []},

        "auditing_webpage_submitRequest": {
            "members": [
                _bucket(),
                _member("url", required=True, doc="网页URL"),
                _member("detect_type", doc="审核类型"),
                _member("biz_type", doc="审核策略ID"),
            ],
        },
        "auditing_webpage_submitResponse": {"members": []},

        "auditing_webpage_queryRequest": {
            "members": [_bucket(), _job_id(doc="审核任务ID")],
        },
        "auditing_webpage_queryResponse": {"members": []},

        "auditing_live_submitRequest": {
            "members": [
                _bucket(),
                _member("url", required=True, doc="直播流URL（RTMP/HLS/FLV）"),
                _member("detect_type", doc="审核类型"),
                _member("biz_type", doc="审核策略ID"),
                _member("callback", doc="回调地址"),
            ],
        },
        "auditing_live_submitResponse": {"members": []},

        "auditing_live_cancelRequest": {
            "members": [_bucket(), _job_id(doc="审核任务ID")],
        },
        "auditing_live_cancelResponse": {"members": []},

        "auditing_virus_submitRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部文件URL"),
                _member("detect_type", doc="检测类型"),
            ],
        },
        "auditing_virus_submitResponse": {"members": []},

        "auditing_virus_queryRequest": {
            "members": [_bucket(), _job_id(doc="审核任务ID")],
        },
        "auditing_virus_queryResponse": {"members": []},

        "auditing_report_badcaseRequest": {
            "members": [
                _bucket(),
                _member("content_type", required=True, doc="内容类型 1:图片 2:视频 3:音频 4:文本"),
                _member("url", required=True, doc="被举报内容的URL"),
                _member("label", required=True, doc="恶意标签 Porn/Ads/Politics/Terrorism等"),
                _member("suggestion_label", doc="期望处理建议 Block/Review/Normal"),
            ],
        },
        "auditing_report_badcaseResponse": {"members": []},


        # ==============================================================
        # 内容识别（AI）
        # ==============================================================
        "ai_image_coloringRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _output(doc="结果图片本地保存路径"),
            ],
        },
        "ai_image_coloringResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("Output", doc="结果保存的本地路径"),
                _member("ContentType", doc="Content-Type"),
                _member("ContentLength", doc="大小（字节）"),
            ],
        },
        "ai_enhance_imageRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _member("denoise", doc="去噪强度 0-5"),
                _member("sharpen", doc="锐化强度 0-5"),
                _output(),
            ],
        },
        "ai_enhance_imageResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("Output", doc="结果保存的本地路径"),
                _member("ContentType", doc="Content-Type"),
                _member("ContentLength", doc="大小（字节）"),
            ],
        },
        "ai_image_cropRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _member("width", required=True, doc="目标宽度"),
                _member("height", required=True, doc="目标高度"),
                _member("fixed", doc="是否固定尺寸 0/1"),
                _output(),
            ],
        },
        "ai_image_cropResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("Output", doc="结果保存的本地路径"),
                _member("ContentType", doc="Content-Type"),
                _member("ContentLength", doc="大小（字节）"),
            ],
        },
        "ai_image_repairRequest": {
            "members": [
                _bucket(),
                _key(doc="COS对象键"),
                _member("mask_key", doc="遮罩图COS对象键"),
                _member("mask_url", doc="遮罩图URL"),
                _output(),
            ],
        },
        "ai_image_repairResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("Output", doc="结果保存的本地路径"),
                _member("ContentType", doc="Content-Type"),
                _member("ContentLength", doc="大小（字节）"),
            ],
        },
        "ai_detect_faceRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _member("max_face_num", doc="最大人脸数，默认1"),
            ],
        },
        "ai_detect_faceResponse": {"members": []},

        "ai_face_effectRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _member("effect_type", required=True, doc="特效类型"),
                _output(),
            ],
        },
        "ai_face_effectResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("Output", doc="结果保存的本地路径"),
                _member("ContentType", doc="Content-Type"),
                _member("ContentLength", doc="大小（字节）"),
            ],
        },
        "ai_body_recognitionRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _output(doc="结果图片本地保存路径"),
            ],
        },
        "ai_body_recognitionResponse": {"members": []},

        "ai_id_card_ocrRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _member("card_side", doc="正面FRONT/背面BACK"),
            ],
        },
        "ai_id_card_ocrResponse": {"members": []},

        "ai_license_recRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _member("card_type", doc="DRIVING 驾驶证/VEHICLE 行驶证"),
            ],
        },
        "ai_license_recResponse": {"members": []},

        "ai_game_recRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _output(doc="结果图片本地保存路径"),
            ],
        },
        "ai_game_recResponse": {"members": []},

        "ocr_processRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _member("language_type", doc="语言类型 zh/en等"),
                _member("ispdf", doc="是否是PDF true/false"),
                _member("pdf_pagenumber", doc="PDF页码"),
            ],
        },
        "ocr_processResponse": {"members": []},

        "detect_labelRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _output(doc="结果图片本地保存路径"),
            ],
        },
        "detect_labelResponse": {"members": []},
        "detect_carRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _output(doc="结果图片本地保存路径"),
            ],
        },
        "detect_carResponse": {"members": []},
        "assess_qualityRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _output(doc="结果图片本地保存路径"),
            ],
        },
        "assess_qualityResponse": {"members": []},

        "qrcode_detectRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _member("cover", doc="是否覆盖二维码区域 0/1"),
            ],
        },
        "qrcode_detectResponse": {"members": []},

        "qrcode_generateRequest": {
            "members": [
                _bucket(),
                _member("text", required=True, doc="二维码内容文本"),
                _member("width", doc="二维码宽度，默认200"),
                _member("mode", doc="生成类型 0:二维码 1:条形码"),
                _output(doc="生成的二维码图片本地保存路径"),
            ],
        },
        "qrcode_generateResponse": {"members": []},

        "super_resolutionRequest": {
            "members": [
                _bucket(),
                _key(doc="COS对象键"),
                _output(),
            ],
        },
        "super_resolutionResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("Output", doc="结果保存的本地路径"),
                _member("ContentType", doc="Content-Type"),
                _member("ContentLength", doc="大小（字节）"),
            ],
        },
        "goods_mattingRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _output(doc="结果图片本地保存路径"),
            ],
        },
        "goods_mattingResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("Output", doc="结果保存的本地路径"),
                _member("ContentType", doc="Content-Type"),
                _member("ContentLength", doc="大小（字节）"),
            ],
        },
        "pic_mattingRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _output(doc="结果图片本地保存路径"),
            ],
        },
        "pic_mattingResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("Output", doc="结果保存的本地路径"),
                _member("ContentType", doc="Content-Type"),
                _member("ContentLength", doc="大小（字节）"),
            ],
        },
        "portrait_mattingRequest": {
            "members": [
                _bucket(),
                _optional_key(doc="COS对象键"),
                _member("url", doc="外部图片URL"),
                _output(doc="结果图片本地保存路径"),
            ],
        },
        "portrait_mattingResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("Output", doc="结果保存的本地路径"),
                _member("ContentType", doc="Content-Type"),
                _member("ContentLength", doc="大小（字节）"),
            ],
        },

        # ==============================================================
        # 文档处理
        # ==============================================================
        "doc_previewRequest": {
            "members": [
                _bucket(),
                _key(doc="文档在COS上的对象键"),
                _member("page", doc="预览页码，从1开始，默认1"),
                _member("src_type", doc="源文件类型，如 pdf/docx/xlsx/pptx"),
                _member("image_type", doc="输出图片类型 png/jpg，默认png"),
                _member("dsttype", doc="输出格式 png/jpg/pdf，默认png"),
                _output(doc="预览图片保存到本地的路径"),
            ],
        },
        "doc_previewResponse": {
            "members": [
                _member("Status", doc="操作状态"),
                _member("Output", doc="保存的本地路径"),
                _member("ContentType", doc="Content-Type"),
                _member("ContentLength", doc="大小（字节）"),
                _member("Page", doc="当前页码"),
                _member("TotalPage", doc="总页数"),
                _member("TotalSheet", doc="总Sheet数（Excel）"),
            ],
        },
        "doc_preview_htmlRequest": {
            "members": [
                _bucket(),
                _key(doc="文档在COS上的对象键"),
                _member("src_type", doc="源文件类型"),
                _output(doc="保存HTML内容到本地的路径"),
            ],
        },
        "doc_preview_htmlResponse": {"members": []},

        "doc_job_submitRequest": {
            "members": [
                _bucket(),
                _key(doc="文档在COS上的对象键"),
                _member("output_bucket", doc="输出存储桶，默认同bucket"),
                _member("output_key", required=True, doc="输出文件的COS对象键"),
                _member("src_type", doc="源文件类型"),
                _member("tgt_type", doc="目标文件类型 png/jpg/pdf，默认png"),
                _member("start_page", doc="起始页码，默认1"),
                _member("end_page", doc="结束页码，默认-1（所有页）"),
                _member("sheet_id", doc="Sheet编号（Excel文件）"),
            ],
        },
        "doc_job_submitResponse": {"members": []},

        "doc_job_queryRequest": {
            "members": [_bucket(), _job_id(doc="文档转码任务ID")],
        },
        "doc_job_queryResponse": {"members": []},

        "doc_job_listRequest": {
            "members": [
                _bucket(),
                _member("size", doc="每页数量，默认10"),
                _member("page", doc="页码，默认1"),
                _member("status", doc="任务状态 All/Submitted/Running/Success/Failed/Pause/Cancel"),
            ],
        },
        "doc_job_listResponse": {"members": []},


        # ==============================================================
        # 文件处理
        # ==============================================================
        "file_hashRequest": {
            "members": [
                _bucket(),
                _key(doc="COS对象键"),
                _member("hash_type", required=True, doc="哈希类型 md5/sha1/sha256"),
                _member("add_to_header", doc="是否将哈希值写入自定义头部 true/false"),
            ],
        },
        "file_hashResponse": {"members": []},

        "file_hash_job_submitRequest": {
            "members": [
                _bucket(),
                _key(doc="COS对象键"),
                _member("hash_type", required=True, doc="哈希类型 md5/sha1/sha256"),
                _member("add_to_header", doc="是否将哈希值写入自定义头部"),
                _member("callback", doc="回调地址"),
            ],
        },
        "file_hash_job_submitResponse": {"members": []},

        "file_uncompress_submitRequest": {
            "members": [
                _bucket(),
                _key(doc="COS上的压缩文件对象键"),
                _member("output_bucket", doc="解压输出的存储桶，默认同bucket"),
                _member("output_prefix", doc="解压输出的前缀路径"),
                _member("password", doc="压缩包密码"),
            ],
        },
        "file_uncompress_submitResponse": {"members": []},

        "file_compress_submitRequest": {
            "members": [
                _bucket(),
                _member("keys", required=True, doc="要压缩的COS对象键列表，逗号分隔"),
                _member("output_key", required=True, doc="压缩后文件的COS对象键"),
                _member("compress_format", doc="压缩格式 zip/tar/tar.gz，默认zip"),
                _member("prefix", doc="压缩包内文件前缀"),
            ],
        },
        "file_compress_submitResponse": {"members": []},

        "file_zip_previewRequest": {
            "members": [_bucket(), _key(doc="压缩包在COS上的对象键")],
        },
        "file_zip_previewResponse": {"members": []},

        "file_process_jobs_queryRequest": {
            "members": [_bucket(), _job_id(doc="文件处理任务ID")],
        },
        "file_process_jobs_queryResponse": {"members": []},
    },
    "version": "1.0",
}


def register_service(specs):
    """注册 CI 服务到 TCCLI 的服务列表

    由 TCCLI 的 plugin.py 中 import_plugins() 调用。

    Args:
        specs: TCCLI 全局服务规范字典
    """
    specs[service_name] = {
        service_version: _spec,
    }
