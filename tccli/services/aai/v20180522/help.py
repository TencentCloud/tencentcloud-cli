# -*- coding: utf-8 -*-
DESC = "aai-2018-05-22"
INFO = {
  "SentenceRecognition": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "腾讯云项目 ID，可填 0，总长度不超过 1024 字节。"
      },
      {
        "name": "SubServiceType",
        "desc": "子服务类型。0：离线语音识别。1：实时流式识别，2，一句话识别。"
      },
      {
        "name": "EngSerViceType",
        "desc": "引擎类型。8k：电话 8k 通用模型；16k：16k 通用模型。"
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
        "desc": "语音数据，当SourceType 值为1时必须填写，为0可不写。要base64编码。音频数据要小于900k。"
      },
      {
        "name": "DataLen",
        "desc": "数据长度，当 SourceType 值为1时必须填写，为0可不写。"
      }
    ],
    "desc": "识别60s内的短语音，当音频放在请求body中传输时整个请求大小不能超过1M，当音频以url方式传输时，音频时长不可超过60s。所有请求参数放在post的body中采用x-www-form-urlencoded（数据转换成一个字串（name1=value1&name2=value2…）进行urlencode后传输）编码传输。"
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
        "desc": "音量大小，暂仅支持默认值1"
      },
      {
        "name": "Speed",
        "desc": "语速，暂仅支持默认值1"
      },
      {
        "name": "ProjectId",
        "desc": "用户自定义项目id，默认为0"
      },
      {
        "name": "VoiceType",
        "desc": "音色，1-默认音色"
      },
      {
        "name": "PrimaryLanguage",
        "desc": "主语言类型<li>1-中文(包括粤语)，最大300字符</li><li>2-英文，最大支持600字符</li>"
      },
      {
        "name": "SampleRate",
        "desc": "音频采样率：暂仅支持16k"
      }
    ],
    "desc": "腾讯云语音合成技术（TTS）可以将任意文本转化为语音，实现让机器和应用张口说话。\n腾讯TTS技术可以应用到很多场景，比如，移动APP语音播报新闻；智能设备语音提醒；依靠网上现有节目或少量录音，快速合成明星语音，降低邀约成本；支持车载导航语音合成的个性化语音播报。\n内测期间免费使用。"
  }
}