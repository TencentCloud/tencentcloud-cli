# -*- coding: utf-8 -*-
DESC = "ocr-2018-11-19"
INFO = {
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
  "IDCardOCR": {
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
        "name": "CardSide",
        "desc": "FRONT 为身份证有照片的一面（人像面），\nBACK 为身份证有国徽的一面（国徽面）。"
      },
      {
        "name": "Config",
        "desc": "可选字段，根据需要选择是否请求对应字段。\n目前包含的字段为：\nCropIdCard，身份证照片裁剪，bool 类型，\nCropPortrait，人像照片裁剪，bool 类型，\nCopyWarn，复印件告警，bool 类型，\nBorderCheckWarn，遮挡告警，bool 类型，\nReshootWarn，翻拍告警，bool 类型。\n\nSDK 设置方式参考：\nConfig = Json.stringify({\"CropIdCard\":true,\"CropPortrait\":true})\nAPI 3.0 Explorer 设置方式参考：\nConfig = {\"CropIdCard\":true,\"CropPortrait\":true}"
      }
    ],
    "desc": "本接口支持二代身份证正反面所有字段的识别，包括姓名、性别、民族、出生日期、住址、公民身份证号、签发机关、有效期限；具备身份证照片、人像照片的裁剪功能和翻拍件、复印件的识别告警功能。"
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
      }
    ],
    "desc": "本接口支持多场景、任意版面下整图文字的识别，包括中英文、字母、数字和日文、韩文的识别。应用场景包括：印刷文档识别、网络图片识别、广告图文字识别、街景店招识别、菜单识别、视频标题识别、头像文字识别等。"
  }
}