# -*- coding: utf-8 -*-
DESC = "mps-2019-06-12"
INFO = {
  "CreateImageSpriteTemplate": {
    "params": [
      {
        "name": "Width",
        "desc": "雪碧图中小图的宽度，取值范围： [128, 4096]，单位：px。"
      },
      {
        "name": "Height",
        "desc": "雪碧图中小图的高度，取值范围： [128, 4096]，单位：px。"
      },
      {
        "name": "SampleType",
        "desc": "采样类型，取值：\n<li>Percent：按百分比。</li>\n<li>Time：按时间间隔。</li>"
      },
      {
        "name": "SampleInterval",
        "desc": "采样间隔。\n<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>\n<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>"
      },
      {
        "name": "RowCount",
        "desc": "雪碧图中小图的行数。"
      },
      {
        "name": "ColumnCount",
        "desc": "雪碧图中小图的列数。"
      },
      {
        "name": "Name",
        "desc": "雪碧图模板名称，长度限制：64 个字符。"
      }
    ],
    "desc": "创建用户自定义雪碧图模板，数量上限：16。"
  },
  "DeleteAnimatedGraphicsTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "转动图模板唯一标识。"
      }
    ],
    "desc": "删除用户自定义转动图模板。"
  },
  "CreateAnimatedGraphicsTemplate": {
    "params": [
      {
        "name": "Width",
        "desc": "动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "Height",
        "desc": "视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "Fps",
        "desc": "帧率，取值范围：[1, 30]，单位：Hz。"
      },
      {
        "name": "Format",
        "desc": "动图格式，取值为 gif 和 webp。默认为 gif。"
      },
      {
        "name": "Quality",
        "desc": "图片质量，取值范围：[1, 100]，默认值为 75。"
      },
      {
        "name": "Name",
        "desc": "转动图模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      }
    ],
    "desc": "创建用户自定义转动图模板，数量上限：16。"
  },
  "CreateSampleSnapshotTemplate": {
    "params": [
      {
        "name": "Width",
        "desc": "图片宽度，取值范围： [128, 4096]，单位：px。"
      },
      {
        "name": "Height",
        "desc": "图片高度，取值范围： [128, 4096]，单位：px。"
      },
      {
        "name": "SampleType",
        "desc": "采样截图类型，取值：\n<li>Percent：按百分比。</li>\n<li>Time：按时间间隔。</li>"
      },
      {
        "name": "SampleInterval",
        "desc": "采样间隔。\n<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>\n<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>"
      },
      {
        "name": "Name",
        "desc": "采样截图模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Format",
        "desc": "图片格式，取值为 jpg 和 png。默认为 jpg。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      }
    ],
    "desc": "创建用户自定义采样截图模板，数量上限：16。"
  },
  "ModifyAnimatedGraphicsTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "转动图模板唯一标识。"
      },
      {
        "name": "Name",
        "desc": "转动图模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Width",
        "desc": "动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "Height",
        "desc": "视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "Format",
        "desc": "动图格式，取值为 gif 和 webp。"
      },
      {
        "name": "Fps",
        "desc": "帧率，取值范围：[1, 30]，单位：Hz。"
      },
      {
        "name": "Quality",
        "desc": "图片质量，取值范围：[1, 100]，默认值为 75。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      }
    ],
    "desc": "修改用户自定义转动图模板。"
  },
  "DeleteTranscodeTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "转码模板唯一标识。"
      }
    ],
    "desc": "删除用户自定义转码模板。"
  },
  "ModifyTranscodeTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "转码模板唯一标识。"
      },
      {
        "name": "Container",
        "desc": "封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。"
      },
      {
        "name": "Name",
        "desc": "转码模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字节。"
      },
      {
        "name": "RemoveVideo",
        "desc": "是否去除视频数据，可选值：\n<li>0：保留</li>\n<li>1：去除</li>"
      },
      {
        "name": "RemoveAudio",
        "desc": "是否去除音频数据，可选值：\n<li>0：保留</li>\n<li>1：去除</li>"
      },
      {
        "name": "VideoTemplate",
        "desc": "视频流配置参数。"
      },
      {
        "name": "AudioTemplate",
        "desc": "音频流配置参数。"
      },
      {
        "name": "TEHDConfig",
        "desc": "极速高清转码参数，需联系商务架构师开通后才能使用。"
      }
    ],
    "desc": "修改用户自定义转码模板信息。"
  },
  "CreateSnapshotByTimeOffsetTemplate": {
    "params": [
      {
        "name": "Width",
        "desc": "图片宽度，取值范围： [128, 4096]，单位：px。"
      },
      {
        "name": "Height",
        "desc": "图片高度，取值范围： [128, 4096]，单位：px。"
      },
      {
        "name": "Name",
        "desc": "指定时间点截图模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Format",
        "desc": "图片格式，取值可以为 jpg 和 png。默认为 jpg。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      }
    ],
    "desc": "创建用户自定义指定时间点截图模板，数量上限：16。"
  },
  "DescribeSnapshotByTimeOffsetTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "指定时间点截图模板唯一标识过滤条件，数组长度限制：100。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10，最大值：100。"
      },
      {
        "name": "Type",
        "desc": "模板类型过滤条件，可选值：\n<li>Preset：系统预置模板；</li>\n<li>Custom：用户自定义模板。</li>"
      }
    ],
    "desc": "查询指定时间点截图模板，支持根据条件，分页查询。"
  },
  "ModifySampleSnapshotTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "采样截图模板唯一标识。"
      },
      {
        "name": "Name",
        "desc": "采样截图模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Width",
        "desc": "图片宽度，取值范围： [128, 4096]，单位：px。"
      },
      {
        "name": "Height",
        "desc": "图片高度，取值范围： [128, 4096]，单位：px。"
      },
      {
        "name": "SampleType",
        "desc": "采样截图类型，取值：\n<li>Percent：按百分比。</li>\n<li>Time：按时间间隔。</li>"
      },
      {
        "name": "SampleInterval",
        "desc": "采样间隔。\n<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>\n<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>"
      },
      {
        "name": "Format",
        "desc": "图片格式，取值为 jpg 和 png。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      }
    ],
    "desc": "修改用户自定义采样截图模板。"
  },
  "DeleteWatermarkTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "水印模板唯一标识。"
      }
    ],
    "desc": "删除用户自定义水印模板。"
  },
  "DescribeWorkflows": {
    "params": [
      {
        "name": "WorkflowIds",
        "desc": "工作流 ID 过滤条件，数组长度限制：100。"
      },
      {
        "name": "Status",
        "desc": "工作流状态，取值范围：\n<li>Enabled：已启用，</li>\n<li>Disabled：已禁用。</li>\n不填此参数，则不区分工作流状态。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10，最大值：100。"
      }
    ],
    "desc": "根据工作流 ID，获取工作流详情列表。"
  },
  "ResetWorkflow": {
    "params": [
      {
        "name": "WorkflowId",
        "desc": "工作流 ID。"
      },
      {
        "name": "WorkflowName",
        "desc": "工作流名称，最多128字符。同一个用户该名称唯一。"
      },
      {
        "name": "Trigger",
        "desc": "工作流绑定的触发规则，当上传视频命中该规则到该对象时即触发工作流。"
      },
      {
        "name": "OutputStorage",
        "desc": "视频处理的文件输出配置。不填则继承 Trigger 中的存储位置。"
      },
      {
        "name": "OutputDir",
        "desc": "视频处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与触发文件所在的目录一致，即`{inputDir}`。"
      },
      {
        "name": "MediaProcessTask",
        "desc": "视频处理类型任务参数。"
      },
      {
        "name": "TaskPriority",
        "desc": "工作流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。"
      },
      {
        "name": "TaskNotifyConfig",
        "desc": "任务的事件通知信息，不填代表不获取事件通知。"
      }
    ],
    "desc": "重新设置一个已经存在且处于禁用状态的工作流。"
  },
  "DescribeTaskDetail": {
    "params": [
      {
        "name": "TaskId",
        "desc": "视频处理任务的任务 ID。"
      }
    ],
    "desc": "通过任务 ID 查询任务的执行状态和结果的详细信息（最多可以查询3天之内提交的任务）。"
  },
  "ModifyWatermarkTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "水印模板唯一标识。"
      },
      {
        "name": "Name",
        "desc": "水印模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "CoordinateOrigin",
        "desc": "原点位置，可选值：\n<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>\n<li>TopRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>\n<li>BottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>\n<li>BottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下角。</li>\n目前，当 Type 为 image，该字段仅支持 TopLeft。"
      },
      {
        "name": "XPos",
        "desc": "水印原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：\n<li>当字符串以 % 结尾，表示水印 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>\n<li>当字符串以 px 结尾，表示水印 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>"
      },
      {
        "name": "YPos",
        "desc": "水印原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：\n<li>当字符串以 % 结尾，表示水印 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>\n<li>当字符串以 px 结尾，表示水印 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>"
      },
      {
        "name": "ImageTemplate",
        "desc": "图片水印模板，该字段仅对图片水印模板有效。"
      },
      {
        "name": "TextTemplate",
        "desc": "文字水印模板，该字段仅对文字水印模板有效。"
      },
      {
        "name": "SvgTemplate",
        "desc": "SVG水印模板，当 Type 为 svg，该字段必填。当 Type 为 image 或 text，该字段无效。"
      }
    ],
    "desc": "修改用户自定义水印模板，水印类型不允许修改。"
  },
  "DeleteWorkflow": {
    "params": [
      {
        "name": "WorkflowId",
        "desc": "工作流 ID。"
      }
    ],
    "desc": "删除工作流。对于已启用的工作流，需要禁用后才能删除。"
  },
  "DisableWorkflow": {
    "params": [
      {
        "name": "WorkflowId",
        "desc": "工作流 ID。"
      }
    ],
    "desc": "禁用工作流。"
  },
  "DescribeSampleSnapshotTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "采样截图模板唯一标识过滤条件，数组长度限制：100。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10，最大值：100。"
      },
      {
        "name": "Type",
        "desc": "模板类型过滤条件，可选值：\n<li>Preset：系统预置模板；</li>\n<li>Custom：用户自定义模板。</li>"
      }
    ],
    "desc": "查询采样截图模板，支持根据条件，分页查询。"
  },
  "DescribeTranscodeTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "转码模板唯一标识过滤条件，数组长度限制：100。"
      },
      {
        "name": "Type",
        "desc": "模板类型过滤条件，可选值：\n<li>Preset：系统预置模板；</li>\n<li>Custom：用户自定义模板。</li>"
      },
      {
        "name": "ContainerType",
        "desc": "封装格式过滤条件，可选值：\n<li>Video：视频格式，可以同时包含视频流和音频流的封装格式板；</li>\n<li>PureAudio：纯音频格式，只能包含音频流的封装格式。</li>"
      },
      {
        "name": "TEHDType",
        "desc": "极速高清过滤条件，用于过滤普通转码或极速高清转码模板，可选值：\n<li>Common：普通转码模板；</li>\n<li>TEHD：极速高清模板。</li>"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10，最大值：100。"
      }
    ],
    "desc": "根据转码模板唯一标识，获取转码模板详情列表。返回结果包含符合条件的所有用户自定义模板及[系统预置转码模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。"
  },
  "DeleteSampleSnapshotTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "采样截图模板唯一标识。"
      }
    ],
    "desc": "删除用户自定义采样截图模板。"
  },
  "ProcessLiveMedia": {
    "params": [
      {
        "name": "Url",
        "desc": "直播流 URL。"
      },
      {
        "name": "OutputStorage",
        "desc": "直播流处理输出文件的目标存储。如处理有文件输出，该参数为必填项。"
      },
      {
        "name": "OutputDir",
        "desc": "直播流处理生成的文件输出的目标目录，如`/movie/201909/`，如果不填为 `/` 目录。"
      },
      {
        "name": "AiRecognitionTask",
        "desc": "直播流内容识别类型任务参数。"
      },
      {
        "name": "AiAnalysisTask",
        "desc": "直播流内容分析类型任务参数。"
      },
      {
        "name": "TaskNotifyConfig",
        "desc": "任务的事件通知信息，不填代表不获取事件通知。"
      },
      {
        "name": "SessionContext",
        "desc": "来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。"
      },
      {
        "name": "SessionId",
        "desc": "用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。"
      },
      {
        "name": "StartTime",
        "desc": "直播开始时间戳（UTC 时间 单位为秒，该参数仅对于直播流分析有效）。"
      }
    ],
    "desc": "对直播流媒体发起处理任务，功能包括：\n\n1. 智能内容识别（人脸、文本全文、文本关键词、语音全文、语音关键词、物体）。\n2. 智能内容分析（精彩集锦）。\n\n直播流处理事件通知实时写入用户指定的消息队列 CMQ 中，用户需要从消息队列 CMQ 中获取事件通知结果，同时处理过程中存在输出文件的，会写入用户指定的输出文件的目标存储中。"
  },
  "DeleteSnapshotByTimeOffsetTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "指定时间点截图模板唯一标识。"
      }
    ],
    "desc": "删除用户自定义指定时间点截图模板。"
  },
  "DescribeAnimatedGraphicsTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "转动图模板唯一标识过滤条件，数组长度限制：100。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10，最大值：100。"
      },
      {
        "name": "Type",
        "desc": "模板类型过滤条件，可选值：\n<li>Preset：系统预置模板；</li>\n<li>Custom：用户自定义模板。</li>"
      }
    ],
    "desc": "查询转动图模板列表，支持根据条件，分页查询。"
  },
  "EnableWorkflow": {
    "params": [
      {
        "name": "WorkflowId",
        "desc": "工作流 ID。"
      }
    ],
    "desc": "启用工作流。"
  },
  "DescribeUserInfo": {
    "params": [],
    "desc": "用户服务信息查询，返回用户状态和计费类型；若未注册则返回相应错误提示。"
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "Status",
        "desc": "过滤条件：任务状态，可选值：WAITING（等待中）、PROCESSING（处理中）、FINISH（已完成）。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10，最大值：100。"
      },
      {
        "name": "ScrollToken",
        "desc": "翻页标识，分批拉取时使用：当单次请求无法拉取所有数据，接口将会返回 ScrollToken，下一次请求携带该 Token，将会从下一条记录开始获取。"
      }
    ],
    "desc": "* 该接口用于查询任务列表；\n* 当列表数据比较多时，单次接口调用无法拉取整个列表，可通过 ScrollToken 参数，分批拉取；\n* 只能查询到最近三天（72 小时）内的任务。"
  },
  "ModifySnapshotByTimeOffsetTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "指定时间点截图模板唯一标识。"
      },
      {
        "name": "Name",
        "desc": "指定时间点截图模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Width",
        "desc": "图片宽度，取值范围： [128, 4096]，单位：px。"
      },
      {
        "name": "Height",
        "desc": "图片高度，取值范围： [128, 4096]，单位：px。"
      },
      {
        "name": "Format",
        "desc": "图片格式，取值可以为 jpg 和 png。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      }
    ],
    "desc": "修改用户自定义指定时间点截图模板。"
  },
  "CreateTranscodeTemplate": {
    "params": [
      {
        "name": "Container",
        "desc": "封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。"
      },
      {
        "name": "Name",
        "desc": "转码模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "RemoveVideo",
        "desc": "是否去除视频数据，可选值：\n<li>0：保留</li>\n<li>1：去除</li>\n默认值：0。"
      },
      {
        "name": "RemoveAudio",
        "desc": "是否去除音频数据，可选值：\n<li>0：保留</li>\n<li>1：去除</li>\n默认值：0。"
      },
      {
        "name": "VideoTemplate",
        "desc": "视频流配置参数，当 RemoveVideo 为 0，该字段必填。"
      },
      {
        "name": "AudioTemplate",
        "desc": "音频流配置参数，当 RemoveAudio 为 0，该字段必填。"
      },
      {
        "name": "TEHDConfig",
        "desc": "极速高清转码参数，需联系商务架构师开通后才能使用。"
      }
    ],
    "desc": "创建用户自定义转码模板，数量上限：1000。"
  },
  "CreateWorkflow": {
    "params": [
      {
        "name": "WorkflowName",
        "desc": "工作流名称，最多128字符。同一个用户该名称唯一。"
      },
      {
        "name": "Trigger",
        "desc": "工作流绑定的触发规则，当上传视频命中该规则到该对象时即触发工作流。"
      },
      {
        "name": "OutputStorage",
        "desc": "视频处理的文件输出存储位置。不填则继承 Trigger 中的存储位置。"
      },
      {
        "name": "OutputDir",
        "desc": "视频处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与触发文件所在的目录一致。"
      },
      {
        "name": "MediaProcessTask",
        "desc": "视频处理类型任务参数。"
      },
      {
        "name": "TaskNotifyConfig",
        "desc": "任务的事件通知配置，不填代表不获取事件通知。"
      },
      {
        "name": "TaskPriority",
        "desc": "工作流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。"
      }
    ],
    "desc": "对 COS 中指定 Bucket 的目录下上传的媒体文件，设置处理规则，包括：\n1. 视频转码（带水印）；\n2. 视频转动图；\n3. 对视频按指定时间点截图；\n4. 对视频采样截图；\n5. 对视频截图雪碧图；\n6. 对视频转自适应码流。\n\n注意：创建工作流成功后是禁用状态，需要手动启用。"
  },
  "ProcessMedia": {
    "params": [
      {
        "name": "InputInfo",
        "desc": "视频处理的文件输入信息。"
      },
      {
        "name": "OutputStorage",
        "desc": "视频处理输出文件的目标存储。不填则继承 InputInfo 中的存储位置。"
      },
      {
        "name": "OutputDir",
        "desc": "视频处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与 InputInfo 中文件所在的目录一致。"
      },
      {
        "name": "MediaProcessTask",
        "desc": "视频处理类型任务参数。"
      },
      {
        "name": "TaskNotifyConfig",
        "desc": "任务的事件通知信息，不填代表不获取事件通知。"
      },
      {
        "name": "TasksPriority",
        "desc": "任务流的优先级，数值越大优先级越高，取值范围是-10到 10，不填代表0。"
      },
      {
        "name": "SessionId",
        "desc": "用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。"
      },
      {
        "name": "SessionContext",
        "desc": "来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。"
      }
    ],
    "desc": "对 COS 中的媒体文件发起处理任务，功能包括：\n1. 视频转码（带水印）；\n2. 视频转动图；\n3. 对视频按指定时间点截图；\n4. 对视频采样截图；\n5. 对视频截图雪碧图；\n6. 对视频转自适应码流。"
  },
  "ModifyImageSpriteTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "雪碧图模板唯一标识。"
      },
      {
        "name": "Name",
        "desc": "雪碧图模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Width",
        "desc": "雪碧图中小图的宽度，取值范围： [128, 4096]，单位：px。"
      },
      {
        "name": "Height",
        "desc": "雪碧图中小图的高度，取值范围： [128, 4096]，单位：px。"
      },
      {
        "name": "SampleType",
        "desc": "采样类型，取值：\n<li>Percent：按百分比。</li>\n<li>Time：按时间间隔。</li>"
      },
      {
        "name": "SampleInterval",
        "desc": "采样间隔。\n<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>\n<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>"
      },
      {
        "name": "RowCount",
        "desc": "雪碧图中小图的行数。"
      },
      {
        "name": "ColumnCount",
        "desc": "雪碧图中小图的列数。"
      }
    ],
    "desc": "修改用户自定义雪碧图模板。"
  },
  "DescribeImageSpriteTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "雪碧图模板唯一标识过滤条件，数组长度限制：100。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10，最大值：100。"
      },
      {
        "name": "Type",
        "desc": "模板类型过滤条件，可选值：\n<li>Preset：系统预置模板；</li>\n<li>Custom：用户自定义模板。</li>"
      }
    ],
    "desc": "查询雪碧图模板，支持根据条件，分页查询。"
  },
  "DescribeWatermarkTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "水印模板唯一标识过滤条件，数组长度限制：100。"
      },
      {
        "name": "Type",
        "desc": "水印类型过滤条件，可选值：\n<li>image：图片水印；</li>\n<li>text：文字水印。</li>"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数\n<li>默认值：10；</li>\n<li>最大值：100。</li>"
      }
    ],
    "desc": "查询用户自定义水印模板，支持根据条件，分页查询。"
  },
  "CreateWatermarkTemplate": {
    "params": [
      {
        "name": "Type",
        "desc": "水印类型，可选值：\n<li>image：图片水印；</li>\n<li>text：文字水印。</li>"
      },
      {
        "name": "Name",
        "desc": "水印模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "CoordinateOrigin",
        "desc": "原点位置，可选值：\n<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>\n<li>TopRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>\n<li>BottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>\n<li>BottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下角。</li>\n默认值：TopLeft。目前，当 Type 为 image，该字段仅支持 TopLeft。"
      },
      {
        "name": "XPos",
        "desc": "水印原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：\n<li>当字符串以 % 结尾，表示水印 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>\n<li>当字符串以 px 结尾，表示水印 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>\n默认值：0px。"
      },
      {
        "name": "YPos",
        "desc": "水印原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：\n<li>当字符串以 % 结尾，表示水印 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>\n<li>当字符串以 px 结尾，表示水印 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>\n默认值：0px。"
      },
      {
        "name": "ImageTemplate",
        "desc": "图片水印模板，仅当 Type 为 image，该字段必填且有效。"
      },
      {
        "name": "TextTemplate",
        "desc": "文字水印模板，仅当 Type 为 text，该字段必填且有效。"
      },
      {
        "name": "SvgTemplate",
        "desc": "SVG 水印模板，仅当 Type 为 svg，该字段必填且有效。"
      }
    ],
    "desc": "创建用户自定义水印模板，数量上限：1000。"
  },
  "DeleteImageSpriteTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "雪碧图模板唯一标识。"
      }
    ],
    "desc": "删除雪碧图模板。"
  }
}