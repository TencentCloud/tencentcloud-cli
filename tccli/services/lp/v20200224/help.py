# -*- coding: utf-8 -*-
DESC = "lp-2020-02-24"
INFO = {
  "QueryLoginProtection": {
    "params": [
      {
        "name": "LoginIp",
        "desc": "登录来源的外网 IP。"
      },
      {
        "name": "Uid",
        "desc": "用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。"
      },
      {
        "name": "LoginTime",
        "desc": "登录时间戳，单位：秒。"
      },
      {
        "name": "AccountType",
        "desc": "用户账号类型（QQ 开放帐号、微信开放账号需要 提交工单 由腾讯云进行资格审核）：\n1：QQ 开放帐号。\n2：微信开放账号。\n4：手机号。\n0：其他。\n10004：手机号 MD5。"
      },
      {
        "name": "AppIdU",
        "desc": "accountType 是 QQ 或微信开放账号时，该参数必填，表示 QQ 或微信分配给网站或应用的 AppID，用来唯一标识网站或应用。"
      },
      {
        "name": "AssociateAccount",
        "desc": "accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID。"
      },
      {
        "name": "NickName",
        "desc": "昵称，UTF-8 编码。"
      },
      {
        "name": "PhoneNumber",
        "desc": "手机号：国家代码-手机号， 如0086-15912345687（0086前不需要+号）。"
      },
      {
        "name": "EmailAddress",
        "desc": "用户邮箱地址（非系统自动生成）。"
      },
      {
        "name": "RegisterTime",
        "desc": "注册来源的外网 IP。"
      },
      {
        "name": "Address",
        "desc": "地址。"
      },
      {
        "name": "CookieHash",
        "desc": "用户 HTTP 请求中的 cookie 进行2次 hash 的值，只要保证相同 cookie 的 hash 值一致即可。"
      },
      {
        "name": "LoginSource",
        "desc": "登录来源：\n0：其他\n1：PC 网页\n2：移动页面\n3：App\n4：微信公众号"
      },
      {
        "name": "LoginType",
        "desc": "登录方式：\n0：其他\n1：手动帐号密码输入\n2：动态短信密码登录\n3：二维码扫描登录"
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
        "name": "Result",
        "desc": "注册结果：\n0：失败\n1：成功"
      },
      {
        "name": "Reason",
        "desc": "失败原因：\n0：其他\n1：参数错误\n2：帐号冲突\n3：验证错误"
      },
      {
        "name": "LoginSpend",
        "desc": "登录耗时，单位：秒。"
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
        "name": "AppVersion",
        "desc": "App 客户端版本。"
      },
      {
        "name": "Imei",
        "desc": "手机设备号。"
      },
      {
        "name": "BusinessId",
        "desc": "业务 ID 网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据。"
      },
      {
        "name": "WxSubType",
        "desc": "1：微信公众号\n2：微信小程序"
      },
      {
        "name": "RandNum",
        "desc": "Token 签名随机数，微信小程序必填，建议16个字符。"
      },
      {
        "name": "WxToken",
        "desc": "如果是微信小程序，该字段为以 ssesion_key 为 key 去签名随机数radnNum得到的值（hmac_sha256 签名算法）。\n如果是微信公众号或第三方登录，则为授权的 access_token（注意：不是普通 access_token，具体看 微信官方文档）。"
      }
    ],
    "desc": "登录保护服务（LoginProtection，LP）针对网站和 APP 的用户登录场景，实时检测是否存在盗号、撞库等恶意登录行为，帮助开发者发现异常登录，降低恶意用户登录给业务带来的风险。"
  }
}