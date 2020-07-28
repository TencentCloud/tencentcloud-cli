# -*- coding: utf-8 -*-
DESC = "ams-2020-06-08"
INFO = {
  "CreateAudioModerationTask": {
    "params": [
      {
        "name": "BizType",
        "desc": "业务类型, 定义 模版策略，输出存储配置。如果没有BizType，可以先参考 【创建业务配置】接口进行创建"
      },
      {
        "name": "Type",
        "desc": "异步检测结果回调通知接收URL。支持HTTP和HTTPS"
      },
      {
        "name": "Seed",
        "desc": "回调签名key，具体可以查看签名文档。"
      },
      {
        "name": "CallbackUrl",
        "desc": "接收审核信息回调地址，如果设置，则审核过程中产生的违规音频片段和画面截帧发送此接口"
      },
      {
        "name": "Tasks",
        "desc": "输入的任务信息，最多可以同时创建10个任务"
      }
    ],
    "desc": "本接口（Audio Moderation）用于提交音频内容（包括音频文件或流地址）进行智能审核任务，使用前请您登陆控制台开通音频内容安全服务。\n\n### 功能使用说明：\n- 前往“内容安全控制台-音频内容安全”开启使用音频内容安全服务，首次开通可获得20小时免费调用时长\n\n### 接口功能说明：\n- 支持对音频流或音频文件进行检测，判断其中是否包含违规内容；\n- 支持设置回调地址 Callback 获取检测结果，或通过接口(查询音频检测结果)主动轮询获取检测结果；\n- 支持识别违规内容，包括：低俗、谩骂、色情、涉政、广告等场景；\n- 支持批量提交检测任务。检测任务列表最多支持10个；\n\n### 音频文件调用说明：\n- 音频文件大小支持：文件 < 500M；\n- 音频文件时长支持：< 1小时；\n- 音频码率类型支持：128 Kbps - 256 Kbps ；\n- 音频文件支持格式：wav、mp3、aac、flac、amr、3gp、 m4a、wma、ogg、ape；\n- 支持音视频文件分离并对音频文件进行独立识别；\n\n### 音频流调用说明：\n- 音频流时长支持：< 3小时；\n- 音频码率类型支持：128 Kbps - 256 Kbps ；\n- 音频流支持的传输协议：RTMP、HTTP、HTTPS；\n- 音频流格式支持的类型：rtp、srtp、rtmp、rtmps、mmsh、 mmst、hls、http、tcp、https、m3u8；\n- 支持音视频流分离并对音频流进行独立识别；"
  },
  "DescribeBizConfig": {
    "params": [
      {
        "name": "BizType",
        "desc": "审核业务类类型"
      }
    ],
    "desc": "查看单个配置"
  },
  "CreateBizConfig": {
    "params": [
      {
        "name": "BizType",
        "desc": "业务ID"
      },
      {
        "name": "MediaModeration",
        "desc": "审核分类信息"
      },
      {
        "name": "BizName",
        "desc": "页面名称"
      },
      {
        "name": "ModerationCategories",
        "desc": "审核内容，可选：Polity (政治); Porn (色情); Illegal(违法);Abuse (谩骂); Terror (暴恐); Ad (广告);"
      }
    ],
    "desc": "创建业务配置，1个账号最多可以创建20个配置。在创建业务配置之前，你需要以下步骤：\n1. 开通COS存储捅功能，新建存储桶，cms_segments\n2. 授权天御对 cms_segments存储桶对读写权限。\n这个存储桶用来存储 视频转换过程中生成对音频和图片。"
  },
  "DescribeTaskDetail": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID，创建任务后返回的TaskId字段"
      },
      {
        "name": "ShowAllSegments",
        "desc": "是否展示所有分片，默认只展示命中规则的分片"
      }
    ],
    "desc": "查看任务详情"
  }
}