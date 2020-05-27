# -*- coding: utf-8 -*-
DESC = "cms-2019-03-21"
INFO = {
  "DeleteTextSample": {
    "params": [
      {
        "name": "Ids",
        "desc": "唯一标识数组，目前暂时只支持单个删除"
      }
    ],
    "desc": "本文档适用于文本内容安全、音频内容安全自定义识别库的管理。\n<br>\n删除文本样本库，暂时只支持单个删除。"
  },
  "CreateTextSample": {
    "params": [
      {
        "name": "Contents",
        "desc": "关键词数组"
      },
      {
        "name": "EvilType",
        "desc": "恶意类型\n100：正常\n20001：政治\n20002：色情 \n20006：涉毒违法\n20007：谩骂 \n24001：暴恐\n20105：广告引流"
      },
      {
        "name": "Label",
        "desc": "样本类型\n1：黑库\n2：白库"
      },
      {
        "name": "Test",
        "desc": "测试修改参数"
      }
    ],
    "desc": "本文档适用于文本内容安全、音频内容安全自定义识别库的管理。\n<br>\n通过该接口可以将文本新增到样本库。"
  },
  "CreateFileSample": {
    "params": [
      {
        "name": "Contents",
        "desc": "文件类型结构数组"
      },
      {
        "name": "EvilType",
        "desc": "恶意类型\n100：正常\n20001：政治\n20002：色情 \n20006：涉毒违法\n20007：谩骂 \n24001：暴恐\n20105：广告引流"
      },
      {
        "name": "FileType",
        "desc": "image：图片"
      },
      {
        "name": "Label",
        "desc": "样本类型\n1：黑库\n2：白库"
      }
    ],
    "desc": "本文档适用于图片内容安全、视频内容安全自定义识别库的管理。\n<br>\n通过该接口可以将图片新增到样本库。"
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
    "desc": "本文档适用于文本内容安全、音频内容安全自定义识别库的管理。\n<br>\n支持批量查询文本样本库。"
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
    "desc": "本文档适用于图片内容安全、视频内容安全自定义识别库的管理。\n<br>\n查询图片样本库，支持批量查询。"
  },
  "TextModeration": {
    "params": [
      {
        "name": "Content",
        "desc": "文本内容Base64编码。原文长度需小于15000字节，即5000个汉字以内。"
      },
      {
        "name": "BizType",
        "desc": "该字段用于标识业务场景。您可以在内容安全控制台创建对应的ID，配置不同的内容审核策略，通过接口调用，默认不填为0，后端使用默认策略"
      },
      {
        "name": "DataId",
        "desc": "数据ID，英文字母、下划线、-组成，不超过64个字符"
      },
      {
        "name": "SdkAppId",
        "desc": "业务应用ID"
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
  "DeleteFileSample": {
    "params": [
      {
        "name": "Ids",
        "desc": "唯一标识数组"
      }
    ],
    "desc": "本文档适用于图片内容安全、视频内容安全自定义识别库的管理。\n<br>\n删除图片样本库，支持批量删除，一次提交不超过20个。"
  }
}