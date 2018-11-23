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
        "desc": "图片数据，需要使用base64对图片的二进制数据进行编码；"
      }
    ],
    "desc": "速算题目批改接口，根据用户上传的图片或图片的URL识别图片中的数学算式，进而给出算式的正确性评估。"
  }
}