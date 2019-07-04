# -*- coding: utf-8 -*-
DESC = "tci-2019-03-18"
INFO = {
  "CreateLibrary": {
    "params": [
      {
        "name": "LibraryName",
        "desc": "人员库名称"
      },
      {
        "name": "LibraryId",
        "desc": "人员库唯一标志符，为空则系统自动生成。"
      }
    ],
    "desc": "创建人员库"
  },
  "SubmitAudioTask": {
    "params": [
      {
        "name": "Lang",
        "desc": "音频源的语言，默认0为英文，1为中文"
      },
      {
        "name": "Url",
        "desc": "音频URL。客户请求为URL方式时必须带此字段指名音频的url。"
      },
      {
        "name": "VoiceEncodeType",
        "desc": "语音编码类型 1:pcm"
      },
      {
        "name": "VoiceFileType",
        "desc": "语音文件类型 1:raw, 2:wav, 3:mp3（三种格式目前仅支持16k采样率16bit）"
      },
      {
        "name": "Functions",
        "desc": "功能开关列表，表示是否需要打开相应的功能，返回相应的信息"
      },
      {
        "name": "ClassId",
        "desc": "课堂标识符"
      },
      {
        "name": "Identity",
        "desc": "身份，1：老师 2：学生"
      },
      {
        "name": "VocabLibNameList",
        "desc": "识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析"
      }
    ],
    "desc": "音频任务提交接口"
  },
  "CreateFace": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员唯一标识符"
      },
      {
        "name": "Images",
        "desc": "图片数据 base64 字符串，与 Urls 参数选择一个输入"
      },
      {
        "name": "LibraryId",
        "desc": "人员库唯一标识符"
      },
      {
        "name": "Urls",
        "desc": "图片下载地址，与 Images 参数选择一个输入"
      }
    ],
    "desc": "创建人脸"
  },
  "ModifyPerson": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员唯一标识符"
      },
      {
        "name": "JobNumber",
        "desc": "人员工作号码"
      },
      {
        "name": "LibraryId",
        "desc": "人员库唯一标识符"
      },
      {
        "name": "Mail",
        "desc": "人员邮箱"
      },
      {
        "name": "Male",
        "desc": "人员性别"
      },
      {
        "name": "PersonName",
        "desc": "人员名称"
      },
      {
        "name": "PhoneNumber",
        "desc": "人员电话号码"
      },
      {
        "name": "StudentNumber",
        "desc": "人员学生号码"
      }
    ],
    "desc": "修改人员信息"
  },
  "DescribeImageTaskStatistic": {
    "params": [
      {
        "name": "JobId",
        "desc": "图像任务标识符"
      }
    ],
    "desc": "获取图像任务统计信息"
  },
  "AIAssistant": {
    "params": [
      {
        "name": "FileContent",
        "desc": "输入分析对象内容"
      },
      {
        "name": "FileType",
        "desc": "输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址,audio_url: 音频文件"
      },
      {
        "name": "Lang",
        "desc": "音频源的语言，默认0为英文，1为中文"
      },
      {
        "name": "LibrarySet",
        "desc": "查询人员库列表"
      },
      {
        "name": "Template",
        "desc": "标准化模板选择：0：AI助教基础版本，1：AI评教基础版本，2：AI评教标准版本。AI 助教基础版本功能包括：人脸检索、人脸检测、人脸表情识别、学生动作选项，音频信息分析，微笑识别。AI 评教基础版本功能包括：人脸检索、人脸检测、人脸表情识别、音频信息分析。AI 评教标准版功能包括人脸检索、人脸检测、人脸表情识别、手势识别、音频信息分析、音频关键词分析、视频精彩集锦分析。"
      },
      {
        "name": "VocabLibNameList",
        "desc": "识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析"
      },
      {
        "name": "VoiceEncodeType",
        "desc": "语音编码类型 1:pcm"
      },
      {
        "name": "VoiceFileType",
        "desc": "语音文件类型 1:raw, 2:wav, 3:mp3，10:视频（三种音频格式目前仅支持16k采样率16bit）"
      }
    ],
    "desc": "提供 AI 助教基础版本功能接口"
  },
  "ModifyLibrary": {
    "params": [
      {
        "name": "LibraryId",
        "desc": "人员库唯一标识符"
      },
      {
        "name": "LibraryName",
        "desc": "人员库名称"
      }
    ],
    "desc": "修改人员库信息"
  },
  "SubmitDoubleVideoHighlights": {
    "params": [
      {
        "name": "FileContent",
        "desc": "学生视频url"
      },
      {
        "name": "LibIds",
        "desc": "需要检索的人脸合集库，不在库中的人脸将不参与精彩集锦；目前仅支持输入一个人脸库。"
      },
      {
        "name": "Functions",
        "desc": "详细功能开关配置项"
      },
      {
        "name": "PersonInfoList",
        "desc": "需要匹配的人员信息列表。"
      },
      {
        "name": "FrameInterval",
        "desc": "视频处理的抽帧间隔，单位毫秒。建议留空。"
      },
      {
        "name": "PersonIds",
        "desc": "旧版本需要匹配的人员信息列表。"
      },
      {
        "name": "SimThreshold",
        "desc": "人脸检索的相似度阈值，默认值0.89。建议留空。"
      },
      {
        "name": "TeacherFileContent",
        "desc": "老师视频url"
      }
    ],
    "desc": "发起双路视频生成精彩集锦接口。该接口可以通过客户传入的学生音视频及老师视频两路Url，自动生成一堂课程的精彩集锦。需要通过SubmitDoubleVideoHighlights接口获取生成结果。"
  },
  "DescribePersons": {
    "params": [
      {
        "name": "LibraryId",
        "desc": "人员库唯一标识符"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      }
    ],
    "desc": "拉取人员列表"
  },
  "DescribeHighlightResult": {
    "params": [
      {
        "name": "JobId",
        "desc": "精彩集锦任务唯一id。在URL方式时提交请求后会返回一个JobId，后续查询该url的结果时使用这个JobId进行查询。"
      }
    ],
    "desc": "视频精彩集锦结果查询接口，异步查询客户提交的请求的结果。"
  },
  "DescribeAITaskResult": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务唯一标识符。在URL方式时提交请求后会返回一个任务标识符，后续查询该url的结果时使用这个标识符进行查询。"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      }
    ],
    "desc": "获取标准化接口任务结果"
  },
  "DeletePerson": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员唯一标识符"
      },
      {
        "name": "LibraryId",
        "desc": "人员库唯一标识符"
      }
    ],
    "desc": "删除人员"
  },
  "DescribeLibraries": {
    "params": [],
    "desc": "获取人员库列表"
  },
  "CancelTask": {
    "params": [
      {
        "name": "JobId",
        "desc": "待取消任务标志符。"
      }
    ],
    "desc": "用于取消已经提交的任务"
  },
  "SubmitImageTask": {
    "params": [
      {
        "name": "FileContent",
        "desc": "输入分析对象内容"
      },
      {
        "name": "FileType",
        "desc": "输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址"
      },
      {
        "name": "Functions",
        "desc": "任务控制选项"
      },
      {
        "name": "LightStandardSet",
        "desc": "光照标准列表"
      },
      {
        "name": "FrameInterval",
        "desc": "抽帧的时间间隔，单位毫秒，默认值1000。"
      },
      {
        "name": "LibrarySet",
        "desc": "查询人员库列表"
      },
      {
        "name": "MaxVideoDuration",
        "desc": "最大的视频长度，单位毫秒，默认值为两小时"
      },
      {
        "name": "SimThreshold",
        "desc": "人脸识别中的相似度阈值，默认值为0.89"
      }
    ],
    "desc": "提交图像分析任务"
  },
  "DescribeVocabLib": {
    "params": [],
    "desc": "查询词汇库"
  },
  "CreateVocab": {
    "params": [
      {
        "name": "VocabLibName",
        "desc": "要添加词汇的词汇库名"
      },
      {
        "name": "VocabList",
        "desc": "要添加的词汇列表"
      }
    ],
    "desc": "创建词汇"
  },
  "SubmitCheckAttendanceTask": {
    "params": [
      {
        "name": "FileContent",
        "desc": "输入数据"
      },
      {
        "name": "FileType",
        "desc": "视频流类型，vod_url表示点播URL，live_url表示直播URL，默认vod_url"
      },
      {
        "name": "LibraryIds",
        "desc": "人员库 ID列表"
      },
      {
        "name": "AttendanceThreshold",
        "desc": "确定出勤阀值；默认为0.92"
      },
      {
        "name": "EnableStranger",
        "desc": "是否开启陌生人模式，开启后才会推送陌生人事件，默认不开启"
      },
      {
        "name": "EndTime",
        "desc": "考勤结束时间（到视频的第几秒结束考勤），单位秒；默认为900 \n对于直播场景，使用绝对时间戳，单位秒，默认当前时间往后12小时"
      },
      {
        "name": "NoticeUrl",
        "desc": "通知回调地址，要求方法为post，application/json格式"
      },
      {
        "name": "StartTime",
        "desc": "考勤开始时间（从视频的第几秒开始考勤），单位秒；默认为0 \n对于直播场景，使用绝对时间戳，单位秒，默认当前时间"
      },
      {
        "name": "Threshold",
        "desc": "识别阈值；默认为0.8"
      }
    ],
    "desc": "提交人员考勤任务"
  },
  "DescribeConversationTask": {
    "params": [
      {
        "name": "JobId",
        "desc": "音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。"
      },
      {
        "name": "Identity",
        "desc": "要查询明细的流的身份，1 老师 2 学生"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      }
    ],
    "desc": "音频对话任务评估任务信息查询接口，异步查询客户提交的请求的结果。"
  },
  "DeleteLibrary": {
    "params": [
      {
        "name": "LibraryId",
        "desc": "人员库唯一标识符"
      }
    ],
    "desc": "删除人员库"
  },
  "DescribeImageTask": {
    "params": [
      {
        "name": "JobId",
        "desc": "任务标识符"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      }
    ],
    "desc": "拉取任务详情"
  },
  "SubmitHighlights": {
    "params": [
      {
        "name": "Functions",
        "desc": "表情配置开关项。"
      },
      {
        "name": "FileContent",
        "desc": "视频url。"
      },
      {
        "name": "FileType",
        "desc": "视频类型及来源，目前只支持点播类型：\"vod_url\"。"
      },
      {
        "name": "LibIds",
        "desc": "需要检索的人脸合集库，不在库中的人脸将不参与精彩集锦。"
      },
      {
        "name": "FrameInterval",
        "desc": "视频处理的抽帧间隔，单位毫秒。建议留空。"
      },
      {
        "name": "KeywordsLanguage",
        "desc": "关键词语言类型，0为英文，1为中文。"
      },
      {
        "name": "KeywordsStrings",
        "desc": "关键词数组，当且仅当Funtions中的EnableKeywordWonderfulTime为true时有意义，匹配相应的关键字。"
      },
      {
        "name": "MaxVideoDuration",
        "desc": "处理视频的总时长，单位毫秒。该值为0或未设置时，默认值两小时生效；当该值大于视频实际时长时，视频实际时长生效；当该值小于视频实际时长时，该值生效；当获取视频实际时长失败时，若该值设置则生效，否则默认值生效。建议留空。"
      },
      {
        "name": "SimThreshold",
        "desc": "人脸检索的相似度阈值，默认值0.89。建议留空。"
      }
    ],
    "desc": "发起视频生成精彩集锦接口。该接口可以通过客户传入的课程音频数据及相关策略（如微笑抽取，专注抽取等），自动生成一堂课程的精彩集锦。需要通过QueryHighlightResult接口获取生成结果。"
  },
  "DescribeAttendanceResult": {
    "params": [
      {
        "name": "JobId",
        "desc": "任务唯一标识符"
      }
    ],
    "desc": "人脸考勤查询结果"
  },
  "CreateVocabLib": {
    "params": [
      {
        "name": "VocabLibName",
        "desc": "词汇库名称"
      }
    ],
    "desc": "建立词汇库"
  },
  "DeleteVocab": {
    "params": [
      {
        "name": "VocabLibName",
        "desc": "要删除词汇的词汇库名"
      },
      {
        "name": "VocabList",
        "desc": "要删除的词汇列表"
      }
    ],
    "desc": "删除词汇"
  },
  "CheckAttendance": {
    "params": [
      {
        "name": "FileContent",
        "desc": "输入数据"
      },
      {
        "name": "FileType",
        "desc": "输入类型，picture_url:图片，vod_url:视频文件"
      },
      {
        "name": "LibraryId",
        "desc": "人员库 ID"
      },
      {
        "name": "PersonIdSet",
        "desc": "人员 ID 列表"
      },
      {
        "name": "AttendanceThreshold",
        "desc": "确定出勤阀值；默认为0.92"
      },
      {
        "name": "EndTime",
        "desc": "考勤结束时间（到视频的第几秒结束考勤），单位秒；默认为900"
      },
      {
        "name": "StartTime",
        "desc": "考勤开始时间（从视频的第几秒开始考勤），单位秒；默认为0"
      },
      {
        "name": "Threshold",
        "desc": "识别阈值；默认为0.7"
      }
    ],
    "desc": "人员考勤"
  },
  "CheckFacePhoto": {
    "params": [
      {
        "name": "FileContent",
        "desc": "输入分析对象内容"
      },
      {
        "name": "FileType",
        "desc": "输入分析对象类型，picture_url:图片地址"
      }
    ],
    "desc": "检查人脸图片是否合法"
  },
  "DescribeVocab": {
    "params": [
      {
        "name": "VocabLibName",
        "desc": "要查询词汇的词汇库名"
      }
    ],
    "desc": "查询词汇"
  },
  "DeleteVocabLib": {
    "params": [
      {
        "name": "VocabLibName",
        "desc": "词汇库名称"
      }
    ],
    "desc": "删除词汇库"
  },
  "DescribePerson": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员唯一标识符"
      },
      {
        "name": "LibraryId",
        "desc": "人员库唯一标识符"
      }
    ],
    "desc": "获取人员详情"
  },
  "DeleteFace": {
    "params": [
      {
        "name": "FaceIdSet",
        "desc": "人脸标识符数组"
      },
      {
        "name": "PersonId",
        "desc": "人员唯一标识符"
      },
      {
        "name": "LibraryId",
        "desc": "人员库唯一标识符"
      }
    ],
    "desc": "删除人脸"
  },
  "DescribeAudioTask": {
    "params": [
      {
        "name": "JobId",
        "desc": "音频任务唯一id。在URL方式时提交请求后会返回一个jobid，后续查询该url的结果时使用这个jobid进行查询。"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      }
    ],
    "desc": "音频评估任务信息查询接口，异步查询客户提交的请求的结果。"
  },
  "TransmitAudioStream": {
    "params": [
      {
        "name": "Functions",
        "desc": "功能开关列表，表示是否需要打开相应的功能，返回相应的信息"
      },
      {
        "name": "SeqId",
        "desc": "流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义。"
      },
      {
        "name": "SessionId",
        "desc": "语音段唯一标识，一个完整语音一个SessionId。"
      },
      {
        "name": "UserVoiceData",
        "desc": "当前数据包数据, 流式模式下数据包大小可以按需设置，在网络良好的情况下，建议设置为0.5k，且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数），编码格式要求为BASE64。"
      },
      {
        "name": "VoiceEncodeType",
        "desc": "语音编码类型 1:pcm。"
      },
      {
        "name": "VoiceFileType",
        "desc": "语音文件类型 \t1: raw, 2: wav, 3: mp3 (语言文件格式目前仅支持 16k 采样率 16bit 编码单声道，如有不一致可能导致评估不准确或失败)。"
      },
      {
        "name": "IsEnd",
        "desc": "是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。"
      },
      {
        "name": "Lang",
        "desc": "音频源的语言，默认0为英文，1为中文"
      },
      {
        "name": "VocabLibNameList",
        "desc": "识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析"
      }
    ],
    "desc": "分析音频信息"
  }
}