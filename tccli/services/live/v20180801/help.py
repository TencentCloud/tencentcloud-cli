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
        "desc": "您的推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为 live。"
      }
    ],
    "desc": "断开推流连接，但可以重新推流。"
  },
  "DescribeLiveWatermarks": {
    "params": [],
    "desc": "查询水印列表。"
  },
  "DescribeConcurrentRecordStreamNum": {
    "params": [
      {
        "name": "LiveType",
        "desc": "直播类型，SlowLive：慢直播。\nNormalLive：普通直播。"
      },
      {
        "name": "StartTime",
        "desc": "起始时间，格式：yyyy-mm-dd HH:MM:SS。\n可以查询最近180天的数据。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，格式：yyyy-mm-dd HH:MM:SS。\n时间跨度最大支持31天。"
      },
      {
        "name": "MainlandOrOversea",
        "desc": "如果为空，查询所有地区数据；如果为“Mainland”，查询国内数据；如果为“Oversea”，则查询国外数据。"
      },
      {
        "name": "PushDomains",
        "desc": "推流域名列表，不填表示总体数据。"
      }
    ],
    "desc": "查询并发录制路数，对慢直播和普通直播适用。"
  },
  "CreateLiveRecord": {
    "params": [
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的 AppName保持一致，默认为 live。"
      },
      {
        "name": "DomainName",
        "desc": "推流域名。多域名推流必须设置。"
      },
      {
        "name": "StartTime",
        "desc": "录制开始时间。中国标准时间，需要 URLEncode(rfc3986)。如 2017-01-01 10:10:01，编码为：2017-01-01+10%3a10%3a01。\n定时录制模式，必须设置该字段；实时视频录制模式，忽略该字段。"
      },
      {
        "name": "EndTime",
        "desc": "录制结束时间。中国标准时间，需要 URLEncode(rfc3986)。如 2017-01-01 10:30:01，编码为：2017-01-01+10%3a30%3a01。\n定时录制模式，必须设置该字段；实时录制模式，为可选字段。如果通过Highlight参数，设置录制为实时视频录制模式，其设置的结束时间不应超过当前时间+30分钟，如果设置的结束时间超过当前时间+30分钟或者小于当前时间或者不设置该参数，则实际结束时间为当前时间+30分钟。"
      },
      {
        "name": "RecordType",
        "desc": "录制类型。\n“video” : 音视频录制【默认】。\n“audio” : 纯音频录制。\n在定时录制模式或实时视频录制模式下，该参数均有效，不区分大小写。"
      },
      {
        "name": "FileFormat",
        "desc": "录制文件格式。其值为：\n“flv”【默认】,“hls”,”mp4”,“aac”,”mp3”。\n在定时录制模式或实时视频录制模式下，该参数均有效，不区分大小写。"
      },
      {
        "name": "Highlight",
        "desc": "开启实时视频录制模式标志。\n0：不开启实时视频录制模式，即定时录制模式【默认】。见[示例一](#.E7.A4.BA.E4.BE.8B1-.E5.88.9B.E5.BB.BA.E5.AE.9A.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1)。\n1：开启实时视频录制模式。见[示例二](#.E7.A4.BA.E4.BE.8B2-.E5.88.9B.E5.BB.BA.E5.AE.9E.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1)。"
      },
      {
        "name": "MixStream",
        "desc": "开启 A+B=C混流C流录制标志。\n0：不开启 A+B=C混流C流录制【默认】。\n1：开启 A+B=C混流C流录制。\n在定时录制模式或实时视频录制模式下，该参数均有效。"
      },
      {
        "name": "StreamParam",
        "desc": "录制流参数。当前支持以下参数：\nrecord_interval - 录制分片时长，单位 秒，1800 - 7200。\nstorage_time - 录制文件存储时长，单位 秒。\neg. record_interval=3600&storage_time=2592000。\n注：参数需要url encode。\n在定时录制模式或实时视频录制模式下，该参数均有效。"
      }
    ],
    "desc": "- 使用前提\n  1. 录制文件存放于点播平台，所以用户如需使用录制功能，需首先自行开通点播服务。\n  2. 录制文件存放后相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，具体请参考 [对应文档](https://cloud.tencent.com/document/product/266/2838)。\n\n- 模式说明\n  该接口支持两种录制模式：\n  1. 定时录制模式【默认模式】。\n    需要传入开始时间与结束时间，录制任务根据时间自动开始与结束。\n  2. 实时视频录制模式。\n    忽略传入的开始时间，在录制任务创建后立即开始录制，录制时长支持最大为30分钟，如果传入的结束时间与当前时间差大于30分钟，则按30分钟计算，实时视频录制主要用于录制精彩视频场景，时长建议控制在5分钟以内。\n\n- 注意事项\n  1. 调用接口超时设置应大于3秒，小于3秒重试以及频繁调用都有可能产生重复录制任务。\n  2. 受限于音视频文件格式（FLV/MP4/HLS）对编码类型的支持，视频编码类型支持 H.264，音频编码类型支持 AAC。\n  3. 为避免恶意或非主观的频繁 API 请求，对定时录制模式最大创建任务数做了限制：其中，当天可以创建的最大任务数不超过4000（不含已删除的任务）；当前时刻并发运行的任务数不超过400。有超出此限制的需要提工单申请。"
  },
  "UpdateLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "水印 ID。\n在添加水印接口 [AddLiveWatermark](/document/product/267/30154) 调用返回值中获取水印 ID。"
      },
      {
        "name": "PictureUrl",
        "desc": "水印图片 URL。"
      },
      {
        "name": "XPosition",
        "desc": "显示位置，X轴偏移，默认 0。"
      },
      {
        "name": "YPosition",
        "desc": "显示位置，Y轴偏移，默认 0。"
      },
      {
        "name": "WatermarkName",
        "desc": "水印名称。"
      },
      {
        "name": "Width",
        "desc": "水印宽度，占直播原始画面宽度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始宽度。"
      },
      {
        "name": "Height",
        "desc": "水印高度，占直播原始画面宽度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始高度。"
      }
    ],
    "desc": "更新水印。"
  },
  "ModifyLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 ID。"
      },
      {
        "name": "TemplateName",
        "desc": "模板名称。\n长度上限：255字节。"
      },
      {
        "name": "Description",
        "desc": "描述信息。\n长度上限：1024字节。"
      },
      {
        "name": "SnapshotInterval",
        "desc": "截图间隔，单位s，默认10s。\n范围： 5s ~ 600s。"
      },
      {
        "name": "Width",
        "desc": "截图宽度。默认：0（原始宽）。"
      },
      {
        "name": "Height",
        "desc": "截图高度。默认：0（原始高）。"
      },
      {
        "name": "PornFlag",
        "desc": "是否开启鉴黄，默认 0 。\n0：不开启。\n1：开启。"
      },
      {
        "name": "CosAppId",
        "desc": "Cos 应用 ID。"
      },
      {
        "name": "CosBucket",
        "desc": "Cos Bucket名称。"
      },
      {
        "name": "CosRegion",
        "desc": "Cos 地域。"
      },
      {
        "name": "CosPrefix",
        "desc": "Cos Bucket文件夹前缀。"
      },
      {
        "name": "CosFileName",
        "desc": "Cos 文件名称。"
      }
    ],
    "desc": "修改截图模板配置。"
  },
  "ModifyLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 ID。"
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
        "desc": "FLV 录制参数，开启 FLV 录制时设置。"
      },
      {
        "name": "HlsParam",
        "desc": "HLS 录制参数，开启 HLS 录制时设置。"
      },
      {
        "name": "Mp4Param",
        "desc": "MP4 录制参数，开启 MP4 录制时设置。"
      },
      {
        "name": "AacParam",
        "desc": "AAC 录制参数，开启 AAC 录制时设置。"
      },
      {
        "name": "HlsSpecialParam",
        "desc": "HLS 录制定制参数。"
      },
      {
        "name": "Mp3Param",
        "desc": "MP3 录制参数，开启 MP3 录制时设置。"
      }
    ],
    "desc": "修改录制模板配置。"
  },
  "CreateLiveWatermarkRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为live。"
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
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为 live。"
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
        "desc": "分页大小。\n最大值：100。\n取值范围：1~100 之间的任意整数。\n默认值：10。\n注： 目前只支持10000条内的查询。"
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
    "desc": "用于查询推断流事件。<br>\n\n注意：该接口可通过使用IsFilter进行过滤，返回推流历史记录。"
  },
  "CreateCommonMixStream": {
    "params": [
      {
        "name": "MixStreamSessionId",
        "desc": "混流会话（申请混流开始到取消混流结束）标识 ID。"
      },
      {
        "name": "InputStreamList",
        "desc": "混流输入流列表。"
      },
      {
        "name": "OutputParams",
        "desc": "混流输出流参数。"
      },
      {
        "name": "MixStreamTemplateId",
        "desc": "输入模板 ID，若设置该参数，将按默认模板布局输出，无需填入自定义位置参数。\n不填默认为0。\n两输入源支持10，20，30，40，50。\n三输入源支持310，390，391。\n四输入源支持410。\n五输入源支持510，590。\n六输入源支持610。"
      },
      {
        "name": "ControlParams",
        "desc": "混流的特殊控制参数。如无特殊需求，无需填写。"
      }
    ],
    "desc": "该接口用来创建通用混流。用法与旧接口 mix_streamv2.start_mix_stream_advanced 基本一致。\n注意：当前最多支持16路混流。"
  },
  "DescribeHttpStatusInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始时间，北京时间，\n格式：yyyy-mm-dd HH:MM:SS。\nStartTime不能为3个月前。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，北京时间，\n格式：yyyy-mm-dd HH:MM:SS。\n注：EndTime 和 StartTime 只支持最近1天的数据查询。"
      },
      {
        "name": "PlayDomains",
        "desc": "播放域名列表。"
      }
    ],
    "desc": "查询某段时间内5分钟粒度的各播放http状态码的个数。\n备注：数据延迟1小时，如10:00-10:59点的数据12点才能查到。"
  },
  "DescribeProvinceIspPlayInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始时间点，当前使用北京时间，\n例：2019-02-21 10:00:00。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间点，当前使用北京时间，\n例：2019-02-21 12:00:00。\n注：EndTime 和 StartTime 只支持最近1天的数据查询。"
      },
      {
        "name": "Granularity",
        "desc": "支持如下粒度：\n1：1分钟粒度（跨度不支持超过1天）"
      },
      {
        "name": "StatType",
        "desc": "统计指标类型：\n“Bandwidth”：带宽\n“FluxPerSecond”：平均流量\n“Flux”：流量\n“Request”：请求数\n“Online”：并发连接数"
      },
      {
        "name": "PlayDomains",
        "desc": "播放域名列表。"
      },
      {
        "name": "ProvinceNames",
        "desc": "要查询的省份（地区）英文名称列表，如 Beijing。"
      },
      {
        "name": "IspNames",
        "desc": "要查询的运营商英文名称列表，如 China Mobile ，如果为空，查询所有运营商的数据。"
      },
      {
        "name": "MainlandOrOversea",
        "desc": "地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。"
      }
    ],
    "desc": "查询某省份某运营商下行播放数据，包括带宽，流量，请求数，并发连接数信息。"
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
  "DescribeStreamPushInfoList": {
    "params": [
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "StartTime",
        "desc": "起始时间点，格式为yyyy-mm-dd HH:MM:SS。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间点，格式为yyyy-mm-dd HH:MM:SS，最大时间跨度支持6小时，支持最近6天数据查询。"
      },
      {
        "name": "PushDomain",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为 live。"
      }
    ],
    "desc": "查询流id的上行推流质量数据，包括音视频的帧率，码率，流逝时间，编码格式等。"
  },
  "DescribeLiveSnapshotRules": {
    "params": [],
    "desc": "获取截图规则列表"
  },
  "DeleteLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 ID。\n1. 在创建转码模板接口 [CreateLiveTranscodeTemplate](/document/product/267/32646) 调用的返回值中获取模板 ID。\n2. 可以从接口 [DescribeLiveTranscodeTemplates](/document/product/267/32641) 查询已经创建的过的模板列表。"
      }
    ],
    "desc": "删除转码模板。"
  },
  "DescribeTopClientIpSumInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始时间点，格式为yyyy-mm-dd HH:MM:SS。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间点，格式为yyyy-mm-dd HH:MM:SS\n时间跨度在[0,4小时]，支持最近1天数据查询。"
      },
      {
        "name": "PlayDomains",
        "desc": "播放域名，默认为不填，表示求总体数据。"
      },
      {
        "name": "PageNum",
        "desc": "页号，范围是[1,1000]，默认值是1。"
      },
      {
        "name": "PageSize",
        "desc": "每页个数，范围是[1,1000]，默认值是20。"
      },
      {
        "name": "OrderParam",
        "desc": "排序指标，可选值包括TotalRequest（默认值），FailedRequest,TotalFlux。"
      },
      {
        "name": "MainlandOrOversea",
        "desc": "地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。"
      },
      {
        "name": "OutLanguage",
        "desc": "输出字段使用的语言，可选值：Chinese（默认值），English；目前国家，省份和运营商支持多语言。"
      }
    ],
    "desc": "查询某段时间top n客户端ip汇总信息（暂支持top 1000）"
  },
  "ModifyPullStreamStatus": {
    "params": [
      {
        "name": "ConfigIds",
        "desc": "配置 ID 列表。"
      },
      {
        "name": "Status",
        "desc": "目标状态。0无效，2正在运行，4暂停。"
      }
    ],
    "desc": "修改直播拉流配置的状态。"
  },
  "DescribeLiveRecordTemplates": {
    "params": [
      {
        "name": "IsDelayLive",
        "desc": "是否属于慢直播模板，默认：0。\n0： 标准直播。\n1：慢直播。"
      }
    ],
    "desc": "获取录制模板列表。"
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
  "DescribeVisitTopSumInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始时间点，格式为yyyy-mm-dd HH:MM:SS。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间点，格式为yyyy-mm-dd HH:MM:SS\n时间跨度在(0,4小时]，支持最近1天数据查询。"
      },
      {
        "name": "TopIndex",
        "desc": "峰值指标，可选值包括”Domain”，”StreamId”。"
      },
      {
        "name": "PlayDomains",
        "desc": "播放域名，默认为不填，表示求总体数据。"
      },
      {
        "name": "PageNum",
        "desc": "页号，\n范围是[1,1000]，\n默认值是1。"
      },
      {
        "name": "PageSize",
        "desc": "每页个数，范围是[1,1000]，\n默认值是20。"
      },
      {
        "name": "OrderParam",
        "desc": "排序指标，可选值包括” AvgFluxPerSecond”，”TotalRequest”（默认）,“TotalFlux”。"
      }
    ],
    "desc": "查询某时间段top n的域名或流id信息（暂支持top 1000）。"
  },
  "DescribeLiveDomainCert": {
    "params": [
      {
        "name": "DomainName",
        "desc": "播放域名。"
      }
    ],
    "desc": "获取域名证书信息。"
  },
  "AddLiveWatermark": {
    "params": [
      {
        "name": "PictureUrl",
        "desc": "水印图片 URL。"
      },
      {
        "name": "WatermarkName",
        "desc": "水印名称。"
      },
      {
        "name": "XPosition",
        "desc": "显示位置，X轴偏移，默认 0。"
      },
      {
        "name": "YPosition",
        "desc": "显示位置，Y轴偏移，默认 0。"
      },
      {
        "name": "Width",
        "desc": "水印宽度，占直播原始画面宽度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始宽度。"
      },
      {
        "name": "Height",
        "desc": "水印高度，占直播原始画面宽度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始高度。"
      }
    ],
    "desc": "添加水印，成功返回水印 ID 后，需要调用[CreateLiveWatermarkRule](/document/product/267/32629)接口将水印 ID 绑定到流使用。"
  },
  "DeleteLiveWatermarkRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径。与推流和播放地址中的 AppName 保持一致，默认为live。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "删除水印规则"
  },
  "DeleteLiveCallbackRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。"
      }
    ],
    "desc": "删除回调规则。"
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
        "desc": "区域id：\n1-深圳，\n2-上海，\n3-天津，\n4-中国香港。\n如有改动，需同时传入IspId。"
      },
      {
        "name": "IspId",
        "desc": "运营商id,1-电信,2-移动,3-联通,4-其他,AreaId为4的时候,IspId只能为其他。如有改动，需同时传入AreaId。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间。\n使用UTC格式时间，\n例如：2019-01-08T10:00:00Z。\n注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，注意：\n1. 结束时间必须大于开始时间；\n2. 结束时间和开始时间必须大于当前时间；\n3. 结束时间 和 开始时间 间隔必须小于七天。\n\n使用UTC格式时间，\n例如：2019-01-08T10:00:00Z。\n注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。"
      }
    ],
    "desc": "更新拉流配置。"
  },
  "CreateLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "模板名称。\n长度上限：255字节。\n仅支持中文、英文、数字、_、-。"
      },
      {
        "name": "CosAppId",
        "desc": "Cos 应用 ID。"
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
        "desc": "描述信息。\n长度上限：1024字节。\n仅支持中文、英文、数字、_、-。"
      },
      {
        "name": "SnapshotInterval",
        "desc": "截图间隔，单位s，默认10s。\n范围： 5s ~ 600s。"
      },
      {
        "name": "Width",
        "desc": "截图宽度。默认：0（原始宽）。"
      },
      {
        "name": "Height",
        "desc": "截图高度。默认：0（原始高）。"
      },
      {
        "name": "PornFlag",
        "desc": "是否开启鉴黄，0：不开启，1：开启。默认：0。"
      },
      {
        "name": "CosPrefix",
        "desc": "Cos Bucket文件夹前缀。"
      },
      {
        "name": "CosFileName",
        "desc": "Cos 文件名称。"
      }
    ],
    "desc": "创建截图模板，成功返回模板id后，需要调用[CreateLiveSnapshotRule](/document/product/267/32625)接口，将模板id绑定到流使用。\n<br>截图相关文档：[直播截图](/document/product/267/32737)。"
  },
  "DescribeLiveStreamOnlineList": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。多域名用户需要填写 DomainName。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。多路径用户需要填写 AppName。"
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
        "desc": "流名称，用于精确查询。"
      }
    ],
    "desc": "返回正在直播中的流列表。适用于推流成功后查询在线流信息。"
  },
  "DeleteLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 ID。\n1. 在创建回调模板接口 [CreateLiveCallbackTemplate](/document/product/267/32637) 调用的返回值中获取模板 ID。\n2. 可以从接口 [DescribeLiveCallbackTemplates](/document/product/267/32632) 查询已经创建的过的模板列表。"
      }
    ],
    "desc": "删除回调模板。"
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
        "desc": "配置 ID。\n1. 在添加拉流配置接口 [CreatePullStreamConfig](/document/api/267/30159) 调用返回值中获取配置 ID。\n2. 可以从接口 [DescribePullStreamConfigs](/document/api/267/30158) 中查询已创建过的拉流配置列表。"
      }
    ],
    "desc": "删除直播拉流配置。"
  },
  "DescribeLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 ID。"
      }
    ],
    "desc": "获取单个录制模板。"
  },
  "DescribePullStreamConfigs": {
    "params": [
      {
        "name": "ConfigId",
        "desc": "配置 ID。"
      }
    ],
    "desc": "查询直播拉流配置。"
  },
  "DeleteLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "水印 ID。\n在添加水印接口 [AddLiveWatermark](/document/product/267/30154) 调用返回值中获取水印 ID。"
      }
    ],
    "desc": "删除水印。"
  },
  "DescribePlayErrorCodeSumInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始时间点，北京时间。\n格式：yyyy-mm-dd HH:MM:SS。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间点，北京时间。\n格式：yyyy-mm-dd HH:MM:SS。\n注：EndTime 和 StartTime 只支持最近1天的数据查询。"
      },
      {
        "name": "PlayDomains",
        "desc": "播放域名列表，不填表示总体数据。"
      },
      {
        "name": "PageNum",
        "desc": "页数，范围[1,1000]，默认值是1。"
      },
      {
        "name": "PageSize",
        "desc": "每页个数，范围：[1,1000]，默认值是20。"
      },
      {
        "name": "MainlandOrOversea",
        "desc": "地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。"
      },
      {
        "name": "GroupType",
        "desc": "分组参数，可选值：CountryProIsp（默认值），Country（国家），默认是按照国家+省份+运营商来进行分组；目前国外的省份和运营商暂时无法识别。"
      },
      {
        "name": "OutLanguage",
        "desc": "输出字段使用的语言，可选值：Chinese（默认值），English，目前国家，省份和运营商支持多语言。"
      }
    ],
    "desc": "查询下行播放错误码信息。"
  },
  "AddDelayLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。"
      },
      {
        "name": "DomainName",
        "desc": "推流域名。"
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
        "desc": "延播设置的过期时间。UTC 格式，例如：2018-11-29T19:00:00Z。\n注意：\n1. 默认7天后过期，且最长支持7天内生效。\n2. 北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。"
      }
    ],
    "desc": "对流设置延播时间\n注意：如果在推流前设置延播，需要提前5分钟设置。\n目前该接口只支持流粒度的，域名及应用粒度功能支持当前开发中。\n"
  },
  "DescribeStreamDayPlayInfoList": {
    "params": [
      {
        "name": "DayTime",
        "desc": "日期，格式：YYYY-mm-dd。\n第二天凌晨3点出昨天的数据，建议在这个时间点之后查询最新数据。"
      },
      {
        "name": "PlayDomain",
        "desc": "播放域名。"
      },
      {
        "name": "PageNum",
        "desc": "页号，范围[1,1000]，默认值是1。"
      },
      {
        "name": "PageSize",
        "desc": "每页个数，范围[100,1000]，默认值是1000。"
      }
    ],
    "desc": "查询天维度每条流的播放数据，包括总流量等。"
  },
  "ModifyLivePlayDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "播放域名。"
      },
      {
        "name": "PlayType",
        "desc": "拉流域名类型。1-国内；2-全球；3-境外"
      }
    ],
    "desc": "修改播放域名信息。"
  },
  "ModifyLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 Id。"
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
        "desc": "音频码率，默认0。\n范围：0-500。"
      },
      {
        "name": "Description",
        "desc": "模板描述。"
      },
      {
        "name": "VideoBitrate",
        "desc": "视频码率。范围：100kbps - 8000kbps。\n注意：码率必须是100的倍数。"
      },
      {
        "name": "Width",
        "desc": "宽。0-3000。"
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
        "desc": "高。0-3000。"
      },
      {
        "name": "Fps",
        "desc": "帧率。0-200。"
      },
      {
        "name": "Gop",
        "desc": "关键帧间隔，单位：秒。0-50。"
      },
      {
        "name": "Rotate",
        "desc": "旋转角度。\n0 90 180 270。"
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
      },
      {
        "name": "AdaptBitratePercent",
        "desc": "极速高清相比 VideoBitrate 少多少码率，0.1到0.5。"
      }
    ],
    "desc": "修改转码模板配置。"
  },
  "DeleteLiveTranscodeRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "播放域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为 live。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "TemplateId",
        "desc": "模板ID。"
      }
    ],
    "desc": "删除转码规则。\nDomainName+AppName+StreamName+TemplateId唯一标识单个转码规则，如需删除需要强匹配。其中TemplateId必填，其余参数为空时也需要传空字符串进行强匹配。"
  },
  "DeleteLiveSnapshotRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "删除截图规则。"
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
    "desc": "获取禁推流列表。"
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
  "DescribeLiveDomains": {
    "params": [
      {
        "name": "DomainStatus",
        "desc": "域名状态过滤。0-停用，1-启用。"
      },
      {
        "name": "DomainType",
        "desc": "域名类型过滤。0-推流，1-播放。"
      },
      {
        "name": "PageSize",
        "desc": "分页大小，范围：10~100。默认10。"
      },
      {
        "name": "PageNum",
        "desc": "取第几页，范围：1~100000。默认1。"
      },
      {
        "name": "IsDelayLive",
        "desc": "0 普通直播 1慢直播 默认0。"
      },
      {
        "name": "DomainPrefix",
        "desc": "域名前缀。"
      }
    ],
    "desc": "根据域名状态、类型等信息查询用户的域名信息。"
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
  "CreateLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "模板名称。\n长度上限：255字节。\n仅支持中文、英文、数字、_、-。"
      },
      {
        "name": "Description",
        "desc": "描述信息。\n长度上限：1024字节。\n仅支持中文、英文、数字、_、-。"
      },
      {
        "name": "StreamBeginNotifyUrl",
        "desc": "开播回调 URL，\n相关协议文档：[事件消息通知](/document/product/267/32744)。"
      },
      {
        "name": "StreamEndNotifyUrl",
        "desc": "断流回调 URL，\n相关协议文档：[事件消息通知](/document/product/267/32744)。"
      },
      {
        "name": "RecordNotifyUrl",
        "desc": "录制回调 URL，\n相关协议文档：[事件消息通知](/document/product/267/32744)。"
      },
      {
        "name": "SnapshotNotifyUrl",
        "desc": "截图回调 URL，\n相关协议文档：[事件消息通知](/document/product/267/32744)。"
      },
      {
        "name": "PornCensorshipNotifyUrl",
        "desc": "鉴黄回调 URL，\n相关协议文档：[事件消息通知](/document/product/267/32741)。"
      },
      {
        "name": "CallbackKey",
        "desc": "回调 Key，回调 URL 公用，回调签名详见事件消息通知文档。\n[事件消息通知](/document/product/267/32744)。"
      }
    ],
    "desc": "创建回调模板，成功返回模板id后，需要调用[CreateLiveCallbackRule](/document/product/267/32638)接口将模板 ID 绑定到域名/路径使用。\n<br>回调协议相关文档：[事件消息通知](/document/product/267/32744)。"
  },
  "ResumeLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为 live。"
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
    "desc": "恢复某条流的推流。"
  },
  "DescribeLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 ID。\n1. 在创建回调模板接口 [CreateLiveCallbackTemplate](/document/product/267/32637) 调用的返回值中获取模板 ID。\n2. 可以从接口 [DescribeLiveCallbackTemplates](/document/product/267/32632) 查询已经创建的过的模板列表。"
      }
    ],
    "desc": "获取单个回调模板。"
  },
  "DeleteLiveDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "要删除的域名"
      },
      {
        "name": "DomainType",
        "desc": "类型。0-推流，1-播放"
      }
    ],
    "desc": "删除已添加的直播域名"
  },
  "ModifyLiveCallbackTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 ID。"
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
        "desc": "开播回调 URL。"
      },
      {
        "name": "StreamEndNotifyUrl",
        "desc": "断流回调 URL。"
      },
      {
        "name": "RecordNotifyUrl",
        "desc": "录制回调 URL。"
      },
      {
        "name": "SnapshotNotifyUrl",
        "desc": "截图回调 URL。"
      },
      {
        "name": "PornCensorshipNotifyUrl",
        "desc": "鉴黄回调 URL。"
      },
      {
        "name": "CallbackKey",
        "desc": "回调 Key，回调 URL 公用，回调签名详见事件消息通知文档。\n[事件消息通知](/document/product/267/32744)。"
      }
    ],
    "desc": "修改回调模板。"
  },
  "DescribeProIspPlaySumInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始时间，北京时间，\n格式：yyyy-mm-dd HH:MM:SS。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，北京时间，\n格式：yyyy-mm-dd HH:MM:SS。\n注：EndTime 和 StartTime 只支持最近1天的数据查询。"
      },
      {
        "name": "StatType",
        "desc": "统计的类型，可选值：”Province”，”Isp”，“CountryOrArea”。"
      },
      {
        "name": "PlayDomains",
        "desc": "不填则为总体数据。"
      },
      {
        "name": "PageNum",
        "desc": "页号，范围是[1,1000]，默认值是1。"
      },
      {
        "name": "PageSize",
        "desc": "每页个数，范围是[1,1000]，默认值是20。"
      },
      {
        "name": "MainlandOrOversea",
        "desc": "地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。"
      },
      {
        "name": "OutLanguage",
        "desc": "输出字段使用的语言，可选值：Chinese（默认值），English；目前国家，省份和运营商支持多语言。"
      }
    ],
    "desc": "查询某段时间内每个国家地区每个省份每个运营商的平均每秒流量，总流量，总请求数信息。"
  },
  "DescribeStreamPlayInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "开始时间，北京时间，格式为yyyy-mm-dd HH:MM:SS，\n当前时间 和 开始时间 间隔不超过30天。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，北京时间，格式为yyyy-mm-dd HH:MM:SS，\n结束时间 和 开始时间  必须在同一天内。"
      },
      {
        "name": "PlayDomain",
        "desc": "播放域名，\n若不填，则为查询所有播放域名的在线流数据。"
      },
      {
        "name": "StreamName",
        "desc": "流名称，精确匹配。\n若不填，则为查询总体播放数据。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与播放地址中的AppName保持一致，会精确匹配，在同时传递了StreamName时生效。\n若不填，则为查询总体播放数据。\n注意：按AppName查询，需要联系客服同学提单支持。"
      }
    ],
    "desc": "查询播放数据，支持按流名称查询详细播放数据，也可按播放域名查询详细总数据。\n注意：按AppName查询，需要联系客服同学提单支持。"
  },
  "CreateLiveCert": {
    "params": [
      {
        "name": "CertType",
        "desc": "证书类型。0-用户添加证书；1-腾讯云托管证书。\n注意：当证书类型为0时，HttpsCrt和HttpsKey必选；\n当证书类型为1时，优先使用CloudCertId对应证书，若CloudCertId为空则使用HttpsCrt和HttpsKey。"
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
        "desc": "描述。"
      },
      {
        "name": "CloudCertId",
        "desc": "腾讯云证书托管ID。"
      }
    ],
    "desc": "添加证书"
  },
  "DescribeLiveTranscodeRules": {
    "params": [],
    "desc": "获取转码规则列表"
  },
  "DescribeLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 ID。\n调用 [CreateLiveSnapshotTemplate](/document/product/267/32624) 时返回的模板 ID。"
      }
    ],
    "desc": "获取单个截图模板。"
  },
  "DescribeLiveCallbackTemplates": {
    "params": [],
    "desc": "获取回调模板列表"
  },
  "DescribeLiveSnapshotTemplates": {
    "params": [],
    "desc": "获取截图模板列表。"
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
  "DescribeLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 ID。\n注意：在创建转码模板接口 [CreateLiveTranscodeTemplate](/document/product/267/32646) 调用的返回值中获取模板 ID。"
      }
    ],
    "desc": "获取单个转码模板。"
  },
  "DescribeScreenShotSheetNumList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "utc起始时间，格式为yyyy-mm-ddTHH:MM:SSZ"
      },
      {
        "name": "EndTime",
        "desc": "utc结束时间，格式为yyyy-mm-ddTHH:MM:SSZ，支持查询最近1年数据。"
      },
      {
        "name": "Zone",
        "desc": "地域信息，可选值包括Mainland，Oversea，前者是查询中国大陆范围内的数据，后者是除中国大陆范围之外的数据，若不传该参数，则查询所有地区的数据。"
      },
      {
        "name": "PushDomains",
        "desc": "推流域名（支持查询2019年11 月1日之后的域名维度数据）。"
      },
      {
        "name": "Granularity",
        "desc": "数据维度，数据延迟1个半小时，可选值包括：1、Minute（5分钟粒度，最大支持查询时间范围是31天），2、Day（天粒度，默认值，最大支持查询时间范围是186天当天）。"
      }
    ],
    "desc": "接口用来查询直播增值业务--截图的张数"
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
  "DescribeLiveTranscodeDetailInfo": {
    "params": [
      {
        "name": "PushDomain",
        "desc": "推流域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "DayTime",
        "desc": "查询时间，北京时间，\n格式：yyyymmdd。\n注意：支持查询近1个月内某天的详细数据。"
      },
      {
        "name": "PageNum",
        "desc": "页数，默认1，\n不超过100页。"
      },
      {
        "name": "PageSize",
        "desc": "每页个数，默认20，\n范围：[10,1000]。"
      },
      {
        "name": "StartDayTime",
        "desc": "起始天时间，北京时间，\n格式：yyyymmdd。\n注意：支持查询近1个月内的详细数据。"
      },
      {
        "name": "EndDayTime",
        "desc": "结束天时间，北京时间，\n格式：yyyymmdd。\n注意：支持查询近1个月内的详细数据，注意DayTime 与（StartDayTime，EndDayTime）必须要传一个，如果都传，会以DayTime为准 。"
      }
    ],
    "desc": "支持查询某天或某段时间的转码详细信息。"
  },
  "DescribeLogDownloadList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "开始时间，北京时间。\n格式：yyyy-mm-dd HH:MM:SS。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，北京时间。\n格式：yyyy-mm-dd HH:MM:SS。\n注意：结束时间 - 开始时间 <=7天。"
      },
      {
        "name": "PlayDomains",
        "desc": "域名列表。"
      }
    ],
    "desc": "批量获取日志URL。"
  },
  "DescribeLiveRecordRules": {
    "params": [],
    "desc": "获取录制规则列表"
  },
  "DescribeLiveDelayInfoList": {
    "params": [],
    "desc": "获取直播延播列表。"
  },
  "DescribeLiveStreamPublishedList": {
    "params": [
      {
        "name": "DomainName",
        "desc": "您的推流域名。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间。\nUTC 格式，例如：2016-06-30T19:00:00Z。\n不超过当前时间。\n注意：EndTime和StartTime相差不可超过30天。"
      },
      {
        "name": "StartTime",
        "desc": "起始时间。 \nUTC 格式，例如：2016-06-29T19:00:00Z。\n最长支持查询60天内数据。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。不支持模糊匹配。"
      },
      {
        "name": "PageNum",
        "desc": "取得第几页。\n默认值：1。"
      },
      {
        "name": "PageSize",
        "desc": "分页大小。\n最大值：100。\n取值范围：1~100 之前的任意整数。\n默认值：10。"
      },
      {
        "name": "StreamName",
        "desc": "流名称，支持模糊匹配。"
      }
    ],
    "desc": "返回已经推过流的流列表。<br>\n注意：分页最多支持查询1万条记录，可通过调整查询时间范围来获取更多数据。"
  },
  "DescribeLiveDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "域名。"
      }
    ],
    "desc": "查询直播域名信息。"
  },
  "CreateLiveCallbackRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为live。"
      },
      {
        "name": "TemplateId",
        "desc": "模板ID。"
      }
    ],
    "desc": "创建回调规则，需要先调用[CreateLiveCallbackTemplate](/document/product/267/32637)接口创建回调模板，将返回的模板id绑定到域名/路径进行使用。\n<br>回调协议相关文档：[事件消息通知](/document/product/267/32744)。"
  },
  "BindLiveDomainCert": {
    "params": [
      {
        "name": "CertId",
        "desc": "证书Id。使用添加证书接口获取证书Id。"
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
    "desc": "域名绑定证书。\n注意：需先调用添加证书接口进行证书添加。获取到证书Id后再调用该接口进行绑定。"
  },
  "DescribeLiveCallbackRules": {
    "params": [],
    "desc": "获取回调规则列表"
  },
  "DescribePlayErrorCodeDetailInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始时间，北京时间，\n格式：yyyy-mm-dd HH:MM:SS。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，北京时间，\n格式：yyyy-mm-dd HH:MM:SS。\n注：EndTime 和 StartTime 只支持最近1天的数据查询。"
      },
      {
        "name": "Granularity",
        "desc": "查询粒度：\n1-1分钟粒度。"
      },
      {
        "name": "StatType",
        "desc": "是，可选值包括”4xx”,”5xx”，支持”4xx,5xx”等这种混合模式。"
      },
      {
        "name": "PlayDomains",
        "desc": "播放域名列表。"
      },
      {
        "name": "MainlandOrOversea",
        "desc": "地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。"
      }
    ],
    "desc": "查询下行播放错误码信息，某段时间内1分钟粒度的各http错误码出现的次数，包括4xx，5xx。\n\n"
  },
  "DeleteLiveRecordRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。\n域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为 live。\n域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。\n域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。"
      }
    ],
    "desc": "删除录制规则。"
  },
  "ForbidLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为 live。"
      },
      {
        "name": "DomainName",
        "desc": "您的推流域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "ResumeTime",
        "desc": "恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。\n注意：\n1. 默认禁播7天，且最长支持禁播90天。\n2. 北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。"
      },
      {
        "name": "Reason",
        "desc": "禁推原因。\n注明：请务必填写禁推原因，防止误操作。\n长度限制：2048字节。"
      }
    ],
    "desc": "禁止某条流的推送，可以预设某个时刻将流恢复。"
  },
  "AddLiveDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "域名名称。"
      },
      {
        "name": "DomainType",
        "desc": "域名类型，\n0：推流域名，\n1：播放域名。"
      },
      {
        "name": "PlayType",
        "desc": "拉流域名类型：\n1：国内，\n2：全球，\n3：境外。\n默认值：1。"
      },
      {
        "name": "IsDelayLive",
        "desc": "是否是慢直播：\n0： 普通直播，\n1 ：慢直播 。\n默认值： 0。"
      },
      {
        "name": "IsMiniProgramLive",
        "desc": "是否是小程序直播：\n0： 标准直播，\n1 ：小程序直播 。\n默认值： 0。"
      }
    ],
    "desc": "添加域名，一次只能提交一个域名。域名必须已备案。"
  },
  "DescribeLiveDomainPlayInfoList": {
    "params": [
      {
        "name": "PlayDomains",
        "desc": "播放域名列表。"
      }
    ],
    "desc": "查询实时的域名维度下行播放数据，由于数据处理有耗时，接口默认查询4分钟前的准实时数据。"
  },
  "CreateLiveRecordRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "TemplateId",
        "desc": "模板 ID。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为 live。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。\n注：如果本参数设置为非空字符串，规则将只对此推流起作用。"
      }
    ],
    "desc": "创建录制规则，需要先调用[CreateLiveRecordTemplate](/document/product/267/32614)接口创建录制模板，将返回的模板id绑定到流使用。\n<br>录制相关文档：[直播录制](/document/product/267/32739)。"
  },
  "DescribeLiveWatermark": {
    "params": [
      {
        "name": "WatermarkId",
        "desc": "水印 ID。"
      }
    ],
    "desc": "获取单个水印信息。"
  },
  "DescribeLiveTranscodeTemplates": {
    "params": [],
    "desc": "获取转码模板列表。"
  },
  "CreateLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "模板名。仅支持中文、英文、数字、_、-。"
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
      },
      {
        "name": "IsDelayLive",
        "desc": "直播类型，默认 0。\n0：普通直播，\n1：慢直播。"
      },
      {
        "name": "HlsSpecialParam",
        "desc": "HLS专属录制参数。"
      },
      {
        "name": "Mp3Param",
        "desc": "Mp3录制参数，开启Mp3录制时设置。"
      }
    ],
    "desc": "创建录制模板，成功返回模板id后，需要调用[CreateLiveRecordRule](/document/product/267/32615)接口，将模板id绑定到流进行使用。\n<br>录制相关文档：[直播录制](/document/product/267/32739)。"
  },
  "DescribeBillBandwidthAndFluxList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始时间点，格式为yyyy-mm-dd HH:MM:SS。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间点，格式为yyyy-mm-dd HH:MM:SS，起始和结束时间跨度不支持超过31天。"
      },
      {
        "name": "PlayDomains",
        "desc": "直播播放域名，若不填，表示总体数据。"
      },
      {
        "name": "MainlandOrOversea",
        "desc": "可选值：\nMainland：查询国内数据，\nOversea：则查询国外数据，\n默认：查询国内+国外的数据。\n注：LEB（快直播）只支持国内+国外数据查询。"
      },
      {
        "name": "Granularity",
        "desc": "数据粒度，支持如下粒度：\n5：5分钟粒度，（跨度不支持超过1天），\n60：1小时粒度（跨度不支持超过一个月），\n1440：天粒度（跨度不支持超过一个月）。\n默认值：5。"
      },
      {
        "name": "ServiceName",
        "desc": "服务名称，可选值包括LVB(标准直播)，LEB(快直播)，默认值是LVB。"
      }
    ],
    "desc": "直播计费带宽和流量数据查询。"
  },
  "ForbidLiveDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "待停用的直播域名。"
      }
    ],
    "desc": "停止使用某个直播域名。"
  },
  "CreateLiveTranscodeRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "播放域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致。如果只绑定域名，则此处填空。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。如果只绑定域名或路径，则此处填空。"
      },
      {
        "name": "TemplateId",
        "desc": "指定已有的模板Id。"
      }
    ],
    "desc": "创建转码规则，需要先调用[CreateLiveTranscodeTemplate](/document/product/267/32646)接口创建转码模板，将返回的模板id绑定到流使用。\n<br>转码相关文档：[直播转封装及转码](/document/product/267/32736)。"
  },
  "DescribeLiveWatermarkRules": {
    "params": [],
    "desc": "获取水印规则列表。"
  },
  "DeleteLiveRecord": {
    "params": [
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "TaskId",
        "desc": "任务ID，全局唯一标识录制任务。\n从接口 [CreateLiveRecord](/document/product/267/30148) 的返回值中获取TaskId。"
      }
    ],
    "desc": "注：DeleteLiveRecord 接口仅用于删除录制任务记录，不具备停止录制的功能，也不能删除正在进行中的录制。如果需要停止录制任务，请使用终止录制[StopLiveRecord](/document/product/267/30146) 接口。"
  },
  "CreateLiveSnapshotRule": {
    "params": [
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "TemplateId",
        "desc": "模板 ID。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。\n注：如果本参数设置为非空字符串，规则将只对此推流起作用。"
      }
    ],
    "desc": "创建截图规则，需要先调用[CreateLiveSnapshotTemplate](/document/product/267/32624)接口创建截图模板，然后将返回的模板 ID 绑定到流进行使用。\n<br>截图相关文档：[直播截图](/document/product/267/32737)。\n注意：单个域名仅支持关联一个截图模板。"
  },
  "DescribeGroupProIspPlayInfoList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始时间点，格式为yyyy-mm-dd HH:MM:SS。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间点，格式为yyyy-mm-dd HH:MM:SS\n时间跨度在（0,3小时]，支持最近1个月数据查询。"
      },
      {
        "name": "PlayDomains",
        "desc": "播放域名，默认为不填，表示求总体数据。"
      },
      {
        "name": "ProvinceNames",
        "desc": "省份列表，默认不填，则返回各省份的数据。"
      },
      {
        "name": "IspNames",
        "desc": "运营商列表，默认不填，则返回整个运营商的数据。"
      },
      {
        "name": "MainlandOrOversea",
        "desc": "国内还是国外，如果为空，查询所有地区数据；如果为“Mainland”，查询国内数据；如果为“Oversea”，则查询国外数据。"
      }
    ],
    "desc": "查询按省份和运营商分组的下行播放数据。"
  },
  "DescribeAllStreamPlayInfoList": {
    "params": [
      {
        "name": "QueryTime",
        "desc": "查询时间点，精确到分钟粒度，支持最近1个月的数据查询，数据延迟为5分钟左右，如果要查询实时的数据，建议传递5分钟前的时间点，格式为yyyy-mm-dd HH:MM:SS。"
      }
    ],
    "desc": "输入某个时间点（1分钟维度），查询该时间点所有流的下行信息。"
  },
  "DescribeLivePlayAuthKey": {
    "params": [
      {
        "name": "DomainName",
        "desc": "域名。"
      }
    ],
    "desc": "查询播放鉴权key。"
  },
  "DescribeLiveStreamState": {
    "params": [
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为 live。"
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
  "DeleteLiveRecordTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 ID。"
      }
    ],
    "desc": "删除录制模板。"
  },
  "ResumeDelayLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为live。"
      },
      {
        "name": "DomainName",
        "desc": "推流域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "恢复延迟播放设置"
  },
  "CreateLiveTranscodeTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "模板名称，例：900 900p 仅支持字母和数字的组合。"
      },
      {
        "name": "VideoBitrate",
        "desc": "视频码率。范围：100-8000。\n注意：码率必须是100的倍数。"
      },
      {
        "name": "Vcodec",
        "desc": "视频编码：h264/h265，默认h264。"
      },
      {
        "name": "Acodec",
        "desc": "音频编码：aac，默认原始音频格式。\n注意：当前该参数未生效，待后续支持！"
      },
      {
        "name": "AudioBitrate",
        "desc": "音频码率：默认0。0-500。"
      },
      {
        "name": "Description",
        "desc": "模板描述。"
      },
      {
        "name": "Width",
        "desc": "宽，默认0。"
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
        "desc": "高，默认0。"
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
      },
      {
        "name": "AiTransCode",
        "desc": "是否是极速高清模板，0：否，1：是。默认0。"
      },
      {
        "name": "AdaptBitratePercent",
        "desc": "极速高清相比VideoBitrate少多少码率，0.1到0.5"
      }
    ],
    "desc": "创建转码模板，成功返回模板id后，需要调用[CreateLiveTranscodeRule](/document/product/267/32647)接口，将返回的模板id绑定到流使用。\n<br>转码相关文档：[直播转封装及转码](/document/product/267/32736)。"
  },
  "DescribeLiveCerts": {
    "params": [],
    "desc": "获取证书信息列表"
  },
  "EnableLiveDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "待启用的直播域名。"
      }
    ],
    "desc": "启用状态为停用的直播域名。"
  },
  "CancelCommonMixStream": {
    "params": [
      {
        "name": "MixStreamSessionId",
        "desc": "混流会话（申请混流开始到取消混流结束）标识 ID。"
      }
    ],
    "desc": "该接口用来取消混流。用法与 mix_streamv2.cancel_mix_stream 基本一致。"
  },
  "DescribeLivePackageInfo": {
    "params": [
      {
        "name": "PackageType",
        "desc": "包类型，可选值：\n0：流量包；\n1：转码包。"
      }
    ],
    "desc": "查询用户套餐包总量、使用量、剩余量、包状态、购买时间和过期时间等。"
  },
  "CreatePullStreamConfig": {
    "params": [
      {
        "name": "FromUrl",
        "desc": "源 Url ，用于拉流的地址。目前可支持直播流及点播文件。\n注意：\n1. 多个点播url之间使用空格拼接。\n2. 目前上限支持10个url。\n3. 支持拉流文件格式：flv，rtmp，hls，mp4。"
      },
      {
        "name": "ToUrl",
        "desc": "目的 Url ，用于推流的地址，目前限制该目标地址为腾讯域名。\n仅支持：rtmp 协议。"
      },
      {
        "name": "AreaId",
        "desc": "选择完成转拉推的服务所在区域:\n1-深圳，\n2-上海，\n3-天津，\n4-中国香港。"
      },
      {
        "name": "IspId",
        "desc": "选择完成转拉推服务使用的运营商网络：\n1-电信，\n2-移动，\n3-联通，\n4-其他。\n注：AreaId 为4的时候，IspId 只能为其他。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间。\n使用 UTC 格式时间，\n例如：2019-01-08T10:00:00Z。\n注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，注意：\n1. 结束时间必须大于开始时间；\n2. 结束时间和开始时间必须大于当前时间；\n3. 结束时间 和 开始时间 间隔必须小于七天。\n使用 UTC 格式时间，\n例如：2019-01-08T10:00:00Z。\n注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。"
      }
    ],
    "desc": "创建临时拉流转推任务，目前限制添加10条任务。\n\n注意：该接口用于创建临时拉流转推任务，\n拉流源地址即 FromUrl 可以是腾讯或非腾讯数据源，\n但转推目标地址即 ToUrl 目前限制为已注册的腾讯直播域名。"
  },
  "DescribeLiveStreamPushInfoList": {
    "params": [
      {
        "name": "PushDomain",
        "desc": "推流域名。"
      },
      {
        "name": "AppName",
        "desc": "推流路径，与推流和播放地址中的AppName保持一致，默认为live。"
      },
      {
        "name": "PageNum",
        "desc": "页数，\n范围[1,10000]，\n默认值：1。"
      },
      {
        "name": "PageSize",
        "desc": "每页个数，\n范围：[1,1000]，\n默认值： 200。"
      }
    ],
    "desc": "查询所有实时流的推流信息，包括客户端IP，服务端IP，帧率，码率，域名，开始推流时间。"
  },
  "DeleteLiveSnapshotTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 ID。\n1. 在创建截图模板接口 [CreateLiveSnapshotTemplate](/document/product/267/32624) 调用的返回值中获取。\n2. 可以从接口 [DescribeLiveSnapshotTemplates](/document/product/267/32619) 中查询已创建的截图模板列表。"
      }
    ],
    "desc": "删除截图模板"
  }
}