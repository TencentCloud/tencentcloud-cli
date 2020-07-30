# -*- coding: utf-8 -*-
DESC = "tms-2020-07-13"
INFO = {
  "TextModeration": {
    "params": [
      {
        "name": "Content",
        "desc": "文本内容Base64编码。原文长度需小于15000字节，即5000个汉字以内。"
      },
      {
        "name": "DataId",
        "desc": "数据ID，英文字母、下划线、-组成，不超过64个字符"
      },
      {
        "name": "BizType",
        "desc": "该字段用于标识业务场景。您可以在内容安全控制台创建对应的ID，配置不同的内容审核策略，通过接口调用，默认不填为0，后端使用默认策略。 -- 该字段暂未开放。"
      },
      {
        "name": "User",
        "desc": "用户相关信息"
      },
      {
        "name": "Device",
        "desc": "设备相关信息"
      }
    ],
    "desc": "文本内容检测（Text Moderation）服务使用了深度学习技术，识别涉黄、涉政、涉恐等有害内容，同时支持用户配置词库，打击自定义的违规文本。"
  }
}