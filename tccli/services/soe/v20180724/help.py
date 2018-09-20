# -*- coding: utf-8 -*-
DESC = "soe-2018-07-24"
INFO = {
  "InitOralProcess": {
    "params": [
      {
        "name": "SessionId",
        "desc": "语音段唯一标识，一段语音一个SessionId"
      },
      {
        "name": "RefText",
        "desc": "被评估语音对应的文本"
      },
      {
        "name": "WorkMode",
        "desc": "语音输入模式，0流式分片，1非流式一次性评估"
      },
      {
        "name": "EvalMode",
        "desc": "评估模式，0:词模式, 1:句子模式，当为词模式评估时，能够提供每个音节的评估信息，当为句子模式时，能够提供完整度和流利度信息。"
      },
      {
        "name": "ScoreCoeff",
        "desc": "评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段"
      }
    ],
    "desc": "初始化发音评估过程，每一轮评估前进行调用。语音输入模式分为流式模式和非流式模式，流式模式支持数据分片传输，可以加快评估响应速度。评估模式分为词模式和句子模式，词模式会标注每个音节的详细信息；句子模式会有完整度和流利度的评估。"
  },
  "TransmitOralProcess": {
    "params": [
      {
        "name": "SeqId",
        "desc": "流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义，非流式模式下无意义"
      },
      {
        "name": "IsEnd",
        "desc": "是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义"
      },
      {
        "name": "VoiceFileType",
        "desc": "语音文件类型 \t1:raw, 2:wav, 3:mp3(mp3格式目前仅支持16k采样率16bit编码单声道)"
      },
      {
        "name": "VoiceEncodeType",
        "desc": "语音编码类型\t1:pcm"
      },
      {
        "name": "UserVoiceData",
        "desc": "当前数据包数据, 流式模式下数据包大小可以按需设置，数据包大小必须 >= 4K，编码格式要求为BASE64。"
      },
      {
        "name": "SessionId",
        "desc": "语音段唯一标识，一个完整语音一个SessionId"
      },
      {
        "name": "SoeAppId",
        "desc": "业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，需要结合[控制台](https://console.cloud.tencent.com/soe)使用。"
      }
    ],
    "desc": "传输音频数据，必须在完成发音评估初始化接口之后调用，且SessonId要与初始化接口保持一致。分片传输时，尽量保证SeqId顺序传输。当使用mp3格式时目前仅支持16k采样率16bit单声道编码方式。"
  }
}