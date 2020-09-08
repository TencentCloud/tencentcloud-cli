# -*- coding: utf-8 -*-
DESC = "af-2020-02-26"
INFO = {
  "QueryAntiFraud": {
    "params": [
      {
        "name": "PhoneNumber",
        "desc": "电话号码(五选二)"
      },
      {
        "name": "IdNumber",
        "desc": "Id(五选二)"
      },
      {
        "name": "BankCardNumber",
        "desc": "银行卡号(五选二)"
      },
      {
        "name": "UserIp",
        "desc": "用户请求来源 IP(五选二)"
      },
      {
        "name": "Imei",
        "desc": "国际移动设备识别码(五选二)"
      },
      {
        "name": "Idfa",
        "desc": "ios 系统广告标示符(五选二)"
      },
      {
        "name": "Scene",
        "desc": "业务场景 ID，需要找技术对接"
      },
      {
        "name": "Name",
        "desc": "姓名"
      },
      {
        "name": "EmailAddress",
        "desc": "用户邮箱地址"
      },
      {
        "name": "Address",
        "desc": "用户住址"
      },
      {
        "name": "Mac",
        "desc": "MAC 地址"
      },
      {
        "name": "Imsi",
        "desc": "国际移动用户识别码"
      },
      {
        "name": "AccountType",
        "desc": "关联的腾讯帐号 QQ：1；\n开放帐号微信： 2；"
      },
      {
        "name": "Uid",
        "desc": "可选的 QQ 或微信 openid"
      },
      {
        "name": "AppIdU",
        "desc": "qq 或微信分配给网站或应用的 appid，用来\n唯一标识网站或应用"
      },
      {
        "name": "WifiMac",
        "desc": "WIFI MAC"
      },
      {
        "name": "WifiSSID",
        "desc": "WIFI 服务集标识"
      },
      {
        "name": "WifiBSSID",
        "desc": "WIFI-BSSID"
      },
      {
        "name": "BusinessId",
        "desc": "业务 ID，在多个业务中使用此服务，通过此\nID 区分统计数据"
      },
      {
        "name": "IdCryptoType",
        "desc": "Id加密类型\n0：不加密（默认值）\n1：md5\n2：sha256\n3：SM3"
      },
      {
        "name": "PhoneCryptoType",
        "desc": "手机号加密类型\n0：不加密（默认值）\n1：md5, 2：sha256\n3：SM3"
      },
      {
        "name": "NameCryptoType",
        "desc": "姓名加密类型\n0：不加密（默认值）\n1：md5\n2：sha256\n3：SM3"
      }
    ],
    "desc": "天御反欺诈服务，主要应用于银行、证券、保险、P2P等金融行业客户，通过腾讯的大数据风控能力，\n可以准确识别恶意用户信息，解决客户在支付、活动、理财，风控等业务环节遇到的欺诈威胁，降低企业\n的损失。"
  }
}