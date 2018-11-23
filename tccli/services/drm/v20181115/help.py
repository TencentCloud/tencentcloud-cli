# -*- coding: utf-8 -*-
DESC = "drm-2018-11-15"
INFO = {
  "CreateLicense": {
    "params": [
      {
        "name": "DrmType",
        "desc": "DRM方案类型，接口取值：WIDEVINE，FAIRPLAY。"
      },
      {
        "name": "LicenseRequest",
        "desc": "Base64编码的终端设备License Request数据。"
      },
      {
        "name": "ContentType",
        "desc": "内容类型，接口取值：VodVideo,LiveVideo。"
      },
      {
        "name": "Tracks",
        "desc": "授权播放的Track列表。\n该值为空时，默认授权所有track播放。"
      },
      {
        "name": "PlaybackPolicy",
        "desc": "播放策略参数。"
      }
    ],
    "desc": "本接口用来生成DRM方案对应的播放许可证，开发者需提供DRM方案类型、内容类型参数，后台将生成许可证后返回许可证数据\n开发者需要转发终端设备发出的许可证请求信息。"
  },
  "StartEncryption": {
    "params": [
      {
        "name": "CosEndPoint",
        "desc": "cos的end point。"
      },
      {
        "name": "CosSecretId",
        "desc": "cos api密钥id。"
      },
      {
        "name": "CosSecretKey",
        "desc": "cos api密钥。"
      },
      {
        "name": "DrmType",
        "desc": "使用的DRM方案类型，接口取值WIDEVINE,FAIRPLAY"
      },
      {
        "name": "SourceObject",
        "desc": "存储在COS上的原始内容信息"
      },
      {
        "name": "OutputObjects",
        "desc": "加密后的内容存储到COS的对象"
      }
    ],
    "desc": "开发者调用该接口，启动一次内容文件的DRM加密工作流"
  },
  "DescribeKeys": {
    "params": [
      {
        "name": "DrmType",
        "desc": "使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。"
      },
      {
        "name": "Tracks",
        "desc": "加密的track列表，接口取值VIDEO、AUDIO。"
      },
      {
        "name": "ContentType",
        "desc": "内容类型。接口取值VodVideo,LiveVideo"
      },
      {
        "name": "RsaPublicKey",
        "desc": "Base64编码的Rsa公钥，用来加密出参中的SessionKey。\n如果该参数为空，则出参中SessionKey为明文。"
      },
      {
        "name": "ContentId",
        "desc": "一个加密内容的唯一标识。\n如果该参数为空，则后台自动生成"
      }
    ],
    "desc": "开发者需要指定使用的DRM类型、和需要加密的Track类型，后台返回加密使用的密钥\n如果加密使用的ContentID没有关联的密钥信息，后台会自动生成新的密钥返回\n"
  }
}