# -*- coding: utf-8 -*-
DESC = "drm-2018-11-15"
INFO = {
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
  "AddFairPlayPem": {
    "params": [
      {
        "name": "Pem",
        "desc": "加密后的fairplay方案申请时使用的私钥。\n请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对私钥文件中的字段进行加密，并对加密结果进行base64编码。"
      },
      {
        "name": "Ask",
        "desc": "加密后的fairplay方案申请返回的ask数据。\n请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对Ask字符串进行加密，并对加密结果进行base64编码。"
      },
      {
        "name": "PemDecryptKey",
        "desc": "私钥的解密密钥。\nopenssl在生成rsa时，可能会需要设置加密密钥，请记住设置的密钥。\n请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。"
      },
      {
        "name": "BailorId",
        "desc": "委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。"
      },
      {
        "name": "Priority",
        "desc": "私钥的优先级，优先级数值越高，优先级越高。\n该值可以不传，后台将自动分配一个优先级。"
      }
    ],
    "desc": "本接口用来设置fairplay方案所需的私钥、私钥密钥、ask等信息。\n如需使用fairplay方案，请务必先设置私钥。"
  },
  "CreateEncryptKeys": {
    "params": [
      {
        "name": "DrmType",
        "desc": "使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。"
      },
      {
        "name": "Keys",
        "desc": "设置的加密密钥列表。"
      },
      {
        "name": "ContentId",
        "desc": "一个加密内容的唯一标识。"
      },
      {
        "name": "ContentType",
        "desc": "内容类型。接口取值VodVideo,LiveVideo。"
      }
    ],
    "desc": "该接口用来设置加密的密钥。注意，同一个content id，只能设置一次！"
  },
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
  "ModifyFairPlayPem": {
    "params": [
      {
        "name": "Pem",
        "desc": "加密后的fairplay方案申请时使用的私钥。\n请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对私钥文件中的字段进行加密，并对加密结果进行base64编码。"
      },
      {
        "name": "Ask",
        "desc": "加密后的fairplay方案申请返回的ask数据。\n请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对Ask字符串进行加密，并对加密结果进行base64编码。"
      },
      {
        "name": "FairPlayPemId",
        "desc": "要修改的私钥id"
      },
      {
        "name": "PemDecryptKey",
        "desc": "私钥的解密密钥。\nopenssl在生成rsa时，可能会需要设置加密密钥，请记住设置的密钥。\n请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。"
      },
      {
        "name": "BailorId",
        "desc": "委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。"
      },
      {
        "name": "Priority",
        "desc": "私钥的优先级，优先级数值越高，优先级越高。\n该值可以不传，后台将自动分配一个优先级。"
      }
    ],
    "desc": "本接口用来设置fairplay方案所需的私钥、私钥密钥、ask等信息。\n如需使用fairplay方案，请务必先设置私钥。"
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
  },
  "DescribeAllKeys": {
    "params": [
      {
        "name": "DrmType",
        "desc": "使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。"
      },
      {
        "name": "RsaPublicKey",
        "desc": "Base64编码的Rsa公钥，用来加密出参中的SessionKey。\n如果该参数为空，则出参中SessionKey为明文。"
      },
      {
        "name": "ContentId",
        "desc": "一个加密内容的唯一标识。"
      },
      {
        "name": "ContentType",
        "desc": "内容类型。接口取值VodVideo,LiveVideo。"
      }
    ],
    "desc": "本接口用来查询指定DRM类型、ContentType的所有加密密钥\n"
  },
  "DeleteFairPlayPem": {
    "params": [
      {
        "name": "BailorId",
        "desc": "委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。"
      },
      {
        "name": "FairPlayPemId",
        "desc": "要删除的pem id。\n当未传入该值时，将删除所有的私钥。"
      }
    ],
    "desc": "本接口用来删除fairplay方案的私钥、ask等信息\n注：高风险操作，删除后，您将无法使用腾讯云DRM提供的fairplay服务。\n由于缓存，删除操作需要约半小时生效"
  },
  "DescribeFairPlayPem": {
    "params": [
      {
        "name": "BailorId",
        "desc": "委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。"
      },
      {
        "name": "FairPlayPemId",
        "desc": "需要查询的pem id。\n当该值未填入时，将返回所有的私钥信息。"
      }
    ],
    "desc": "该接口用来查询设置的FairPlay私钥校验信息。可用该接口校验设置的私钥与本身的私钥是否一致。"
  }
}