# -*- coding: utf-8 -*-
DESC = "ocr-2018-11-19"
INFO = {
  "BusinessCardOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "Config",
        "desc": "可选字段，根据需要选择是否请求对应字段。\n目前支持的字段为：\nRetImageType-“PROPROCESS” 图像预处理，string 类型。\n图像预处理功能为，检测图片倾斜的角度，将原本倾斜的图片围绕中心点转正，最终输出一张正的名片抠图。\n\nSDK 设置方式参考：\nConfig = Json.stringify({\"RetImageType\":\"PROPROCESS\"})\nAPI 3.0 Explorer 设置方式参考：\nConfig = {\"RetImageType\":\"PROPROCESS\"}"
      }
    ],
    "desc": "本接口支持名片各字段的自动定位与识别，包含姓名、电话、手机号、邮箱、公司、部门、职位、网址、地址、QQ、微信、MSN等。"
  },
  "IDCardOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "CardSide",
        "desc": "FRONT 为身份证有照片的一面（人像面），\nBACK 为身份证有国徽的一面（国徽面）。"
      },
      {
        "name": "Config",
        "desc": "可选字段，根据需要选择是否请求对应字段。\n目前包含的字段为：\nCropIdCard，身份证照片裁剪，bool 类型，默认false，\nCropPortrait，人像照片裁剪，bool 类型，默认false，\nCopyWarn，复印件告警，bool 类型，默认false，\nBorderCheckWarn，边框和框内遮挡告警，bool 类型，默认false，\nReshootWarn，翻拍告警，bool 类型，默认false，\nDetectPsWarn，PS检测告警，bool类型，默认false，\nTempIdWarn，临时身份证告警，bool类型，默认false，\nInvalidDateWarn，身份证有效日期不合法告警，bool类型，默认false。\n\nSDK 设置方式参考：\nConfig = Json.stringify({\"CropIdCard\":true,\"CropPortrait\":true})\nAPI 3.0 Explorer 设置方式参考：\nConfig = {\"CropIdCard\":true,\"CropPortrait\":true}"
      }
    ],
    "desc": "本接口支持中国大陆居民二代身份证正反面所有字段的识别，包括姓名、性别、民族、出生日期、住址、公民身份证号、签发机关、有效期限；具备身份证照片、人像照片的裁剪功能和翻拍、PS、复印件告警功能，以及边框和框内遮挡告警、临时身份证告警和身份证有效期不合法告警等扩展功能。"
  },
  "MLIDCardOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。( 中国地区之外不支持这个字段 )\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "RetImage",
        "desc": "是否返回图片"
      }
    ],
    "desc": "本接口支持马来西亚身份证识别，识别字段包括身份证号、姓名、性别、地址；具备身份证人像照片的裁剪功能和翻拍、复印件告警功能。\n本接口暂未完全对外开放，如需咨询，请[联系商务](https://cloud.tencent.com/about/connect)\n"
  },
  "GeneralAccurateOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持图像整体文字的检测和识别，返回文字框位置与文字内容。相比通用印刷体识别接口，准确率和召回率更高。"
  },
  "VinOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持图片内车辆识别代号（VIN）的检测和识别。"
  },
  "MLIDPassportOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。"
      },
      {
        "name": "RetImage",
        "desc": "是否返回图片"
      }
    ],
    "desc": "本接口支持马来西亚身护照识别，识别字段包括护照ID、姓名、出生日期、性别、有效期、发行国、国籍；具备护照人像照片的裁剪功能和翻拍、复印件告警功能。\n本接口暂未完全对外开放，如需咨询，请[联系商务](https://cloud.tencent.com/about/connect)"
  },
  "QuotaInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持定额发票的发票号码、发票代码及金额等关键字段的识别。"
  },
  "GeneralFastOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持图片中整体文字的检测和识别，返回文字框位置与文字内容。相比通用印刷体识别接口，识别速度更快、支持的 QPS 更高。"
  },
  "VehicleLicenseOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "CardSide",
        "desc": "FRONT 为行驶证主页正面（有红色印章的一面），\nBACK 为行驶证副页正面（有号码号牌的一面）。"
      }
    ],
    "desc": "本接口支持行驶证主页和副页所有字段的自动定位与识别，包含车牌号码、车辆类型、所有人、住址、使用性质、品牌型号、车辆识别代码、发动机号、注册日期、发证日期等。"
  },
  "BizLicenseOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持快速精准识别营业执照上的字段，包括注册号、公司名称、经营场所、主体类型、法定代表人、注册资金、组成形式、成立日期、营业期限和经营范围等字段。"
  },
  "GeneralHandwritingOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持图片内手写体文字的检测和识别，针对手写字体无规则、字迹潦草、模糊等特点进行了识别能力的增强。"
  },
  "VatInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持增值税专用发票、增值税普通发票、增值税电子发票全字段的内容检测和识别，包括发票代码、发票号码、开票日期、合计金额、校验码、税率、合计税额、价税合计、购买方识别号、复核、销售方识别号、开票人、密码区1、密码区2、密码区3、密码区4、发票名称、购买方名称、销售方名称、服务名称、备注、规格型号、数量、单价、金额、税额、收款人等字段。"
  },
  "WaybillOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持市面上主流版式电子运单的识别，包括收件人和寄件人的姓名、电话、地址以及运单号等字段。"
  },
  "GeneralBasicOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "Scene",
        "desc": "保留字段。"
      },
      {
        "name": "LanguageType",
        "desc": "识别语言类型。\n支持自动识别语言类型，同时支持自选语言种类，默认中英文混合(zh)。\n可选值：\nzh\\auto\\jap\\kor\\\nspa\\fre\\ger\\por\\\nvie\\may\\rus\\ita\\\nhol\\swe\\fin\\dan\\\nnor\\hun\\tha\\lat\n可选值分别表示：\n中英文混合、自动识别、日语、韩语、\n西班牙语、法语、德语、葡萄牙语、\n越南语、马来语、俄语、意大利语、\n荷兰语、瑞典语、芬兰语、丹麦语、\n挪威语、匈牙利语、泰语、拉丁语系。"
      }
    ],
    "desc": "本接口支持多场景、任意版面下整图文字的识别。支持自动识别语言类型，同时支持自选语言种类（推荐），除中英文外，支持日语、韩语、西班牙语、法语、德语、葡萄牙语、越南语、马来语、俄语、意大利语、荷兰语、瑞典语、芬兰语、丹麦语、挪威语、匈牙利语、泰语等多种语言。应用场景包括：印刷文档识别、网络图片识别、广告图文字识别、街景店招识别、菜单识别、视频标题识别、头像文字识别等。"
  },
  "PermitOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持对卡式港澳台通行证的识别，包括签发地点、签发机关、有效期限、性别、出生日期、英文姓名、姓名、证件号等字段。"
  },
  "TableOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持图片内表格文档的检测和识别，返回每个单元格的文字内容，支持将识别结果保存为 Excel 格式。"
  },
  "ArithmeticOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持作业算式题目的自动识别，目前覆盖 K12 学力范围内的 14 种题型，包括加减乘除四则运算、分数四则运算、竖式四则运算、脱式计算等。"
  },
  "LicensePlateOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持对中国大陆机动车车牌的自动定位和识别，返回地域编号和车牌号信息。"
  },
  "TrainTicketOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持火车票全字段的识别，包括编号、票价、姓名、座位号、出发时间、出发站、到达站、车次、席别等。\n"
  },
  "TaxiInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持出租车发票关键字段的识别，包括发票号码、发票代码、金额、日期等字段。"
  },
  "EnglishOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持图像英文文字的检测和识别，返回文字框位置与文字内容。支持多场景、任意版面下的英文、字母、数字和常见字符的识别，同时覆盖英文印刷体和英文手写体识别。"
  },
  "BankCardOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持对中国大陆主流银行卡的卡号、银行信息、有效期等关键字段的检测与识别。"
  },
  "CarInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持机动车销售统一发票和二手车销售统一发票的识别，包括发票号码、发票代码、合计金额、合计税额等二十多个字段。"
  },
  "DriverLicenseOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持对驾驶证主页所有字段的自动定位与识别，包含证号、姓名、性别、国籍、住址、出生日期、初次领证日期、准驾车型、有效期限等。"
  },
  "FlightInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持机票行程单关键字段的识别，包括姓名、身份证件号码、航班号、票价 、合计、电子客票号码、填开日期等。"
  }
}