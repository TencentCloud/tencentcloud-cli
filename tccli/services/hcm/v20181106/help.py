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
        "desc": "业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 HcmAppid 可以在[控制台](https://console.cloud.tencent.com/hcm)【应用管理】下新建。"
      },
      {
        "name": "Url",
        "desc": "图片url，与Image参数二者填一即可；"
      },
      {
        "name": "SupportHorizontalImage",
        "desc": "横屏拍摄开关，若开启则支持传输横屏拍摄的图片；"
      },
      {
        "name": "RejectNonArithmeticImage",
        "desc": "拒绝非速算图（如风景图、人物图）开关，若开启，则遇到非速算图会快速返回拒绝的结果，但极端情况下可能会影响评估结果（比如算式截图贴到风景画里可能被判为非速算图直接返回了）。"
      },
      {
        "name": "IsAsync",
        "desc": "异步模式标识，0：同步模式，1：异步模式。默认为同步模式"
      },
      {
        "name": "EnableDispRelatedVertical",
        "desc": "是否展开耦合算式中的竖式计算"
      },
      {
        "name": "EnableDispMidresult",
        "desc": "是否展示竖式算式的中间结果和格式控制字符"
      },
      {
        "name": "EnablePdfRecognize",
        "desc": "是否开启pdf识别，默认开启"
      },
      {
        "name": "PdfPageIndex",
        "desc": "pdf页码，从0开始，默认为0"
      },
      {
        "name": "LaTex",
        "desc": "是否返回LaTex，默认为0返回普通格式，设置成1返回LaTex格式"
      }
    ],
    "desc": "速算题目批改接口，根据用户上传的图片或图片的URL识别图片中的数学算式，进而给出算式的正确性评估。"
  }
}