# -*- coding: utf-8 -*-
DESC = "gme-2018-07-11"
INFO = {
  "DescribeFilterResult": {
    "params": [
      {
        "name": "BizId",
        "desc": "应用ID"
      },
      {
        "name": "FileId",
        "desc": "文件ID"
      }
    ],
    "desc": "根据应用ID和文件ID查询识别结果"
  },
  "DescribeAppStatistics": {
    "params": [
      {
        "name": "BizId",
        "desc": "GME应用ID"
      },
      {
        "name": "StartDate",
        "desc": "数据开始时间，东八区时间，格式: 年-月-日，如: 2018-07-13"
      },
      {
        "name": "EndDate",
        "desc": "数据结束时间，东八区时间，格式: 年-月-日，如: 2018-07-13"
      },
      {
        "name": "Services",
        "desc": "要查询的服务列表，取值：RealTimeSpeech/VoiceMessage/VoiceFilter"
      }
    ],
    "desc": "本接口(DescribeAppStatistics)用于获取某个GME应用的用量数据。包括实时语音，语音消息及转文本，语音分析等。最长查询周期为最近30天。"
  },
  "DescribeScanResultList": {
    "params": [
      {
        "name": "BizId",
        "desc": "应用 ID，登录[控制台](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID"
      },
      {
        "name": "TaskIdList",
        "desc": "查询的任务 ID 列表，任务 ID 列表最多支持 100 个。"
      },
      {
        "name": "Limit",
        "desc": "任务返回结果数量，默认10，上限500。大文件任务忽略此参数，返回全量结果"
      }
    ],
    "desc": "本接口(DescribeScanResultList)用于查询语音检测结果，查询任务列表最多支持100个。\n<p style=\"color:red\">如果在提交语音检测任务时未设置 Callback 字段，则需要通过本接口获取检测结果</p>"
  },
  "VoiceFilter": {
    "params": [
      {
        "name": "BizId",
        "desc": "应用ID，登录[控制台](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID"
      },
      {
        "name": "FileId",
        "desc": "文件ID，表示文件唯一ID"
      },
      {
        "name": "FileName",
        "desc": "文件名"
      },
      {
        "name": "FileUrl",
        "desc": "文件url，urlencode编码，FileUrl和FileContent二选一"
      },
      {
        "name": "FileContent",
        "desc": "文件内容，base64编码，FileUrl和FileContent二选一"
      },
      {
        "name": "OpenId",
        "desc": "用户ID"
      }
    ],
    "desc": "本接口用于识别涉黄、涉政等违规音频，成功会回调配置在应用的回调地址。回调示例如下：\n{\"BizId\":0,\"FileId\":\"test_file_id\",\"FileName\":\"test_file_name\",\"FileUrl\":\"test_file_url\",\"OpenId\":\"test_open_id\",\"TimeStamp\":\"0000-00-00 00:00:00\",\"Data\":[{\"Type\":1,\"Word\":\"xx\"}]}\nType表示过滤类型，1：政治，2：色情，3：谩骂"
  },
  "DescribeFilterResultList": {
    "params": [
      {
        "name": "BizId",
        "desc": "应用ID"
      },
      {
        "name": "StartDate",
        "desc": "开始时间，格式为 年-月-日，如: 2018-07-11"
      },
      {
        "name": "EndDate",
        "desc": "结束时间，格式为 年-月-日，如: 2018-07-11"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认值为10，最大值为100。"
      }
    ],
    "desc": "根据日期查询识别结果列表"
  },
  "ScanVoice": {
    "params": [
      {
        "name": "BizId",
        "desc": "应用ID，登录[控制台 - 服务管理](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID"
      },
      {
        "name": "Scenes",
        "desc": "语音检测场景，参数值目前要求为 default。 预留场景设置： 谩骂、色情、涉政、广告、暴恐、违禁等场景，<a href=\"#Label_Value\">具体取值见上述 Label 说明。</a>"
      },
      {
        "name": "Live",
        "desc": "是否为直播流。值为 false 时表示普通语音文件检测；为 true 时表示语音流检测。"
      },
      {
        "name": "Tasks",
        "desc": "语音检测任务列表，列表最多支持100个检测任务。结构体中包含：\n<li>DataId：数据的唯一ID</li>\n<li>Url：数据文件的url，为 urlencode 编码，流式则为拉流地址</li>"
      },
      {
        "name": "Callback",
        "desc": "异步检测结果回调地址，具体见上述<a href=\"#Callback_Declare\">回调相关说明</a>。（说明：该字段为空时，必须通过接口(查询语音检测结果)获取检测结果）。"
      }
    ],
    "desc": "本接口(ScanVoice)用于提交语音检测任务，检测任务列表最多支持100个。使用前请您登录[控制台 - 服务配置](https://console.cloud.tencent.com/gamegme/conf)开启语音分析服务。\n</br></br>\n\n<h4><b>功能试用说明：</b></h4>\n<li>打开前往<a href=\"https://console.cloud.tencent.com/gamegme/tryout\">控制台 - 产品试用</a>免费试用语音分析服务。</li>\n</br>\n\n<h4><b>接口功能说明：</b></h4>\n<li>支持对语音流或语音文件进行检测，判断其中是否包含违规内容。</li>\n<li>支持设置回调地址 Callback 获取检测结果，同时支持通过接口(查询语音检测结果)主动轮询获取检测结果。</li>\n<li>支持场景输入，包括：谩骂、色情、涉政等场景</li>\n<li>支持批量提交检测任务。检测任务列表最多支持100个。</li>\n</br>\n<h4><b>音频文件限制说明：</b></h4>\n<li>音频文件大小限制：100 M</li>\n<li>音频文件时长限制：30分钟</li>\n<li>音频文件格式支持的类型：.wav、.m4a、.amr、.mp3、.aac、.wma、.ogg</li>\n</br>\n<h4><b>语音流限制说明：</b></h4>\n<li>语音流格式支持的类型：.m3u8、.flv</li>\n<li>语音流支持的传输协议：RTMP、HTTP、HTTPS</li>\n<li>语音流时长限制：4小时</li>\n<li>支持音视频流分离并对音频流进行分析</li>\n</br>\n<h4 id=\"Label_Value\"><b>Scenes 与 Label 参数说明：</b></h4>\n<p>提交语音检测任务时，需要指定 Scenes 场景参数，<font color=\"red\">目前要求您设置 Scenes 参数值为：[\"default\"]</font>；而在检测结果中，则包含请求时指定的场景，以及对应类型的检测结果。</p>\n<table>\n<thread>\n<tr>\n<th>场景</th>\n<th>描述</th>\n<th>Label</th>\n</tr>\n</thread>\n<tbody>\n<tr>\n<td>语音检测</td>\n<td>语音检测的检测类型</td>\n<td>\n<p>normal:正常文本</p>\n<p>porn:色情</p>\n<p>politics:涉政</p>\n<p>abuse:谩骂</p>\n<p>ad :广告</p>\n<p>terrorism:暴恐</p>\n<p>contraband :违禁</p>\n<p>customized:自定义词库。目前白名单开放，如有需要请<a href=\"https://cloud.tencent.com/apply/p/8809fjcik56\">联系我们</a>。</p>\n</td>\n</tr>\n</tbody>\n</table>\n</br>\n<h4 id=\"Callback_Declare\"><b>回调相关说明：</b></h4>\n<li>如果在请求参数中指定了回调地址参数 Callback，即一个 HTTP(S) 协议接口的 URL，则需要支持 POST 方法，传输数据编码采用 UTF-8。</li>\n<li>在推送回调数据后，接收到的 HTTP 状态码为 200 时，表示推送成功。</li>\n<li>HTTP 头参数说明：</li>\n<table>\n<thread>\n<tr>\n<th>名称</th>\n<th>类型</th>\n<th>是否必需</th>\n<th>描述</th>\n</tr>\n</thread>\n<tbody>\n<tr>\n<td>Signatue</td>\n<td>string</td>\n<td>是</td>\n<td>签名，具体见<a href=\"#Callback_Signatue\">签名生成说明</a></td>\n</tr>\n</tbody>\n</table>\n<ul  id=\"Callback_Signatue\">\n\t<li>签名生成说明：</li>\n\t<ul>\n\t\t<li>使用 HMAC-SH1 算法, 最终结果做 BASE64 编码;</li>\n\t\t<li>签名原文串为 POST+body 的整个json内容(长度以 Content-Length 为准);</li>\n\t\t<li>签名key为应用的 SecretKey，可以通过控制台查看。</li>\n\t</ul>\n</ul>\n\n<li>回调示例如下<font color=\"red\">（详细字段说明见结构：\n<a href=\"https://cloud.tencent.com/document/api/607/35375#DescribeScanResult\" target=\"_blank\">DescribeScanResult</a>）</font>：</li>\n<pre><code>{\n\t\"Code\": 0,\n\t\"DataId\": \"1400000000_test_data_id\",\n\t\"ScanFinishTime\": 1566720906,\n\t\"HitFlag\": true,\n\t\"Live\": false,\n\t\"Msg\": \"\",\n\t\"ScanPiece\": [{\n\t\t\"DumpUrl\": \"\",\n\t\t\"HitFlag\": true,\n\t\t\"MainType\": \"abuse\",\n\t\t\"RoomId\": \"123\",\n\t\t\"OpenId\": \"xxx\",\n\t\t\"Info\":\"\",\n\t\t\"Offset\": 0,\n\t\t\"Duration\": 3400,\n\t\t\"PieceStartTime\":1574684231,\n\t\t\"ScanDetail\": [{\n\t\t\t\"EndTime\": 1110,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 1110\n\t\t}, {\n\t\t\t\"EndTime\": 1380,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 930\n\t\t}, {\n\t\t\t\"EndTime\": 1560,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 930\n\t\t}, {\n\t\t\t\"EndTime\": 2820,\n\t\t\t\"KeyWord\": \"xxx\",\n\t\t\t\"Label\": \"abuse\",\n\t\t\t\"Rate\": \"90.00\",\n\t\t\t\"StartTime\": 2490\n\t\t}]\n\t}],\n\t\"ScanStartTime\": 1566720905,\n\t\"Scenes\": [\n\t\t\"default\"\n\t],\n\t\"Status\": \"Success\",\n\t\"TaskId\": \"xxx\",\n\t\"Url\": \"https://xxx/xxx.m4a\"\n}\n</code></pre>"
  },
  "CreateApp": {
    "params": [
      {
        "name": "AppName",
        "desc": "应用名称"
      },
      {
        "name": "ProjectId",
        "desc": "腾讯云项目ID，默认为0，表示默认项目"
      },
      {
        "name": "EngineList",
        "desc": "需要支持的引擎列表，默认全选。"
      },
      {
        "name": "RegionList",
        "desc": "服务区域列表，默认全选。"
      },
      {
        "name": "RealtimeSpeechConf",
        "desc": "实时语音服务配置数据"
      },
      {
        "name": "VoiceMessageConf",
        "desc": "语音消息及转文本服务配置数据"
      },
      {
        "name": "VoiceFilterConf",
        "desc": "语音分析服务配置数据"
      },
      {
        "name": "Tags",
        "desc": "需要添加的标签列表"
      }
    ],
    "desc": "本接口(CreateApp)用于创建一个GME应用。"
  },
  "ModifyAppStatus": {
    "params": [
      {
        "name": "BizId",
        "desc": "应用ID，创建应用后由后台生成并返回。"
      },
      {
        "name": "Status",
        "desc": "应用状态，取值：open/close"
      }
    ],
    "desc": "本接口(ModifyAppStatus)用于修改应用总开关状态。"
  }
}