# -*- coding: utf-8 -*-
DESC = "facefusion-2018-12-01"
INFO = {
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
        "desc": "返回图像方式（url 或 base64) ，二选一。当前仅支持 url 方式，base64 方式后期开放。"
      },
      {
        "name": "PornDetect",
        "desc": "0表示不需要鉴黄，1表示需要鉴黄。2018年12月1号以前创建的活动默认值为0，其他情况默认值为1."
      },
      {
        "name": "CelebrityIdentify",
        "desc": "0表示不需要鉴政，1表示需要鉴政。2018年12月1号以前创建的活动默认值为0，其他情况默认值为1。鉴政接口同时会对名人明星进行识别，您可以根据实际需要过滤。"
      }
    ],
    "desc": "本接口用于人脸融合，用户上传人脸图片，获取与模板融合后的人脸图片。未发布的活动请求频率限制为1次/秒，已发布的活动请求频率限制50次/秒。如有需要提高活动的请求频率限制，请在控制台中申请。\n>     \n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  }
}