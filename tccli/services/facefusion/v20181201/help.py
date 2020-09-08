# -*- coding: utf-8 -*-
DESC = "facefusion-2018-12-01"
INFO = {
  "DescribeMaterialList": {
    "params": [
      {
        "name": "ActivityId",
        "desc": "活动Id"
      },
      {
        "name": "MaterialId",
        "desc": "素材Id"
      },
      {
        "name": "Limit",
        "desc": "每次拉取条数"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      }
    ],
    "desc": "通常通过腾讯云人脸融合的控制台可以查看到素材相关的参数数据，可以满足使用。本接口返回活动的素材数据，包括素材状态等。用于用户通过Api查看素材相关数据，方便使用。"
  },
  "FaceFusion": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "活动 ID，请在人脸融合控制台查看。"
      },
      {
        "name": "ModelId",
        "desc": "素材 ID，请在人脸融合控制台查看。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据。请确保人脸为正脸，无旋转。若某些手机拍摄后人脸被旋转，请使用图片的 EXIF 信息对图片进行旋转处理；请勿在 base64 数据中包含头部，如“data:image/jpeg;base64,”。"
      },
      {
        "name": "RspImgType",
        "desc": "返回图像方式（url 或 base64) ，二选一。url有效期为30天。"
      },
      {
        "name": "PornDetect",
        "desc": "历史遗留字段，无需填写。因为融合只需提取人脸特征，不需要鉴黄。"
      },
      {
        "name": "CelebrityIdentify",
        "desc": "0表示不需要鉴政，1表示需要鉴政。默认值为0。\n请注意，鉴政服务开启后，您需要根据返回结果自行判断是否调整您的业务逻辑。例如提示您的用户图片非法，请更换图片。"
      }
    ],
    "desc": "本接口用于人脸融合，用户上传人脸图片，获取与模板融合后的人脸图片。未发布的活动请求频率限制为1次/秒，已发布的活动请求频率限制50次/秒。如有需要提高活动的请求频率限制，请在控制台中申请。\n>     \n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "FuseFace": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "活动 ID，请在人脸融合控制台查看。"
      },
      {
        "name": "ModelId",
        "desc": "素材 ID，请在人脸融合控制台查看。"
      },
      {
        "name": "RspImgType",
        "desc": "返回图像方式（url 或 base64) ，二选一。url有效期为30天。"
      },
      {
        "name": "MergeInfos",
        "desc": "用户人脸图片、素材模板图的人脸位置信息。"
      },
      {
        "name": "FuseProfileDegree",
        "desc": "脸型融合比例，数值越高，融合后的脸型越像素材人物。取值范围[0,100] \n若此参数不填写，则使用人脸融合控制台中脸型参数数值。（换脸版算法暂不支持此参数调整）"
      },
      {
        "name": "FuseFaceDegree",
        "desc": "五官融合比例，数值越高，融合后的五官越像素材人物。取值范围[0,100] \n若此参数不填写，则使用人脸融合控制台中五官参数数值。（换脸版算法暂不支持此参数调整）"
      },
      {
        "name": "CelebrityIdentify",
        "desc": "0表示不需要鉴政，1表示需要鉴政。默认值为0。\n请注意，鉴政服务开启后，您需要根据返回结果自行判断是否调整您的业务逻辑。例如提示您的用户图片非法，请更换图片。"
      }
    ],
    "desc": "本接口用于单脸、多脸融合，用户上传人脸图片，获取与模板融合后的人脸图片。查看 <a href=\"https://cloud.tencent.com/document/product/670/38247\" target=\"_blank\">选脸融合接入指引</a>。\n\n未发布的活动请求频率限制为1次/秒，已发布的活动请求频率限制50次/秒。如有需要提高活动的请求频率限制，请在控制台中申请。\n>\n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  }
}