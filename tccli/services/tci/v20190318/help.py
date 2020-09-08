# -*- coding: utf-8 -*-
DESC = "tci-2019-03-18"
INFO = {
  "SubmitOpenClassTask": {
    "params": [
      {
        "name": "FileContent",
        "desc": "输入分析对象内容，输入数据格式参考FileType参数释义"
      },
      {
        "name": "FileType",
        "desc": "输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址,picture: 图片二进制数据的BASE64编码"
      },
      {
        "name": "LibrarySet",
        "desc": "查询人员库列表，可填写学生们的注册照所在人员库"
      },
      {
        "name": "MaxVideoDuration",
        "desc": "视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束"
      }
    ],
    "desc": "**提交线下小班（无课桌）课任务**  \n线下小班课是指有学生无课桌的课堂，满座15人以下，全局画面且背景不动，能清晰看到。  \n  \n**提供的功能接口有：**学生人脸识别、学生表情识别、学生肢体动作识别。  可分析的指标维度包括：身份识别、正脸、侧脸、抬头、低头、高兴、中性、高兴、中性、惊讶、厌恶、恐惧、愤怒、蔑视、悲伤、站立、举手、坐着等。\n  \n**对场景的要求为：**真实常规教室，满座15人以下，全局画面且背景不动；人脸上下角度在20度以内，左右角度在15度以内，歪头角度在15度以内；光照均匀，无遮挡，人脸清晰可见；像素最好在 100X100 像素以上但是图像整体质量不能超过1080p。\n    \n**结果查询方式：**图像任务直接返回结果，点播及直播任务通过DescribeAITaskResult查询结果。"
  },
  "SubmitCheckAttendanceTaskPlus": {
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
        "desc": "确定出勤阈值；默认为0.92"
      },
      {
        "name": "EnableStranger",
        "desc": "是否开启陌生人模式，陌生人模式是指在任务中发现的非注册人脸库中的人脸也返回相关统计信息，默认不开启"
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
    "desc": "支持多路视频流，提交高级人员考勤任务"
  },
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
        "desc": "语音文件类型 1:raw, 2:wav, 3:mp3，10:视频（三种音频格式目前仅支持16k采样率16bit）"
      },
      {
        "name": "Functions",
        "desc": "功能开关列表，表示是否需要打开相应的功能，返回相应的信息"
      },
      {
        "name": "FileType",
        "desc": "视频文件类型，默认点播，直播填 live_url"
      },
      {
        "name": "MuteThreshold",
        "desc": "静音阈值设置，如果静音检测开关开启，则静音时间超过这个阈值认为是静音片段，在结果中会返回, 没给的话默认值为3s"
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
        "name": "LibraryId",
        "desc": "人员库唯一标识符"
      },
      {
        "name": "PersonId",
        "desc": "人员唯一标识符"
      },
      {
        "name": "JobNumber",
        "desc": "人员工作号码"
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
        "desc": "输入分析对象内容，输入数据格式参考FileType参数释义"
      },
      {
        "name": "FileType",
        "desc": "输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，audio_url: 音频文件，picture：图片二进制数据的BASE64编码"
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
        "name": "MaxVideoDuration",
        "desc": "视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束"
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
  "DeleteVocabLib": {
    "params": [
      {
        "name": "VocabLibName",
        "desc": "词汇库名称"
      }
    ],
    "desc": "删除词汇库"
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
    "desc": "发起双路视频生成精彩集锦接口。该接口可以通过客户传入的学生音视频及老师视频两路Url，自动生成一堂课程的精彩集锦。需要通过DescribeHighlightResult\n接口获取生成结果。"
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
  "SubmitConversationTask": {
    "params": [
      {
        "name": "Lang",
        "desc": "音频源的语言，默认0为英文，1为中文"
      },
      {
        "name": "StudentUrl",
        "desc": "学生音频流"
      },
      {
        "name": "TeacherUrl",
        "desc": "教师音频流"
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
        "name": "VocabLibNameList",
        "desc": "识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析"
      }
    ],
    "desc": "对话任务分析接口"
  },
  "SubmitTraditionalClassTask": {
    "params": [
      {
        "name": "FileContent",
        "desc": "输入分析对象内容，输入数据格式参考FileType参数释义"
      },
      {
        "name": "FileType",
        "desc": "输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture：图片二进制数据的BASE64编码"
      },
      {
        "name": "LibrarySet",
        "desc": "查询人员库列表，可填写学生们的注册照所在人员库"
      },
      {
        "name": "MaxVideoDuration",
        "desc": "视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束"
      }
    ],
    "desc": "**提交线下传统面授大班课（含课桌）任务。**  \n传统教室课堂是指有学生课堂有课桌的课堂，满座20-50人，全局画面且背景不动。  \n  \n**提供的功能接口有：**学生人脸识别、学生表情识别、学生肢体动作识别。可分析的指标维度包括：学生身份识别、正脸、侧脸、抬头、低头、高兴、中性、高兴、中性、惊讶、厌恶、恐惧、愤怒、蔑视、悲伤、举手、站立、坐着、趴桌子、玩手机等  \n  \n**对场景的要求为：**传统的学生上课教室，满座20-50人，全局画面且背景不动；人脸上下角度在20度以内，左右角度在15度以内，歪头角度在15度以内；光照均匀，无遮挡，人脸清晰可见；像素最好在 100X100 像素以上，但是图像整体质量不能超过1080p。\n    \n**结果查询方式：**图像任务直接返回结果，点播及直播任务通过DescribeAITaskResult查询结果。\n  "
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
        "name": "LibraryId",
        "desc": "人员库唯一标识符"
      },
      {
        "name": "PersonId",
        "desc": "人员唯一标识符"
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
    "desc": "用于取消已经提交的任务，目前只支持图像任务。"
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
  "SubmitOneByOneClassTask": {
    "params": [
      {
        "name": "FileContent",
        "desc": "输入分析对象内容，输入数据格式参考FileType参数释义"
      },
      {
        "name": "FileType",
        "desc": "输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture: 图片二进制数据的BASE64编码"
      },
      {
        "name": "Lang",
        "desc": "音频源的语言，默认0为英文，1为中文 "
      },
      {
        "name": "LibrarySet",
        "desc": "查询人员库列表，可填写学生的注册照所在人员库"
      },
      {
        "name": "MaxVideoDuration",
        "desc": "视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束"
      },
      {
        "name": "VocabLibNameList",
        "desc": "识别词库名列表，这些词汇库用来维护关键词，评估学生对这些关键词的使用情况"
      },
      {
        "name": "VoiceEncodeType",
        "desc": "语音编码类型 1:pcm，当FileType为vod_url或live_url时为必填"
      },
      {
        "name": "VoiceFileType",
        "desc": "语音文件类型10:视频（三种音频格式目前仅支持16k采样率16bit），当FileType为vod_url或live_url时为必填"
      }
    ],
    "desc": "**提交在线1对1课堂任务**  \n对于在线1对1课堂，老师通过视频向学生授课，并且学生人数为1人。通过上传学生端的图像信息，可以获取学生的听课情况分析。 具体指一路全局画面且背景不动，有1位学生的头像或上半身的画面，要求画面稳定清晰。\n  \n**提供的功能接口有：**学生人脸识别、学生表情识别、语音识别。可分析的指标维度包括：学生身份识别、正脸、侧脸、抬头、低头、人脸坐标、人脸尺寸、高兴、中性、高兴、中性、惊讶、厌恶、恐惧、愤怒、蔑视、悲伤、语音转文字、发音时长、非发音时长、音量、语速等。\n  \n**对场景的要求为：**真实常规1v1授课场景，学生2人以下，全局画面且背景不动；人脸上下角度在20度以内，左右角度在15度以内，歪头角度在15度以内；光照均匀，无遮挡，人脸清晰可见；像素最好在 100X100 像素以上，但是图像整体质量不能超过1080p。\n    \n**结果查询方式：**图像任务直接返回结果，点播及直播任务通过DescribeAITaskResult查询结果。"
  },
  "SubmitPartialBodyClassTask": {
    "params": [
      {
        "name": "FileContent",
        "desc": "输入分析对象内容，输入数据格式参考FileType参数释义"
      },
      {
        "name": "FileType",
        "desc": "输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture: 图片二进制数据的BASE64编码"
      },
      {
        "name": "Lang",
        "desc": "音频源的语言，默认0为英文，1为中文"
      },
      {
        "name": "LibrarySet",
        "desc": "查询人员库列表，可填写老师的注册照所在人员库"
      },
      {
        "name": "MaxVideoDuration",
        "desc": "视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束"
      },
      {
        "name": "VocabLibNameList",
        "desc": "识别词库名列表，这些词汇库用来维护关键词，评估老师授课过程中，对这些关键词的使用情况"
      },
      {
        "name": "VoiceEncodeType",
        "desc": "语音编码类型 1:pcm，当FileType为vod_url或live_url时为必填"
      },
      {
        "name": "VoiceFileType",
        "desc": "语音文件类型 10:视频（三种音频格式目前仅支持16k采样率16bit），当FileType为vod_url或live_url时为必填"
      }
    ],
    "desc": "**在线小班课任务**：此场景是在线授课场景，老师一般为坐着授课，摄像头可以拍摄到老师的头部及上半身。拍摄视频为一路全局画面，且背景不动，要求画面稳定清晰。通过此接口可分析老师授课的行为及语音，以支持AI评教。    \n  \n**提供的功能接口有：**老师人脸识别、老师表情识别、老师手势识别、光线识别、语音识别。 可分析的指标维度包括：身份识别、正脸、侧脸、人脸坐标、人脸尺寸、高兴、中性、高兴、中性、惊讶、厌恶、恐惧、愤怒、蔑视、悲伤、点赞手势、听你说手势、听我说手势、拿教具行为、语音转文字、发音时长、非发音时长、音量、语速、指定关键词的使用等 \n  \n**对场景的要求为：**在线常规授课场景，全局画面且背景不动；人脸上下角度在20度以内，左右角度在15度以内，歪头角度在15度以内；光照均匀，无遮挡，人脸清晰可见；像素最好在 100X100 像素以上，但是图像整体质量不能超过1080p。\n    \n**结果查询方式：**图像任务直接返回结果，点播及直播任务通过DescribeAITaskResult查询结果。"
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
        "desc": "确定出勤阈值；默认为0.92"
      },
      {
        "name": "EnableStranger",
        "desc": "是否开启陌生人模式，陌生人模式是指在任务中发现的非注册人脸库中的人脸也返回相关统计信息，默认不开启"
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
    "desc": "提交人员考勤任务，支持包括点播和直播资源；支持通过DescribeAttendanceResult查询结果，也支持通过NoticeUrl设置考勤回调结果，回调结果结构如下：\n##### 回调事件结构\n | 参数名称 | 类型 | 描述 | \n | ----  | ---  | ------  |\n | jobid | Integer | 任务ID | \n | person_info | array of PersonInfo | 识别到的人员列表 | \n#####子结构PersonInfo\n | 参数名称 | 类型 | 描述 | \n | ----  | ---  | ------  |\n | traceid | String | 可用于区分同一路视频流下的不同陌生人 | \n | personid | String | 识别到的人员ID，如果是陌生人则返回空串 | \n | libid | String | 识别到的人员所在的库ID，如果是陌生人则返回空串 | \n | timestamp | uint64 | 识别到人脸的绝对时间戳，单位ms | \n | image_url | string | 识别到人脸的事件抓图的下载地址，不长期保存，需要请及时下载 | "
  },
  "CreatePerson": {
    "params": [
      {
        "name": "LibraryId",
        "desc": "人员库唯一标识符"
      },
      {
        "name": "PersonName",
        "desc": "人员名称"
      },
      {
        "name": "Images",
        "desc": "图片数据 base64 字符串，与 Urls 参数选择一个输入"
      },
      {
        "name": "JobNumber",
        "desc": "人员工作号码"
      },
      {
        "name": "Mail",
        "desc": "人员邮箱"
      },
      {
        "name": "Male",
        "desc": "人员性别，0：未知 1：男性，2：女性"
      },
      {
        "name": "PersonId",
        "desc": "自定义人员 ID，注意不能使用 tci_person_ 前缀"
      },
      {
        "name": "PhoneNumber",
        "desc": "人员电话号码"
      },
      {
        "name": "StudentNumber",
        "desc": "人员学生号码"
      },
      {
        "name": "Urls",
        "desc": "图片下载地址，与 Images 参数选择一个输入"
      }
    ],
    "desc": "创建人员"
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
  "SubmitImageTask": {
    "params": [
      {
        "name": "FileContent",
        "desc": "输入分析对象内容，输入数据格式参考FileType参数释义"
      },
      {
        "name": "FileType",
        "desc": "输入分析对象类型，picture：二进制图片的 base64 编码字符串，picture_url:图片地址，vod_url：视频地址，live_url：直播地址"
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
        "name": "EventsCallBack",
        "desc": "结果更新回调地址。"
      },
      {
        "name": "FrameInterval",
        "desc": "抽帧的时间间隔，单位毫秒，默认值1000，保留字段，当前不支持填写。"
      },
      {
        "name": "LibrarySet",
        "desc": "查询人员库列表"
      },
      {
        "name": "MaxVideoDuration",
        "desc": "视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束"
      },
      {
        "name": "SimThreshold",
        "desc": "人脸识别中的相似度阈值，默认值为0.89，保留字段，当前不支持填写。"
      }
    ],
    "desc": "提交图像分析任务"
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
  "SubmitImageTaskPlus": {
    "params": [
      {
        "name": "FileContent",
        "desc": "输入分析对象内容，输入数据格式参考FileType参数释义"
      },
      {
        "name": "FileType",
        "desc": "输入分析对象类型，picture：二进制图片的 base64 编码字符串，picture_url:图片地址，vod_url：视频地址，live_url：直播地址"
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
        "desc": "抽帧的时间间隔，单位毫秒，默认值1000，保留字段，当前不支持填写。"
      },
      {
        "name": "LibrarySet",
        "desc": "查询人员库列表"
      },
      {
        "name": "MaxVideoDuration",
        "desc": "视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束"
      },
      {
        "name": "SimThreshold",
        "desc": "人脸识别中的相似度阈值，默认值为0.89，保留字段，当前不支持填写。"
      }
    ],
    "desc": "高级图像分析任务，开放了图像任务里的所有开关，可以根据场景深度定制图像分析任务。支持的图像类别有，图片链接、图片二进制数据、点播链接和直播链接。"
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
  "DescribeHighlightResult": {
    "params": [
      {
        "name": "JobId",
        "desc": "精彩集锦任务唯一id。在URL方式时提交请求后会返回一个JobId，后续查询该url的结果时使用这个JobId进行查询。"
      }
    ],
    "desc": "视频精彩集锦结果查询接口，异步查询客户提交的请求的结果。"
  },
  "DescribePerson": {
    "params": [
      {
        "name": "LibraryId",
        "desc": "人员库唯一标识符"
      },
      {
        "name": "PersonId",
        "desc": "人员唯一标识符"
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
  "SubmitFullBodyClassTask": {
    "params": [
      {
        "name": "FileContent",
        "desc": "输入分析对象内容，输入数据格式参考FileType参数释义"
      },
      {
        "name": "FileType",
        "desc": "输入分析对象类型，picture_url:图片地址，vod_url:视频地址，live_url：直播地址，picture: 图片二进制数据的BASE64编码"
      },
      {
        "name": "Lang",
        "desc": "音频源的语言，默认0为英文，1为中文"
      },
      {
        "name": "LibrarySet",
        "desc": "查询人员库列表，可填写老师的注册照所在人员库"
      },
      {
        "name": "MaxVideoDuration",
        "desc": "视频评估时间，单位秒，点播场景默认值为2小时（无法探测长度时）或完整视频，直播场景默认值为10分钟或直播提前结束"
      },
      {
        "name": "VocabLibNameList",
        "desc": "识别词库名列表，这些词汇库用来维护关键词，评估老师授课过程中，对这些关键词的使用情况"
      },
      {
        "name": "VoiceEncodeType",
        "desc": "语音编码类型 1:pcm，当FileType为vod_url或live_url时为必填"
      },
      {
        "name": "VoiceFileType",
        "desc": "语音文件类型 10:视频（三种音频格式目前仅支持16k采样率16bit），当FileType为vod_url或live_url时为必填"
      }
    ],
    "desc": "**传统课堂授课任务**：在此场景中，老师为站立授课，有白板或投影供老师展示课程内容，摄像头可以拍摄到老师的半身或者全身。拍摄视频为一路全局画面，且背景不动，要求画面稳定清晰。通过此接口可分析老师授课的行为及语音，以支持AI评教。  \n  \n**提供的功能接口有：**老师人脸识别、老师表情识别、老师肢体动作识别、语音识别。  可分析的指标维度包括：身份识别、正脸、侧脸、人脸坐标、人脸尺寸、高兴、中性、高兴、中性、惊讶、厌恶、恐惧、愤怒、蔑视、悲伤、正面讲解、写板书、指黑板、语音转文字、发音时长、非发音时长、音量、语速、指定关键词的使用等\n  \n**对场景的要求为：**真实场景老师1人出现在画面中，全局画面且背景不动；人脸上下角度在20度以内，左右角度在15度以内，歪头角度在15度以内；光照均匀，无遮挡，人脸清晰可见；像素最好在 100X100 像素以上，但是图像整体质量不能超过1080p。\n    \n**结果查询方式：**图像任务直接返回结果，点播及直播任务通过DescribeAITaskResult查询结果。"
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
        "name": "StorageMode",
        "desc": "是否临时保存 音频链接"
      },
      {
        "name": "VocabLibNameList",
        "desc": "识别词库名列表，评估过程使用这些词汇库中的词汇进行词汇使用行为分析"
      }
    ],
    "desc": "分析音频信息"
  }
}