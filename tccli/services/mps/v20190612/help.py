# -*- coding: utf-8 -*-
DESC = "mps-2019-06-12"
INFO = {
  "CreateSnapshotByTimeOffsetTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "指定时间点截图模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Width",
        "desc": "截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "Height",
        "desc": "截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "分辨率自适应，可选值：\n<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>\n<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>\n默认值：open。"
      },
      {
        "name": "Format",
        "desc": "图片格式，取值可以为 jpg 和 png。默认为 jpg。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "FillType",
        "desc": "填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：\n<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>\n<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>\n<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>\n<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>\n默认值：black 。"
      }
    ],
    "desc": "创建用户自定义指定时间点截图模板，数量上限：16。"
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
  "CreateAnimatedGraphicsTemplate": {
    "params": [
      {
        "name": "Fps",
        "desc": "帧率，取值范围：[1, 30]，单位：Hz。"
      },
      {
        "name": "Width",
        "desc": "动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "Height",
        "desc": "动图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "分辨率自适应，可选值：\n<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>\n<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>\n默认值：open。"
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
  "DescribeAdaptiveDynamicStreamingTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "转自适应码流模板唯一标识过滤条件，数组长度限制：100。"
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
    "desc": "查询转自适应码流模板，支持根据条件，分页查询。"
  },
  "CreateContentReviewTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "内容审核模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Comment",
        "desc": "内容审核模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "PornConfigure",
        "desc": "鉴黄控制参数。"
      },
      {
        "name": "TerrorismConfigure",
        "desc": "鉴恐控制参数。"
      },
      {
        "name": "PoliticalConfigure",
        "desc": "鉴政控制参数。"
      },
      {
        "name": "ProhibitedConfigure",
        "desc": "违禁控制参数。违禁内容包括：\n<li>谩骂；</li>\n<li>涉毒违法。</li>\n注意：此参数尚未支持。"
      },
      {
        "name": "UserDefineConfigure",
        "desc": "用户自定义内容审核控制参数。"
      }
    ],
    "desc": "创建用户自定义内容审核模板，数量上限：50。"
  },
  "CreateSampleSnapshotTemplate": {
    "params": [
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
        "name": "Width",
        "desc": "截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "Height",
        "desc": "截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "分辨率自适应，可选值：\n<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>\n<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>\n默认值：open。"
      },
      {
        "name": "Format",
        "desc": "图片格式，取值为 jpg 和 png。默认为 jpg。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "FillType",
        "desc": "填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：\n<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>\n<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>\n<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>\n<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>\n默认值：black 。"
      }
    ],
    "desc": "创建用户自定义采样截图模板，数量上限：16。"
  },
  "EditMedia": {
    "params": [
      {
        "name": "FileInfos",
        "desc": "输入的视频文件信息。"
      },
      {
        "name": "OutputStorage",
        "desc": "视频处理输出文件的目标存储。"
      },
      {
        "name": "OutputObjectPath",
        "desc": "视频处理输出文件的目标路径。"
      },
      {
        "name": "TaskNotifyConfig",
        "desc": "任务的事件通知信息，不填代表不获取事件通知。"
      },
      {
        "name": "TasksPriority",
        "desc": "任务优先级，数值越大优先级越高，取值范围是-10到 10，不填代表0。"
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
    "desc": "对视频进行编辑（剪辑、拼接等），生成一个新的点播视频。编辑的功能包括：\n\n1. 对一个文件进行剪辑，生成一个新的视频；\n2. 对多个文件进行拼接，生成一个新的视频；\n3. 对多个文件进行剪辑，然后再拼接，生成一个新的视频。"
  },
  "DeleteAIAnalysisTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "视频内容分析模板唯一标识。"
      }
    ],
    "desc": "删除用户自定义内容分析模板。\n\n注意：模板 ID 为 10000 以下的为系统预置模板，不允许删除。"
  },
  "DeletePersonSample": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人物 ID。"
      }
    ],
    "desc": "该接口用于根据人物 ID，删除人物样本。"
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
        "desc": "模板描述信息，长度限制：256 个字符。"
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
        "desc": "极速高清转码参数。"
      }
    ],
    "desc": "修改用户自定义转码模板信息。"
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
  "DescribeAIAnalysisTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "视频内容分析模板唯一标识过滤条件，数组长度限制：10。"
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
    "desc": "根据内容分析模板唯一标识，获取内容分析模板详情列表。返回结果包含符合条件的所有用户自定义内容分析模板及系统预置视频内容分析模板"
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
  "ModifyAIRecognitionTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "视频内容识别模板唯一标识。"
      },
      {
        "name": "Name",
        "desc": "视频内容识别模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Comment",
        "desc": "视频内容识别模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "FaceConfigure",
        "desc": "人脸识别控制参数。"
      },
      {
        "name": "OcrFullTextConfigure",
        "desc": "文本全文识别控制参数。"
      },
      {
        "name": "OcrWordsConfigure",
        "desc": "文本关键词识别控制参数。"
      },
      {
        "name": "AsrFullTextConfigure",
        "desc": "语音全文识别控制参数。"
      },
      {
        "name": "AsrWordsConfigure",
        "desc": "语音关键词识别控制参数。"
      }
    ],
    "desc": "修改用户自定义内容识别模板。"
  },
  "ModifyAdaptiveDynamicStreamingTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "转自适应码流模板唯一标识。"
      },
      {
        "name": "Name",
        "desc": "模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Format",
        "desc": "转自适应码流格式，取值范围：\n<li>HLS，</li>\n<li>MPEG-DASH。</li>"
      },
      {
        "name": "DisableHigherVideoBitrate",
        "desc": "是否禁止视频低码率转高码率，取值范围：\n<li>0：否，</li>\n<li>1：是。</li>"
      },
      {
        "name": "DisableHigherVideoResolution",
        "desc": "是否禁止视频分辨率转高分辨率，取值范围：\n<li>0：否，</li>\n<li>1：是。</li>"
      },
      {
        "name": "StreamInfos",
        "desc": "转自适应码流输入流参数信息，最多输入10路流。\n注意：各个流的帧率必须保持一致；如果不一致，采用第一个流的帧率作为输出帧率。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      }
    ],
    "desc": "修改转自适应码流模板"
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
        "desc": "截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "Height",
        "desc": "截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "分辨率自适应，可选值：\n<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>\n<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>\n默认值：open。"
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
      },
      {
        "name": "FillType",
        "desc": "填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：\n<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>\n<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>\n<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>\n<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>\n默认值：black 。"
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
        "name": "AiContentReviewTask",
        "desc": "视频内容审核类型任务参数。"
      },
      {
        "name": "AiAnalysisTask",
        "desc": "视频内容分析类型任务参数。"
      },
      {
        "name": "AiRecognitionTask",
        "desc": "视频内容识别类型任务参数。"
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
  "ParseLiveStreamProcessNotification": {
    "params": [
      {
        "name": "Content",
        "desc": "从 CMQ 获取到的直播流事件通知内容。"
      }
    ],
    "desc": "从 CMQ 获取到消息后，从消息的 msgBody 字段中解析出 MPS 直播流处理事件通知的内容。\n该接口不用于发起网络调用，而是用来帮助生成各个语言平台的 SDK，您可以参考 SDK 的中解析函数的实现事件通知的解析。"
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
        "desc": "动图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "分辨率自适应，可选值：\n<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>\n<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>\n默认值：open。"
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
  "DescribeWordSamples": {
    "params": [
      {
        "name": "Usages",
        "desc": "<b>关键词应用场景过滤条件，可选值：</b>\n1. Recognition.Ocr：通过光学字符识别技术，进行内容识别；\n2. Recognition.Asr：通过语音识别技术，进行内容识别；\n3. Review.Ocr：通过光学字符识别技术，进行内容审核；\n4. Review.Asr：通过语音识别技术，进行内容审核；\n<b>可合并简写为：</b>\n5. Recognition：通过光学字符识别技术、语音识别技术，进行内容识别，等价于 1+2；\n6. Review：通过光学字符识别技术、语音识别技术，进行内容审核，等价于 3+4；\n可多选，元素间关系为 or，即关键词的应用场景包含该字段集合中任意元素的记录，均符合该条件。"
      },
      {
        "name": "Keywords",
        "desc": "关键词过滤条件，数组长度限制：100 个词。"
      },
      {
        "name": "Tags",
        "desc": "标签过滤条件，数组长度限制：20 个词。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：100，最大值：100。"
      }
    ],
    "desc": "该接口用于根据应用场景、关键词、标签，分页查询关键词样本信息。"
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
        "desc": "原点位置，可选值：\n<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>\n<li>TopRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>\n<li>BottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>\n<li>BottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下角。</li>"
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
  "DeleteWordSamples": {
    "params": [
      {
        "name": "Keywords",
        "desc": "关键词，数组长度限制：100 个词。"
      }
    ],
    "desc": "该接口用于批量删除关键词样本。"
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
  "DeleteAdaptiveDynamicStreamingTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "自适应转码模板唯一标识。"
      }
    ],
    "desc": "删除转自适应码流模板"
  },
  "CreateAdaptiveDynamicStreamingTemplate": {
    "params": [
      {
        "name": "Format",
        "desc": "自适应转码格式，取值范围：\n<li>HLS，</li>\n<li>MPEG-DASH。</li>"
      },
      {
        "name": "StreamInfos",
        "desc": "转自适应码流输出子流参数信息，最多输出10路子流。\n注意：各个子流的帧率必须保持一致；如果不一致，采用第一个子流的帧率作为输出帧率。"
      },
      {
        "name": "Name",
        "desc": "模板名称，长度限制：64 个字符。"
      },
      {
        "name": "DisableHigherVideoBitrate",
        "desc": "是否禁止视频低码率转高码率，取值范围：\n<li>0：否，</li>\n<li>1：是。</li>\n默认为否。"
      },
      {
        "name": "DisableHigherVideoResolution",
        "desc": "是否禁止视频分辨率转高分辨率，取值范围：\n<li>0：否，</li>\n<li>1：是。</li>\n默认为否。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      }
    ],
    "desc": "创建转自适应码流模板，数量上限：100。"
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
  "CreateWatermarkTemplate": {
    "params": [
      {
        "name": "Type",
        "desc": "水印类型，可选值：\n<li>image：图片水印；</li>\n<li>text：文字水印；</li>\n<li>svg：SVG 水印。</li>"
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
        "desc": "原点位置，可选值：\n<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>\n<li>TopRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>\n<li>BottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>\n<li>BottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下角。</li>\n默认值：TopLeft。"
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
  "DescribePersonSamples": {
    "params": [
      {
        "name": "Type",
        "desc": "拉取的人物类型，可选值：\n<li>UserDefine：用户自定义人物库；</li>\n<li>Default：系统默认人物库。</li>\n\n默认值：UserDefine，拉取用户自定义人物库人物。\n说明：如果是拉取系统默认人物库，只能使用人物名字或者人物 ID + 人物名字的方式进行拉取，且人脸图片只返回一张。"
      },
      {
        "name": "PersonIds",
        "desc": "人物 ID，数组长度限制：100。"
      },
      {
        "name": "Names",
        "desc": "人物名称，数组长度限制：20。"
      },
      {
        "name": "Tags",
        "desc": "人物标签，数组长度限制：20。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：100，最大值：100。"
      }
    ],
    "desc": "该接口用于查询人物样本信息，支持根据人物 ID、名称、标签，分页查询。"
  },
  "ParseNotification": {
    "params": [
      {
        "name": "Content",
        "desc": "从 CMQ 获取到的事件通知内容。"
      }
    ],
    "desc": "从 CMQ 获取到消息后，从消息的 msgBody 字段中解析出 MPS 事件通知的内容。\n该接口不用于发起网络调用，而是用来帮助生成各个语言平台的 SDK，您可以参考 SDK 的中解析函数的实现事件通知的解析。"
  },
  "DeleteAIRecognitionTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "视频内容识别模板唯一标识。"
      }
    ],
    "desc": "删除用户自定义内容识别模板。"
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
  "CreateAIAnalysisTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "视频内容分析模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Comment",
        "desc": "视频内容分析模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "ClassificationConfigure",
        "desc": "智能分类任务控制参数。"
      },
      {
        "name": "TagConfigure",
        "desc": "智能标签任务控制参数。"
      },
      {
        "name": "CoverConfigure",
        "desc": "智能封面任务控制参数。"
      },
      {
        "name": "FrameTagConfigure",
        "desc": "智能按帧标签任务控制参数。"
      }
    ],
    "desc": "创建用户自定义内容分析模板，数量上限：50。"
  },
  "ManageTask": {
    "params": [
      {
        "name": "OperationType",
        "desc": "操作类型，取值范围：\n<li>Abort：终止任务。</li>"
      },
      {
        "name": "TaskId",
        "desc": "视频处理的任务 ID。"
      }
    ],
    "desc": "对已发起的任务进行管理。\n> 注意：目前仅支持终止执行中的直播流处理任务。"
  },
  "ModifyAIAnalysisTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "视频内容分析模板唯一标识。"
      },
      {
        "name": "Name",
        "desc": "视频内容分析模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Comment",
        "desc": "视频内容分析模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "ClassificationConfigure",
        "desc": "智能分类任务控制参数。"
      },
      {
        "name": "TagConfigure",
        "desc": "智能标签任务控制参数。"
      },
      {
        "name": "CoverConfigure",
        "desc": "智能封面任务控制参数。"
      },
      {
        "name": "FrameTagConfigure",
        "desc": "智能按帧标签任务控制参数。"
      }
    ],
    "desc": "修改用户自定义内容分析模板。\n\n注意：模板 ID 10000 以下的为系统预置模板，不允许修改。"
  },
  "DescribeMediaMetaData": {
    "params": [
      {
        "name": "InputInfo",
        "desc": "需要获取元信息的文件输入信息。"
      }
    ],
    "desc": "获取媒体的元信息，包括视频画面宽、高、编码格式、时长、帧率等。"
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
        "desc": "极速高清转码参数。"
      }
    ],
    "desc": "创建用户自定义转码模板，数量上限：1000。"
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
        "desc": "截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "Height",
        "desc": "截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "分辨率自适应，可选值：\n<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>\n<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>\n默认值：open。"
      },
      {
        "name": "Format",
        "desc": "图片格式，取值可以为 jpg 和 png。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "FillType",
        "desc": "填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：\n<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>\n<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>\n<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>\n<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>\n默认值：black 。"
      }
    ],
    "desc": "修改用户自定义指定时间点截图模板。"
  },
  "ModifyPersonSample": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人物 ID。"
      },
      {
        "name": "Name",
        "desc": "名称，长度限制：128 个字符。"
      },
      {
        "name": "Description",
        "desc": "描述，长度限制：1024 个字符。"
      },
      {
        "name": "Usages",
        "desc": "人物应用场景，可选值：\n1. Recognition：用于内容识别，等价于 Recognition.Face。\n2. Review：用于内容审核，等价于 Review.Face。\n3. All：用于内容识别、内容审核，等价于 1+2。"
      },
      {
        "name": "FaceOperationInfo",
        "desc": "人脸操作信息。"
      },
      {
        "name": "TagOperationInfo",
        "desc": "标签操作信息。"
      }
    ],
    "desc": "该接口用于根据人物 ID，修改人物样本信息，包括名称、描述的修改，以及人脸、标签的添加、删除、重置操作。人脸删除操作需保证至少剩余 1 张图片，否则，请使用重置操作。"
  },
  "CreateWordSamples": {
    "params": [
      {
        "name": "Usages",
        "desc": "<b>关键词应用场景，可选值：</b>\n1. Recognition.Ocr：通过光学字符识别技术，进行内容识别；\n2. Recognition.Asr：通过语音识别技术，进行内容识别；\n3. Review.Ocr：通过光学字符识别技术，进行内容审核；\n4. Review.Asr：通过语音识别技术，进行内容审核；\n<b>可合并简写为：</b>\n5. Recognition：通过光学字符识别技术、语音识别技术，进行内容识别，等价于 1+2；\n6. Review：通过光学字符识别技术、语音识别技术，进行内容审核，等价于 3+4；\n7. All：通过光学字符识别技术、语音识别技术，进行内容识别、内容审核，等价于 1+2+3+4。"
      },
      {
        "name": "Words",
        "desc": "关键词，数组长度限制：100。"
      }
    ],
    "desc": "该接口用于批量创建关键词样本，样本用于通过OCR、ASR技术，进行内容审核、内容识别等视频处理。"
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
        "name": "AiContentReviewTask",
        "desc": "视频内容审核类型任务参数。"
      },
      {
        "name": "AiAnalysisTask",
        "desc": "视频内容分析类型任务参数。"
      },
      {
        "name": "AiRecognitionTask",
        "desc": "视频内容识别类型任务参数。"
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
    "desc": "对 COS 中指定 Bucket 的目录下上传的媒体文件，设置处理规则，包括：\n1. 视频转码（带水印）；\n2. 视频转动图；\n3. 对视频按指定时间点截图；\n4. 对视频采样截图；\n5. 对视频截图雪碧图；\n6. 对视频转自适应码流；\n7. 智能内容审核（鉴黄、鉴恐、鉴政）；\n8. 智能内容分析（标签、分类、封面、按帧标签）；\n9. 智能内容识别（人脸、文本全文、文本关键词、语音全文、语音关键词）。\n\n注意：创建工作流成功后是禁用状态，需要手动启用。"
  },
  "ProcessLiveStream": {
    "params": [
      {
        "name": "Url",
        "desc": "直播流 URL（必须是直播文件地址，支持 rtmp，hls 和 flv 等）。"
      },
      {
        "name": "TaskNotifyConfig",
        "desc": "任务的事件通知信息，用于指定直播流处理的结果。"
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
        "name": "AiContentReviewTask",
        "desc": "视频内容审核类型任务参数。"
      },
      {
        "name": "AiRecognitionTask",
        "desc": "视频内容识别类型任务参数。"
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
    "desc": "对直播流媒体发起处理任务，功能包括：\n\n* 智能内容审核（画面鉴黄、鉴政、鉴暴、声音鉴黄）。\n\n直播流处理事件通知实时写入用户指定的消息队列 CMQ 中，用户需要从消息队列 CMQ 中获取事件通知结果，同时处理过程中存在输出文件的，会写入用户指定的输出文件的目标存储中。"
  },
  "ModifyContentReviewTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "内容审核模板唯一标识。"
      },
      {
        "name": "Name",
        "desc": "内容审核模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Comment",
        "desc": "内容审核模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "PornConfigure",
        "desc": "鉴黄控制参数。"
      },
      {
        "name": "TerrorismConfigure",
        "desc": "鉴恐控制参数。"
      },
      {
        "name": "PoliticalConfigure",
        "desc": "鉴政控制参数。"
      },
      {
        "name": "ProhibitedConfigure",
        "desc": "违禁控制参数。违禁内容包括：\n<li>谩骂；</li>\n<li>涉毒违法。</li>\n注意：此参数尚未支持。"
      },
      {
        "name": "UserDefineConfigure",
        "desc": "用户自定义内容审核控制参数。"
      }
    ],
    "desc": "修改用户自定义内容审核模板。"
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
        "name": "AiContentReviewTask",
        "desc": "视频内容审核类型任务参数。"
      },
      {
        "name": "AiAnalysisTask",
        "desc": "视频内容分析类型任务参数。"
      },
      {
        "name": "AiRecognitionTask",
        "desc": "视频内容识别类型任务参数。"
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
    "desc": "对 COS 中的媒体文件发起处理任务，功能包括：\n1. 视频转码（带水印）；\n2. 视频转动图；\n3. 对视频按指定时间点截图；\n4. 对视频采样截图；\n5. 对视频截图雪碧图；\n6. 对视频转自适应码流；\n7. 智能内容审核（鉴黄、鉴恐、鉴政）；\n8. 智能内容分析（标签、分类、封面、按帧标签）；\n9. 智能内容识别（人脸、文本全文、文本关键词、语音全文、语音关键词）。"
  },
  "CreateAIRecognitionTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "视频内容识别模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Comment",
        "desc": "视频内容识别模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "FaceConfigure",
        "desc": "人脸识别控制参数。"
      },
      {
        "name": "OcrFullTextConfigure",
        "desc": "文本全文识别控制参数。"
      },
      {
        "name": "OcrWordsConfigure",
        "desc": "文本关键词识别控制参数。"
      },
      {
        "name": "AsrFullTextConfigure",
        "desc": "语音全文识别控制参数。"
      },
      {
        "name": "AsrWordsConfigure",
        "desc": "语音关键词识别控制参数。"
      }
    ],
    "desc": "创建用户自定义内容识别模板，数量上限：50。"
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
        "desc": "雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "Height",
        "desc": "雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "分辨率自适应，可选值：\n<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>\n<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>\n默认值：open。"
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
        "name": "FillType",
        "desc": "填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：\n<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>\n<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>\n默认值：black 。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      }
    ],
    "desc": "修改用户自定义雪碧图模板。"
  },
  "ModifyWordSample": {
    "params": [
      {
        "name": "Keyword",
        "desc": "关键词，长度限制：128 个字符。"
      },
      {
        "name": "Usages",
        "desc": "<b>关键词应用场景，可选值：</b>\n1. Recognition.Ocr：通过光学字符识别技术，进行内容识别；\n2. Recognition.Asr：通过语音识别技术，进行内容识别；\n3. Review.Ocr：通过光学字符识别技术，进行内容审核；\n4. Review.Asr：通过语音识别技术，进行内容审核；\n<b>可合并简写为：</b>\n5. Recognition：通过光学字符识别技术、语音识别技术，进行内容识别，等价于 1+2；\n6. Review：通过光学字符识别技术、语音识别技术，进行内容审核，等价于 3+4；\n7. All：通过光学字符识别技术、语音识别技术，进行内容识别、内容审核，等价于 1+2+3+4。"
      },
      {
        "name": "TagOperationInfo",
        "desc": "标签操作信息。"
      }
    ],
    "desc": "该接口用于修改关键词的应用场景、标签，关键词本身不可修改，如需修改，可删除重建。"
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
  "DeleteContentReviewTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "内容审核模板唯一标识。"
      }
    ],
    "desc": "删除用户自定义内容审核模板。"
  },
  "CreatePersonSample": {
    "params": [
      {
        "name": "Name",
        "desc": "人物名称，长度限制：20 个字符。"
      },
      {
        "name": "Usages",
        "desc": "人物应用场景，可选值：\n1. Recognition：用于内容识别，等价于 Recognition.Face。\n2. Review：用于内容审核，等价于 Review.Face。\n3. All：用于内容识别、内容审核，等价于 1+2。"
      },
      {
        "name": "Description",
        "desc": "人物描述，长度限制：1024 个字符。"
      },
      {
        "name": "FaceContents",
        "desc": "人脸图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串，仅支持 jpeg、png 图片格式。数组长度限制：5 张图片。\n注意：图片必须是单人像正面人脸较清晰的照片，像素不低于 200*200。"
      },
      {
        "name": "Tags",
        "desc": "人物标签\n<li>数组长度限制：20 个标签；</li>\n<li>单个标签长度限制：128 个字符。</li>"
      }
    ],
    "desc": "该接口用于创建人物样本，用于通过人脸识别等技术，进行内容识别、内容审核等视频处理。"
  },
  "DescribeAIRecognitionTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "视频内容识别模板唯一标识过滤条件，数组长度限制：10。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10，最大值：50。"
      }
    ],
    "desc": "根据内容识别模板唯一标识，获取内容识别模板详情列表。返回结果包含符合条件的所有用户自定义内容识别模板及系统预置视频内容识别模板"
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
  "CreateImageSpriteTemplate": {
    "params": [
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
      },
      {
        "name": "Width",
        "desc": "雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "Height",
        "desc": "雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n<li>当 Width、Height 均为 0，则分辨率同源；</li>\n<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>\n<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>\n<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n默认值：0。"
      },
      {
        "name": "ResolutionAdaptive",
        "desc": "分辨率自适应，可选值：\n<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>\n<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>\n默认值：open。"
      },
      {
        "name": "FillType",
        "desc": "填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：\n<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>\n<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>\n默认值：black 。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      }
    ],
    "desc": "创建用户自定义雪碧图模板，数量上限：16。"
  },
  "DeleteImageSpriteTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "雪碧图模板唯一标识。"
      }
    ],
    "desc": "删除雪碧图模板。"
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
  "DescribeContentReviewTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "内容审核模板唯一标识过滤条件，数组长度限制：50。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10，最大值：50。"
      }
    ],
    "desc": "根据内容审核模板唯一标识，获取内容审核模板详情列表。返回结果包含符合条件的所有用户自定义模板及系统预置内容审核模板。"
  }
}