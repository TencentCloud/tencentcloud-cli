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
        "name": "Url",
        "desc": "语音 URL，公网可下载。当 SourceType 值为 0 时须填写该字段，为 1 时不填；URL 的长度大于 0，小于 2048，需进行urlencode编码。"
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
        "name": "Data",
        "desc": "语音数据，当SourceType 值为1时必须填写，为0可不写。要base64编码"
      },
      {
        "name": "DataLen",
        "desc": "数据长度，当 SourceType 值为1时必须填写，为0可不写。"
      }
    ],
    "desc": "识别60s内的短语音。"
  }
}