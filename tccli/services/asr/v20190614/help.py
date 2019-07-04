# -*- coding: utf-8 -*-
DESC = "asr-2019-06-14"
INFO = {
  "SentenceRecognition": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "腾讯云项目 ID，可填 0，总长度不超过 1024 字节。"
      },
      {
        "name": "SubServiceType",
        "desc": "子服务类型。2： 一句话识别。"
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
        "desc": "语音 URL，公网可下载。当 SourceType 值为 0（语音 URL上传） 时须填写该字段，为 1 时不填；URL 的长度大于 0，小于 2048，需进行urlencode编码。音频时间长度要小于60s。"
      },
      {
        "name": "Data",
        "desc": "语音数据，当SourceType 值为1（本地语音数据上传）时必须填写，当SourceType 值为0（语音 URL上传）可不写。要使用base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于600KB。"
      },
      {
        "name": "DataLen",
        "desc": "数据长度，单位为字节。当 SourceType 值为1（本地语音数据上传）时必须填写，当 SourceType 值为0（语音 URL上传）可不写（此数据长度为数据未进行base64编码时的数据长度）。"
      }
    ],
    "desc": "本接口用于对60秒之内的短音频文件进行识别，支持本地语音文件上传和语音URL上传两种请求方式。\n\n当音频文件通过请求中body内容上传时，请求大小不能超过600KB；当音频以url方式传输时，音频时长不可超过60s。\n\n所有请求参数放在POST请求的body中，编码类型采用x-www-form-urlencoded，参数进行urlencode编码后传输。\n\n现暂只支持中文普通话和带有一定方言口音的中文普通话识别，支持识别8k16bit和16k16bit的mp3或者wav格式的单声道音频。\n"
  }
}