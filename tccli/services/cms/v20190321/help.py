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
    "desc": "视频内容检测（Video Moderation, VM）服务能识别涉黄、涉政、涉恐等违规视频，同时支持用户配置视频黑库，打击自定义的违规内容。"
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
    "desc": "音频内容检测（Audio Moderation, AM）服务使用了波形分析、声纹分析等技术，能识别涉黄、涉政、涉恐等违规音频，同时支持用户配置音频黑库，打击自定义的违规内容。"
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
  }
}