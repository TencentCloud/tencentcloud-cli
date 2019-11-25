# -*- coding: utf-8 -*-
DESC = "sms-2019-07-11"
INFO = {
  "PullSmsSendStatus": {
    "params": [
      {
        "name": "Limit",
        "desc": "拉取最大条数，最多100条"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在[短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid,示例如1400006666。"
      }
    ],
    "desc": "拉取短信下发状态"
  },
  "SendSms": {
    "params": [
      {
        "name": "PhoneNumberSet",
        "desc": "下发手机号码，采用 e.164 标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。最多不要超过200个手机号。"
      },
      {
        "name": "TemplateID",
        "desc": "模板 ID，必须填写已审核通过的模板 ID。模板ID可登录[短信控制台](https://console.cloud.tencent.com/sms/smslist)查看。"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在[短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid,示例如1400006666。"
      },
      {
        "name": "Sign",
        "desc": "短信签名内容，使用 UTF-8 编码，必须填写已审核通过的签名\n签名信息可登录[短信控制台](https://console.cloud.tencent.com/sms/smslist) 查看。"
      },
      {
        "name": "TemplateParamSet",
        "desc": "模板参数，若无模板参数，则设置为空。"
      },
      {
        "name": "ExtendCode",
        "desc": "短信码号扩展号，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)"
      },
      {
        "name": "SessionContext",
        "desc": "用户的 session 内容，可以携带用户侧ID等上下文信息,server 会原样返回"
      },
      {
        "name": "SenderId",
        "desc": "国际/港澳台短信senderid，国内短信填空。\n默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)"
      }
    ],
    "desc": "短信发送接口，用户给用户发短信验证码、通知类短信或营销短信。\n\n"
  },
  "SmsPackagesStatistics": {
    "params": [
      {
        "name": "Limit",
        "desc": "最大上限\n注：目前固定设置为0"
      },
      {
        "name": "Offset",
        "desc": "偏移量\n注：目前固定设置为0"
      },
      {
        "name": "NumberOfPullPackages",
        "desc": "需要拉取的套餐包个数"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在[短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid,示例如1400006666。"
      }
    ],
    "desc": "用户套餐包信息统计"
  },
  "SendStatusStatistics": {
    "params": [
      {
        "name": "Limit",
        "desc": "最大上限\n注：目前固定设置为0"
      },
      {
        "name": "Offset",
        "desc": "偏移量\n注：目前固定设置为0"
      },
      {
        "name": "StartDateTime",
        "desc": "拉取起始时间，yyyymmddhh 需要拉取的起始时间，精确到小时"
      },
      {
        "name": "EndDataTime",
        "desc": "结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时\n注：EndDataTime 必须大于StartDateTime"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在[短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid,示例如1400006666。"
      }
    ],
    "desc": "统计用户发送短信的数据"
  },
  "CallbackStatusStatistics": {
    "params": [
      {
        "name": "Limit",
        "desc": "最大上限\n注：目前固定设置为0"
      },
      {
        "name": "Offset",
        "desc": "偏移量\n注：目前固定设置为0"
      },
      {
        "name": "StartDateTime",
        "desc": "开始时间，yyyymmddhh 需要拉取的起始时间，精确到小时"
      },
      {
        "name": "EndDataTime",
        "desc": "结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时\n注：EndDataTime 必须大于StartDateTime"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在[短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid,示例如1400006666。"
      }
    ],
    "desc": "统计用户回执的数据"
  },
  "PullSmsReplyStatus": {
    "params": [
      {
        "name": "Limit",
        "desc": "拉取最大条数，最多100条"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在[短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid,示例如1400006666。"
      }
    ],
    "desc": "拉取短信回复状态"
  },
  "PullSmsSendStatusByPhoneNumber": {
    "params": [
      {
        "name": "SendDateTime",
        "desc": "拉取起始时间，UNIX 时间戳（时间：秒）"
      },
      {
        "name": "Offset",
        "desc": "偏移量\n注：目前固定设置为0"
      },
      {
        "name": "Limit",
        "desc": "拉取最大条数，最多 100"
      },
      {
        "name": "PhoneNumber",
        "desc": "下发目的手机号码，依据 e.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在[短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid,示例如1400006666。"
      }
    ],
    "desc": "拉取单个号码短信下发状态"
  },
  "PullSmsReplyStatusByPhoneNumber": {
    "params": [
      {
        "name": "SendDateTime",
        "desc": "拉取起始时间，UNIX 时间戳（时间：秒）"
      },
      {
        "name": "Offset",
        "desc": "偏移量\n注：目前固定设置为0"
      },
      {
        "name": "Limit",
        "desc": "拉取最大条数，最多 100"
      },
      {
        "name": "PhoneNumber",
        "desc": "下发目的手机号码，依据 e.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。"
      },
      {
        "name": "SmsSdkAppid",
        "desc": "短信SdkAppid在[短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid,示例如1400006666。"
      }
    ],
    "desc": "拉取单个号码短信回复状态"
  }
}