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
        "desc": "输出图片类型，0 表示 Image 字段是图片所在的 url，1 表示 Image 字段是 base64 编码后的图像数据"
      },
      {
        "name": "EccAppid",
        "desc": "业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数（暂时无需传入）。"
      },
      {
        "name": "SessionId",
        "desc": "图像识别唯一标识，一次识别一个 SessionId，使用识别功能时 SessionId 可用于使用文本批改接口，此时按图像批改价格收费；如使用文本批改接口时没有传入 SessionId，则需要收取文本批改的费用"
      },
      {
        "name": "ServerType",
        "desc": "服务类型，0：“图像识别”，只返回识别结果，1：“图像批改”，同时返回识别结果与批改结果。默认为 0"
      },
      {
        "name": "Title",
        "desc": "作文题目，可选参数"
      },
      {
        "name": "Grade",
        "desc": "年级标准， 默认以 cet4 为标准，取值与意义如下：elementary 小学，grade7 grade8 grade9分别对应初一，初二，初三。 grade10 grade11 grade12 分别对应高一，高二，高三，以及 cet4 和 cet6 分别表示 英语4级和6级。"
      },
      {
        "name": "Requirement",
        "desc": "作文提纲，可选参数，作文的写作要求。"
      },
      {
        "name": "ModelTitle",
        "desc": "范文标题，可选参数，本接口可以依据提供的范文对作文进行评分。"
      },
      {
        "name": "ModelContent",
        "desc": "范文内容，可选参数，同上，范文的正文部分。"
      },
      {
        "name": "IsAsync",
        "desc": "异步模式标识，0：同步模式，1：异步模式。默认为同步模式"
      }
    ],
    "desc": "https://ecc.tencentcloudapi.com/?Action=EHOCR\n图像识别批改接口"
  },
  "DescribeTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务 ID"
      },
      {
        "name": "EccAppid",
        "desc": "业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数（暂时无需传入）。"
      }
    ],
    "desc": "异步任务结果查询接口"
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
        "name": "Requirement",
        "desc": "作文提纲，可选参数，作文的写作要求。"
      },
      {
        "name": "ModelTitle",
        "desc": "范文标题，可选参数，本接口可以依据提供的范文对作文进行评分。"
      },
      {
        "name": "ModelContent",
        "desc": "范文内容，可选参数，同上，范文的正文部分。"
      },
      {
        "name": "EccAppid",
        "desc": "业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数（暂时无需传入）。"
      },
      {
        "name": "IsAsync",
        "desc": "异步模式标识，0：同步模式，1：异步模式，默认为同步模式"
      },
      {
        "name": "SessionId",
        "desc": "图像识别唯一标识，一次识别一个 SessionId。当传入此前识别接口使用过的 SessionId，则本次批改按图像批改价格收费；如使用了识别接口且本次没有传入 SessionId，则需要加取文本批改的费用；如果直接使用文本批改接口，则只收取文本批改的费用"
      }
    ],
    "desc": "接口请求域名： ecc.tencentcloudapi.com \n纯文本英语作文批改"
  },
  "CorrectMultiImage": {
    "params": [
      {
        "name": "Image",
        "desc": "图片的url链接或base64数据。每张图片数据作为数组的一个元素，数组个数与图片个数保持一致。存放类别依据InputType而定，url与base64编码不能混合使用。"
      },
      {
        "name": "InputType",
        "desc": "输出图片类型，0 表示 Image 字段是图片所在的 url，1 表示 Image 字段是 base64 编码后的图像数据。"
      },
      {
        "name": "EccAppid",
        "desc": "业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数。"
      },
      {
        "name": "SessionId",
        "desc": "图像识别唯一标识，一次识别一个 SessionId，使用识别功能时 SessionId 可用于使用文本批改接口，此时按图像批改价格收费；如使用文本批改接口时没有传入 SessionId，则需要收取文本批改的费用。"
      },
      {
        "name": "ServerType",
        "desc": "服务类型，0：“多图像识别”，只返回识别结果；1：“多图像批改”，同时返回识别结果与批改结果。默认为 0。"
      },
      {
        "name": "Title",
        "desc": "作文题目，可选参数"
      },
      {
        "name": "Grade",
        "desc": "年级标准， 默认以 cet4 为标准，取值与意义如下：elementary 小学，grade7 grade8 grade9分别对应初一，初二，初三。 grade10 grade11 grade12 分别对应高一，高二，高三，以及 cet4 和 cet6 分别表示 英语4级和6级。"
      },
      {
        "name": "Requirement",
        "desc": "作文提纲，可选参数，作文的写作要求。"
      },
      {
        "name": "ModelTitle",
        "desc": "范文标题，可选参数，本接口可以依据提供的范文对作文进行评分。"
      },
      {
        "name": "ModelContent",
        "desc": "范文内容，可选参数，同上，范文的正文部分。"
      },
      {
        "name": "IsAsync",
        "desc": "异步模式标识，0：同步模式，1：异步模式。默认为同步模式"
      }
    ],
    "desc": "https://ecc.tencentcloudapi.com/?Action=CorrectMultiImage\n多图像识别批改接口"
  }
}