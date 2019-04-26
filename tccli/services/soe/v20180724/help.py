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
        "desc": "被评估语音对应的文本，句子模式下不超过个 20 单词或者中文文字，段落模式不超过 120 单词或者中文文字，中文评估使用 utf-8 编码，自由说模式该值传空。"
      },
      {
        "name": "WorkMode",
        "desc": "语音输入模式，0：流式分片，1：非流式一次性评估"
      },
      {
        "name": "EvalMode",
        "desc": "评估模式，0：词模式（中文评测模式下为文字模式），1：句子模式，2：段落模式，3：自由说模式，当为词模式评估时，能够提供每个音节的评估信息，当为句子模式时，能够提供完整度和流利度信息。"
      },
      {
        "name": "ScoreCoeff",
        "desc": "评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段"
      },
      {
        "name": "SoeAppId",
        "desc": "业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。"
      },
      {
        "name": "IsLongLifeSession",
        "desc": "长效session标识，当该参数为1时，session的持续时间为300s，但会一定程度上影响第一个数据包的返回速度，且TransmitOralProcess必须同时为1才可生效。"
      },
      {
        "name": "StorageMode",
        "desc": "音频存储模式，0：不存储，1：存储到公共对象存储，输出结果为该会话最后一个分片TransmitOralProcess 返回结果 AudioUrl 字段。"
      },
      {
        "name": "SentenceInfoEnabled",
        "desc": "输出断句中间结果标识，0：不输出，1：输出，通过设置该参数，可以在评估过程中的分片传输请求中，返回已经评估断句的中间结果，中间结果可用于客户端 UI 更新，输出结果为TransmitOralProcess请求返回结果 SentenceInfoSet 字段。"
      },
      {
        "name": "ServerType",
        "desc": "评估语言，0：英文，1：中文。"
      },
      {
        "name": "IsAsync",
        "desc": "异步模式标识，0：同步模式，1：异步模式。"
      },
      {
        "name": "TextMode",
        "desc": "输入文本模式，0: 普通文本，1: 音素结构文本"
      }
    ],
    "desc": "初始化发音评估过程，每一轮评估前进行调用。语音输入模式分为流式模式和非流式模式，流式模式支持数据分片传输，可以加快评估响应速度。评估模式分为词模式和句子模式，词模式会标注每个音节的详细信息；句子模式会有完整度和流利度的评估。"
  },
  "TransmitOralProcess": {
    "params": [
      {
        "name": "SeqId",
        "desc": "流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义，当IsLongLifeSession不为1且为非流式模式时无意义。"
      },
      {
        "name": "IsEnd",
        "desc": "是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。"
      },
      {
        "name": "VoiceFileType",
        "desc": "语音文件类型 \t1:raw, 2:wav, 3:mp3(三种格式目前仅支持16k采样率16bit编码单声道，如有不一致可能导致评估不准确或失败)。"
      },
      {
        "name": "VoiceEncodeType",
        "desc": "语音编码类型\t1:pcm。"
      },
      {
        "name": "UserVoiceData",
        "desc": "当前数据包数据, 流式模式下数据包大小可以按需设置，在网络稳定时，分片大小建议设置0.5k，且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数），编码格式要求为BASE64。"
      },
      {
        "name": "SessionId",
        "desc": "语音段唯一标识，一个完整语音一个SessionId。"
      },
      {
        "name": "SoeAppId",
        "desc": "业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。"
      },
      {
        "name": "IsLongLifeSession",
        "desc": "长效session标识，当该参数为1时，session的持续时间为300s，但会一定程度上影响第一个数据包的返回速度。当InitOralProcess接口调用时此项为1时，此项必填1才可生效。"
      },
      {
        "name": "IsQuery",
        "desc": "查询标识，当该参数为1时，该请求为查询请求，请求返回该 Session 的评估结果。"
      }
    ],
    "desc": "传输音频数据，必须在完成发音评估初始化接口之后调用，且SessonId要与初始化接口保持一致。分片传输时，尽量保证SeqId顺序传输。音频源目前仅支持16k采样率16bit单声道编码方式，如有不一致可能导致评估不准确或失败。"
  },
  "TransmitOralProcessWithInit": {
    "params": [
      {
        "name": "SeqId",
        "desc": "流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义，当IsLongLifeSession不为1且为非流式模式时无意义。"
      },
      {
        "name": "IsEnd",
        "desc": "是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。"
      },
      {
        "name": "VoiceFileType",
        "desc": "语音文件类型 \t1:raw, 2:wav, 3:mp3(三种格式目前仅支持16k采样率16bit编码单声道，如有不一致可能导致评估不准确或失败)。"
      },
      {
        "name": "VoiceEncodeType",
        "desc": "语音编码类型\t1:pcm。"
      },
      {
        "name": "UserVoiceData",
        "desc": "当前数据包数据, 流式模式下数据包大小可以按需设置，在网络良好的情况下，建议设置为0.5k，且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数），编码格式要求为BASE64。"
      },
      {
        "name": "SessionId",
        "desc": "语音段唯一标识，一个完整语音一个SessionId。"
      },
      {
        "name": "RefText",
        "desc": "被评估语音对应的文本，句子模式下不超过个 20 单词或者中文文字，段落模式不超过 120 单词或者中文文字，中文评估使用 utf-8 编码，自由说模式该值传空。"
      },
      {
        "name": "WorkMode",
        "desc": "语音输入模式，0：流式分片，1：非流式一次性评估"
      },
      {
        "name": "EvalMode",
        "desc": "评估模式，0：词模式（中文评测模式下为文字模式），1：句子模式，2：段落模式，3：自由说模式，当为词模式评估时，能够提供每个音节的评估信息，当为句子模式时，能够提供完整度和流利度信息。"
      },
      {
        "name": "ScoreCoeff",
        "desc": "评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段"
      },
      {
        "name": "SoeAppId",
        "desc": "业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。"
      },
      {
        "name": "StorageMode",
        "desc": "音频存储模式，0：不存储，1：存储到公共对象存储，输出结果为该会话最后一个分片TransmitOralProcess 返回结果 AudioUrl 字段。"
      },
      {
        "name": "SentenceInfoEnabled",
        "desc": "输出断句中间结果标识，0：不输出，1：输出，通过设置该参数，可以在评估过程中的分片传输请求中，返回已经评估断句的中间结果，中间结果可用于客户端 UI 更新，输出结果为TransmitOralProcess请求返回结果 SentenceInfoSet 字段。"
      },
      {
        "name": "ServerType",
        "desc": "评估语言，0：英文，1：中文。"
      },
      {
        "name": "IsAsync",
        "desc": "异步模式标识，0：同步模式，1：异步模式。"
      },
      {
        "name": "IsQuery",
        "desc": "查询标识，当该参数为1时，该请求为查询请求，请求返回该 Session 评估结果。"
      },
      {
        "name": "TextMode",
        "desc": "输入文本模式，0: 普通文本，1: 音素结构文本"
      }
    ],
    "desc": "初始化并传输音频数据，分片传输时，尽量保证SeqId顺序传输。音频源目前仅支持16k采样率16bit单声道编码方式，如有不一致可能导致评估不准确或失败。"
  }
}