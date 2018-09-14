# -*- coding: utf-8 -*-
DESC = "aai-2018-05-22"
INFO = {
  "SimultaneousInterpreting": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "腾讯云项目 ID，可填 0，总长度不超过 1024 字节。"
      },
      {
        "name": "SubServiceType",
        "desc": "子服务类型。0：离线语音识别。1：实时流式识别，2，一句话识别。3：同传。"
      },
      {
        "name": "RecEngineModelType",
        "desc": "识别引擎类型。8k_zh： 8k 中文会场模型；16k_zh：16k 中文会场模型，8k_en： 8k 英文会场模型；16k_en：16k 英文会场模型。当前仅支持16K。"
      },
      {
        "name": "Data",
        "desc": "语音数据，要base64编码。"
      },
      {
        "name": "DataLen",
        "desc": "数据长度。"
      },
      {
        "name": "VoiceId",
        "desc": "声音id，标识一句话。"
      },
      {
        "name": "IsEnd",
        "desc": "是否是一句话的结束。"
      },
      {
        "name": "VoiceFormat",
        "desc": "声音编码的格式1:pcm，4:speex，6:silk，默认为1。"
      },
      {
        "name": "OpenTranslate",
        "desc": "是否需要翻译结果，1表示需要翻译，0是不需要。"
      },
      {
        "name": "SourceLanguage",
        "desc": "如果需要翻译，表示源语言类型，可取值：zh，en。"
      },
      {
        "name": "TargetLanguage",
        "desc": "如果需要翻译，表示目标语言类型，可取值：zh，en。"
      },
      {
        "name": "Seq",
        "desc": "表明当前语音分片的索引，从0开始"
      }
    ],
    "desc": "该接口是实时流式识别，可同时返回语音识别文本及翻译文本，当前仅支持中文和英文。该接口可配合同传windows客户端，提供会议现场同传服务。"
  },
  "SentenceRecognition": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "腾讯云项目 ID，可填 0，总长度不超过 1024 字节。"
      },
      {
        "name": "SubServiceType",
        "desc": "子服务类型。2，一句话识别。"
      },
      {
        "name": "EngSerViceType",
        "desc": "引擎类型。8k：电话 8k 通用模型；16k：16k 通用模型。只支持单声道音频识别。"
      },
      {
        "name": "SourceType",
        "desc": "语音数据来源。0：语音 URL；1：语音数据（post body）。"
      },
      {
        "name": "VoiceFormat",
        "desc": "识别音频的音频格式（支持mp3,wav）。"
      },
      {
        "name": "UsrAudioKey",
        "desc": "用户端对此任务的唯一标识，用户自助生成，用于用户查找识别结果。"
      },
      {
        "name": "Url",
        "desc": "语音 URL，公网可下载。当 SourceType 值为 0 时须填写该字段，为 1 时不填；URL 的长度大于 0，小于 2048，需进行urlencode编码。音频时间长度要小于60s。"
      },
      {
        "name": "Data",
        "desc": "语音数据，当SourceType 值为1时必须填写，为0可不写。要base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于900k。"
      },
      {
        "name": "DataLen",
        "desc": "数据长度，当 SourceType 值为1时必须填写，为0可不写（此数据长度为数据未进行base64编码时的数据长度）。"
      }
    ],
    "desc": "识别60s内的短语音，当音频放在请求body中传输时整个请求大小不能超过1M，当音频以url方式传输时，音频时长不可超过60s。所有请求参数放在post的body中采用x-www-form-urlencoded（数据转换成一个字串（name1=value1&name2=value2…）进行urlencode后）编码传输。"
  },
  "Chat": {
    "params": [
      {
        "name": "Text",
        "desc": "聊天输入文本"
      },
      {
        "name": "ProjectId",
        "desc": "腾讯云项目 ID，可填 0，总长度不超过 1024 字节。"
      },
      {
        "name": "User",
        "desc": "json格式，比如 {\"id\":\"test\",\"gender\":\"male\"}。记录当前与机器人交互的用户id，非必须但强烈建议传入，否则多轮聊天功能会受影响"
      }
    ],
    "desc": "提供基于文本的基础聊天能力，可以让您的应用快速拥有具备深度语义理解的机器聊天功能。"
  },
  "TextToVoice": {
    "params": [
      {
        "name": "Text",
        "desc": "合成语音的源文本"
      },
      {
        "name": "SessionId",
        "desc": "一次请求对应一个SessionId，会原样返回，建议传入类似于uuid的字符串防止重复"
      },
      {
        "name": "ModelType",
        "desc": "模型类型，1-默认模型"
      },
      {
        "name": "Volume",
        "desc": "音量大小，范围：[0，10]，分别对应10个等级的音量，默认为0"
      },
      {
        "name": "Speed",
        "desc": "语速，范围：[-2，2]，分别对应不同语速：0.6倍，0.8倍，1.0倍，1.2倍，1.5倍，默认为0"
      },
      {
        "name": "ProjectId",
        "desc": "项目id，用户自定义，默认为0"
      },
      {
        "name": "VoiceType",
        "desc": "音色<li>0-女声1，亲和风格(默认)</li><li>1-男声1，成熟风格</li><li>2-男声2，成熟风格</li>"
      },
      {
        "name": "PrimaryLanguage",
        "desc": "主语言类型<li>1-中文(包括粤语)，最大100字符</li><li>2-英文，最大支持400字符</li>"
      },
      {
        "name": "SampleRate",
        "desc": "音频采样率，16000：16k，8000：8k，默认16k"
      }
    ],
    "desc": "腾讯云语音合成技术（TTS）可以将任意文本转化为语音，实现让机器和应用张口说话。\n腾讯TTS技术可以应用到很多场景，比如，移动APP语音播报新闻；智能设备语音提醒；依靠网上现有节目或少量录音，快速合成明星语音，降低邀约成本；支持车载导航语音合成的个性化语音播报。\n内测期间免费使用。"
  }
}