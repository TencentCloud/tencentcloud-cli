# -*- coding: utf-8 -*-
DESC = "ame-2019-09-16"
INFO = {
  "DescribeItemById": {
    "params": [
      {
        "name": "ItemIDs",
        "desc": "歌曲ID，目前暂不支持批量查询"
      }
    ],
    "desc": "根据歌曲ID查询歌曲信息"
  },
  "ReportData": {
    "params": [
      {
        "name": "ReportData",
        "desc": "上报数据\n注:reportData为客户端压缩后的上报数据进行16进制转换的字符串数据\n压缩说明：\na) 上报的json格式字符串通过流的转换（ByteArrayInputStream, java.util.zip.GZIPOutputStream），获取到压缩后的字节数组。\nb) 将压缩后的字节数组转成16进制字符串。\n\nreportData由两部分数据组成：\n1）report_type（上报类型）\n2）data（歌曲上报数据）\n不同的report_type对应的data数据结构不一样。\n\n详细说明请参考文档reportdata.docx：\nhttps://github.com/ame-demo/doc"
      }
    ],
    "desc": "客户上报用户数据功能，为了更好的为用户提供优质服务"
  },
  "DescribeLyric": {
    "params": [
      {
        "name": "ItemId",
        "desc": "歌曲ID"
      },
      {
        "name": "SubItemType",
        "desc": "歌词格式，可选项，可不填写，目前填写只能填LRC-LRC。该字段为预留的扩展字段。后续如果不填，会返回歌曲的所有格式的歌词。如果填写某个正确的格式，则只返回该格式的歌词。"
      }
    ],
    "desc": "根据接口的模式及歌曲ID来取得歌词信息。"
  },
  "DescribeItems": {
    "params": [
      {
        "name": "Offset",
        "desc": "offset (Default = 0)，(当前页-1) * Limit"
      },
      {
        "name": "Limit",
        "desc": "条数，必须大于0，最大值为30"
      },
      {
        "name": "CategoryId",
        "desc": "（电台/歌单）ID，CategoryId和CategoryCode两个必传1个，可以从<a href=\"https://cloud.tencent.com/document/product/1155/40109\">获取分类内容（Station）列表接口</a>中获取。"
      },
      {
        "name": "CategoryCode",
        "desc": "（电台/歌单）ID，CategoryId和CategoryCode两个必传1个，可以从<a href=\"https://cloud.tencent.com/document/product/1155/40109\">获取分类内容（Station）列表接口</a>中获取。"
      }
    ],
    "desc": "分类内容下歌曲列表获取，根据CategoryID或CategoryCode"
  },
  "DescribeMusic": {
    "params": [
      {
        "name": "ItemId",
        "desc": "歌曲ID"
      },
      {
        "name": "IdentityId",
        "desc": "在应用前端播放音乐C端用户的唯一标识。无需是账户信息，用户唯一标识即可。"
      },
      {
        "name": "SubItemType",
        "desc": "填 MP3-64K-FTD-P 获取歌曲热门片段"
      },
      {
        "name": "Ssl",
        "desc": "CDN URL Protocol:HTTP or HTTPS/SSL\nValues:Y , N(default)"
      }
    ],
    "desc": "根据接口的模式及歌曲ID来取得对应权限的歌曲播放地址等信息。"
  },
  "DescribeStations": {
    "params": [
      {
        "name": "Limit",
        "desc": "条数，必须大于0"
      },
      {
        "name": "Offset",
        "desc": "offset (Default = 0)，(当前页-1) * Limit"
      }
    ],
    "desc": "获取素材库列表时使用"
  }
}