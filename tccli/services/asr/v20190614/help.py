# -*- coding: utf-8 -*-
DESC = "asr-2019-06-14"
INFO = {
  "GetAsrVocabList": {
    "params": [],
    "desc": "用户通过该接口，可获得所有的热词表及其信息。"
  },
  "CreateRecTask": {
    "params": [
      {
        "name": "EngineModelType",
        "desc": "引擎模型类型。\n电话场景：\n• 8k_zh：电话 8k 中文普通话通用（可用于双声道音频）；\n• 8k_zh_s：电话 8k 中文普通话话者分离（仅适用于单声道音频）；\n非电话场景：\n• 16k_zh：16k 中文普通话通用；\n• 16k_zh_video：16k 音视频领域；\n• 16k_en：16k 英语；\n• 16k_ca：16k 粤语；\n• 16k_ja：16k 日语；"
      },
      {
        "name": "ChannelNum",
        "desc": "语音声道数。1：单声道；2：双声道（仅支持 8k_zh 引擎模型）。"
      },
      {
        "name": "ResTextFormat",
        "desc": "识别结果返回形式。0： 识别结果文本(含分段时间戳)； 1：仅支持16k中文引擎，含识别结果详情(词时间戳列表，一般用于生成字幕场景)。"
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
        "desc": "语音的URL地址，需要公网可下载。长度小于2048字节，当 SourceType 值为 0 时须填写该字段，为 1 时不需要填写。注意：请确保录音文件时长在5个小时之内，否则可能识别失败。请保证文件的下载速度，否则可能下载失败。"
      },
      {
        "name": "Data",
        "desc": "语音数据，当SourceType 值为1时必须填写，为0可不写。要base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于5MB。"
      },
      {
        "name": "DataLen",
        "desc": "数据长度，非必填（此数据长度为数据未进行base64编码时的数据长度）。"
      },
      {
        "name": "HotwordId",
        "desc": "热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。"
      },
      {
        "name": "FilterDirty",
        "desc": "是否过滤脏词（目前支持中文普通话引擎）。0：不过滤脏词；1：过滤脏词；2：将脏词替换为 * 。默认值为 0。"
      },
      {
        "name": "FilterModal",
        "desc": "是否过语气词（目前支持中文普通话引擎）。0：不过滤语气词；1：部分过滤；2：严格过滤 。默认值为 0。"
      },
      {
        "name": "ConvertNumMode",
        "desc": "是否进行阿拉伯数字智能转换（目前支持中文普通话引擎）。0：不转换，直接输出中文数字，1：根据场景智能转换为阿拉伯数字。默认值为 1。"
      },
      {
        "name": "Extra",
        "desc": "附加参数"
      },
      {
        "name": "SpeakerDiarization",
        "desc": "是否开启话者分离，0：不开启，1：开启(仅支持8k_zh/16k_zh引擎模型，单声道音频)"
      },
      {
        "name": "SpeakerNumber",
        "desc": "话者分离人数（需配合开启话者分离使用），支持2-10（8k_zh仅支持2， 16k_zh支持2-10）\n注：话者分离目前是beta版本，请根据您的需要谨慎使用"
      },
      {
        "name": "FilterPunc",
        "desc": "是否过滤标点符号（目前支持中文普通话引擎）。 0：不过滤，1：过滤句末标点，2：过滤所有标点。默认为0。"
      }
    ],
    "desc": "本接口服务对时长5小时以内的录音文件进行识别，异步返回识别全部结果， HTTP RESTful 形式。\n<br>• 支持中文普通话、英语、粤语和日语\n<br>• 支持通用、音视频领域\n<br>• 支持wav、mp3、m4a的音频格式\n<br>• 支持语音 URL 和本地语音文件两种请求方式\n<br>• 语音 URL 的音频时长不能长于5小时，文件大小不超过512MB\n<br>• 本地语音文件不能大于5MB\n<br>• 支持回调或轮询的方式获取结果，结果获取请参考[ 录音文件识别结果查询](https://cloud.tencent.com/document/product/1093/37822)。"
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
  "SetVocabState": {
    "params": [
      {
        "name": "VocabId",
        "desc": "热词表ID。"
      },
      {
        "name": "State",
        "desc": "热词表状态，1：设为默认状态；0：设为非默认状态。"
      }
    ],
    "desc": "用户通过该接口可以设置热词表的默认状态。初始状态为0，用户可设置状态为1，即为默认状态。默认状态表示用户在请求识别时，如不设置热词表ID，则默认使用状态为1的热词表。"
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
  "DownloadAsrVocab": {
    "params": [
      {
        "name": "VocabId",
        "desc": "词表ID。"
      }
    ],
    "desc": "用户通过本接口进行热词表的下载，获得词表权重文件形式的 base64 值，文件形式为通过 “|” 分割的词和权重，即 word|weight 的形式。"
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
        "desc": "引擎模型类型。\n电话场景：\n• 8k_zh：电话 8k 中文普通话通用；\n非电话场景：\n• 16k_zh：16k 中文普通话通用；\n• 16k_en：16k 英语；\n• 16k_ca：16k 粤语；\n• 16k_ja：16k 日语；"
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
        "desc": "语音数据，当SourceType 值为1（本地语音数据上传）时必须填写，当SourceType 值为0（语音 URL上传）可不写。要使用base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。数据长度要小于3MB（Base64后）。"
      },
      {
        "name": "DataLen",
        "desc": "数据长度，单位为字节。当 SourceType 值为1（本地语音数据上传）时必须填写，当 SourceType 值为0（语音 URL上传）可不写（此数据长度为数据未进行base64编码时的数据长度）。"
      },
      {
        "name": "HotwordId",
        "desc": "热词id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词id设置，自动生效默认热词；如果进行了单独的热词id设置，那么将生效单独设置的热词id。"
      },
      {
        "name": "FilterDirty",
        "desc": "是否过滤脏词（目前支持中文普通话引擎）。0：不过滤脏词；1：过滤脏词；2：将脏词替换为 * 。"
      },
      {
        "name": "FilterModal",
        "desc": "是否过语气词（目前支持中文普通话引擎）。0：不过滤语气词；1：部分过滤；2：严格过滤 。"
      },
      {
        "name": "FilterPunc",
        "desc": "是否过滤标点符号（目前支持中文普通话引擎）。 0：不过滤，1：过滤句末标点，2：过滤所有标点。默认为0。"
      },
      {
        "name": "ConvertNumMode",
        "desc": "是否进行阿拉伯数字智能转换。0：不转换，直接输出中文数字，1：根据场景智能转换为阿拉伯数字。默认值为1"
      }
    ],
    "desc": "本接口用于对60秒之内的短音频文件进行识别。\n<br>•   支持中文普通话、英语、粤语、日语。\n<br>•   支持本地语音文件上传和语音URL上传两种请求方式，音频时长不能超过60s。\n<br>•   音频格式支持wav、mp3；采样率支持8000Hz或者16000Hz；采样精度支持16bits；声道支持单声道。\n<br>•   当音频文件通过请求中body内容上传时，请求大小不能超过3MB。\n<br>•   所有请求参数放在POST请求的body中，编码类型采用x-www-form-urlencoded，参数进行urlencode编码后传输。"
  }
}