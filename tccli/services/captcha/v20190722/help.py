# -*- coding: utf-8 -*-
DESC = "captcha-2019-07-22"
INFO = {
  "DescribeCaptchaResult": {
    "params": [
      {
        "name": "CaptchaType",
        "desc": "验证码类型，9：滑块验证码"
      },
      {
        "name": "Ticket",
        "desc": "验证码返回给用户的票据"
      },
      {
        "name": "UserIp",
        "desc": "用户操作来源的外网 IP"
      },
      {
        "name": "Randstr",
        "desc": "验证票据需要的随机字符串"
      },
      {
        "name": "CaptchaAppId",
        "desc": "验证码应用ID"
      },
      {
        "name": "AppSecretKey",
        "desc": "用于服务器端校验验证码票据的验证密钥，请妥善保密，请勿泄露给第三方"
      },
      {
        "name": "BusinessId",
        "desc": "业务 ID，网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据"
      },
      {
        "name": "SceneId",
        "desc": "场景 ID，网站或应用的业务下有多个场景使用此服务，通过此 ID 区分统计数据"
      },
      {
        "name": "MacAddress",
        "desc": "mac 地址或设备唯一标识"
      },
      {
        "name": "Imei",
        "desc": "手机设备号"
      }
    ],
    "desc": "核查验证码票据结果"
  }
}