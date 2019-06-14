# -*- coding: utf-8 -*-
DESC = "tbp-2019-03-11"
INFO = {
  "Reset": {
    "params": [
      {
        "name": "BotId",
        "desc": "机器人标识"
      },
      {
        "name": "UserId",
        "desc": "子账户id，每个终端对应一个"
      },
      {
        "name": "BotVersion",
        "desc": "机器人版本号。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev"
      },
      {
        "name": "BotEnv",
        "desc": "机器人环境{dev:测试;release:线上}。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev"
      }
    ],
    "desc": "对当前机器人的会话状态进行复位"
  },
  "PostText": {
    "params": [
      {
        "name": "BotId",
        "desc": "机器人标识"
      },
      {
        "name": "InputText",
        "desc": "请求的文本"
      },
      {
        "name": "UserId",
        "desc": "子账户id，每个终端对应一个"
      },
      {
        "name": "BotVersion",
        "desc": "机器人版本号。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev"
      },
      {
        "name": "SessionAttributes",
        "desc": "透传字段，传递给后台"
      },
      {
        "name": "NeedTts",
        "desc": "是否将机器人回答合成音频并返回url"
      },
      {
        "name": "Volume",
        "desc": "音量大小，范围：[0，10]。默认值为0，代表正常音量"
      },
      {
        "name": "Speed",
        "desc": "语速，范围：[-2，2]。0代表1.0倍"
      },
      {
        "name": "VoiceType",
        "desc": "音色,{0：女声,1:男声}"
      },
      {
        "name": "SampleRate",
        "desc": "返回音频的采样率{8k,16k}。默认16k"
      },
      {
        "name": "BotEnv",
        "desc": "机器人环境{dev:测试;release:线上}。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev"
      },
      {
        "name": "TtsVoiceFormat",
        "desc": "TTS合成音频格式，{0：wav}。该字段在当前版本仅支持取值为0。"
      }
    ],
    "desc": "机器人会话接口，接收文本信息，传递给后台机器人"
  }
}