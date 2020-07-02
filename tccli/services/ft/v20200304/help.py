# -*- coding: utf-8 -*-
DESC = "ft-2020-03-04"
INFO = {
  "SwapGenderPic": {
    "params": [
      {
        "name": "GenderInfos",
        "desc": "人脸转化性别信息。 \n您可以输入最多3个 GenderInfo 来实现给一张图中的最多3张人脸转换性别。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url ，对应图片 base64 编码后大小不可超过5M。 \n图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 \n图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "RspImgType",
        "desc": "返回图像方式（base64 或 url ) ，二选一。url有效期为1天。"
      }
    ],
    "desc": "用户上传一张人脸图片，基于人脸编辑与生成算法，输出一张人脸性别转换的图片。男变女可实现美颜、淡妆、加刘海和长发的效果；女变男可实现加胡须、变短发的效果。 "
  },
  "ChangeAgePic": {
    "params": [
      {
        "name": "AgeInfos",
        "desc": "人脸变老变年轻信息。 \n您可以输入最多3个 AgeInfo 来实现给一张图中的最多3张人脸变老变年轻。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url ，对应图片 base64 编码后大小不可超过5M。 \n图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 \n图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "RspImgType",
        "desc": "返回图像方式（base64 或 url ) ，二选一。url有效期为1天。"
      }
    ],
    "desc": "用户上传一张人脸图片，基于人脸编辑与生成算法，输出一张人脸变老或变年轻的图片，支持实现人脸不同年龄的变化。"
  }
}