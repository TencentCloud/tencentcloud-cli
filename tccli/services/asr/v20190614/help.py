# -*- coding: utf-8 -*-
DESC = "asr-2019-06-14"
INFO = {
  "CreateRecTask": {
    "params": [
      {
        "name": "EngineModelType",
        "desc": "引擎模型类型。\n8k_zh：电话 8k 中文普通话通用，可用于双声道音频的识别；\n8k_zh_s：电话 8k 中文普通话话者分离，仅用于单声道；\n16k_zh：16k 中文普通话通用；\n16k_en：16k 英语；\n16k_ca：16k 粤语。"
      },
      {
        "name": "ChannelNum",
        "desc": "语音声道数。1：单声道；2：双声道（仅在电话 8k 通用模型下支持）。"
      },
      {
        "name": "ResTextFormat",
        "desc": "识别结果文本编码方式。0：UTF-8。"
      },
      {
        "name": "SourceType",
        "desc": "语音数据来源。0：语音 URL；1：语音数据（post body）。"
      },
      {
        "name": "CallbackUrl",
        "desc": "回调 URL，用户自行搭建的用于接收识别结果的服务器地址， 长度小于2048字节。如果用户使用回调方式获取识别结果，需提交该参数；如果用户使用轮询方式获取识别结果，则无需提交该参数。"
      },
      {
        "name": "Url",
        "desc": "语音的URL地址，需要公网可下载。长度小于2048字节，当 SourceType 值为 0 时须填写该字段，为 1 时不需要填写。注意：请确保录音文件时长在一个小时之内，否则可能识别失败。请保证文件的下载速度，否则可能下载失败。"
      },
      {
        "name": "Data",
        "desc": "语音数据，当SourceType 值为1时必须填写，为0可不写。要base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于5MB。"
      },
      {
        "name": "DataLen",
        "desc": "数据长度，当 SourceType 值为1时必须填写，为0可不写（此数据长度为数据未进行base64编码时的数据长度）。"
      },
      {
        "name": "HotwordId",
        "desc": "热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。"
      }
    ],
    "desc": "本接口服务对录音时长1小时以内的录音文件进行识别，异步返回识别全部结果。\n<br>• 接口是 HTTP RESTful 形式\n<br>• 接口支持wav、mp3、silk、amr、m4a等主流音频格式\n<br>• 支持语音 URL 和本地语音文件两种请求方式\n<br>• 本地语音文件上传的文件不能大于5MB，语音 URL的音频时长不能长于1小时\n<br>• 支持中文普通话、英语和粤语。\n<br>• 支持回调或轮询的方式获取结果，结果获取请参考[ 录音文件识别结果查询](https://cloud.tencent.com/document/product/1093/37822)。"
  },
  "DescribeTaskStatus": {
    "params": [
      {
        "name": "TaskId",
        "desc": "从CreateRecTask接口获取的TaskId，用于获取任务状态与结果。"
      }
    ],
    "desc": "在调用录音文件识别请求接口后，有回调和轮询两种方式获取识别结果。\n<br>• 当采用回调方式时，识别完成后会将结果通过 POST 请求的形式通知到用户在请求时填写的回调 URL，具体请参见[ 录音识别结果回调 ](https://cloud.tencent.com/document/product/1093/37139#callback)。\n<br>• 当采用轮询方式时，需要主动提交任务ID来轮询识别结果，共有任务成功、等待、执行中和失败四种结果，具体信息请参见下文说明。\n"
  },
  "GetAsrVocab": {
    "params": [
      {
        "name": "VocabId",
        "desc": "热词表ID"
      }
    ],
    "desc": "用户根据词表的ID可以获取对应的热词表信息"
  },
  "UpdateAsrVocab": {
    "params": [
      {
        "name": "VocabId",
        "desc": "热词表ID"
      },
      {
        "name": "Name",
        "desc": "热词表名称"
      },
      {
        "name": "WordWeights",
        "desc": "词权重数组，包含全部的热词和对应的权重。每个热词的长度不大于10，权重为[1,10]之间整数，数组长度不大于128"
      },
      {
        "name": "WordWeightStr",
        "desc": "词权重文件（纯文本文件）的二进制base64编码，以行分隔，每行的格式为word|weight，即以英文符号|为分割，左边为词，右边为权重，如：你好|5。\n当用户传此参数（参数长度大于0），即以此参数解析词权重，WordWeights会被忽略"
      },
      {
        "name": "Description",
        "desc": "热词表描述"
      }
    ],
    "desc": "用户通过本接口进行对应的词表信息更新。"
  },
  "CreateAsrVocab": {
    "params": [
      {
        "name": "Name",
        "desc": "热词表名称，长度在1-255之间"
      },
      {
        "name": "Description",
        "desc": "热词表描述，长度在0-1000之间"
      },
      {
        "name": "WordWeights",
        "desc": "词权重数组，包含全部的热词和对应的权重。每个热词的长度不大于10，权重为[1,10]之间整数，数组长度不大于128"
      },
      {
        "name": "WordWeightStr",
        "desc": "词权重文件（纯文本文件）的二进制base64编码，以行分隔，每行的格式为word|weight，即以英文符号|为分割，左边为词，右边为权重，如：你好|5。\n当用户传此参数（参数长度大于0），即以此参数解析词权重，WordWeights会被忽略"
      }
    ],
    "desc": "用户通过本接口进行热词表的创建。\n<br>•   默认最多可创建30个热词表。\n<br>•   每个热词表最多可添加128个词，每个词最长10个字，不能超出限制。\n<br>•   热词表可以通过数组或者本地文件形式上传。\n<br>•   本地文件必须为UTF-8编码格式，每行仅添加一个热词且不能包含标点和特殊字符。\n<br>•   热词权重取值范围为[1,10]之间的整数，权重越大代表该词被识别出来的概率越大。"
  },
  "DeleteAsrVocab": {
    "params": [
      {
        "name": "VocabId",
        "desc": "热词表Id"
      }
    ],
    "desc": "用户通过本接口进行热词表的删除。"
  },
  "SentenceRecognition": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "腾讯云项目 ID，可填 0，总长度不超过 1024 字节。"
      },
      {
        "name": "SubServiceType",
        "desc": "子服务类型。2： 一句话识别。"
      },
      {
        "name": "EngSerViceType",
        "desc": "引擎模型类型。\n8k_zh：电话 8k 中文普通话通用；\n16k_zh：16k 中文普通话通用；\n16k_en：16k 英语；\n16k_ca：16k 粤语。"
      },
      {
        "name": "SourceType",
        "desc": "语音数据来源。0：语音 URL；1：语音数据（post body）。"
      },
      {
        "name": "VoiceFormat",
        "desc": "识别音频的音频格式。mp3、wav。"
      },
      {
        "name": "UsrAudioKey",
        "desc": "用户端对此任务的唯一标识，用户自助生成，用于用户查找识别结果。"
      },
      {
        "name": "Url",
        "desc": "语音 URL，公网可下载。当 SourceType 值为 0（语音 URL上传） 时须填写该字段，为 1 时不填；URL 的长度大于 0，小于 2048，需进行urlencode编码。音频时间长度要小于60s。"
      },
      {
        "name": "Data",
        "desc": "语音数据，当SourceType 值为1（本地语音数据上传）时必须填写，当SourceType 值为0（语音 URL上传）可不写。要使用base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于600KB。"
      },
      {
        "name": "DataLen",
        "desc": "数据长度，单位为字节。当 SourceType 值为1（本地语音数据上传）时必须填写，当 SourceType 值为0（语音 URL上传）可不写（此数据长度为数据未进行base64编码时的数据长度）。"
      },
      {
        "name": "HotwordId",
        "desc": "热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。"
      }
    ],
    "desc": "本接口用于对60秒之内的短音频文件进行识别。\n<br>•   支持中文普通话、英语、粤语。\n<br>•   支持本地语音文件上传和语音URL上传两种请求方式。\n<br>•   音频格式支持wav、mp3；采样率支持8000Hz或者16000Hz；采样精度支持16bits；声道支持单声道。\n<br>•   当音频文件通过请求中body内容上传时，请求大小不能超过600KB；当音频以URL方式传输时，音频时长不可超过60s。\n<br>•   所有请求参数放在POST请求的body中，编码类型采用x-www-form-urlencoded，参数进行urlencode编码后传输。"
  }
}