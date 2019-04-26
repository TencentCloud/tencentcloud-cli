# -*- coding: utf-8 -*-
DESC = "vod-2018-07-17"
INFO = {
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
  "ConfirmEvents": {
    "params": [
      {
        "name": "EventHandles",
        "desc": "事件句柄，数组长度限制：16。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "* 开发者调用拉取事件通知，获取到事件后，必须调用该接口来确认消息已经收到；\n* 开发者获取到事件句柄后，等待确认的有效时间为 30 秒，超出 30 秒会报参数错误（4000）；\n* 更多参考[服务端事件通知](https://cloud.tencent.com/document/product/266/7829)。"
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
        "name": "TasksPriority",
        "desc": "任务流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。"
      },
      {
        "name": "TasksNotifyMode",
        "desc": "任务流状态变更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。"
      },
      {
        "name": "SessionContext",
        "desc": "来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 250 个字符。"
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
    "desc": "对来源为 URL 的音视频媒体发起处理任务，功能包括：\n\n1. 智能内容审核（鉴黄、鉴恐、鉴政）；\n2. 智能内容分析（标签、分类、封面）。"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改用户自定义转码模板信息。"
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
  "DescribeMediaInfos": {
    "params": [
      {
        "name": "FileIds",
        "desc": "媒体文件 ID 列表，N 从 0 开始取值，最大 19。"
      },
      {
        "name": "Filters",
        "desc": "指定所有媒体文件需要返回的信息，可同时指定多个信息，N 从 0 开始递增。如果未填写该字段，默认返回所有信息。选项有：\n<li>basicInfo（视频基础信息）。</li>\n<li>metaData（视频元信息）。</li>\n<li>transcodeInfo（视频转码结果信息）。</li>\n<li>animatedGraphicsInfo（视频转动图结果信息）。</li>\n<li>imageSpriteInfo（视频雪碧图信息）。</li>\n<li>snapshotByTimeOffsetInfo（视频指定时间点截图信息）。</li>\n<li>sampleSnapshotInfo（采样截图信息）。</li>\n<li>keyFrameDescInfo（打点信息）。</li>"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID 。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "1. 该接口可以获取多个视频的多种信息，包括：\n    1. 基础信息（basicInfo）：包括视频名称、大小、时长、封面图片等。\n    2. 元信息（metaData）：包括视频流信息、音频流信息等。\n    3. 转码结果信息（transcodeInfo）：包括该视频转码生成的各种码率的视频的地址、规格、码率、分辨率等。\n    4. 转动图结果信息（animatedGraphicsInfo）：对视频转动图（如 gif）后，动图相关信息。\n    5. 采样截图信息（sampleSnapshotInfo）：对视频采样截图后，相关截图信息。\n    6. 雪碧图信息（imageSpriteInfo）：对视频截取雪碧图之后，雪碧图的相关信息。\n    7. 指定时间点截图信息（snapshotByTimeOffsetInfo）：对视频依照指定时间点截图后，各个截图的信息。\n    8. 视频打点信息（keyFrameDescInfo）：对视频设置的各个打点信息。\n2. 可以指定回包只返回部分信息。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "根据视频内容分析模板唯一标识，获取视频内容分析模板详情列表。返回结果包含符合条件的所有用户自定义视频内容分析模板及[系统预置视频内容分析模板]"
  },
  "PullEvents": {
    "params": [
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "* 该接口用于从点播服务端获取事件通知，详见[服务端事件通知](https://cloud.tencent.com/document/product/266/7829)；\n* 接口为长轮询模式，即：如果服务端存在未消费事件，则立即返回给请求方；如果服务端没有未消费事件，则后台会将请求挂起，直到有新的事件产生为止；\n* 请求最多挂起 5 秒，建议请求方将超时时间设置为 10 秒；\n* 若该接口有事件返回，调用方必须再调用[确认事件通知](https://cloud.tencent.com/document/product/266/33434)接口，确认事件通知已经处理，否则该事件通知后续会再次被拉取到。"
  },
  "LiveRealTimeClip": {
    "params": [
      {
        "name": "StreamId",
        "desc": "推流[直播码](https://cloud.tencent.com/document/product/267/5959)。"
      },
      {
        "name": "StartTime",
        "desc": "流剪辑的开始时间，格式参照 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。"
      },
      {
        "name": "EndTime",
        "desc": "流剪辑的结束时间，格式参照 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。"
      },
      {
        "name": "IsPersistence",
        "desc": "是否固化。0 不固化，1 固化。默认不固化。"
      },
      {
        "name": "ExpireTime",
        "desc": "剪辑固化后的视频存储过期时间。格式参照 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。填“9999-12-31T23:59:59Z”表示永不过期。过期后该媒体文件及其相关资源（转码结果、雪碧图等）将被永久删除。仅 IsPersistence 为 1 时有效，默认剪辑固化的视频永不过期。"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "直播即时剪辑，是指在直播过程中（即直播尚未结束时），客户可以在过往直播内容中选择一段，实时生成一个新的视频（HLS 格式），开发者可以将其立即分享出去，或者长久保存起来。\n\n腾讯云点播支持两种即时剪辑模式：\n- 剪辑固化：将剪辑出来的视频保存成独立的视频，拥有独立 FileId；适用于将精彩片段**长久保存**的场景；\n- 剪辑不固化：剪辑得到的视频附属于直播录制文件，没有独立 FileId；适用于将精彩片段**临时分享**的场景。\n\n注意：\n- 使用直播即时剪辑功能的前提是：目标直播流开启了[时移回看](https://cloud.tencent.com/document/product/267/32742#.E5.BC.80.E9.80.9A.E6.AD.A5.E9.AA.A4)功能。\n- 直播即时剪辑是基于直播录制生成的 m3u8 文件进行的，故而其最小剪辑精度为一个 ts 切片，无法实现秒级或者更为精确的剪辑精度。\n\n\n### 剪辑固化\n所谓剪辑固化，是指将剪辑出来的视频是保存成一个独立的视频（拥有独立的 FileId）。其生命周期不受原始直播录制视频影响（即使原始录制视频被删除，剪辑结果也不会受到任何影响）；也可以对其进行转码、微信发布等二次处理。\n\n举例如下：一场完整的足球比赛，直播录制出来的原始视频可能长达 2 个小时，客户出于节省成本的目的可以对这个视频存储 2 个月，但对于直播即时剪辑的「精彩时刻」视频却可以指定存储更长时间，同时可以单独对「精彩时刻」视频进行转码、微信发布等额外的点播操作，这时候可以选择直播即时剪辑并且固化的方案。\n\n剪辑固化的优势在于其生命周期与原始录制视频相互独立，可以独立管理、长久保存。\n\n### 剪辑不固化\n所谓剪辑不固化，是指剪辑所得到的结果（m3u8 文件）与直播录制视频共享相同的 ts 分片，新生成的视频不是一个独立完整的视频（没有独立 FileId，只有播放 URL），其有效期与直播录制的完整视频有效期是一致的。一旦直播录制出来的视频被删除，也会导致该片段无法播放。\n\n剪辑不固化，由于其剪辑结果不是一个独立的视频，因而也不会纳入点播媒资视频管理（比如控制台的视频总数不会统计这一片段）中，也无法单独针对这个片段做转码、微信发布等任何视频处理操作。\n\n剪辑不固化的优势在于其剪辑操作十分“轻量化”，不会产生额外的存储开销。但其不足之处在于生命周期与原始录制视频相同，且无法进一步进行转码等视频处理。"
  },
  "ApplyUpload": {
    "params": [
      {
        "name": "MediaType",
        "desc": "媒体类型，可选值请参考[上传能力综述](https://cloud.tencent.com/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)。"
      },
      {
        "name": "MediaName",
        "desc": "媒体名称。"
      },
      {
        "name": "CoverType",
        "desc": "封面类型，可选值请参考[上传能力综述](https://cloud.tencent.com/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)。"
      },
      {
        "name": "Procedure",
        "desc": "媒体后续任务操作，详见[上传指定任务流](https://cloud.tencent.com/document/product/266/9759)。"
      },
      {
        "name": "ExpireTime",
        "desc": "媒体文件过期时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。"
      },
      {
        "name": "StorageRegion",
        "desc": "指定上传园区，仅适用于对上传地域有特殊需求的用户。"
      },
      {
        "name": "ClassId",
        "desc": "分类ID，用于对媒体进行分类管理，可通过[创建分类](https://cloud.tencent.com/document/product/266/7812)接口，创建分类，获得分类 ID。\n<li>默认值：0，表示其他分类。</li>"
      },
      {
        "name": "SourceContext",
        "desc": "来源上下文，用于透传用户请求信息，上传回调接口将返回该字段值，最长 250 个字符。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "* 该接口用于申请媒体文件（和封面文件）的上传，获取文件上传到腾讯云点播的元信息（包括上传路径、上传签名等），用于后续上传接口。\n* 上传流程请参考[服务端上传综述](https://cloud.tencent.com/document/product/266/9759#.E4.B8.8A.E4.BC.A0.E6.B5.81.E7.A8.8B)。"
  },
  "SearchMedia": {
    "params": [
      {
        "name": "Text",
        "desc": "搜索文本，模糊匹配媒体文件名称或描述信息，匹配项越多，匹配度越高，排序越优先。长度限制：64 个字符。"
      },
      {
        "name": "Tags",
        "desc": "标签集合，匹配集合中任意元素。\n<li>单个标签长度限制：8 个字符。</li>\n<li>数组长度限制：10。</li>"
      },
      {
        "name": "ClassIds",
        "desc": "分类 ID 集合，匹配集合指定 ID 的分类及其所有子类。数组长度限制：10。"
      },
      {
        "name": "StartTime",
        "desc": "创建时间的开始时间。\n<li>大于等于开始时间。</li>\n<li>格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。</li>"
      },
      {
        "name": "EndTime",
        "desc": "创建时间的结束时间。\n<li>小于结束时间。</li>\n<li>格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。</li>"
      },
      {
        "name": "SourceType",
        "desc": "媒体文件来源，来源取值参见 [SourceType](https://cloud.tencent.com/document/product/266/31773#MediaSourceData)。"
      },
      {
        "name": "StreamId",
        "desc": "推流[直播码](https://cloud.tencent.com/document/product/267/5959)。"
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
        "desc": "偏移量。\n<li>默认值：0。</li>\n<li>取值范围：Offset + Limit 不超过 5000。</li>"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10。"
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "搜索媒体信息，支持各种条件筛选，以及对返回结果进行排序、过滤等功能，具体包括：\n- 根据媒体文件名或描述信息进行文本模糊搜索。\n- 根据媒体分类、标签进行检索。\n    - 指定分类集合 ClassIds（见输入参数），返回满足集合中任意分类的媒体。例如：假设媒体分类有电影、电视剧、综艺，其中电影又有子分类历史片、动作片、言情片。如果 ClassIds 指定了电影、电视剧，那么电影和电视剧下的所有子分类\n    都会返回；而如果 ClassIds 指定的是历史片、动作片，那么只有这 2 个子分类下的媒体才会返回。\n    - 指定标签集合 Tags（见输入参数），返回满足集合中任意标签的媒体。例如：假设媒体标签有二次元、宫斗、鬼畜，如果 Tags 指定了二次元、鬼畜 2 个标签，那么只要符合这 2 个标签中任意一个的媒体都会被检索出来。\n- 允许指定筛选某一来源 Source（见输入参数）的媒体。\n- 允许根据直播推流码、Vid（见输入参数）筛选直播录制的媒体。\n- 允许根据媒体的创建范围筛选媒体。\n- 允许对上述条件进行任意组合，检索同时满足以上条件的媒体。例如可以筛选从 2018 年 12 月 1 日到 2018 年 12 月 8 日创建的电影、电视剧分类下带有宫斗、鬼畜标签的媒体。\n- 允许对结果进行排序，允许通过 Offset 和 Limit 实现只返回部分结果。\n\n接口搜索限制：\n- 搜索结果超过 5000条，不再支持分页查询超过 5000 部分的数据。"
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
      },
      {
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "修改用户自定义水印模板，水印类型不允许修改。"
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
    "desc": "删除指定名字的任务流模板"
  },
  "DescribeProcedureTemplates": {
    "params": [
      {
        "name": "Names",
        "desc": "任务流模板名字过滤条件，数组长度限制：100。"
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
    "desc": "根据转码模板唯一标识，获取转码模板详情列表。返回结果包含符合条件的所有用户自定义模板及[系统预置转码模板](https://cloud.tencent.com/document/product/266/11701#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。"
  },
  "SimpleHlsClip": {
    "params": [
      {
        "name": "Url",
        "desc": "需要裁剪的腾讯云点播 HLS 视频 URL。"
      },
      {
        "name": "StartTimeOffset",
        "desc": "裁剪的开始偏移时间，单位秒。默认 0，即从视频开头开始裁剪。负数表示距离视频结束多少秒开始裁剪。比如 -10 表示从倒数第 10 秒开始裁剪。"
      },
      {
        "name": "EndTimeOffset",
        "desc": "裁剪的结束偏移时间，单位秒。默认 0，即裁剪到视频尾部。负数表示距离视频结束多少秒结束裁剪。比如 -10 表示到倒数第 10 秒结束裁剪。"
      }
    ],
    "desc": "对 HLS 视频进行按时间段裁剪。\n\n注意：裁剪出来的视频与原始视频共用 ts，仅生成新的 m3u8。原始视频删除后，该裁剪视频也会被删除。"
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
  "CreateProcedureTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "任务流名字（支持中文，不超过20个字）。"
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
    "desc": "重新设置已存在的任务流模板的任务内容"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "创建用户自定义转码模板，数量上限：1000。"
  },
  "ProcessMedia": {
    "params": [
      {
        "name": "FileId",
        "desc": "媒体文件 ID。"
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
        "name": "TasksPriority",
        "desc": "任务流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。"
      },
      {
        "name": "TasksNotifyMode",
        "desc": "任务流状态变更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。"
      },
      {
        "name": "SessionContext",
        "desc": "来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 250 个字符。"
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
    "desc": "对点播中的音视频媒体发起处理任务，功能包括：\n1. 视频转码（带水印）；\n2. 视频转动图；\n3. 对视频按指定时间点截图；\n4. 对视频采样截图；\n5. 对视频截图雪碧图；\n6. 对视频截取一张图做封面；\n7. 对视频转自适应码流（并加密）；\n8. 智能内容审核（鉴黄、鉴恐、鉴政）；\n9. 智能内容分析（标签、分类、封面）。"
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
        "desc": "媒体文件过期时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。填“9999-12-31T23:59:59Z”表示永不过期。过期后该媒体文件及其相关资源（转码结果、雪碧图等）将被永久删除。"
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
        "name": "SubAppId",
        "desc": "点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。"
      }
    ],
    "desc": "创建用户自定义视频内容分析模板，数量上限：50。"
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
        "desc": "水印类型过滤条件，可选值：\n<li>image：图片水印；</li>\n<li>text：文字水印。</li>"
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
  }
}