# -*- coding: utf-8 -*-
DESC = "vod-2018-07-17"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      },
      {
        "name": "FillType",
        "desc": "填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：\n<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>\n<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>\n<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>\n<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>\n默认值：black 。"
      }
    ],
    "desc": "创建用户自定义指定时间点截图模板，数量上限：16。"
  },
  "EditMedia": {
    "params": [
      {
        "name": "InputType",
        "desc": "输入视频的类型，可以取的值为  File，Stream 两种。"
      },
      {
        "name": "FileInfos",
        "desc": "输入的视频文件信息，当 InputType 为 File 时必填。"
      },
      {
        "name": "StreamInfos",
        "desc": "输入的流信息，当 InputType 为 Stream 时必填。"
      },
      {
        "name": "Definition",
        "desc": "编辑模板 ID，取值有 10，20，不填代表使用 10 模板。\n<li>10：拼接时，以分辨率最高的输入为基准；</li>\n<li>20：拼接时，以码率最高的输入为基准；</li>"
      },
      {
        "name": "ProcedureName",
        "desc": "[任务流模板](/document/product/266/11700#.E4.BB.BB.E5.8A.A1.E6.B5.81.E6.A8.A1.E6.9D.BF)名字，如果要对生成的新视频执行任务流时填写。"
      },
      {
        "name": "OutputConfig",
        "desc": "编辑后生成的文件配置。"
      },
      {
        "name": "SessionContext",
        "desc": "标识来源上下文，用于透传用户请求信息，在EditMediaComplete回调和任务流状态变更回调将返回该字段值，最长 1000个字符。"
      },
      {
        "name": "TasksPriority",
        "desc": "任务的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。"
      },
      {
        "name": "SessionId",
        "desc": "用于任务去重的识别码，如果一天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "对视频进行编辑（剪辑、拼接等），生成一个新的点播视频。编辑的功能包括：\n\n1. 对点播中的一个文件进行剪辑，生成一个新的视频；\n2. 对点播中的多个文件进行拼接，生成一个新的视频；\n3. 对点播中的多个文件进行剪辑，然后再拼接，生成一个新的视频；\n4. 对点播中的一个流，直接生成一个新的视频；\n5. 对点播中的一个流进行剪辑，生成一个新的视频；\n6. 对点播中的多个流进行拼接，生成一个新的视频；\n7. 对点播中的多个流进行剪辑，然后拼接，生成一个新的视频。\n\n对于生成的新视频，还可以指定生成后的视频是否要执行任务流。\n\n>当对直播流做剪辑、拼接等操作时，请确保流结束后再操作。否则生成的视频可能不完整。\n\n如使用事件通知，事件通知的类型为 [视频编辑完成](https://cloud.tencent.com/document/product/266/33794)。"
  },
  "ApplyUpload": {
    "params": [
      {
        "name": "MediaType",
        "desc": "媒体类型，可选值请参考 [上传能力综述](/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)。"
      },
      {
        "name": "MediaName",
        "desc": "媒体名称。"
      },
      {
        "name": "CoverType",
        "desc": "封面类型，可选值请参考 [上传能力综述](/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)。"
      },
      {
        "name": "Procedure",
        "desc": "媒体后续任务处理操作，即完成媒体上传后，可自动发起任务流操作。参数值为任务流模板名，云点播支持 [创建任务流模板](/document/product/266/33819) 并为模板命名。"
      },
      {
        "name": "ExpireTime",
        "desc": "媒体文件过期时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。"
      },
      {
        "name": "StorageRegion",
        "desc": "指定上传园区，仅适用于对上传地域有特殊需求的用户。"
      },
      {
        "name": "ClassId",
        "desc": "分类ID，用于对媒体进行分类管理，可通过 [创建分类](/document/product/266/7812) 接口，创建分类，获得分类 ID。\n<li>默认值：0，表示其他分类。</li>"
      },
      {
        "name": "SourceContext",
        "desc": "来源上下文，用于透传用户请求信息，[上传完成回调](/document/product/266/7830) 将返回该字段值，最长 250 个字符。"
      },
      {
        "name": "SessionContext",
        "desc": "会话上下文，用于透传用户请求信息，当指定 Procedure 参数后，[任务流状态变更回调](/document/product/266/9636) 将返回该字段值，最长 1000 个字符。"
      },
      {
        "name": "ExtInfo",
        "desc": "保留字段，特殊用途时使用。"
      },
      {
        "name": "SubAppId",
        "desc": "点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "* 我们强烈建议您使用云点播提供的 [服务端上传 SDK](/document/product/266/9759#1.-.E5.8F.91.E8.B5.B7.E4.B8.8A.E4.BC.A0) 来上传文件。直接调用 API 进行上传的难度和工作量都显著大于使用 SDK。\n* 该接口用于申请媒体文件（和封面文件）的上传，获取文件上传到云点播的元信息（包括上传路径、上传签名等），用于后续上传接口。\n* 上传流程请参考 [服务端上传综述](/document/product/266/9759)。"
  },
  "DeleteAnimatedGraphicsTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "转动图模板唯一标识。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "删除用户自定义转动图模板。"
  },
  "DescribeAIAnalysisTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "视频内容分析模板唯一标识过滤条件，数组长度最大值：100。"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "根据视频内容分析模板唯一标识，获取视频内容分析模板详情列表。返回结果包含符合条件的所有用户自定义视频内容分析模板及[系统预置视频内容分析模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.88.86.E6.9E.90.E6.A8.A1.E6.9D.BF)。"
  },
  "PullEvents": {
    "params": [
      {
        "name": "ExtInfo",
        "desc": "保留字段，特殊用途时使用。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "* 该接口用于业务服务器以 [可靠回调](https://cloud.tencent.com/document/product/266/33779#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83) 的方式获取事件通知；\n* 接口为长轮询模式，即：如果服务端存在未消费事件，则立即返回给请求方；如果服务端没有未消费事件，则后台会将请求挂起，直到有新的事件产生为止；\n* 请求最多挂起5秒，建议请求方将超时时间设置为10秒；\n* 若该接口有事件返回，调用方必须在<font color=\"red\">30秒</font>内调用 [确认事件通知](https://cloud.tencent.com/document/product/266/33434) 接口，确认事件通知已经处理，否则该事件通知在<font color=\"red\">30秒</font>后会再次被拉取到。"
  },
  "ProcessMediaByProcedure": {
    "params": [
      {
        "name": "FileId",
        "desc": "媒体文件 ID。"
      },
      {
        "name": "ProcedureName",
        "desc": "[任务流模板](/document/product/266/11700#.E4.BB.BB.E5.8A.A1.E6.B5.81.E6.A8.A1.E6.9D.BF)名字。"
      },
      {
        "name": "TasksPriority",
        "desc": "任务流的优先级，数值越大优先级越高，取值范围是-10到10，不填代表0。"
      },
      {
        "name": "TasksNotifyMode",
        "desc": "任务流状态变更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。"
      },
      {
        "name": "SessionContext",
        "desc": "来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。"
      },
      {
        "name": "SessionId",
        "desc": "用于去重的识别码，如果一天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。"
      },
      {
        "name": "ExtInfo",
        "desc": "保留字段，特殊用途时使用。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "使用任务流模板，对点播中的视频发起处理任务。\n有两种方式创建任务流模板：\n1. 在控制台上创建和修改任务流模板；\n2. 通过任务流模板接口创建任务流模板。\n\n如使用事件通知，事件通知的类型为 [任务流状态变更](https://cloud.tencent.com/document/product/266/9636)。"
  },
  "DeleteTranscodeTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "转码模板唯一标识。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "删除用户自定义转码模板。"
  },
  "DescribeTaskDetail": {
    "params": [
      {
        "name": "TaskId",
        "desc": "视频处理任务的任务 ID。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "通过任务 ID 查询任务的执行状态和结果的详细信息（最多可以查询3天之内提交的任务）。"
  },
  "DescribeReviewDetails": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始日期。使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。"
      },
      {
        "name": "EndTime",
        "desc": "结束日期，需大于起始日期。使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "该接口返回查询时间范围内每天使用的视频内容审核时长数据，单位： 秒。\n\n1. 可以查询最近365天内的视频内容审核时长统计数据。\n2. 查询时间跨度不超过90天。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "该接口用于根据应用场景、关键词、标签，分页查询关键词样本信息。"
  },
  "DescribeStorageData": {
    "params": [
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "查询存储空间使用情况和文件数量。"
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
      },
      {
        "name": "HighlightConfigure",
        "desc": "智能精彩集锦任务控制参数。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改用户自定义视频内容分析模板。\n\n注意：模板 ID 10000 以下的为系统预置模板，不允许修改。"
  },
  "DeleteProcedureTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "任务流名字。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "删除用户自定义的任务流模板。  "
  },
  "DeleteAdaptiveDynamicStreamingTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "自适应转码模板唯一标识。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "删除转自适应码流模板"
  },
  "CreateAdaptiveDynamicStreamingTemplate": {
    "params": [
      {
        "name": "Format",
        "desc": "自适应转码格式，取值范围：\n<li>HLS。</li>"
      },
      {
        "name": "StreamInfos",
        "desc": "自适应转码输出子流参数信息，最多输出10路子流。\n注意：各个子流的帧率必须保持一致；如果不一致，采用第一个子流的帧率作为输出帧率。"
      },
      {
        "name": "Name",
        "desc": "模板名称，长度限制：64 个字符。"
      },
      {
        "name": "DrmType",
        "desc": "DRM方案类型，取值范围：\n<li>SimpleAES。</li>\n如果取值为空字符串，代表不对视频做 DRM 保护。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "创建转自适应码流模板，数量上限：100。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "查询采样截图模板，支持根据条件，分页查询。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "创建用户自定义转动图模板，数量上限：16。"
  },
  "ModifyClass": {
    "params": [
      {
        "name": "ClassId",
        "desc": "分类 ID"
      },
      {
        "name": "ClassName",
        "desc": "分类名称。长度限制：1-64 个字符。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改媒体分类属性。"
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "Status",
        "desc": "过滤条件：任务状态，可选值：WAITING（等待中）、PROCESSING（处理中）、FINISH（已完成）。"
      },
      {
        "name": "FileId",
        "desc": "过滤条件：文件 ID。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10，最大值：100。"
      },
      {
        "name": "ScrollToken",
        "desc": "翻页标识，分批拉取时使用：当单次请求无法拉取所有数据，接口将会返回 ScrollToken，下一次请求携带该 Token，将会从下一条记录开始获取。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "* 该接口用于查询任务列表；\n* 当列表数据比较多时，单次接口调用无法拉取整个列表，可通过 ScrollToken 参数，分批拉取；\n* 只能查询到最近三天（72 小时）内的任务。"
  },
  "ResetProcedureTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "任务流名字"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "MediaProcessTask",
        "desc": "视频处理类型任务参数。"
      },
      {
        "name": "AiContentReviewTask",
        "desc": "AI 智能内容审核类型任务参数。"
      },
      {
        "name": "AiAnalysisTask",
        "desc": "AI 智能内容分析类型任务参数。"
      },
      {
        "name": "AiRecognitionTask",
        "desc": "AI 内容识别类型任务参数。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "重新设置用户自定义任务流模板的内容。  "
  },
  "DescribeCDNUsageData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始日期，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。"
      },
      {
        "name": "EndTime",
        "desc": "结束日期，需大于开始日期，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。"
      },
      {
        "name": "DataType",
        "desc": "CDN 统计数据类型，有效值：\n<li>Flux：流量，单位为 byte。</li>\n<li>Bandwidth：带宽，单位为 bps。</li>"
      },
      {
        "name": "DataInterval",
        "desc": "用量数据的时间粒度，单位：分钟，取值有：\n<li>5：5 分钟粒度，返回指定查询时间内5分钟粒度的明细数据。</li>\n<li>60：小时粒度，返回指定查询时间内1小时粒度的数据。</li>\n<li>1440：天粒度，返回指定查询时间内1天粒度的数据。</li>\n默认值为1440，返回天粒度的数据。\n当该字段为1时，表示以管理员身份查询所有子应用（含主应用）的用量合计。"
      },
      {
        "name": "DomainNames",
        "desc": "域名列表。一次最多查询20个域名的用量数据。可以指定多个域名，查询这些域名叠加的用量数据。默认返回所有域名叠加的用量数据。"
      },
      {
        "name": "SubAppId",
        "desc": "点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。\n当该字段为1时，表示以管理员身份查询所有子应用（含主应用）的用量合计，此时时间粒度只支持天粒度。"
      }
    ],
    "desc": "该接口用于查询点播 CDN 的流量、带宽等统计数据。\n   1. 可以查询最近365天内的 CDN 用量数据。\n   2.  查询时间跨度不超过90天。\n   3. 可以指定用量数据的时间粒度，支持5分钟、1小时、1天的时间粒度。\n   4.  流量为查询时间粒度内的总流量，带宽为查询时间粒度内的峰值带宽。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "创建用户自定义转码模板，数量上限：100。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改用户自定义雪碧图模板。"
  },
  "DeleteClass": {
    "params": [
      {
        "name": "ClassId",
        "desc": "分类 ID"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "* 仅当待删分类无子分类且无媒体关联情况下，可删除分类；\n* 否则，请先执行[删除媒体](/document/product/266/31764)及子分类，再删除该分类；"
  },
  "ExecuteFunction": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "调用后端接口名称。"
      },
      {
        "name": "FunctionArg",
        "desc": "接口参数，具体参数格式调用时与后端协调。"
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
        "name": "ExtInfo",
        "desc": "保留字段，特殊用途时使用。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "本接口仅用于定制开发的特殊场景，除非云点播客服人员主动告知您需要使用本接口，其它情况请勿调用。"
  },
  "DescribeMediaProcessUsageData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始日期。使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#52)。"
      },
      {
        "name": "EndTime",
        "desc": "结束日期，需大于等于起始日期。使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#52)。"
      },
      {
        "name": "Type",
        "desc": "查询视频处理任务类型，默认查询转码。目前只支持转码类型数据查询。\n<li>Transcode: 转码</li>"
      },
      {
        "name": "SubAppId",
        "desc": "点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "该接口返回查询时间范围内每天使用的视频处理用量信息。\n   1. 可以查询最近365天内的视频处理统计数据。\n   2. 查询时间跨度不超过90天。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改用户自定义转动图模板。"
  },
  "ComposeMedia": {
    "params": [
      {
        "name": "Tracks",
        "desc": "输入的媒体轨道列表，包括视频、音频、图片等素材组成的多个轨道信息。输入的多个轨道在时间轴上和输出媒体文件的时间轴对齐，时间轴上相同时间点的各个轨道的素材进行重叠，视频或者图片按轨道顺序进行图像的叠加，轨道顺序高的素材叠加在上面；音频素材进行混音。"
      },
      {
        "name": "Output",
        "desc": "输出的媒体文件信息。"
      },
      {
        "name": "Canvas",
        "desc": "制作视频文件时使用的画布。"
      },
      {
        "name": "SessionContext",
        "desc": "标识来源上下文，用于透传用户请求信息，在ComposeMediaComplete回调将返回该字段值，最长 1000个字符。"
      },
      {
        "name": "SessionId",
        "desc": "用于任务去重的识别码，如果一天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "该接口用于制作媒体文件，可以\n\n1. 对一个媒体文件进行剪辑，生成一个新的媒体文件；\n2. 对多个媒体文件进行裁剪拼接，生成一个新的媒体文件；\n3. 对多个媒体文件的媒体流进行裁剪拼接，生成一个新的媒体文件。\n\n如使用事件通知，事件通知的类型为 [视频合成完成](https://cloud.tencent.com/document/product/266/43000)。"
  },
  "CreateContentReviewTemplate": {
    "params": [
      {
        "name": "ReviewWallSwitch",
        "desc": "审核结果是否进入审核墙（对审核结果进行人工复核）的开关。\n<li>ON：是；</li>\n<li>OFF：否。</li>"
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
      },
      {
        "name": "ScreenshotInterval",
        "desc": "截帧间隔，单位为秒。当不填时，默认截帧间隔为 1 秒，最小值为 0.5 秒。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "创建用户自定义视频内容审核模板，数量上限：50。"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      },
      {
        "name": "FillType",
        "desc": "填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：\n<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>\n<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>\n<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>\n<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>\n默认值：black 。"
      }
    ],
    "desc": "创建用户自定义采样截图模板，数量上限：16。"
  },
  "DeleteAIAnalysisTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "视频内容分析模板唯一标识。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "删除用户自定义视频内容分析模板。\n\n注意：模板 ID 为 10000 以下的为系统预置模板，不允许删除。"
  },
  "DescribeMediaInfos": {
    "params": [
      {
        "name": "FileIds",
        "desc": "媒体文件 ID 列表，N 从 0 开始取值，最大 19。"
      },
      {
        "name": "Filters",
        "desc": "指定所有媒体文件需要返回的信息，可同时指定多个信息，N 从 0 开始递增。如果未填写该字段，默认返回所有信息。选项有：\n<li>basicInfo（视频基础信息）。</li>\n<li>metaData（视频元信息）。</li>\n<li>transcodeInfo（视频转码结果信息）。</li>\n<li>animatedGraphicsInfo（视频转动图结果信息）。</li>\n<li>imageSpriteInfo（视频雪碧图信息）。</li>\n<li>snapshotByTimeOffsetInfo（视频指定时间点截图信息）。</li>\n<li>sampleSnapshotInfo（采样截图信息）。</li>\n<li>keyFrameDescInfo（打点信息）。</li>\n<li>adaptiveDynamicStreamingInfo（转自适应码流信息）。</li>\n<li>miniProgramReviewInfo（小程序审核信息）。</li>"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID 。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "1. 该接口可以获取多个媒体文件的多种信息，包括：\n    1. 基础信息（basicInfo）：包括媒体名称、分类、播放地址、封面图片等。\n    2. 元信息（metaData）：包括大小、时长、视频流信息、音频流信息等。\n    3. 转码结果信息（transcodeInfo）：包括该媒体转码生成的各种规格的媒体地址、视频流参数、音频流参数等。\n    4. 转动图结果信息（animatedGraphicsInfo）：对视频转动图（如 gif）后的动图信息。\n    5. 采样截图信息（sampleSnapshotInfo）：对视频采样截图后的截图信息。\n    6. 雪碧图信息（imageSpriteInfo）：对视频截取雪碧图后的雪碧图信息。\n    7. 指定时间点截图信息（snapshotByTimeOffsetInfo）：对视频依照指定时间点截图后，的截图信息。\n    8. 视频打点信息（keyFrameDescInfo）：对视频设置的打点信息。\n    9. 转自适应码流信息（adaptiveDynamicStreamingInfo）：包括规格、加密类型、打包格式等相关信息。\n2. 可以指定回包只返回部分信息。"
  },
  "LiveRealTimeClip": {
    "params": [
      {
        "name": "StreamId",
        "desc": "推流[直播码](https://cloud.tencent.com/document/product/267/5959)。"
      },
      {
        "name": "StartTime",
        "desc": "流剪辑的开始时间，格式参照 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。"
      },
      {
        "name": "EndTime",
        "desc": "流剪辑的结束时间，格式参照 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。"
      },
      {
        "name": "IsPersistence",
        "desc": "是否固化。0 不固化，1 固化。默认不固化。"
      },
      {
        "name": "ExpireTime",
        "desc": "剪辑固化后的视频存储过期时间。格式参照 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。填“9999-12-31T23:59:59Z”表示永不过期。过期后该媒体文件及其相关资源（转码结果、雪碧图等）将被永久删除。仅 IsPersistence 为 1 时有效，默认剪辑固化的视频永不过期。"
      },
      {
        "name": "Procedure",
        "desc": "剪辑固化后的视频点播任务流处理，详见[上传指定任务流](https://cloud.tencent.com/document/product/266/9759)。仅 IsPersistence 为 1 时有效。"
      },
      {
        "name": "MetaDataRequired",
        "desc": "是否需要返回剪辑后的视频元信息。0 不需要，1 需要。默认不需要。"
      },
      {
        "name": "Host",
        "desc": "即时剪辑使用的域名，必须在直播侧开通时移。"
      },
      {
        "name": "ExtInfo",
        "desc": "系统保留字段，请勿填写。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "直播即时剪辑，是指在直播过程中（即直播尚未结束时），客户可以在过往直播内容中选择一段，实时生成一个新的视频（HLS 格式），开发者可以将其立即分享出去，或者长久保存起来。\n\n腾讯云点播支持两种即时剪辑模式：\n- 剪辑固化：将剪辑出来的视频保存成独立的视频，拥有独立 FileId；适用于将精彩片段**长久保存**的场景；\n- 剪辑不固化：剪辑得到的视频附属于直播录制文件，没有独立 FileId；适用于将精彩片段**临时分享**的场景。\n\n注意：\n- 使用直播即时剪辑功能的前提是：目标直播流开启了[时移回看](https://cloud.tencent.com/document/product/267/32742)功能。\n- 直播即时剪辑是基于直播录制生成的 m3u8 文件进行的，故而其最小剪辑精度为一个 ts 切片，无法实现秒级或者更为精确的剪辑精度。\n\n\n### 剪辑固化\n所谓剪辑固化，是指将剪辑出来的视频是保存成一个独立的视频（拥有独立的 FileId）。其生命周期不受原始直播录制视频影响（即使原始录制视频被删除，剪辑结果也不会受到任何影响）；也可以对其进行转码、微信发布等二次处理。\n\n举例如下：一场完整的足球比赛，直播录制出来的原始视频可能长达 2 个小时，客户出于节省成本的目的可以对这个视频存储 2 个月，但对于直播即时剪辑的「精彩时刻」视频却可以指定存储更长时间，同时可以单独对「精彩时刻」视频进行转码、微信发布等额外的点播操作，这时候可以选择直播即时剪辑并且固化的方案。\n\n剪辑固化的优势在于其生命周期与原始录制视频相互独立，可以独立管理、长久保存。\n\n### 剪辑不固化\n所谓剪辑不固化，是指剪辑所得到的结果（m3u8 文件）与直播录制视频共享相同的 ts 分片，新生成的视频不是一个独立完整的视频（没有独立 FileId，只有播放 URL），其有效期与直播录制的完整视频有效期是一致的。一旦直播录制出来的视频被删除，也会导致该片段无法播放。\n\n剪辑不固化，由于其剪辑结果不是一个独立的视频，因而也不会纳入点播媒资视频管理（例如控制台的视频总数不会统计这一片段）中，也无法单独针对这个片段做转码、微信发布等任何视频处理操作。\n\n剪辑不固化的优势在于其剪辑操作十分“轻量化”，不会产生额外的存储开销。但其不足之处在于生命周期与原始录制视频相同，且无法进一步进行转码等视频处理。"
  },
  "PullUpload": {
    "params": [
      {
        "name": "MediaUrl",
        "desc": "要拉取的媒体 URL，暂不支持拉取 HLS 和 Dash 格式。\n支持的扩展名详见[媒体类型](https://cloud.tencent.com/document/product/266/9760#.E5.AA.92.E4.BD.93.E7.B1.BB.E5.9E.8B)。"
      },
      {
        "name": "MediaName",
        "desc": "媒体名称。"
      },
      {
        "name": "CoverUrl",
        "desc": "要拉取的视频封面 URL。仅支持 gif、jpeg、png 三种图片格式。"
      },
      {
        "name": "Procedure",
        "desc": "媒体后续任务操作，详见[上传指定任务流](https://cloud.tencent.com/document/product/266/9759)。"
      },
      {
        "name": "ExpireTime",
        "desc": "媒体文件过期时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。"
      },
      {
        "name": "StorageRegion",
        "desc": "指定上传园区，仅适用于对上传地域有特殊需求的用户（目前仅支持北京、上海和重庆园区）。"
      },
      {
        "name": "ClassId",
        "desc": "分类ID，用于对媒体进行分类管理，可通过[创建分类](https://cloud.tencent.com/document/product/266/7812)接口，创建分类，获得分类 ID。"
      },
      {
        "name": "SessionContext",
        "desc": "来源上下文，用于透传用户请求信息，当指定 Procedure 任务后，任务流状态变更回调将返回该字段值，最长 1000 个字符。"
      },
      {
        "name": "SessionId",
        "desc": "用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。"
      },
      {
        "name": "ExtInfo",
        "desc": "保留字段，特殊用途时使用。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "该接口用于将一个网络上的视频拉取到云点播平台。"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      },
      {
        "name": "FillType",
        "desc": "填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：\n<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>\n<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>\n<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>\n<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>\n默认值：black 。"
      }
    ],
    "desc": "修改用户自定义采样截图模板。"
  },
  "DeleteSuperPlayerConfig": {
    "params": [
      {
        "name": "Name",
        "desc": "播放器配置名称。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "删除超级播放器配置。  \n*注：系统预置播放器配置不允许删除。*"
  },
  "DescribeProcedureTemplates": {
    "params": [
      {
        "name": "Names",
        "desc": "任务流模板名字过滤条件，数组长度限制：100。"
      },
      {
        "name": "Type",
        "desc": "任务流模板类型过滤条件，可选值：\n<li>Preset：系统预置任务流模板；</li>\n<li>Custom：用户自定义任务流模板。</li>"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "根据任务流模板名字，获取任务流模板详情列表。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "根据转码模板唯一标识，获取转码模板详情列表。返回结果包含符合条件的所有用户自定义模板及[系统预置转码模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。"
  },
  "ParseStreamingManifest": {
    "params": [
      {
        "name": "MediaManifestContent",
        "desc": "待解析的索引文件内容。"
      },
      {
        "name": "ManifestType",
        "desc": "视频索引文件格式。默认 m3u8 格式。\n<li>m3u8</li>\n<li>mpd</li>"
      }
    ],
    "desc": "上传 HLS 视频时，解析索引文件内容，返回待上传的分片文件列表。分片文件路径必须是当前目录或子目录的相对路径，不能是 URL，不能是绝对路径。"
  },
  "CreateProcedureTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "任务流名字（支持中文，不超过20个字）。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "MediaProcessTask",
        "desc": "视频处理类型任务参数。"
      },
      {
        "name": "AiContentReviewTask",
        "desc": "AI 智能内容审核类型任务参数。"
      },
      {
        "name": "AiAnalysisTask",
        "desc": "AI 智能内容分析类型任务参数。"
      },
      {
        "name": "AiRecognitionTask",
        "desc": "AI 内容识别类型任务参数。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "创建用户自定义的任务流模板，模板上限：50。"
  },
  "PushUrlCache": {
    "params": [
      {
        "name": "Urls",
        "desc": "预热的 URL 列表，单次最多指定20个 URL。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "1. 预热指定的 URL 列表。\n2. URL 的域名必须已在云点播中注册。\n3. 单次请求最多指定20个 URL。"
  },
  "DeleteMedia": {
    "params": [
      {
        "name": "FileId",
        "desc": "媒体文件的唯一标识。"
      },
      {
        "name": "DeleteParts",
        "desc": "指定本次需要删除的部分。默认值为 \"[]\", 表示删除媒体及其对应的全部视频处理文件。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID 。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "* 删除媒体及其对应的视频处理文件（如转码视频、雪碧图、截图、微信发布视频等）；\n* 可单独删除指定 ID 的视频文件下的转码，或者微信发布文件；"
  },
  "CreateSuperPlayerConfig": {
    "params": [
      {
        "name": "Name",
        "desc": "播放器配置名称，长度限制：64 个字符。只允许出现 [0-9a-zA-Z] 及 _- 字符（如 test_ABC-123），同一个用户该名称唯一。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "DrmSwitch",
        "desc": "播放 DRM 保护的自适应码流开关：\n<li>ON：开启，表示仅播放 DRM  保护的自适应码流输出；</li>\n<li>OFF：关闭，表示播放未加密的自适应码流输出。</li>\n默认为 OFF。"
      },
      {
        "name": "AdaptiveDynamicStreamingDefinition",
        "desc": "允许输出的未加密的自适应码流模板 ID，当 DrmSwitch 为 OFF 时必填。"
      },
      {
        "name": "DrmStreamingsInfo",
        "desc": "允许输出的 DRM 自适应码流模板内容，当 DrmSwitch 为 ON 时必填。"
      },
      {
        "name": "ImageSpriteDefinition",
        "desc": "允许输出的雪碧图模板 ID。"
      },
      {
        "name": "ResolutionNames",
        "desc": "播放器对不于不同分辨率的子流展示名字，不填或者填空数组则使用默认配置：\n<li>MinEdgeLength：240，Name：流畅；</li>\n<li>MinEdgeLength：480，Name：标清；</li>\n<li>MinEdgeLength：720，Name：高清；</li>\n<li>MinEdgeLength：1080，Name：全高清；</li>\n<li>MinEdgeLength：1440，Name：2K；</li>\n<li>MinEdgeLength：2160，Name：4K；</li>\n<li>MinEdgeLength：4320，Name：8K。</li>"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "创建超级播放器配置，数量上限：100。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "该接口用于根据人物 ID，修改人物样本信息，包括名称、描述的修改，以及人脸、标签的添加、删除、重置操作。人脸删除操作需保证至少剩余 1 张图片，否则，请使用重置操作。"
  },
  "DeleteContentReviewTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "内容审核模板唯一标识。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "删除用户自定义视频内容审核模板。"
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
      },
      {
        "name": "HighlightConfigure",
        "desc": "智能精彩集锦任务控制参数。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "创建用户自定义视频内容分析模板，数量上限：50。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "查询指定时间点截图模板，支持根据条件，分页查询。"
  },
  "ProcessMediaByUrl": {
    "params": [
      {
        "name": "InputInfo",
        "desc": "输入视频信息，包括视频 URL ， 名称、视频自定义 ID。"
      },
      {
        "name": "OutputInfo",
        "desc": "输出文件 COS 路径信息。"
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
        "name": "TasksPriority",
        "desc": "任务流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。"
      },
      {
        "name": "TasksNotifyMode",
        "desc": "任务流状态变更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "对来源为 URL 的音视频媒体发起处理任务，功能包括：\n\n1. 智能内容审核（鉴黄、鉴恐、鉴政）；\n2. 智能内容分析（标签、分类、封面、按帧标签）；\n3. 智能内容识别（视频片头片尾、人脸、文本全文、文本关键词、语音全文、语音关键词、物体）。"
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
        "desc": "极速高清转码参数。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改用户自定义转码模板信息。"
  },
  "DescribeContentReviewTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "内容审核模板唯一标识过滤条件，数组长度限制：100。"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "根据视频内容审核模板唯一标识，获取视频内容审核模板详情列表。返回结果包含符合条件的所有用户自定义模板及[系统预置内容审核模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.AE.A1.E6.A0.B8.E6.A8.A1.E6.9D.BF)。"
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
        "desc": "SVG 水印模板，该字段仅对 SVG 水印模板有效。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改用户自定义水印模板，水印类型不允许修改。"
  },
  "DescribeStorageDetails": {
    "params": [
      {
        "name": "StartTime",
        "desc": "起始时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#52)。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，需大于开始日期，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#52)。"
      },
      {
        "name": "Interval",
        "desc": "查询时间间隔，有效值：\n<li>Minute：每分钟一个统计数据。</li>\n<li>Hour：每小时一个统计数据。</li>\n<li>Day：每天一个统计数据。</li>\n默认按时间跨度决定，小于1小时按分钟，小于等于7天按小时，大于7天按天展示。"
      },
      {
        "name": "StorageType",
        "desc": "查询的存储类型，有效值：\n<li>TotalStorage：存储总量。</li>\n<li>StandardStorage：标准存储。</li>\n<li>InfrequentStorage：低频存储。</li>\n默认值为 TotalStorage。"
      },
      {
        "name": "SubAppId",
        "desc": "点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。\n当该字段为1时，表示以管理员身份查询所有子应用（含主应用）的用量合计。"
      }
    ],
    "desc": "该接口返回查询时间范围内使用的点播存储空间，单位：字节。\n   1. 可以查询最近365天内的存储空间数据；\n   2. 查询时间跨度不超过90天；\n   3. 分钟粒度查询跨度不超过5天；\n   4. 小时粒度查询跨度不超过10天。"
  },
  "DeleteWordSamples": {
    "params": [
      {
        "name": "Keywords",
        "desc": "关键词，数组长度限制：100 个词。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "该接口用于批量删除关键词样本。"
  },
  "ModifySubAppIdInfo": {
    "params": [
      {
        "name": "SubAppId",
        "desc": "子应用 ID。"
      },
      {
        "name": "Name",
        "desc": "子应用名称，长度限制：40个字符。"
      },
      {
        "name": "Description",
        "desc": "子应用简介，长度限制： 300个字符。"
      }
    ],
    "desc": "该接口用于修改子应用信息，但不允许修改主应用信息。"
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
        "desc": "图片水印模板，当 Type 为 image，该字段必填。当 Type 为 text，该字段无效。"
      },
      {
        "name": "TextTemplate",
        "desc": "文字水印模板，当 Type 为 text，该字段必填。当 Type 为 image，该字段无效。"
      },
      {
        "name": "SvgTemplate",
        "desc": "SVG水印模板，当 Type 为 svg，该字段必填。当 Type 为 image 或 text，该字段无效。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "该接口用于查询人物样本信息，支持根据人物 ID、名称、标签，分页查询。"
  },
  "DeleteAIRecognitionTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "视频内容识别模板唯一标识。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "删除用户自定义视频内容识别模板。"
  },
  "CreateSubAppId": {
    "params": [
      {
        "name": "Name",
        "desc": "子应用名称，长度限制：40个字符。"
      },
      {
        "name": "Description",
        "desc": "子应用简介，长度限制： 300个字符。"
      }
    ],
    "desc": "该接口用于创建点播子应用。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "查询转动图模板列表，支持根据条件，分页查询。"
  },
  "ForbidMediaDistribution": {
    "params": [
      {
        "name": "FileIds",
        "desc": "媒体文件列表，每次最多可提交 20 条。"
      },
      {
        "name": "Operation",
        "desc": "forbid：禁播，recover：解禁。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID 。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "* 对媒体禁播后，除了点播控制台预览，其他场景访问视频各种资源的 URL（原始文件、转码输出文件、截图等）均会返回 403。\n  禁播/解禁操作全网生效时间约 5~10 分钟。"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      },
      {
        "name": "FillType",
        "desc": "填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：\n<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>\n<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>\n<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>\n<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>\n默认值：black 。"
      }
    ],
    "desc": "修改用户自定义指定时间点截图模板。"
  },
  "ModifySuperPlayerConfig": {
    "params": [
      {
        "name": "Name",
        "desc": "播放器配置名称。"
      },
      {
        "name": "DrmSwitch",
        "desc": "播放 DRM 保护的自适应码流开关：\n<li>ON：开启，表示仅播放 DRM  保护的自适应码流输出；</li>\n<li>OFF：关闭，表示播放未加密的自适应码流输出。</li>"
      },
      {
        "name": "AdaptiveDynamicStreamingDefinition",
        "desc": "允许输出的未加密的自适应码流模板 ID。"
      },
      {
        "name": "DrmStreamingsInfo",
        "desc": "允许输出的 DRM 自适应码流模板内容。"
      },
      {
        "name": "ImageSpriteDefinition",
        "desc": "允许输出的雪碧图模板 ID。"
      },
      {
        "name": "ResolutionNames",
        "desc": "播放器对不于不同分辨率的子流展示名字。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改超级播放器配置。"
  },
  "CreateClass": {
    "params": [
      {
        "name": "ParentId",
        "desc": "父类 ID，一级分类填写 -1。"
      },
      {
        "name": "ClassName",
        "desc": "分类名称，长度限制：1-64 个字符。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "* 用于对媒体进行分类管理；\n* 该接口不影响既有媒体的分类，如需修改媒体分类，请调用[修改媒体文件属性](/document/product/266/31762)接口。\n* 分类层次不可超过 4 层。\n* 每个分类的子类数量不可超过 500 个。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "该接口用于批量创建关键词样本，样本用于通过OCR、ASR技术，进行内容审核、内容识别等视频处理。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "查询转自适应码流模板，支持根据条件，分页查询。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "查询雪碧图模板，支持根据条件，分页查询。"
  },
  "DescribeAllClass": {
    "params": [
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "* 获得用户的所有分类信息。"
  },
  "DescribeWatermarkTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "水印模板唯一标识过滤条件，数组长度限制：100。"
      },
      {
        "name": "Type",
        "desc": "水印类型过滤条件，可选值：\n<li>image：图片水印；</li>\n<li>text：文字水印；</li>\n<li>svg：SVG 水印。</li>"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数\n<li>默认值：10；</li>\n<li>最大值：100。</li>"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
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
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "FillType",
        "desc": "填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：\n<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>\n<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>\n默认值：black 。"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "创建用户自定义雪碧图模板，数量上限：16。"
  },
  "DescribeAIRecognitionTemplates": {
    "params": [
      {
        "name": "Definitions",
        "desc": "视频内容识别模板唯一标识过滤条件，数组长度限制：100。"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "根据视频内容识别模板唯一标识，获取视频内容识别模板详情列表。返回结果包含符合条件的所有用户自定义视频内容识别模板及[系统预置视频内容识别模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E8.AF.86.E5.88.AB.E6.A8.A1.E6.9D.BF)。"
  },
  "DescribeSuperPlayerConfigs": {
    "params": [
      {
        "name": "Names",
        "desc": "播放器配置名字过滤条件，数组长度限制：100。"
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
        "desc": "播放器配置类型过滤条件，可选值：\n<li>Preset：系统预置配置；</li>\n<li>Custom：用户自定义配置。</li>"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "查询超级播放器配置，支持根据条件，分页查询。"
  },
  "DescribeSubAppIds": {
    "params": [],
    "desc": "该接口用于获取当前账号有权限的子应用列表，包含主应用。若尚未开通子应用功能，接口将返回 \n FailedOperation。"
  },
  "CommitUpload": {
    "params": [
      {
        "name": "VodSessionKey",
        "desc": "点播会话，取申请上传接口的返回值 VodSessionKey。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "该接口用于确认媒体文件（和封面文件）上传到腾讯云点播的结果，并存储媒体信息，返回文件的播放地址和文件 ID。"
  },
  "ConfirmEvents": {
    "params": [
      {
        "name": "EventHandles",
        "desc": "事件句柄，即 [拉取事件通知](/document/product/266/33433) 接口输出参数中的 EventSet. EventHandle 字段。\n数组长度限制：16。"
      },
      {
        "name": "ExtInfo",
        "desc": "保留字段，特殊用途时使用。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "* 开发者调用拉取事件通知，获取到事件后，必须调用该接口来确认消息已经收到；\n* 开发者获取到事件句柄后，等待确认的有效时间为 30 秒，超出 30 秒会报参数错误（4000）；\n* 更多参考事件通知的[可靠回调](https://cloud.tencent.com/document/product/266/33779#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83)。"
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
        "name": "HeadTailConfigure",
        "desc": "视频片头片尾识别控制参数。"
      },
      {
        "name": "SegmentConfigure",
        "desc": "视频拆条识别控制参数。"
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
      },
      {
        "name": "ObjectConfigure",
        "desc": "物体识别控制参数。"
      },
      {
        "name": "ScreenshotInterval",
        "desc": "截帧间隔，单位为秒，最小值为 0.5 秒。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改用户自定义视频内容识别模板。"
  },
  "ModifyAdaptiveDynamicStreamingTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "自适应转码模板唯一标识。"
      },
      {
        "name": "Name",
        "desc": "模板名称，长度限制：64 个字符。"
      },
      {
        "name": "Format",
        "desc": "自适应转码格式，取值范围：\n<li>HLS。</li>"
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
        "desc": "自适应转码输入流参数信息，最多输入10路流。\n注意：各个流的帧率必须保持一致；如果不一致，采用第一个流的帧率作为输出帧率。"
      },
      {
        "name": "Comment",
        "desc": "模板描述信息，长度限制：256 个字符。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改转自适应码流模板"
  },
  "SearchMedia": {
    "params": [
      {
        "name": "Text",
        "desc": "搜索文本，模糊匹配媒体文件名称或描述信息，匹配项越多，匹配度越高，排序越优先。长度限制：64个字符。"
      },
      {
        "name": "Tags",
        "desc": "标签集合，匹配集合中任意元素。\n<li>单个标签长度限制：8个字符。</li>\n<li>数组长度限制：10。</li>"
      },
      {
        "name": "ClassIds",
        "desc": "分类 ID 集合，匹配集合指定 ID 的分类及其所有子类。数组长度限制：10。"
      },
      {
        "name": "StartTime",
        "desc": "创建时间的开始时间。\n<li>大于等于开始时间。</li>\n<li>格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。</li>"
      },
      {
        "name": "EndTime",
        "desc": "创建时间的结束时间。\n<li>小于结束时间。</li>\n<li>格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。</li>"
      },
      {
        "name": "SourceType",
        "desc": "媒体文件来源，来源取值参见 [SourceType](https://cloud.tencent.com/document/product/266/31773#MediaSourceData)。"
      },
      {
        "name": "StreamId",
        "desc": "推流 [直播码](https://cloud.tencent.com/document/product/267/5959)。"
      },
      {
        "name": "Vid",
        "desc": "直播录制文件的唯一标识。"
      },
      {
        "name": "Sort",
        "desc": "排序方式。\n<li>Sort.Field 可选值：CreateTime</li>\n<li>指定 Text 搜索时，将根据匹配度排序，该字段无效</li>"
      },
      {
        "name": "Offset",
        "desc": "<div id=\"p_offset\">分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。\n<li>取值范围：Offset + Limit 不超过5000。（参见：<a href=\"#maxResultsDesc\">接口返回结果数限制</a>）</li></div>"
      },
      {
        "name": "Limit",
        "desc": "<div id=\"p_limit\">分页返回的记录条数，默认值：10。将返回第 Offset 到第 Offset+Limit-1 条。\n<li>取值范围：Offset + Limit 不超过5000。（参见：<a href=\"#maxResultsDesc\">接口返回结果数限制</a>）</li></div>"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "搜索媒体信息，支持多种条件筛选，以及支持对返回结果排序、过滤等功能，具体包括：\n- 根据媒体文件名或描述信息进行模糊搜索。\n- 根据媒体分类、标签进行检索。\n    - 指定分类集合 ClassIds（见输入参数），返回满足集合中任意分类的媒体。例如：媒体分类有电影、电视剧、综艺，其中电影分类下又有子分类历史片、动作片、言情片。如果 ClassIds 指定了电影、电视剧，那么电影和电视剧下的所有子分类都会返回；而如果 ClassIds 指定的是历史片、动作片，那么只有这2个子分类下的媒体才会返回。\n    - 指定标签集合 Tags（见输入参数），返回满足集合中任意标签的媒体。例如：媒体标签有二次元、宫斗、鬼畜，如果 Tags 指定了二次元、鬼畜2个标签，那么只要符合这2个标签中任意一个的媒体都会被检索出来。\n- 允许指定筛选某一来源 Source（见输入参数）的媒体。\n- 允许根据直播推流码、Vid（见输入参数）筛选直播录制的媒体。\n- 允许根据媒体的创建范围筛选媒体。\n- 允许对上述条件进行任意组合，检索同时满足以上条件的媒体。例如：筛选创建时间在2018年12月1日到2018年12月8日之间、分类为电影、带有宫斗标签的媒体。\n- 允许对结果进行排序并分页返回，通过 Offset 和 Limit （见输入参数）来控制分页。\n\n<div id=\"maxResultsDesc\">接口返回结果数限制：</div>\n- <b><a href=\"#p_offset\">Offset</a> 和 <a href=\"#p_limit\">Limit</a> 两个参数影响单次分页查询结果数。特别注意：当这2个值都缺省时，本接口最多只返回10条查询结果。</b>\n- <b>最大支持返回5000条搜索结果，超出部分不再支持查询。如果搜索结果量太大，建议使用更精细的筛选条件来减少搜索结果。</b>"
  },
  "DeleteWatermarkTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "水印模板唯一标识。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "删除用户自定义水印模板。"
  },
  "DeletePersonSample": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人物 ID。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "该接口用于根据人物 ID，删除人物样本。"
  },
  "DeleteSnapshotByTimeOffsetTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "指定时间点截图模板唯一标识。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "删除用户自定义指定时间点截图模板。"
  },
  "DeleteSampleSnapshotTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "采样截图模板唯一标识。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "删除用户自定义采样截图模板。"
  },
  "WeChatMiniProgramPublish": {
    "params": [
      {
        "name": "FileId",
        "desc": "媒体文件 ID。"
      },
      {
        "name": "SourceDefinition",
        "desc": "发布视频所对应的转码模板 ID，为0代表原始视频。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "将点播视频发布到微信小程序，供微信小程序播放器播放。"
  },
  "SimpleHlsClip": {
    "params": [
      {
        "name": "Url",
        "desc": "需要裁剪的腾讯云点播 HLS 视频 URL。"
      },
      {
        "name": "StartTimeOffset",
        "desc": "裁剪的开始偏移时间，单位秒。默认 0，即从视频开头开始裁剪。负数表示距离视频结束多少秒开始裁剪。例如 -10 表示从倒数第 10 秒开始裁剪。"
      },
      {
        "name": "EndTimeOffset",
        "desc": "裁剪的结束偏移时间，单位秒。默认 0，即裁剪到视频尾部。负数表示距离视频结束多少秒结束裁剪。例如 -10 表示到倒数第 10 秒结束裁剪。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "对 HLS 视频进行按时间段裁剪。\n\n注意：裁剪出来的视频与原始视频共用 ts，仅生成新的 m3u8。原始视频删除后，该裁剪视频也会被删除。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "该接口用于创建人物样本，用于通过人脸识别等技术，进行内容识别、内容审核等视频处理。"
  },
  "ModifySubAppIdStatus": {
    "params": [
      {
        "name": "SubAppId",
        "desc": "子应用 ID。"
      },
      {
        "name": "Status",
        "desc": "子应用状态，取值范围：\n<li>On：启用</li>\n<li>Off：停用</li>"
      }
    ],
    "desc": "该接口用于启用、停用子应用。被停用的子应用将封停对应域名，并限制控制台访问。"
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
      },
      {
        "name": "ScreenshotInterval",
        "desc": "截帧间隔，单位为秒，最小值为 0.5 秒。"
      },
      {
        "name": "ReviewWallSwitch",
        "desc": "审核结果是否进入审核墙（对审核结果进行人工复核）的开关。\n<li>ON：是；</li>\n<li>OFF：否。</li>"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改用户自定义视频内容审核模板。"
  },
  "ProcessMedia": {
    "params": [
      {
        "name": "FileId",
        "desc": "媒体文件 ID，即该文件在云点播上的全局唯一标识符，在上传成功后由云点播后台分配。可以在 [视频上传完成事件通知](/document/product/266/7830) 或 [云点播控制台](https://console.cloud.tencent.com/vod/media) 获取该字段。"
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
        "name": "TasksPriority",
        "desc": "任务流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。"
      },
      {
        "name": "TasksNotifyMode",
        "desc": "任务流状态变更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。"
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
        "name": "ExtInfo",
        "desc": "保留字段，特殊用途时使用。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "对点播中的音视频媒体发起处理任务，功能包括：\n1. 视频转码（带水印）；\n2. 视频转动图；\n3. 对视频按指定时间点截图；\n4. 对视频采样截图；\n5. 对视频截图雪碧图；\n6. 对视频截取一张图做封面；\n7. 对视频转自适应码流（并加密）；\n8. 智能内容审核（鉴黄、鉴恐、鉴政）；\n9. 智能内容分析（标签、分类、封面、按帧标签）；\n10. 智能内容识别（视频片头片尾、人脸、文本全文、文本关键词、语音全文、语音关键词、物体）。\n\n如使用事件通知，事件通知的类型为 [任务流状态变更](https://cloud.tencent.com/document/product/266/9636)。"
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
        "name": "HeadTailConfigure",
        "desc": "视频片头片尾识别控制参数。"
      },
      {
        "name": "SegmentConfigure",
        "desc": "视频拆条识别控制参数。"
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
      },
      {
        "name": "ObjectConfigure",
        "desc": "物体识别控制参数。"
      },
      {
        "name": "ScreenshotInterval",
        "desc": "截帧间隔，单位为秒。当不填时，默认截帧间隔为 1 秒，最小值为 0.5 秒。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "创建用户自定义视频内容识别模板，数量上限：50。"
  },
  "ModifyMediaInfo": {
    "params": [
      {
        "name": "FileId",
        "desc": "媒体文件唯一标识。"
      },
      {
        "name": "Name",
        "desc": "媒体文件名称，最长 64 个字符。"
      },
      {
        "name": "Description",
        "desc": "媒体文件描述，最长 128 个字符。"
      },
      {
        "name": "ClassId",
        "desc": "媒体文件分类 ID。"
      },
      {
        "name": "ExpireTime",
        "desc": "媒体文件过期时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。填“9999-12-31T23:59:59Z”表示永不过期。过期后该媒体文件及其相关资源（转码结果、雪碧图等）将被永久删除。"
      },
      {
        "name": "CoverData",
        "desc": "视频封面图片文件（如 jpeg, png 等）进行 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串，仅支持 gif、jpeg、png 三种图片格式。"
      },
      {
        "name": "AddKeyFrameDescs",
        "desc": "新增的一组视频打点信息，如果某个偏移时间已存在打点，则会进行覆盖操作，单个媒体文件最多 100 个打点信息。同一个请求里，AddKeyFrameDescs 的时间偏移参数必须与 DeleteKeyFrameDescs 都不同。"
      },
      {
        "name": "DeleteKeyFrameDescs",
        "desc": "要删除的一组视频打点信息的时间偏移，单位：秒。同一个请求里，AddKeyFrameDescs 的时间偏移参数必须与 DeleteKeyFrameDescs 都不同。"
      },
      {
        "name": "ClearKeyFrameDescs",
        "desc": "取值 1 表示清空视频打点信息，其他值无意义。\n同一个请求里，ClearKeyFrameDescs 与 AddKeyFrameDescs 不能同时出现。"
      },
      {
        "name": "AddTags",
        "desc": "新增的一组标签，单个媒体文件最多 16 个标签，单个标签最多 16 个字符。同一个请求里，AddTags 参数必须与 DeleteTags 都不同。"
      },
      {
        "name": "DeleteTags",
        "desc": "要删除的一组标签。同一个请求里，AddTags 参数必须与 DeleteTags 都不同。"
      },
      {
        "name": "ClearTags",
        "desc": "取值 1 表示清空媒体文件所有标签，其他值无意义。\n同一个请求里，ClearTags 与 AddTags 不能同时出现。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID 。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改媒体文件的属性，包括分类、名称、描述、标签、过期时间、打点信息、视频封面等。"
  },
  "DeleteImageSpriteTemplate": {
    "params": [
      {
        "name": "Definition",
        "desc": "雪碧图模板唯一标识。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "删除雪碧图模板。"
  }
}