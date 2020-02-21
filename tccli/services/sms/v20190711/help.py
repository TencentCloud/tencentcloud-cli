# -*- coding: utf-8 -*-
DESC = "sms-2019-07-11"
INFO = {
  "ModifySmsSign": {
    "params": [
      {
        "name": "SignId",
        "desc": "待修改的签名 ID。"
      },
      {
        "name": "SignName",
        "desc": "签名名称。"
      },
      {
        "name": "SignType",
        "desc": "签名类型。其中每种类型后面标注了其可选的 DocumentType（证明类型）：\n0：公司（0，1，2，3）。\n1：APP（0，1，2，3，4） 。\n2：网站（0，1，2，3，5）。\n3：公众号或者小程序（0，1，2，3，6）。\n4：商标（7）。\n5：政府/机关事业单位/其他机构（2，3）。\n注：必须按照对应关系选择证明类型，否则会审核失败。"
      },
      {
        "name": "DocumentType",
        "desc": "证明类型：\n0：三证合一。\n1：企业营业执照。\n2：组织机构代码证书。\n3：社会信用代码证书。\n4：应用后台管理截图(个人开发APP)。\n5：网站备案后台截图(个人开发网站)。\n6：小程序设置页面截图(个人认证小程序)。\n7：商标注册书。"
      },
      {
        "name": "International",
        "desc": "是否国际/港澳台短信：\n0：表示国内短信。\n1：表示国际/港澳台短信。"
      },
      {
        "name": "UsedMethod",
        "desc": "签名用途：\n0：自用。\n1：他用。"
      },
      {
        "name": "ProofImage",
        "desc": "签名对应的资质证明图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。"
      },
      {
        "name": "CommissionImage",
        "desc": "委托授权证明。选择 UsedMethod 为他用之后需要提交委托的授权证明。\n图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。\n注：只有 UsedMethod 在选择为 1（他用）时，这个字段才会生效。"
      },
      {
        "name": "Remark",
        "desc": "签名的申请备注。"
      }
    ],
    "desc": "修改短信签名"
  },
  "AddSmsSign": {
    "params": [
      {
        "name": "SignName",
        "desc": "签名名称。"
      },
      {
        "name": "SignType",
        "desc": "签名类型。其中每种类型后面标注了其可选的 DocumentType（证明类型）：\n0：公司（0，1，2，3）。\n1：APP（0，1，2，3，4） 。\n2：网站（0，1，2，3，5）。\n3：公众号或者小程序（0，1，2，3，6）。\n4：商标（7）。\n5：政府/机关事业单位/其他机构（2，3）。\n注：必须按照对应关系选择证明类型，否则会审核失败。"
      },
      {
        "name": "DocumentType",
        "desc": "证明类型：\n0：三证合一。\n1：企业营业执照。\n2：组织机构代码证书。\n3：社会信用代码证书。\n4：应用后台管理截图（个人开发APP）。\n5：网站备案后台截图（个人开发网站）。\n6：小程序设置页面截图（个人认证小程序）。\n7：商标注册书。"
      },
      {
        "name": "International",
        "desc": "是否国际/港澳台短信：\n0：表示国内短信。\n1：表示国际/港澳台短信。"
      },
      {
        "name": "UsedMethod",
        "desc": "签名用途：\n0：自用。\n1：他用。"
      },
      {
        "name": "ProofImage",
        "desc": "签名对应的资质证明图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。"
      },
      {
        "name": "CommissionImage",
        "desc": "委托授权证明。选择 UsedMethod 为他用之后需要提交委托的授权证明。\n图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。\n注：只有 UsedMethod 在选择为 1（他用）时，这个字段才会生效。"
      },
      {
        "name": "Remark",
        "desc": "签名的申请备注。"
      }
    ],
    "desc": "添加短信签名"
  },
  "PullSmsSendStatus": {
    "params": [
      {
        "name": "Limit",
        "desc": "拉取最大条数，最多100条。"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid，示例如1400006666。"
      }
    ],
    "desc": "拉取短信下发状态。"
  },
  "SendSms": {
    "params": [
      {
        "name": "PhoneNumberSet",
        "desc": "下发手机号码，采用 e.164 标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号。"
      },
      {
        "name": "TemplateID",
        "desc": "模板 ID，必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 查看。"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist)  添加应用后生成的实际SdkAppid，示例如1400006666。"
      },
      {
        "name": "Sign",
        "desc": "短信签名内容，使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台](https://console.cloud.tencent.com/sms/smslist)  查看。注：国内短信为必填参数。"
      },
      {
        "name": "TemplateParamSet",
        "desc": "模板参数，若无模板参数，则设置为空。"
      },
      {
        "name": "ExtendCode",
        "desc": "短信码号扩展号，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)。"
      },
      {
        "name": "SessionContext",
        "desc": "用户的 session 内容，可以携带用户侧 ID 等上下文信息，server 会原样返回。"
      },
      {
        "name": "SenderId",
        "desc": "国际/港澳台短信 senderid，国内短信填空，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)。"
      }
    ],
    "desc": "短信发送接口，用户给用户发短信验证码、通知类短信或营销短信。\n\n"
  },
  "DeleteSmsTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "待删除的模板 ID。"
      }
    ],
    "desc": "删除短信模板"
  },
  "SmsPackagesStatistics": {
    "params": [
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid，示例如1400006666。"
      },
      {
        "name": "Limit",
        "desc": "最大上限(需要拉取的套餐包个数)。"
      },
      {
        "name": "Offset",
        "desc": "偏移量。\n注：目前固定设置为0。"
      }
    ],
    "desc": "用户套餐包信息统计。"
  },
  "SendStatusStatistics": {
    "params": [
      {
        "name": "StartDateTime",
        "desc": "拉取起始时间，yyyymmddhh 需要拉取的起始时间，精确到小时。"
      },
      {
        "name": "EndDataTime",
        "desc": "结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时\n注：EndDataTime 必须大于 StartDateTime。"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid，示例如1400006666。"
      },
      {
        "name": "Limit",
        "desc": "最大上限。\n注：目前固定设置为0。"
      },
      {
        "name": "Offset",
        "desc": "偏移量。\n注：目前固定设置为0。"
      }
    ],
    "desc": "统计用户发送短信的数据。"
  },
  "CallbackStatusStatistics": {
    "params": [
      {
        "name": "StartDateTime",
        "desc": "开始时间，yyyymmddhh 需要拉取的起始时间，精确到小时。"
      },
      {
        "name": "EndDataTime",
        "desc": "结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时。\n注：EndDataTime 必须大于 StartDateTime。"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid，示例如1400006666。"
      },
      {
        "name": "Limit",
        "desc": "最大上限。\n注：目前固定设置为0。"
      },
      {
        "name": "Offset",
        "desc": "偏移量。\n注：目前固定设置为0。"
      }
    ],
    "desc": "统计用户回执的数据。"
  },
  "PullSmsReplyStatus": {
    "params": [
      {
        "name": "Limit",
        "desc": "拉取最大条数，最多100条。"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid,示例如1400006666。"
      }
    ],
    "desc": "拉取短信回复状态。"
  },
  "PullSmsSendStatusByPhoneNumber": {
    "params": [
      {
        "name": "SendDateTime",
        "desc": "拉取起始时间，UNIX 时间戳（时间：秒）。"
      },
      {
        "name": "Offset",
        "desc": "偏移量。\n注：目前固定设置为0。"
      },
      {
        "name": "Limit",
        "desc": "拉取最大条数，最多 100。"
      },
      {
        "name": "PhoneNumber",
        "desc": "下发目的手机号码，依据 e.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid，示例如1400006666。"
      }
    ],
    "desc": "拉取单个号码短信下发状态。"
  },
  "ModifySmsTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "待修改的模板的模板 ID。"
      },
      {
        "name": "TemplateName",
        "desc": "新的模板名称。"
      },
      {
        "name": "TemplateContent",
        "desc": "新的模板内容。"
      },
      {
        "name": "SmsType",
        "desc": "短信类型，0表示普通短信, 1表示营销短信。"
      },
      {
        "name": "International",
        "desc": "是否国际/港澳台短信：\n0：表示国内短信。\n1：表示国际/港澳台短信。"
      },
      {
        "name": "Remark",
        "desc": "模板备注，例如申请原因，使用场景等。"
      }
    ],
    "desc": "修改短信模板"
  },
  "PullSmsReplyStatusByPhoneNumber": {
    "params": [
      {
        "name": "SendDateTime",
        "desc": "拉取起始时间，UNIX 时间戳（时间：秒）。"
      },
      {
        "name": "Offset",
        "desc": "偏移量。\n注：目前固定设置为0。"
      },
      {
        "name": "Limit",
        "desc": "拉取最大条数，最多 100。"
      },
      {
        "name": "PhoneNumber",
        "desc": "下发目的手机号码，依据 e.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid，示例如1400006666。"
      }
    ],
    "desc": "拉取单个号码短信回复状态。"
  },
  "DeleteSmsSign": {
    "params": [
      {
        "name": "SignId",
        "desc": "待删除的签名 ID。"
      }
    ],
    "desc": "删除短信签名"
  },
  "AddSmsTemplate": {
    "params": [
      {
        "name": "TemplateName",
        "desc": "模板名称。"
      },
      {
        "name": "TemplateContent",
        "desc": "模板内容。"
      },
      {
        "name": "SmsType",
        "desc": "短信类型，0表示普通短信, 1表示营销短信。"
      },
      {
        "name": "International",
        "desc": "是否国际/港澳台短信：\n0：表示国内短信。\n1：表示国际/港澳台短信。"
      },
      {
        "name": "Remark",
        "desc": "模板备注，例如申请原因，使用场景等。"
      }
    ],
    "desc": "添加短信模板"
  }
}