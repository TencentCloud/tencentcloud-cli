# -*- coding: utf-8 -*-
DESC = "tbp-2019-06-27"
INFO = {
  "TextReset": {
    "params": [
      {
        "name": "BotId",
        "desc": "机器人标识，用于定义抽象机器人。"
      },
      {
        "name": "BotEnv",
        "desc": "机器人版本，取值\"dev\"或\"release\"，{调试版本：dev；线上版本：release}。"
      },
      {
        "name": "TerminalId",
        "desc": "终端标识，每个终端(或线程)对应一个，区分并发多用户。"
      },
      {
        "name": "PlatformType",
        "desc": "平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount；企业微信: WXWork}。"
      },
      {
        "name": "PlatformId",
        "desc": "当PlatformType为微信公众号或企业微信时，传递对应微信公众号或企业微信的唯一标识"
      }
    ],
    "desc": "会话重置接口。"
  },
  "TextProcess": {
    "params": [
      {
        "name": "BotId",
        "desc": "机器人标识，用于定义抽象机器人。"
      },
      {
        "name": "BotEnv",
        "desc": "机器人版本，取值\"dev\"或\"release\"，{调试版本：dev；线上版本：release}。"
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
        "name": "SessionAttributes",
        "desc": "透传字段，透传给用户自定义的WebService服务。"
      },
      {
        "name": "PlatformType",
        "desc": "平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount；企业微信: WXWork}。"
      },
      {
        "name": "PlatformId",
        "desc": "当PlatformType为微信公众号或企业微信时，传递对应微信公众号或企业微信的唯一标识"
      }
    ],
    "desc": "接收调用侧的文本输入，返回应答文本。"
  }
}