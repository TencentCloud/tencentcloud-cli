# -*- coding: utf-8 -*-
DESC = "tms-2020-07-13"
INFO = {
  "AccountTipoffAccess": {
    "params": [
      {
        "name": "ReportedAccount",
        "desc": "被举报账号，长度低于 128 个字符"
      },
      {
        "name": "ReportedAccountType",
        "desc": "被举报账号类型(1-微信uin 2-QQ号 3-微信群uin 4-qq群号 5-微信openid 6-QQopenid 7-手机号 8-微信号 0-其它string)"
      },
      {
        "name": "EvilType",
        "desc": "被举报账号所属恶意类型(1-诈骗，2-骚扰，3-广告，4-违法违规，5-赌博传销，0-其他)"
      },
      {
        "name": "SenderAccount",
        "desc": "举报者账号，长度低于 128 个字符"
      },
      {
        "name": "SenderAccountType",
        "desc": "举报者账号类型(1-微信uin 2-QQ号 3-微信群uin 4-qq群号 5-微信openid 6-QQopenid 7-手机号 8-微信号 0-其它string)"
      },
      {
        "name": "SenderIP",
        "desc": "举报者IP地址"
      },
      {
        "name": "EvilContent",
        "desc": "包含被举报账号的恶意内容（比如文本、图片链接，长度低于1024个字符）"
      }
    ],
    "desc": "举报恶意账号"
  },
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