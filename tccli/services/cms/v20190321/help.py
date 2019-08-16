# -*- coding: utf-8 -*-
DESC = "cms-2019-03-21"
INFO = {
  "DescribeModerationOverview": {
    "params": [
      {
        "name": "Date",
        "desc": "日期，如2019-01-01， 查询该日期的概览数据"
      },
      {
        "name": "ServiceTypes",
        "desc": "服务类型数组，可以动态配置，Text:文本，Image:图片，Audio:音频，Video:视频, 使用\"ALL\"表示所有类型, 不区分大小写，如 [\"Text\", \"Image\"]查询文本和图片服务的数据，[\"all\"]查询所有服务的数据。"
      },
      {
        "name": "Channels",
        "desc": "渠道号数组，1:直播 2:点播 3:IM 4:GME，统计指定渠道组合的汇总数据，如[1,2]表示获取直播和点播两个渠道的汇总数据，不填[]为所有渠道汇总数据"
      }
    ],
    "desc": "根据日期，渠道和服务类型查询识别结果概览数据"
  },
  "DeleteTextSample": {
    "params": [
      {
        "name": "Ids",
        "desc": "唯一标识数组，目前暂时只支持单个删除"
      }
    ],
    "desc": "删除文字样本库，暂时只支持单个删除"
  },
  "CreateTextSample": {
    "params": [
      {
        "name": "Contents",
        "desc": "关键词数组"
      },
      {
        "name": "EvilType",
        "desc": "恶意类型\n100：正常\n20001：政治\n20002：色情 \n20006：涉毒违法\n20007：谩骂 \n24001：暴恐\n21000：综合\n20105：广告引流"
      },
      {
        "name": "Label",
        "desc": "样本类型\n1：黑库\n2：白库"
      }
    ],
    "desc": "新增文本类型样本库"
  },
  "VideoModeration": {
    "params": [
      {
        "name": "CallbackUrl",
        "desc": "回调Url"
      },
      {
        "name": "FileMD5",
        "desc": "视频文件MD5"
      },
      {
        "name": "FileContent",
        "desc": "视频内容base64"
      },
      {
        "name": "FileUrl",
        "desc": "视频内容Url,其中FileUrl与FileContent二选一"
      }
    ],
    "desc": "视频内容检测（Video Moderation, VM）服务能识别涉黄、涉政、涉恐等违规视频，同时支持用户配置视频黑库，打击自定义的违规内容。\n\n<br>\n接口返回值说明：调用本接口有两个返回值，一个是同步返回值，一个是识别完成后的异步回调返回值。\n\n视频识别结果存在于异步回调返回值中，异步回调返回值明细：\n\n参数名 | 类型 | 描述\n-|-|-\nSeqID | String | 请求seqId唯一标识\nEvilFlag | Integer | 是否恶意：0正常，1可疑（Homology模块下：0未匹配到，1恶意，2白样本）\nEvilType | Integer | 恶意类型：100正常，20001政治，20002色情\nDuration | Integer | 视频时长（单位：秒）\nPornDetect |  | 视频智能鉴黄\nPolityDetect | | 视频涉政识别\nHomology | | 相似度识别\nHitFlag | Integer  | 0正常，1可疑\nScore | Integer | 判断分值\nSeedUrl | String | 命中的种子URL"
  },
  "CreateFileSample": {
    "params": [
      {
        "name": "Contents",
        "desc": "文件类型结构数组"
      },
      {
        "name": "EvilType",
        "desc": "恶意类型\n100：正常\n20001：政治\n20002：色情 \n20006：涉毒违法\n20007：谩骂 \n24001：暴恐\n21000：综合\n20105：广告引流"
      },
      {
        "name": "FileType",
        "desc": "文件类型\nimage：图片\naudio：音频\nvideo：视频"
      },
      {
        "name": "Label",
        "desc": "样本类型\n1：黑库\n2：白库"
      }
    ],
    "desc": "通过该接口可以将文件新增到样本库"
  },
  "AudioModeration": {
    "params": [
      {
        "name": "CallbackUrl",
        "desc": "回调url"
      },
      {
        "name": "FileContent",
        "desc": "音频内容的base64"
      },
      {
        "name": "FileMD5",
        "desc": "音频文件的MD5值"
      },
      {
        "name": "FileUrl",
        "desc": "音频内容Url ，其中FileUrl和FileContent二选一"
      }
    ],
    "desc": "音频内容检测（Audio Moderation, AM）服务使用了波形分析、声纹分析等技术，能识别涉黄、涉政、涉恐等违规音频，同时支持用户配置音频黑库，打击自定义的违规内容。\n\n<br>\n接口返回值说明：调用本接口有两个返回值，一个是同步返回值，一个是识别完成后的异步回调返回值。\n\n音频识别结果存在于异步回调返回值中，异步回调返回值明细：\n\n参数名 | 类型 | 描述\n-|-|-\nSeqID | String | 请求seqId唯一标识\nEvilFlag | Integer | 是否恶意：0正常，1可疑（Homology模块下：0未匹配到，1恶意，2白样本）\nEvilType | Integer | 恶意类型：100正常，20001政治，20002色情，20007谩骂\nDuration | Integer | 音频时长（单位：毫秒）\nPornDetect | | 音频智能鉴黄\nPolityDetect | | 音频涉政识别\nCurseDetect | | 音频谩骂识别\nHomology | | 相似度识别\nHitFlag | Integer | 0正常，1可疑\nScore | Integer | 判断分值\nKeywords | Array of String | 关键词明细\nStartTime | Array of String | 恶意开始时间\nEndTime | Array of String | 恶意结束时间\nSeedUrl | String | 命中的种子URL"
  },
  "DescribeFileSample": {
    "params": [
      {
        "name": "Filters",
        "desc": "支持通过标签值进行筛选"
      },
      {
        "name": "Limit",
        "desc": "数量限制，默认为20，最大值为100"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "OrderDirection",
        "desc": "升序（asc）还是降序（desc），默认：desc"
      },
      {
        "name": "OrderField",
        "desc": "按某个字段排序，目前仅支持CreatedAt排序"
      }
    ],
    "desc": "查询文件样本库，支持批量查询"
  },
  "DeleteFileSample": {
    "params": [
      {
        "name": "Ids",
        "desc": "唯一标识数组"
      }
    ],
    "desc": "删除文件样本库，支持批量删除，一次提交不超过20个"
  },
  "TextModeration": {
    "params": [
      {
        "name": "Content",
        "desc": "文本内容Base64编码"
      }
    ],
    "desc": "文本内容检测（Text Moderation）服务使用了深度学习技术，识别涉黄、涉政、涉恐等有害内容，同时支持用户配置词库，打击自定义的违规文本。"
  },
  "ImageModeration": {
    "params": [
      {
        "name": "FileContent",
        "desc": "文件内容 Base64,与FileUrl必须二填一"
      },
      {
        "name": "FileMD5",
        "desc": "文件MD5值"
      },
      {
        "name": "FileUrl",
        "desc": "文件地址"
      }
    ],
    "desc": "图片内容检测服务（Image Moderation, IM）能自动扫描图片，识别涉黄、涉恐、涉政、涉毒等有害内容，同时支持用户配置图片黑名单，打击自定义的违规图片。"
  },
  "DescribeTextSample": {
    "params": [
      {
        "name": "Filters",
        "desc": "支持通过标签值进行筛选"
      },
      {
        "name": "Limit",
        "desc": "数量限制，默认为20，最大值为100"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "OrderDirection",
        "desc": "升序（asc）还是降序（desc），默认：desc"
      },
      {
        "name": "OrderField",
        "desc": "按某个字段排序，目前仅支持CreatedAt排序"
      }
    ],
    "desc": "支持批量查询文字样本库"
  }
}