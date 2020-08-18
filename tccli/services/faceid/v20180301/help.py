# -*- coding: utf-8 -*-
DESC = "faceid-2018-03-01"
INFO = {
  "GetDetectInfo": {
    "params": [
      {
        "name": "BizToken",
        "desc": "人脸核身流程的标识，调用DetectAuth接口时生成。"
      },
      {
        "name": "RuleId",
        "desc": "用于细分客户使用场景，申请开通服务后，可以在腾讯云慧眼人脸核身控制台（https://console.cloud.tencent.com/faceid） 自助接入里面创建，审核通过后即可调用。如有疑问，请加慧眼小助手微信（faceid001）进行咨询。"
      },
      {
        "name": "InfoType",
        "desc": "指定拉取的结果信息，取值（0：全部；1：文本类；2：身份证正反面；3：视频最佳截图照片；4：视频）。\n如 134表示拉取文本类、视频最佳截图照片、视频。\n默认值：0"
      }
    ],
    "desc": "完成验证后，用BizToken调用本接口获取结果信息，BizToken生成后三天内（3\\*24\\*3,600秒）可多次拉取。"
  },
  "MinorsVerification": {
    "params": [
      {
        "name": "Type",
        "desc": "参与校验的参数类型。\n0：使用手机号进行校验；\n1：使用姓名与身份证号进行校验。"
      },
      {
        "name": "Mobile",
        "desc": "手机号，11位数字，\n特别提示：\n手机号验证只限制在腾讯健康守护可信模型覆盖的数据范围内，与手机号本身在运营商是否实名无关联，不在范围会提示“手机号未实名”，建议客户与传入姓名和身份证号信息组合使用。"
      },
      {
        "name": "IdCard",
        "desc": "身份证号码。"
      },
      {
        "name": "Name",
        "desc": "姓名。"
      }
    ],
    "desc": "未成年人守护接口是通过传入手机号或姓名和身份证号，结合权威数据源和腾讯健康守护可信模型，判断该信息是否真实且年满18周岁。腾讯健康守护可信模型覆盖了上十亿手机库源，覆盖率高、准确率高，如果不在库中的手机号，还可以通过姓名+身份证进行兜底验证。"
  },
  "GetLiveCode": {
    "params": [],
    "desc": "使用数字活体检测模式前，需调用本接口获取数字验证码。"
  },
  "MobileNetworkTimeVerification": {
    "params": [
      {
        "name": "Mobile",
        "desc": "手机号码"
      }
    ],
    "desc": "本接口用于查询手机号在网时长，输入手机号进行查询。"
  },
  "GetActionSequence": {
    "params": [
      {
        "name": "ActionType",
        "desc": "默认不需要使用"
      }
    ],
    "desc": "使用动作活体检测模式前，需调用本接口获取动作顺序。"
  },
  "CheckIdCardInformation": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "身份证人像面的 Base64 值\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\nImageBase64、ImageUrl二者必须提供其中之一。若都提供了，则按照ImageUrl>ImageBase64的优先级使用参数。"
      },
      {
        "name": "ImageUrl",
        "desc": "身份证人像面的 Url 地址\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "Config",
        "desc": "以下可选字段均为bool 类型，默认false：\nCopyWarn，复印件告警\nBorderCheckWarn，边框和框内遮挡告警\nReshootWarn，翻拍告警\nDetectPsWarn，PS检测告警\nTempIdWarn，临时身份证告警\nQuality，图片质量告警（评价图片模糊程度）\n\nSDK 设置方式参考：\nConfig = Json.stringify({\"CopyWarn\":true,\"ReshootWarn\":true})\nAPI 3.0 Explorer 设置方式参考：\nConfig = {\"CopyWarn\":true,\"ReshootWarn\":true}"
      }
    ],
    "desc": "传入身份证人像面照片，识别身份证照片上的信息，并将姓名、身份证号、身份证人像照片与公安权威库的证件照进行比对，是否属于同一个人，从而验证身份证信息的真实性。"
  },
  "BankCardVerification": {
    "params": [
      {
        "name": "IdCard",
        "desc": "开户证件号，与CertType参数的证件类型一致，如：身份证，则传入身份证号。"
      },
      {
        "name": "Name",
        "desc": "姓名"
      },
      {
        "name": "BankCard",
        "desc": "银行卡"
      },
      {
        "name": "CertType",
        "desc": "证件类型，请确认该证件为开户时使用的证件类型，未用于开户的证件信息不支持验证。\n目前默认：0 身份证，其他证件类型需求可以联系小助手faceid001确认。"
      }
    ],
    "desc": "本接口用于银行卡号、姓名、开户证件号信息的真实性和一致性。"
  },
  "Liveness": {
    "params": [
      {
        "name": "VideoBase64",
        "desc": "用于活体检测的视频，视频的BASE64值；\nBASE64编码后的大小不超过8M，支持mp4、avi、flv格式。"
      },
      {
        "name": "LivenessType",
        "desc": "活体检测类型，取值：LIP/ACTION/SILENT。\nLIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。"
      },
      {
        "name": "ValidateData",
        "desc": "数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；\n动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；\n静默模式传参：不需要传递此参数。"
      },
      {
        "name": "Optional",
        "desc": "额外配置，传入JSON字符串。\n{\n\"BestFrameNum\": 2  //需要返回多张最佳截图，取值范围1-10\n}"
      }
    ],
    "desc": "活体检测"
  },
  "LivenessRecognition": {
    "params": [
      {
        "name": "IdCard",
        "desc": "身份证号"
      },
      {
        "name": "Name",
        "desc": "姓名。中文请使用UTF-8编码。"
      },
      {
        "name": "VideoBase64",
        "desc": "用于活体检测的视频，视频的BASE64值；\nBASE64编码后的大小不超过8M，支持mp4、avi、flv格式。"
      },
      {
        "name": "LivenessType",
        "desc": "活体检测类型，取值：LIP/ACTION/SILENT。\nLIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。"
      },
      {
        "name": "ValidateData",
        "desc": "数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；\n动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；\n静默模式传参：空。"
      },
      {
        "name": "Optional",
        "desc": "额外配置，传入JSON字符串。\n{\n\"BestFrameNum\": 2  //需要返回多张最佳截图，取值范围1-10\n}"
      }
    ],
    "desc": "传入视频和身份信息，先判断视频中是否为真人，判断为真人后，再判断该视频中的人与公安权威库的证件照是否属于同一个人。"
  },
  "MobileStatus": {
    "params": [
      {
        "name": "Mobile",
        "desc": "手机号码"
      }
    ],
    "desc": "本接口用于验证手机号的状态，您可以输入手机号进行查询。"
  },
  "IdCardVerification": {
    "params": [
      {
        "name": "IdCard",
        "desc": "身份证号"
      },
      {
        "name": "Name",
        "desc": "姓名"
      }
    ],
    "desc": "传入姓名和身份证号，校验两者的真实性和一致性。"
  },
  "IdCardOCRVerification": {
    "params": [
      {
        "name": "IdCard",
        "desc": "身份证号\n姓名和身份证号、ImageBase64、ImageUrl三者必须提供其中之一。若都提供了，则按照姓名和身份证号>ImageBase64>ImageUrl的优先级使用参数。"
      },
      {
        "name": "Name",
        "desc": "姓名"
      },
      {
        "name": "ImageBase64",
        "desc": "身份证人像面的 Base64 值\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。"
      },
      {
        "name": "ImageUrl",
        "desc": "身份证人像面的 Url 地址\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口用于校验姓名和身份证号的真实性和一致性，您可以通过输入姓名和身份证号或传入身份证人像面照片提供所需验证信息。"
  },
  "BankCard4EVerification": {
    "params": [
      {
        "name": "Name",
        "desc": "姓名"
      },
      {
        "name": "BankCard",
        "desc": "银行卡"
      },
      {
        "name": "Phone",
        "desc": "手机号码"
      },
      {
        "name": "IdCard",
        "desc": "开户证件号，与CertType参数的证件类型一致，如：身份证，则传入身份证号。"
      },
      {
        "name": "CertType",
        "desc": "证件类型，请确认该证件为开户时使用的证件类型，未用于开户的证件信息不支持验证。\n目前默认：0 身份证，其他证件类型需求可以联系小助手faceid001确认。"
      }
    ],
    "desc": "本接口用于输入银行卡号、姓名、开户证件号、开户手机号，校验信息的真实性和一致性。"
  },
  "DetectAuth": {
    "params": [
      {
        "name": "RuleId",
        "desc": "用于细分客户使用场景，申请开通服务后，可以在腾讯云慧眼人脸核身控制台（https://console.cloud.tencent.com/faceid） 自助接入里面创建，审核通过后即可调用。如有疑问，请加慧眼小助手微信（faceid001）进行咨询。"
      },
      {
        "name": "TerminalType",
        "desc": "本接口不需要传递此参数。"
      },
      {
        "name": "IdCard",
        "desc": "身份标识（未使用OCR服务时，必须传入）。\n规则：a-zA-Z0-9组合。最长长度32位。"
      },
      {
        "name": "Name",
        "desc": "姓名。（未使用OCR服务时，必须传入）最长长度32位。中文请使用UTF-8编码。"
      },
      {
        "name": "RedirectUrl",
        "desc": "认证结束后重定向的回调链接地址。最长长度1024位。"
      },
      {
        "name": "Extra",
        "desc": "透传字段，在获取验证结果时返回。"
      },
      {
        "name": "ImageBase64",
        "desc": "用于人脸比对的照片，图片的BASE64值；\nBASE64编码后的图片数据大小不超过3M，仅支持jpg、png格式。"
      }
    ],
    "desc": "每次调用人脸核身SaaS化服务前，需先调用本接口获取BizToken，用来串联核身流程，在验证完成后，用于获取验证结果信息。"
  },
  "ImageRecognition": {
    "params": [
      {
        "name": "IdCard",
        "desc": "身份证号"
      },
      {
        "name": "Name",
        "desc": "姓名。中文请使用UTF-8编码。"
      },
      {
        "name": "ImageBase64",
        "desc": "用于人脸比对的照片，图片的BASE64值；\nBASE64编码后的图片数据大小不超过3M，仅支持jpg、png格式。"
      },
      {
        "name": "Optional",
        "desc": "本接口不需要传递此参数。"
      }
    ],
    "desc": "传入照片和身份信息，判断该照片与公安权威库的证件照是否属于同一个人。"
  },
  "BankCard2EVerification": {
    "params": [
      {
        "name": "Name",
        "desc": "姓名"
      },
      {
        "name": "BankCard",
        "desc": "银行卡"
      }
    ],
    "desc": "本接口用于校验姓名和银行卡号的真实性和一致性。"
  },
  "GetDetectInfoEnhanced": {
    "params": [
      {
        "name": "BizToken",
        "desc": "人脸核身流程的标识，调用DetectAuth接口时生成。"
      },
      {
        "name": "RuleId",
        "desc": "用于细分客户使用场景，由腾讯侧在线下对接时分配。"
      },
      {
        "name": "InfoType",
        "desc": "指定拉取的结果信息，取值（0：全部；1：文本类；2：身份证信息；3：视频最佳截图信息；4：视频信息）。\n如 134表示拉取文本类、视频最佳截图信息、视频信息。\n默认值：0"
      },
      {
        "name": "BestFramesCount",
        "desc": "从活体视频中截取一定张数的最佳帧。默认为0，最大为10，超出10的最多只给10张。（InfoType需要包含3）"
      },
      {
        "name": "IsCutIdCardImage",
        "desc": "是否对身份证照片进行裁边。默认为false。（InfoType需要包含2）"
      },
      {
        "name": "IsNeedIdCardAvatar",
        "desc": "是否需要从身份证中抠出头像。默认为false。（InfoType需要包含2）"
      }
    ],
    "desc": "完成验证后，用BizToken调用本接口获取结果信息，BizToken生成后三天内（3\\*24\\*3,600秒）可多次拉取。"
  },
  "PhoneVerification": {
    "params": [
      {
        "name": "IdCard",
        "desc": "身份证号"
      },
      {
        "name": "Name",
        "desc": "姓名"
      },
      {
        "name": "Phone",
        "desc": "手机号"
      },
      {
        "name": "CiphertextBlob",
        "desc": "有加密需求的用户，接入传入kms的CiphertextBlob"
      },
      {
        "name": "EncryptList",
        "desc": "在使用加密服务时，填入要被加密的字段。本接口中可填入加密后的IdCard，Name，Phone中的一个或多个"
      }
    ],
    "desc": "本接口用于校验手机号、姓名和身份证号的真实性和一致性。"
  },
  "LivenessCompare": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "用于人脸比对的照片，图片的BASE64值；\nBASE64编码后的图片数据大小不超过3M，仅支持jpg、png格式。"
      },
      {
        "name": "VideoBase64",
        "desc": "用于活体检测的视频，视频的BASE64值；\nBASE64编码后的大小不超过8M，支持mp4、avi、flv格式。"
      },
      {
        "name": "LivenessType",
        "desc": "活体检测类型，取值：LIP/ACTION/SILENT。\nLIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。"
      },
      {
        "name": "ValidateData",
        "desc": "数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；\n动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；\n静默模式传参：空。"
      },
      {
        "name": "Optional",
        "desc": "额外配置，传入JSON字符串。\n{\n\"BestFrameNum\": 2  //需要返回多张最佳截图，取值范围1-10\n}"
      }
    ],
    "desc": "传入视频和照片，先判断视频中是否为真人，判断为真人后，再判断该视频中的人与上传照片是否属于同一个人。"
  }
}