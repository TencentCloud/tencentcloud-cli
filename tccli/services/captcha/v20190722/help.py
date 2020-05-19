# -*- coding: utf-8 -*-
DESC = "captcha-2019-07-22"
INFO = {
  "DescribeCaptchaData": {
    "params": [
      {
        "name": "CaptchaAppId",
        "desc": "验证码应用ID"
      },
      {
        "name": "Start",
        "desc": "查询开始时间"
      },
      {
        "name": "End",
        "desc": "查询结束时间"
      },
      {
        "name": "Type",
        "desc": "查询类型"
      }
    ],
    "desc": "安全验证码分类查询数据接口，请求量type=0、验证量type=1、通过量type=2、拦截量type=3  分钟级查询"
  },
  "DescribeCaptchaDataSum": {
    "params": [
      {
        "name": "CaptchaAppId",
        "desc": "验证码应用ID"
      },
      {
        "name": "Start",
        "desc": "查询开始时间"
      },
      {
        "name": "End",
        "desc": "查询结束时间"
      }
    ],
    "desc": "安全验证码查询请求数据概况，例如：按照时间段查询数据  昨日请求量、昨日恶意比例、昨日验证量、昨日通过量、昨日恶意拦截量……"
  },
  "DescribeCaptchaOperData": {
    "params": [
      {
        "name": "CaptchaAppId",
        "desc": "验证码应用ID"
      },
      {
        "name": "Start",
        "desc": "查询开始时间"
      },
      {
        "name": "Type",
        "desc": "查询类型"
      }
    ],
    "desc": "安全验证码用户操作数据查询，验证码加载耗时type = 1 、拦截情况type = 2、 一周通过平均尝试次数 type = 3、尝试次数分布 type = 4"
  },
  "DescribeCaptchaAppIdInfo": {
    "params": [
      {
        "name": "CaptchaAppId",
        "desc": "验证码应用注册APPID"
      }
    ],
    "desc": "查询安全验证码应用APPId信息"
  },
  "DescribeCaptchaUserAllAppId": {
    "params": [],
    "desc": "安全验证码获取用户注册所有APPId和应用名称"
  },
  "UpdateCaptchaAppIdInfo": {
    "params": [
      {
        "name": "CaptchaAppId",
        "desc": "验证码应用ID"
      },
      {
        "name": "AppName",
        "desc": "应用名"
      },
      {
        "name": "DomainLimit",
        "desc": "域名限制"
      },
      {
        "name": "SceneType",
        "desc": "场景类型"
      },
      {
        "name": "CapType",
        "desc": "验证码类型"
      },
      {
        "name": "EvilInterceptGrade",
        "desc": "风险级别"
      },
      {
        "name": "SmartVerify",
        "desc": "智能检测"
      },
      {
        "name": "SmartEngine",
        "desc": "开启智能引擎"
      },
      {
        "name": "SchemeColor",
        "desc": "web风格"
      },
      {
        "name": "CaptchaLanguage",
        "desc": "语言"
      },
      {
        "name": "MailAlarm",
        "desc": "告警邮箱"
      },
      {
        "name": "TopFullScreen",
        "desc": "是否全屏"
      },
      {
        "name": "TrafficThreshold",
        "desc": "流量限制"
      }
    ],
    "desc": "更新验证码应用APPId信息"
  },
  "DescribeCaptchaResult": {
    "params": [
      {
        "name": "CaptchaType",
        "desc": "固定填值：9。可在控制台配置不同验证码类型。"
      },
      {
        "name": "Ticket",
        "desc": "前端回调函数返回的用户验证票据"
      },
      {
        "name": "UserIp",
        "desc": "用户操作来源的外网 IP"
      },
      {
        "name": "Randstr",
        "desc": "前端回调函数返回的随机字符串"
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
      },
      {
        "name": "NeedGetCaptchaTime",
        "desc": "是否返回前端获取验证码时间，取值1：需要返回"
      }
    ],
    "desc": "核查验证码票据结果"
  }
}