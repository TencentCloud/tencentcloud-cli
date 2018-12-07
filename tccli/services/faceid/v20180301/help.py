# -*- coding: utf-8 -*-
DESC = "faceid-2018-03-01"
INFO = {
  "GetDetectInfo": {
    "params": [
      {
        "name": "BizToken",
        "desc": "业务流水号"
      },
      {
        "name": "RuleId",
        "desc": "规则Id。"
      },
      {
        "name": "InfoType",
        "desc": "指定需要拉取何种信息（0：全部；1：文本类；2：身份证正反面；3：截帧（最佳帧）；4：视频）。可拼接。如 134表示拉取文本类、截帧（最佳帧）、视频"
      }
    ],
    "desc": "获取实名核身结果信息"
  },
  "DetectAuth": {
    "params": [
      {
        "name": "RuleId",
        "desc": "规则Id。a-zA-Z0-9组合。最长长度32位。"
      },
      {
        "name": "TerminalType",
        "desc": "终端类型。可选值有：weixinh5, weixinh5native, h5, tinyappsdk, iossdk, androidsdk。只有值为\"weixinh5\"时会返回跳转URL。"
      },
      {
        "name": "IdCard",
        "desc": "身份证号或者是客户系统内部的唯一用户id。（传uid的时候只能使用ImageBase64传的照片进行一比一）a-zA-Z0-9组合。最长长度32位。"
      },
      {
        "name": "Name",
        "desc": "姓名。最长长度32位。"
      },
      {
        "name": "RedirectUrl",
        "desc": "回调地址。最长长度1024位。"
      },
      {
        "name": "Extra",
        "desc": "额外参数，会在getDetectInfo时带回去。最长长度1024位。"
      },
      {
        "name": "ImageBase64",
        "desc": "用于一比一时的照片base64。此时必须传入IdCard。"
      }
    ],
    "desc": "实名核身鉴权。用于获取一次核身流程的BizToken。如果是微信平台，会同时返回一个URL，用作微信平台的跳转。"
  }
}