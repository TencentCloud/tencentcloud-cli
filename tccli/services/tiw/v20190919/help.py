# -*- coding: utf-8 -*-
DESC = "tiw-2019-09-19"
INFO = {
  "SetOnlineRecordCallback": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "客户的SdkAppId"
      },
      {
        "name": "Callback",
        "desc": "实时录制任务结果回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持 http或https协议，即回调地址以http://或https://开头。回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40258"
      }
    ],
    "desc": "设置实时录制回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40258"
  },
  "SetTranscodeCallbackKey": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "应用的SdkAppId"
      },
      {
        "name": "CallbackKey",
        "desc": "设置文档转码回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257"
      }
    ],
    "desc": "设置文档转码回调鉴权密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257"
  },
  "DescribeTranscode": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "客户的SdkAppId"
      },
      {
        "name": "TaskId",
        "desc": "文档转码任务的唯一标识Id"
      }
    ],
    "desc": "查询文档转码任务的执行进度与转码结果"
  },
  "CreateTranscode": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "客户的SdkAppId"
      },
      {
        "name": "Url",
        "desc": "需要进行转码文件地址"
      },
      {
        "name": "IsStaticPPT",
        "desc": "是否为静态PPT，默认为False；\n如果IsStaticPPT为False，后缀名为.ppt或.pptx的文档会动态转码成HTML5页面，其他格式的文档会静态转码成图片；如果IsStaticPPT为True，所有格式的文档会静态转码成图片；"
      },
      {
        "name": "MinResolution",
        "desc": "转码后文档的最小分辨率，不传、传空字符串或分辨率格式错误则使用文档原分辨率\n\n注意分辨率宽高中间为英文字母\"xyz\"的\"x\""
      },
      {
        "name": "ThumbnailResolution",
        "desc": "动态PPT转码可以为文件生成该分辨率的缩略图，不传、传空字符串或分辨率格式错误则不生成缩略图，分辨率格式同MinResolution\n\n静态转码这个参数不起作用"
      },
      {
        "name": "CompressFileType",
        "desc": "转码文件压缩格式，不传、传空字符串或不是指定的格式则不生成压缩文件，目前支持如下压缩格式：\n\nzip： 生成`.zip`压缩包\ntar.gz： 生成`.tar.gz`压缩包"
      }
    ],
    "desc": "创建一个文档转码任务"
  },
  "StartOnlineRecord": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "客户的SdkAppId"
      },
      {
        "name": "RoomId",
        "desc": "需要录制的房间号，取值范围: (1, 4294967295)"
      },
      {
        "name": "RecordUserId",
        "desc": "用于实时录制服务进房的用户ID，格式为`tic_record_user_${RoomId}_${Random}`，其中 `${RoomId} `与录制房间号对应，`${Random}`为一个随机字符串。\n该ID必须是一个单独的未在SDK中使用的ID，实时录制服务使用这个用户ID进入房间进行音视频与白板录制，若该ID和SDK中使用的ID重复，会导致SDK和录制服务互踢，影响正常录制。"
      },
      {
        "name": "RecordUserSig",
        "desc": "与RecordUserId对应的签名"
      },
      {
        "name": "GroupId",
        "desc": "白板的 IM 群组 Id，默认同房间号"
      },
      {
        "name": "Concat",
        "desc": "实时录制视频拼接参数"
      },
      {
        "name": "Whiteboard",
        "desc": "实时录制白板参数，例如白板宽高等"
      },
      {
        "name": "MixStream",
        "desc": "实时录制混流参数\n特别说明：\n1. 混流功能需要根据额外开通， 请联系腾讯云互动白板客服人员\n2. 使用混流功能，必须提供 Extras 参数，且 Extras 参数中必须包含 \"MIX_STREAM\""
      },
      {
        "name": "Extras",
        "desc": "使用到的高级功能列表\n可以选值列表：\nMIX_STREAM - 混流功能"
      },
      {
        "name": "AudioFileNeeded",
        "desc": "是否需要在结果回调中返回各路流的纯音频录制文件，文件格式为mp3"
      }
    ],
    "desc": "发起一个实时录制任务"
  },
  "StopOnlineRecord": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "客户的SdkAppId"
      },
      {
        "name": "TaskId",
        "desc": "需要停止录制的任务 Id"
      }
    ],
    "desc": "停止实时录制"
  },
  "PauseOnlineRecord": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "客户的SdkAppId"
      },
      {
        "name": "TaskId",
        "desc": "实时录制任务 Id"
      }
    ],
    "desc": "暂停实时录制"
  },
  "SetTranscodeCallback": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "客户的SdkAppId"
      },
      {
        "name": "Callback",
        "desc": "文档转码进度回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持http或https协议，即回调地址以http://或https://开头。\n回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260"
      }
    ],
    "desc": "设置文档转码回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260"
  },
  "SetOnlineRecordCallbackKey": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "应用的SdkAppId"
      },
      {
        "name": "CallbackKey",
        "desc": "设置实时录制回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥。回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257"
      }
    ],
    "desc": "设置实时录制回调鉴权密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257"
  },
  "ResumeOnlineRecord": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "客户的SdkAppId"
      },
      {
        "name": "TaskId",
        "desc": "恢复录制的实时录制任务 Id"
      }
    ],
    "desc": "恢复实时录制"
  },
  "DescribeOnlineRecordCallback": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "应用的SdkAppId"
      }
    ],
    "desc": "查询实时录制回调地址"
  },
  "DescribeTranscodeCallback": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "应用的SdkAppId"
      }
    ],
    "desc": "查询文档转码回调地址"
  },
  "DescribeOnlineRecord": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "客户的SdkAppId"
      },
      {
        "name": "TaskId",
        "desc": "实时录制任务Id"
      }
    ],
    "desc": "查询实时录制任务状态与结果"
  }
}