# -*- coding: utf-8 -*-
DESC = "live-2018-08-01"
INFO = {
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
  "DescribeLiveWatermarks": {
    "params": [],
    "desc": "查询水印列表"
  },
  "CreateLiveRecord": {
    "params": [
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "AppName",
        "desc": "直播流所属应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "推流域名。多域名推流必须设置。"
      },
      {
        "name": "StartTime",
        "desc": "任务起始时间，中国标准时间，需要URLEncode。如 2017-01-01 10:10:01，编码为：2017-01-01+10%3a10%3a01。录制视频为精彩视频时，忽略此字段。"
      },
      {
        "name": "EndTime",
        "desc": "任务结束时间，中国标准时间，需要URLEncode。如 2017-01-01 10:30:01，编码为：2017-01-01+10%3a30%3a01。若指定精彩视频录制，结束时间不超过当前时间+30分钟，如果超过或小于起始时间，则实际结束时间为当前时间+30分钟。"
      },
      {
        "name": "RecordType",
        "desc": "录制类型。不区分大小写。\n“video” : 音视频录制【默认】。\n“audio” : 纯音频录制。"
      },
      {
        "name": "FileFormat",
        "desc": "录制文件格式。不区分大小写。其值为：\n“flv”,“hls”,”mp4”,“aac”,”mp3”，默认“flv”。"
      },
      {
        "name": "Highlight",
        "desc": "精彩视频标志。0：普通视频【默认】；1：精彩视频。"
      },
      {
        "name": "MixStream",
        "desc": "A+B=C混流标志。0：非A+B=C混流录制【默认】；1：标示为A+B=C混流录制。"
      },
      {
        "name": "StreamParam",
        "desc": "录制流参数，当前支持以下参数： \ninterval 录制分片时长，单位 秒，0 - 7200\nstorage_time 录制文件存储时长，单位 秒\neg. interval=3600&storage_time=7200\n注：参数需要url encode。"
      }
    ],
    "desc": "- 使用前提\n  1. 录制文件存放于点播平台，所以用户如需使用录制功能，需首先自行开通点播服务。\n  2. 录制文件存放后相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，具体请参考 [对应文档](https://cloud.tencent.com/document/product/266/2838)。\n\n- 模式说明\n  该接口支持两种录制模式：\n  1. 定时录制模式。\n    需要传入开始时间与结束时间，录制任务根据时间自动开始与结束。\n  2. 实时视频录制模式。\n    忽略传入的开始时间，在录制任务创建后立即开始录制，录制时长支持最大为30分钟，如果传入的结束时间与当前时间差大于30分钟，则按30分钟计算，实时视频录制主要用于录制精彩视频场景，时长建议控制在5分钟以内。\n\n- 注意事项\n  1. 调用接口超时设置应大于3秒，小于3秒重试以及频繁调用都有可能产生重复录制任务。"
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
      }
    ],
    "desc": "对流设置延播"
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
  "DescribeLiveStreamState": {
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
    "desc": "返回直播中、无推流或者禁播等状态"
  },
  "DescribeLiveStreamOnlineInfo": {
    "params": [
      {
        "name": "PageNum",
        "desc": "取得第几页。\n默认值：1"
      },
      {
        "name": "PageSize",
        "desc": "分页大小。\n\n最大值：100。\n取值范围：1~100 之前的任意整数。\n默认值：10"
      },
      {
        "name": "Status",
        "desc": "0:未开始推流 1:正在推流 2:服务出错 3:已关闭。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "查询在线推流信息列表"
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
        "desc": "取得第几页。\n默认值：1"
      },
      {
        "name": "PageSize",
        "desc": "分页大小。\n\n最大值：100。\n取值范围：1~100 之前的任意整数。\n默认值：10"
      }
    ],
    "desc": "返回已经推过流的流列表"
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
  "DeleteLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "水印ID。"
      }
    ],
    "desc": "删除水印"
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
    "desc": "添加水印"
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
        "desc": "开始时间。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，注意：\n1. 结束时间必须大于开始时间；\n2. 结束时间和开始时间必须大于当前时间；\n3. 结束时间 和 开始时间 间隔必须小于七天。"
      }
    ],
    "desc": "更新拉流配置"
  },
  "DescribeLiveStreamOnlineList": {
    "params": [
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
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
        "desc": "每页大小，最大100。 \n取值：1~100之前的任意整数。\n默认值：10"
      }
    ],
    "desc": "返回正在直播中的流列表"
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
        "desc": "开始时间。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，注意：\n1. 结束时间必须大于开始时间；\n2. 结束时间和开始时间必须大于当前时间；\n3. 结束时间 和 开始时间 间隔必须小于七天。"
      }
    ],
    "desc": "添加拉流配置，目前限制添加10条任务。"
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
  }
}