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
  "CreateBot": {
    "params": [
      {
        "name": "BotName",
        "desc": "机器人名称"
      },
      {
        "name": "BotCnName",
        "desc": "机器人中文名称"
      }
    ],
    "desc": "创建机器人"
  },
  "TextReset": {
    "params": [
      {
        "name": "BotId",
        "desc": "机器人标识，用于定义抽象机器人。"
      },
      {
        "name": "TerminalId",
        "desc": "终端标识，每个终端(或线程)对应一个，区分并发多用户。"
      },
      {
        "name": "BotEnv",
        "desc": "机器人版本，取值\"dev\"或\"release\"，{调试版本：dev；线上版本：release}。"
      }
    ],
    "desc": "会话重置接口。已废弃，推荐使用最新版TextReset接口。"
  },
  "TextProcess": {
    "params": [
      {
        "name": "BotId",
        "desc": "机器人标识，用于定义抽象机器人。"
      },
      {
        "name": "TerminalId",
        "desc": "终端标识，每个终端(或线程)对应一个，区分并发多用户。"
      },
      {
        "name": "InputText",
        "desc": "请求的文本。"
      },
      {
        "name": "BotEnv",
        "desc": "机器人版本，取值\"dev\"或\"release\"，{调试版本：dev；线上版本：release}。"
      },
      {
        "name": "SessionAttributes",
        "desc": "透传字段，透传给用户自定义的WebService服务。"
      }
    ],
    "desc": "接收调用侧的文本输入，返回应答文本。已废弃，推荐使用最新版TextProcess接口。"
  }
}