# -*- coding: utf-8 -*-
DESC = "live-2018-08-01"
INFO = {
  "DescribeLiveCallbackTemplates": {
    "params": [],
    "desc": "获取回调模板列表"
  },
  "DropLiveStream": {
    "params": [
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
      },
      {
        "name": "AppName",
        "desc": "应用名称。"
      }
    ],
    "desc": "断开推流连接，但可以重新推流"
  },
  "CreateLiveTranscodeRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "TemplateId",
        "desc": "指定已有的模板Id。"
      }
    ],
    "desc": "创建转码规则，需要先调用[CreateLiveTranscodeTemplate](/document/product/267/32646)接口创建转码模板，将返回的模板id绑定到流使用。\n<br>转码相关文档：[直播转封装及转码](/document/product/267/32736)。"
  },
  "DescribeLiveSnapshotTemplates": {
    "params": [],
    "desc": "获取截图模板列表"
  },
  "ModifyLivePlayAuthKey": {
    "params": [
      {
        "name": "DomainName",
        "desc": "域名。"
      },
      {
        "name": "Enable",
        "desc": "是否启用，0：关闭，1：启用。"
      },
      {
        "name": "AuthKey",
        "desc": "鉴权key。"
      },
      {
        "name": "AuthDelta",
        "desc": "有效时间，单位：秒。"
      },
      {
        "name": "AuthBackKey",
        "desc": "鉴权backkey。"
      }
    ],
    "desc": "修改播放鉴权key"
  },
  "CreateLiveRecord": {
    "params": [
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "AppName",
        "desc": "推流App名。"
      },
      {
        "name": "DomainName",
        "desc": "推流域名。多域名推流必须设置。"
      },
      {
        "name": "StartTime",
        "desc": "录制开始时间。中国标准时间，需要URLEncode。如 2017-01-01 10:10:01，编码为：2017-01-01+10%3a10%3a01。\n定时录制模式，必须设置该字段；实时视频录制模式，忽略该字段。"
      },
      {
        "name": "EndTime",
        "desc": "录制结束时间。中国标准时间，需要URLEncode。如 2017-01-01 10:30:01，编码为：2017-01-01+10%3a30%3a01。\n定时录制模式，必须设置该字段；实时录制模式，为可选字段。如果通过Highlight参数，设置录制为实时视频录制模式，其设置的结束时间不应超过当前时间+30分钟，如果设置的结束时间超过当前时间+30分钟或者小于当前时间或者不设置该参数，则实际结束时间为当前时间+30分钟。"
      },
      {
        "name": "RecordType",
        "desc": "录制类型。\n“video” : 音视频录制【默认】。\n“audio” : 纯音频录制。\n在定时录制模式或实时视频录制模式下，该参数均有效，不区分大小写。"
      },
      {
        "name": "FileFormat",
        "desc": "录制文件格式。其值为：\n“flv”,“hls”,”mp4”,“aac”,”mp3”，默认“flv”。\n在定时录制模式或实时视频录制模式下，该参数均有效，不区分大小写。"
      },
      {
        "name": "Highlight",
        "desc": "开启实时视频录制模式标志。0：不开启实时视频录制模式，即采用定时录制模式【默认】；1：开启实时视频录制模式。"
      },
      {
        "name": "MixStream",
        "desc": "开启A+B=C混流C流录制标志。0：不开启A+B=C混流C流录制【默认】；1：开启A+B=C混流C流录制。\n在定时录制模式或实时视频录制模式下，该参数均有效。"
      },
      {
        "name": "StreamParam",
        "desc": "录制流参数。当前支持以下参数：\nrecord_interval - 录制分片时长，单位 秒，1800 - 7200\nstorage_time - 录制文件存储时长，单位 秒\neg. record_interval=3600&storage_time=2592000\n注：参数需要url encode。\n在定时录制模式或实时视频录制模式下，该参数均有效。"
      }
    ],
    "desc": "- 使用前提\n  1. 录制文件存放于点播平台，所以用户如需使用录制功能，需首先自行开通点播服务。\n  2. 录制文件存放后相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，具体请参考 [对应文档](https://cloud.tencent.com/document/product/266/2838)。\n\n- 模式说明\n  该接口支持两种录制模式：\n  1. 定时录制模式【默认模式】。\n    需要传入开始时间与结束时间，录制任务根据时间自动开始与结束。\n  2. 实时视频录制模式。\n    忽略传入的开始时间，在录制任务创建后立即开始录制，录制时长支持最大为30分钟，如果传入的结束时间与当前时间差大于30分钟，则按30分钟计算，实时视频录制主要用于录制精彩视频场景，时长建议控制在5分钟以内。\n\n- 注意事项\n  1. 调用接口超时设置应大于3秒，小于3秒重试以及频繁调用都有可能产生重复录制任务。"
  },
  "UpdateLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "水印ID。"
      },
      {
        "name": "PictureUrl",
        "desc": "水印图片url。"
      },
      {
        "name": "XPosition",
        "desc": "显示位置，X轴偏移。"
      },
      {
        "name": "YPosition",
        "desc": "显示位置，Y轴偏移。"
      },
      {
        "name": "WatermarkName",
        "desc": "水印名称。"
      }
    ],
    "desc": "更新水印"
  },
  "StopLiveRecord": {
    "params": [
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "TaskId",
        "desc": "任务ID，全局唯一标识录制任务。"
      }
    ],
    "desc": "说明：录制后的文件存放于点播平台。用户如需使用录制功能，需首先自行开通点播账号并确保账号可用。录制文件存放后，相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，请参考对应文档。"
  },
  "DeleteLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "水印ID。"
      }
    ],
    "desc": "删除水印"
  },
  "ModifyLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      },
      {
        "name": "TemplateName",
        "desc": "模板名称。"
      },
      {
        "name": "Description",
        "desc": "描述信息。"
      },
      {
        "name": "FlvParam",
        "desc": "Flv录制参数，开启Flv录制时设置。"
      },
      {
        "name": "HlsParam",
        "desc": "Hls录制参数，开启hls录制时设置。"
      },
      {
        "name": "Mp4Param",
        "desc": "Mp4录制参数，开启Mp4录制时设置。"
      },
      {
        "name": "AacParam",
        "desc": "Aac录制参数，开启Aac录制时设置。"
      }
    ],
    "desc": "修改录制模板配置"
  },
  "AddDelayLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "DelayTime",
        "desc": "延播时间，单位：秒，上限：600秒。"
      },
      {
        "name": "ExpireTime",
        "desc": "延播设置的过期时间。UTC 格式，例如：2018-11-29T19:00:00Z。\n注意：默认7天后过期，且最长支持7天内生效。"
      }
    ],
    "desc": "对流设置延播时间\n注意：如果在推流前设置延播，需要提前5分钟设置。\n"
  },
  "CreateLiveWatermarkRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "TemplateId",
        "desc": "水印Id，即调用[AddLiveWatermark](/document/product/267/30154)接口返回的WatermarkId。"
      }
    ],
    "desc": "创建水印规则，需要先调用[AddLiveWatermark](/document/product/267/30154)接口添加水印，将返回的水印id绑定到流使用。"
  },
  "DeleteLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      }
    ],
    "desc": "删除回调模板"
  },
  "DescribeLiveStreamEventList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始时间。 \nUTC 格式，例如：2018-12-29T19:00:00Z。\n支持查询60天内的历史记录。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间。\nUTC 格式，例如：2018-12-29T20:00:00Z。\n不超过当前时间，且和起始时间相差不得超过30天。"
      },
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称，不支持通配符（*）查询，默认模糊匹配。\n可使用IsStrict字段改为精确查询。"
      },
      {
        "name": "PageNum",
        "desc": "取得第几页。\n默认值：1。\n注： 目前只支持10000条内的查询。"
      },
      {
        "name": "PageSize",
        "desc": "分页大小。\n最大值：100。\n取值范围：1~100 之前的任意整数。\n默认值：10。\n注： 目前只支持10000条内的查询。"
      },
      {
        "name": "IsFilter",
        "desc": "是否过滤，默认不过滤。\n0：不进行任何过滤。\n1：过滤掉开播失败的，只返回开播成功的。"
      },
      {
        "name": "IsStrict",
        "desc": "是否精确查询，默认模糊匹配。\n0：模糊匹配。\n1：精确查询。\n注：使用StreamName时该参数生效。"
      },
      {
        "name": "IsAsc",
        "desc": "是否按结束时间正序显示，默认逆序。\n0：逆序。\n1：正序。"
      }
    ],
    "desc": "查询推断流事件"
  },
  "DescribeLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      }
    ],
    "desc": "获取单个转码模板"
  },
  "DescribePullStreamConfigs": {
    "params": [
      {
        "name": "ConfigId",
        "desc": "配置id。"
      }
    ],
    "desc": "查询拉流配置"
  },
  "DeleteLiveRecord": {
    "params": [
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "TaskId",
        "desc": "任务ID，全局唯一标识录制任务。"
      }
    ],
    "desc": "用于删除录制任务"
  },
  "DescribeLiveRecordTemplates": {
    "params": [],
    "desc": "获取录制模板列表"
  },
  "CreateLiveSnapshotRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      }
    ],
    "desc": "创建截图规则，需要先调用[CreateLiveSnapshotTemplate](/document/product/267/32624)接口创建截图模板，然后将返回的模板id绑定到流进行使用。\n<br>截图相关文档：[直播截图](/document/product/267/32737)。"
  },
  "ModifyLivePushAuthKey": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "Enable",
        "desc": "是否启用，0：关闭，1：启用。"
      },
      {
        "name": "MasterAuthKey",
        "desc": "主鉴权key。"
      },
      {
        "name": "BackupAuthKey",
        "desc": "备鉴权key。"
      },
      {
        "name": "AuthDelta",
        "desc": "有效时间，单位：秒。"
      }
    ],
    "desc": "修改直播推流鉴权key"
  },
  "UnBindLiveDomainCert": {
    "params": [
      {
        "name": "DomainName",
        "desc": "播放域名。"
      }
    ],
    "desc": "解绑域名证书"
  },
  "DescribeLiveSnapshotRules": {
    "params": [],
    "desc": "获取截图规则列表"
  },
  "ModifyLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      },
      {
        "name": "Vcodec",
        "desc": "视频编码：\nh264/h265。"
      },
      {
        "name": "Acodec",
        "desc": "音频编码：\naac/mp3。"
      },
      {
        "name": "AudioBitrate",
        "desc": "音频码率，默认0。0-500"
      },
      {
        "name": "Description",
        "desc": "模板描述。"
      },
      {
        "name": "VideoBitrate",
        "desc": "视频码率。100-8000"
      },
      {
        "name": "Width",
        "desc": "宽。0-3000"
      },
      {
        "name": "NeedVideo",
        "desc": "是否保留视频，0：否，1：是。默认1。"
      },
      {
        "name": "NeedAudio",
        "desc": "是否保留音频，0：否，1：是。默认1。"
      },
      {
        "name": "Height",
        "desc": "高。0-3000"
      },
      {
        "name": "Fps",
        "desc": "帧率。0-200"
      },
      {
        "name": "Gop",
        "desc": "关键帧间隔，单位：秒。0-50"
      },
      {
        "name": "Rotate",
        "desc": "旋转角度。0 90 180 270"
      },
      {
        "name": "Profile",
        "desc": "编码质量：\nbaseline/main/high。"
      },
      {
        "name": "BitrateToOrig",
        "desc": "是否不超过原始码率。0：否，1：是。默认0。"
      },
      {
        "name": "HeightToOrig",
        "desc": "是否不超过原始高。0：否，1：是。默认0。"
      },
      {
        "name": "FpsToOrig",
        "desc": "是否不超过原始帧率。0：否，1：是。默认0。"
      }
    ],
    "desc": "修改转码模板配置"
  },
  "DeleteLiveTranscodeRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。域名维度转码，域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配"
      },
      {
        "name": "AppName",
        "desc": "推流路径。域名+AppName+StreamName+TemplateId唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配"
      },
      {
        "name": "StreamName",
        "desc": "流名称。域名+AppName+StreamName+TemplateId唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配"
      },
      {
        "name": "TemplateId",
        "desc": "模板ID域名+AppName+StreamName+TemplateId唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配"
      }
    ],
    "desc": "删除转码规则"
  },
  "DeleteLiveSnapshotRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "删除截图规则"
  },
  "DescribeLiveStreamOnlineInfo": {
    "params": [
      {
        "name": "PageNum",
        "desc": "取得第几页。\n默认值：1。"
      },
      {
        "name": "PageSize",
        "desc": "分页大小。\n最大值：100。\n取值范围：1~100 之前的任意整数。\n默认值：10。"
      },
      {
        "name": "Status",
        "desc": "0:未开始推流 1:正在推流"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "查询在线推流信息列表"
  },
  "DescribeLiveWatermarks": {
    "params": [],
    "desc": "查询水印列表"
  },
  "DescribeLiveRecordRules": {
    "params": [],
    "desc": "获取录制规则列表"
  },
  "DeleteLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      }
    ],
    "desc": "删除转码模板"
  },
  "CreatePullStreamConfig": {
    "params": [
      {
        "name": "FromUrl",
        "desc": "源Url。"
      },
      {
        "name": "ToUrl",
        "desc": "目的Url，目前限制该目标地址为腾讯域名。"
      },
      {
        "name": "AreaId",
        "desc": "区域id,1-深圳,2-上海，3-天津,4-香港。"
      },
      {
        "name": "IspId",
        "desc": "运营商id,1-电信,2-移动,3-联通,4-其他,AreaId为4的时候,IspId只能为其他。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间。\n使用UTC格式时间，\n例如：2019-01-08T10:00:00Z。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，注意：\n1. 结束时间必须大于开始时间；\n2. 结束时间和开始时间必须大于当前时间；\n3. 结束时间 和 开始时间 间隔必须小于七天。\n使用UTC格式时间，\n例如：2019-01-08T10:00:00Z。"
      }
    ],
    "desc": "添加拉流配置，目前限制添加10条任务。"
  },
  "DescribeLivePlayAuthKey": {
    "params": [
      {
        "name": "DomainName",
        "desc": "域名。"
      }
    ],
    "desc": "查询播放鉴权key"
  },
  "DescribeLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      }
    ],
    "desc": "获取单个录制模板"
  },
  "DescribeLiveForbidStreamList": {
    "params": [
      {
        "name": "PageNum",
        "desc": "取得第几页，默认1。"
      },
      {
        "name": "PageSize",
        "desc": "每页大小，最大100。 \n取值：1~100之前的任意整数。\n默认值：10。"
      }
    ],
    "desc": "获取禁推流列表"
  },
  "CreateLiveRecordRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      }
    ],
    "desc": "创建录制规则，需要先调用[CreateLiveRecordTemplate](/document/product/267/32614)接口创建录制模板，将返回的模板id绑定到流使用。\n<br>录制相关文档：[直播录制](/document/product/267/32739)。"
  },
  "DeleteLiveWatermarkRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "删除水印规则"
  },
  "DeleteLiveRecordRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配"
      },
      {
        "name": "AppName",
        "desc": "推流路径。域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配"
      },
      {
        "name": "StreamName",
        "desc": "流名称。域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配"
      }
    ],
    "desc": "删除录制规则"
  },
  "DeleteLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      }
    ],
    "desc": "删除截图模板"
  },
  "CreateLiveCallbackRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径。"
      },
      {
        "name": "TemplateId",
        "desc": "模板ID"
      }
    ],
    "desc": "创建回调规则，需要先调用[CreateLiveCallbackTemplate](/document/product/267/32637)接口创建回调模板，将返回的模板id绑定到域名/路径进行使用。\n<br>回调协议相关文档：[事件消息通知](/document/product/267/32744)。"
  },
  "DeleteLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      }
    ],
    "desc": "删除录制模板"
  },
  "BindLiveDomainCert": {
    "params": [
      {
        "name": "CertId",
        "desc": "证书Id。"
      },
      {
        "name": "DomainName",
        "desc": "播放域名。"
      },
      {
        "name": "Status",
        "desc": "状态，0： 关闭  1：打开。"
      }
    ],
    "desc": "域名绑定证书"
  },
  "DescribeLiveCallbackRules": {
    "params": [],
    "desc": "获取回调规则列表"
  },
  "ModifyLiveCert": {
    "params": [
      {
        "name": "CertId",
        "desc": "证书Id。"
      },
      {
        "name": "CertType",
        "desc": "证书类型。0-用户添加证书；1-腾讯云托管证书。"
      },
      {
        "name": "CertName",
        "desc": "证书名称。"
      },
      {
        "name": "HttpsCrt",
        "desc": "证书内容，即公钥。"
      },
      {
        "name": "HttpsKey",
        "desc": "私钥。"
      },
      {
        "name": "Description",
        "desc": "描述信息。"
      }
    ],
    "desc": "修改证书"
  },
  "DescribeLiveStreamPublishedList": {
    "params": [
      {
        "name": "DomainName",
        "desc": "您的域名。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间。\nUTC 格式，例如：2016-06-30T19:00:00Z。\n不超过当前时间。"
      },
      {
        "name": "StartTime",
        "desc": "起始时间。 \nUTC 格式，例如：2016-06-29T19:00:00Z。\n和当前时间相隔不超过7天。"
      },
      {
        "name": "AppName",
        "desc": "直播流所属应用名称。"
      },
      {
        "name": "PageNum",
        "desc": "取得第几页。\n默认值：1。"
      },
      {
        "name": "PageSize",
        "desc": "分页大小。\n最大值：100。\n取值范围：1~100 之前的任意整数。\n默认值：10。"
      }
    ],
    "desc": "返回已经推过流的流列表"
  },
  "ModifyLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      },
      {
        "name": "TemplateName",
        "desc": "模板名称。"
      },
      {
        "name": "Description",
        "desc": "描述信息。"
      },
      {
        "name": "SnapshotInterval",
        "desc": "截图时间间隔"
      },
      {
        "name": "Width",
        "desc": "截图宽度。"
      },
      {
        "name": "Height",
        "desc": "截图高度。"
      },
      {
        "name": "PornFlag",
        "desc": "是否开启鉴黄，0：不开启，1：开启。"
      },
      {
        "name": "CosAppId",
        "desc": "Cos AppId。"
      },
      {
        "name": "CosBucket",
        "desc": "Cos Bucket名称。"
      },
      {
        "name": "CosRegion",
        "desc": "Cos 地域。"
      }
    ],
    "desc": "修改截图模板配置"
  },
  "ModifyLiveDomainCert": {
    "params": [
      {
        "name": "DomainName",
        "desc": "播放域名。"
      },
      {
        "name": "CertId",
        "desc": "证书Id。"
      },
      {
        "name": "Status",
        "desc": "状态，0：关闭  1：打开。"
      }
    ],
    "desc": "修改域名和证书绑定信息"
  },
  "ResumeDelayLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "恢复延迟播放设置"
  },
  "DescribeLiveDomainCert": {
    "params": [
      {
        "name": "DomainName",
        "desc": "播放域名。"
      }
    ],
    "desc": "获取域名证书信息"
  },
  "CreateLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "模板名称，例：900 900p 仅支持字母和数字的组合。"
      },
      {
        "name": "VideoBitrate",
        "desc": "视频码率。"
      },
      {
        "name": "Vcodec",
        "desc": "视频编码：\nh264/h265。默认h264"
      },
      {
        "name": "Acodec",
        "desc": "音频编码：\naac/mp3。默认原始音频格式"
      },
      {
        "name": "AudioBitrate",
        "desc": "音频码率：默认0。0-500"
      },
      {
        "name": "Description",
        "desc": "模板描述。"
      },
      {
        "name": "Width",
        "desc": "高，默认0。"
      },
      {
        "name": "NeedVideo",
        "desc": "是否保留视频，0：否，1：是。默认1。"
      },
      {
        "name": "NeedAudio",
        "desc": "是否保留音频，0：否，1：是。默认1。"
      },
      {
        "name": "Height",
        "desc": "宽，默认0。"
      },
      {
        "name": "Fps",
        "desc": "帧率，默认0。"
      },
      {
        "name": "Gop",
        "desc": "关键帧间隔，单位：秒。默认原始的间隔"
      },
      {
        "name": "Rotate",
        "desc": "是否旋转，0：否，1：是。默认0。"
      },
      {
        "name": "Profile",
        "desc": "编码质量：\nbaseline/main/high。默认baseline"
      },
      {
        "name": "BitrateToOrig",
        "desc": "是否不超过原始码率，0：否，1：是。默认0。"
      },
      {
        "name": "HeightToOrig",
        "desc": "是否不超过原始高，0：否，1：是。默认0。"
      },
      {
        "name": "FpsToOrig",
        "desc": "是否不超过原始帧率，0：否，1：是。默认0。"
      }
    ],
    "desc": "创建转码模板，成功返回模板id后，需要调用[CreateLiveTranscodeRule](/document/product/267/32647)接口，将返回的模板id绑定到流使用。\n<br>转码相关文档：[直播转封装及转码](/document/product/267/32736)。"
  },
  "ResumeLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "恢复某条流的推送。"
  },
  "DescribeLiveCerts": {
    "params": [],
    "desc": "获取证书信息列表"
  },
  "CreateLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "模板名称。非空的字符串"
      },
      {
        "name": "Description",
        "desc": "描述信息。"
      },
      {
        "name": "StreamBeginNotifyUrl",
        "desc": "开播回调URL，\n相关协议文档：[事件消息通知](/document/product/267/32744)。"
      },
      {
        "name": "StreamEndNotifyUrl",
        "desc": "断流回调URL，\n相关协议文档：[事件消息通知](/document/product/267/32744)。"
      },
      {
        "name": "RecordNotifyUrl",
        "desc": "录制回调URL，\n相关协议文档：[事件消息通知](/document/product/267/32744)。"
      },
      {
        "name": "SnapshotNotifyUrl",
        "desc": "截图回调URL，\n相关协议文档：[事件消息通知](/document/product/267/32744)。"
      },
      {
        "name": "PornCensorshipNotifyUrl",
        "desc": "鉴黄回调URL，\n相关协议文档：[事件消息通知](/document/product/267/32741)。"
      },
      {
        "name": "CallbackKey",
        "desc": "回调key，回调URL公用，鉴权回调说明详见回调格式文档"
      }
    ],
    "desc": "创建回调模板，成功返回模板id后，需要调用[CreateLiveCallbackRule](/document/product/267/32638)接口将模板id绑定到域名/路径使用。\n<br>回调协议相关文档：[事件消息通知](/document/product/267/32744)。"
  },
  "DescribeLiveTranscodeRules": {
    "params": [],
    "desc": "获取转码规则列表"
  },
  "SetLiveWatermarkStatus": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "水印ID。"
      },
      {
        "name": "Status",
        "desc": "状态。0：停用，1:启用"
      }
    ],
    "desc": "设置水印是否启用"
  },
  "ForbidLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "ResumeTime",
        "desc": "恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。\n注意：默认禁播90天，且最长支持禁播90天。"
      }
    ],
    "desc": "禁止某条流的推送，可以预设某个时刻将流恢复。"
  },
  "ModifyPullStreamStatus": {
    "params": [
      {
        "name": "ConfigIds",
        "desc": "配置id列表。"
      },
      {
        "name": "Status",
        "desc": "目标状态。0无效，2正在运行，4暂停。"
      }
    ],
    "desc": "修改直播拉流配置状态"
  },
  "DeleteLiveCallbackRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径。"
      }
    ],
    "desc": "删除回调规则"
  },
  "ModifyPullStreamConfig": {
    "params": [
      {
        "name": "ConfigId",
        "desc": "配置id。"
      },
      {
        "name": "FromUrl",
        "desc": "源Url。"
      },
      {
        "name": "ToUrl",
        "desc": "目的Url。"
      },
      {
        "name": "AreaId",
        "desc": "区域id,1-深圳,2-上海，3-天津,4-香港。如有改动，需同时传入IspId。"
      },
      {
        "name": "IspId",
        "desc": "运营商id,1-电信,2-移动,3-联通,4-其他,AreaId为4的时候,IspId只能为其他。如有改动，需同时传入AreaId。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间。\n使用UTC格式时间，\n例如：2019-01-08T10:00:00Z。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，注意：\n1. 结束时间必须大于开始时间；\n2. 结束时间和开始时间必须大于当前时间；\n3. 结束时间 和 开始时间 间隔必须小于七天。\n\n使用UTC格式时间，\n例如：2019-01-08T10:00:00Z。"
      }
    ],
    "desc": "更新拉流配置"
  },
  "AddLiveWatermark": {
    "params": [
      {
        "name": "PictureUrl",
        "desc": "水印图片url。"
      },
      {
        "name": "WatermarkName",
        "desc": "水印名称。"
      },
      {
        "name": "XPosition",
        "desc": "显示位置,X轴偏移。"
      },
      {
        "name": "YPosition",
        "desc": "显示位置,Y轴偏移。"
      }
    ],
    "desc": "添加水印，成功返回水印id后，需要调用[CreateLiveWatermarkRule](/document/product/267/32629)接口将水印id绑定到流使用。"
  },
  "DescribeLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      }
    ],
    "desc": "获取单个回调模板"
  },
  "DescribeLiveStreamOnlineList": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "PageNum",
        "desc": "取得第几页，默认1。"
      },
      {
        "name": "PageSize",
        "desc": "每页大小，最大100。 \n取值：10~100之间的任意整数。\n默认值：10。"
      },
      {
        "name": "StreamName",
        "desc": "流名称，精确查询。"
      }
    ],
    "desc": "返回正在直播中的流列表"
  },
  "ModifyLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      },
      {
        "name": "TemplateName",
        "desc": "模板名称。"
      },
      {
        "name": "Description",
        "desc": "描述信息。"
      },
      {
        "name": "StreamBeginNotifyUrl",
        "desc": "开播回调URL。"
      },
      {
        "name": "StreamEndNotifyUrl",
        "desc": "断流回调URL。"
      },
      {
        "name": "RecordNotifyUrl",
        "desc": "录制回调URL。"
      },
      {
        "name": "SnapshotNotifyUrl",
        "desc": "截图回调URL。"
      },
      {
        "name": "PornCensorshipNotifyUrl",
        "desc": "鉴黄回调URL。"
      },
      {
        "name": "CallbackKey",
        "desc": "回调key，回调URL公用，鉴权回调说明详见回调格式文档"
      }
    ],
    "desc": "修改回调模板"
  },
  "DescribeLiveStreamState": {
    "params": [
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的推流域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "返回直播中、无推流或者禁播等状态"
  },
  "DeleteLiveCert": {
    "params": [
      {
        "name": "CertId",
        "desc": "证书Id。"
      }
    ],
    "desc": "删除域名对应的证书"
  },
  "DescribeLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "水印ID。"
      }
    ],
    "desc": "获取单个水印信息"
  },
  "DescribeLiveTranscodeTemplates": {
    "params": [],
    "desc": "获取转码模板列表"
  },
  "CreateLiveCert": {
    "params": [
      {
        "name": "CertType",
        "desc": "证书类型。0-用户添加证书；1-腾讯云托管证书。"
      },
      {
        "name": "HttpsCrt",
        "desc": "证书内容，即公钥。"
      },
      {
        "name": "HttpsKey",
        "desc": "私钥。"
      },
      {
        "name": "CertName",
        "desc": "证书名称。"
      },
      {
        "name": "Description",
        "desc": "描述。"
      }
    ],
    "desc": "添加证书"
  },
  "DescribeLivePushAuthKey": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      }
    ],
    "desc": "查询直播推流鉴权key"
  },
  "DeletePullStreamConfig": {
    "params": [
      {
        "name": "ConfigId",
        "desc": "配置id。"
      }
    ],
    "desc": "删除直播拉流配置"
  },
  "DescribeLiveWatermarkRules": {
    "params": [],
    "desc": "获取水印规则列表"
  },
  "CreateLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "模板名。非空的字符串"
      },
      {
        "name": "Description",
        "desc": "描述信息。"
      },
      {
        "name": "FlvParam",
        "desc": "Flv录制参数，开启Flv录制时设置。"
      },
      {
        "name": "HlsParam",
        "desc": "Hls录制参数，开启hls录制时设置。"
      },
      {
        "name": "Mp4Param",
        "desc": "Mp4录制参数，开启Mp4录制时设置。"
      },
      {
        "name": "AacParam",
        "desc": "Aac录制参数，开启Aac录制时设置。"
      }
    ],
    "desc": "创建录制模板，成功返回模板id后，需要调用[CreateLiveRecordRule](/document/product/267/32615)接口，将模板id绑定到流进行使用。\n<br>录制相关文档：[直播录制](/document/product/267/32739)。"
  },
  "DescribeLiveCert": {
    "params": [
      {
        "name": "CertId",
        "desc": "证书Id。"
      }
    ],
    "desc": "获取证书信息"
  },
  "CreateLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "模板名称。非空的字符串"
      },
      {
        "name": "CosAppId",
        "desc": "Cos AppId。"
      },
      {
        "name": "CosBucket",
        "desc": "Cos Bucket名称。"
      },
      {
        "name": "CosRegion",
        "desc": "Cos地区。"
      },
      {
        "name": "Description",
        "desc": "描述信息。"
      },
      {
        "name": "SnapshotInterval",
        "desc": "截图间隔，单位s，默认10s。"
      },
      {
        "name": "Width",
        "desc": "截图宽度。默认：0（原始高）"
      },
      {
        "name": "Height",
        "desc": "截图高度。默认：0（原始宽）"
      },
      {
        "name": "PornFlag",
        "desc": "是否开启鉴黄，0：不开启，1：开启。默认：0."
      }
    ],
    "desc": "创建截图模板，成功返回模板id后，需要调用[CreateLiveSnapshotRule](/document/product/267/32625)接口，将模板id绑定到流使用。\n<br>截图相关文档：[直播截图](/document/product/267/32737)。"
  },
  "DescribeLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板Id。"
      }
    ],
    "desc": "获取单个截图模板"
  }
}