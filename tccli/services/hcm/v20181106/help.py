# -*- coding: utf-8 -*-
DESC = "hcm-2018-11-06"
INFO = {
  "Evaluation": {
    "params": [
      {
        "name": "SessionId",
        "desc": "图片唯一标识，一张图片一个SessionId；"
      },
      {
        "name": "Image",
        "desc": "图片数据，需要使用base64对图片的二进制数据进行编码，与url参数二者填一即可；"
      },
      {
        "name": "HcmAppid",
        "desc": "业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 HcmAppId 可以在[控制台](https://console.cloud.tencent.com/hcm)【应用管理】下新建。"
      },
      {
        "name": "Url",
        "desc": "图片url，与Image参数二者填一即可；"
      }
    ],
    "desc": "速算题目批改接口，根据用户上传的图片或图片的URL识别图片中的数学算式，进而给出算式的正确性评估。"
  }
}