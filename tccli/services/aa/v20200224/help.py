# -*- coding: utf-8 -*-
DESC = "aa-2020-02-24"
INFO = {
  "QueryActivityAntiRush": {
    "params": [
      {
        "name": "AccountType",
        "desc": "用户账号类型（默认开通 QQ 开放账号、手机号，手机 MD5 账号类型查询。如需使用微信开放账号，则需要 提交工单 由腾讯云进行资格审核，审核通过后方可正常使用微信开放账号）：\n1：QQ 开放帐号。\n2：微信开放账号。\n4：手机号。\n0：其他。\n10004：手机号 MD5。"
      },
      {
        "name": "Uid",
        "desc": "用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。"
      },
      {
        "name": "UserIp",
        "desc": "用户的真实外网 IP。若填入非外网有效ip，会返回level=0的风控结果，risktype中会有205的风险码返回作为标识"
      },
      {
        "name": "PostTime",
        "desc": "用户操作时间戳。"
      },
      {
        "name": "AppIdU",
        "desc": "accountType 是QQ开放账号时，该参数必填，表示 QQ 开放平台分配给网站或应用的 AppID，用来唯一标识网站或应用。"
      },
      {
        "name": "NickName",
        "desc": "昵称，UTF-8 编码。"
      },
      {
        "name": "PhoneNumber",
        "desc": "手机号。若 accountType 选4（手机号）、或10004（手机号 MD5），则无需重复填写。否则填入对应的手机号（如15912345687）。accountType为1或2时，该字段支持MD5值；"
      },
      {
        "name": "EmailAddress",
        "desc": "用户邮箱地址。"
      },
      {
        "name": "RegisterTime",
        "desc": "注册时间戳。"
      },
      {
        "name": "RegisterIp",
        "desc": "注册来源的外网 IP。"
      },
      {
        "name": "CookieHash",
        "desc": "用户 HTTP 请求中的 cookie 进行2次 hash 的值，只要保证相同 cookie 的 hash 值一致即可。"
      },
      {
        "name": "Address",
        "desc": "地址。"
      },
      {
        "name": "LoginSource",
        "desc": "登录来源：\n0：其他。\n1：PC 网页。\n2：移动页面。\n3：App。\n4：微信公众号。"
      },
      {
        "name": "LoginType",
        "desc": "登录方式：\n0：其他。\n1：手动账号密码输入。\n2：动态短信密码登录。\n3：二维码扫描登录。"
      },
      {
        "name": "LoginSpend",
        "desc": "登录耗时，单位：秒。"
      },
      {
        "name": "RootId",
        "desc": "用户操作的目的 ID，如点赞等，该字段就是被点赞的消息 ID，如果是投票，则为被投号码的 ID。"
      },
      {
        "name": "Referer",
        "desc": "用户 HTTP 请求的 referer 值。"
      },
      {
        "name": "JumpUrl",
        "desc": "登录成功后跳转页面。"
      },
      {
        "name": "UserAgent",
        "desc": "用户 HTTP 请求的 userAgent。"
      },
      {
        "name": "XForwardedFor",
        "desc": "用户 HTTP 请求中的 x_forward_for。"
      },
      {
        "name": "MouseClickCount",
        "desc": "用户操作过程中鼠标单击次数。"
      },
      {
        "name": "KeyboardClickCount",
        "desc": "用户操作过程中键盘单击次数。"
      },
      {
        "name": "MacAddress",
        "desc": "MAC 地址或设备唯一标识。"
      },
      {
        "name": "VendorId",
        "desc": "手机制造商 ID，如果手机注册，请带上此信息。"
      },
      {
        "name": "Imei",
        "desc": "手机设备号。支持以下格式：\n1.imei明文\n2.idfa明文,\n3.imei小写后MD5值小写\n4.idfa大写后MD5值小写"
      },
      {
        "name": "AppVersion",
        "desc": "App 客户端版本。"
      },
      {
        "name": "BusinessId",
        "desc": "业务 ID 网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据。"
      },
      {
        "name": "WxSubType",
        "desc": "1：微信公众号。\n2：微信小程序。"
      },
      {
        "name": "RandNum",
        "desc": "Token 签名随机数，WxSubType为微信小程序时必填，建议16个字符。"
      },
      {
        "name": "WxToken",
        "desc": "如果 accountType为2而且wxSubType有填，该字段必选，否则不需要填写；\n如果是微信小程序（WxSubType=2），该字段为以ssesion_key为key去签名随机数radnNum得到的值（ hmac_sha256签名算法）；如果是微信公众号或第三方登录，则为授权的access_token（网页版本的access_Token,而且获取token的scope字段必需填写snsapi_userinfo；）"
      },
      {
        "name": "CheckDevice",
        "desc": "是否识别设备异常：\n0：不识别。\n1：识别。"
      }
    ],
    "desc": "腾讯云活动防刷（ActivityAntiRush，AA）是针对电商、O2O、P2P、游戏、支付等行业在促销活动中遇到“羊毛党”恶意刷取优惠福利的行为时，通过防刷引擎，精准识别出“薅羊毛”恶意行为的活动防刷服务，避免了企业被刷带来的巨大经济损失。"
  }
}