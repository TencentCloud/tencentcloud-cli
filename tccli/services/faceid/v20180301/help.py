# -*- coding: utf-8 -*-
DESC = "faceid-2018-03-01"
INFO = {
  "GetDetectInfo": {
    "params": [
      {
        "name": "BizToken",
        "desc": "人脸核身流程的标识，调用DetectAuth接口时生成。"
      },
      {
        "name": "RuleId",
        "desc": "用于细分客户使用场景，由腾讯侧在线下对接时分配。"
      },
      {
        "name": "InfoType",
        "desc": "指定拉取的结果信息，取值（0：全部；1：文本类；2：身份证正反面；3：视频最佳截图照片；4：视频）。\n如 134表示拉取文本类、视频最佳截图照片、视频。"
      }
    ],
    "desc": "完成验证后，用BizToken调用本接口获取结果信息，BizToken生成后三天内（3\\*24\\*3,600秒）可多次拉取。"
  },
  "GetLiveCode": {
    "params": [],
    "desc": "使用数字活体检测模式前，需调用本接口获取数字验证码。"
  },
  "GetActionSequence": {
    "params": [],
    "desc": "使用动作活体检测模式前，需调用本接口获取动作顺序。"
  },
  "LivenessCompare": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "用于人脸比对的照片，图片的BASE64值；\nBASE64编码后的图片数据大小不超过3M，仅支持jpg、png格式。"
      },
      {
        "name": "VideoBase64",
        "desc": "用于活体检测的视频，视频的BASE64值；\nBASE64编码后的大小不超过5M，支持mp4、avi、flv格式。"
      },
      {
        "name": "LivenessType",
        "desc": "活体检测类型，取值：LIP/ACTION/SILENT。\nLIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。"
      },
      {
        "name": "ValidateData",
        "desc": "数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；\n动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；\n静默模式传参：空。"
      },
      {
        "name": "Optional",
        "desc": "本接口不需要传递此参数。"
      }
    ],
    "desc": "传入视频和照片，先判断视频中是否为真人，判断为真人后，再判断该视频中的人与上传照片是否属于同一个人。"
  },
  "BankCardVerification": {
    "params": [
      {
        "name": "IdCard",
        "desc": "身份证号"
      },
      {
        "name": "Name",
        "desc": "姓名"
      },
      {
        "name": "BankCard",
        "desc": "银行卡"
      }
    ],
    "desc": "银行卡核验"
  },
  "LivenessRecognition": {
    "params": [
      {
        "name": "IdCard",
        "desc": "身份证号"
      },
      {
        "name": "Name",
        "desc": "姓名。中文请使用UTF-8编码。"
      },
      {
        "name": "VideoBase64",
        "desc": "用于活体检测的视频，视频的BASE64值；\nBASE64编码后的大小不超过5M，支持mp4、avi、flv格式。"
      },
      {
        "name": "LivenessType",
        "desc": "活体检测类型，取值：LIP/ACTION/SILENT。\nLIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。"
      },
      {
        "name": "ValidateData",
        "desc": "数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；\n动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；\n静默模式传参：空。"
      },
      {
        "name": "Optional",
        "desc": "本接口不需要传递此参数。"
      }
    ],
    "desc": "传入视频和身份信息，先判断视频中是否为真人，判断为真人后，再判断该视频中的人与公安权威库的证件照是否属于同一个人。"
  },
  "IdCardVerification": {
    "params": [
      {
        "name": "IdCard",
        "desc": "身份证号"
      },
      {
        "name": "Name",
        "desc": "姓名"
      }
    ],
    "desc": "传入姓名和身份证号，校验两者的真实性和一致性。"
  },
  "ImageRecognition": {
    "params": [
      {
        "name": "IdCard",
        "desc": "身份证号"
      },
      {
        "name": "Name",
        "desc": "姓名。中文请使用UTF-8编码。"
      },
      {
        "name": "ImageBase64",
        "desc": "用于人脸比对的照片，图片的BASE64值；\nBASE64编码后的图片数据大小不超过3M，仅支持jpg、png格式。"
      },
      {
        "name": "Optional",
        "desc": "本接口不需要传递此参数。"
      }
    ],
    "desc": "传入照片和身份信息，判断该照片与公安权威库的证件照是否属于同一个人。"
  },
  "DetectAuth": {
    "params": [
      {
        "name": "RuleId",
        "desc": "用于细分客户使用场景，由腾讯侧在线下对接时分配。"
      },
      {
        "name": "TerminalType",
        "desc": "本接口不需要传递此参数。"
      },
      {
        "name": "IdCard",
        "desc": "身份标识（与公安权威库比对时必须是身份证号）。\n规则：a-zA-Z0-9组合。最长长度32位。"
      },
      {
        "name": "Name",
        "desc": "姓名。最长长度32位。中文请使用UTF-8编码。"
      },
      {
        "name": "RedirectUrl",
        "desc": "认证结束后重定向的回调链接地址。最长长度1024位。"
      },
      {
        "name": "Extra",
        "desc": "透传字段，在获取验证结果时返回。"
      },
      {
        "name": "ImageBase64",
        "desc": "用于人脸比对的照片，图片的BASE64值；\nBASE64编码后的图片数据大小不超过3M，仅支持jpg、png格式。"
      }
    ],
    "desc": "每次开始核身前，需先调用本接口获取BizToken，用来串联核身流程，在核身完成后，用于获取验证结果信息。"
  }
}