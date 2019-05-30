# -*- coding: utf-8 -*-
DESC = "ecc-2018-12-13"
INFO = {
  "EHOCR": {
    "params": [
      {
        "name": "Image",
        "desc": "图片所在的url或base64编码后的图像数据，依据InputType而定"
      },
      {
        "name": "InputType",
        "desc": "输出图片类型，0表示Image字段是图片所在的url，1表示Image字段是base64编码后的图像数据"
      }
    ],
    "desc": "https://ecc.tencentcloudapi.com/?Action=EHOCR\n作文识别"
  },
  "ECC": {
    "params": [
      {
        "name": "Content",
        "desc": "作文文本，必填"
      },
      {
        "name": "Title",
        "desc": "作文题目，可选参数"
      },
      {
        "name": "Grade",
        "desc": "年级标准， 默认以cet4为标准，取值与意义如下：elementary 小学，grade7 grade8 grade9分别对应初一，初二，初三。 grade10 grade11 grade12 分别对应高一，高二，高三，以及cet4和cet6 分别表示 英语4级和6级。"
      },
      {
        "name": "Outline",
        "desc": "作文提纲，可选参数，作文的写作要求。"
      },
      {
        "name": "ModelSubject",
        "desc": "范文标题，可选参数，本接口可以依据提供的范文对作文进行评分。"
      },
      {
        "name": "ModelContent",
        "desc": "范文内容，可选参数，同上，范文的正文部分。"
      }
    ],
    "desc": "接口请求域名： ecc.tencentcloudapi.com \n纯文本英语作文批改"
  }
}