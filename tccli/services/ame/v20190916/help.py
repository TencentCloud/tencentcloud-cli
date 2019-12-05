# -*- coding: utf-8 -*-
DESC = "ame-2019-09-16"
INFO = {
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
        "desc": "（电台/歌单）ID，CategoryId和CategoryCode两个必传1个"
      },
      {
        "name": "CategoryCode",
        "desc": "（电台/歌单）代码，CategoryId和CategoryCode两个必传1个"
      }
    ],
    "desc": "分类内容下歌曲列表获取，根据CategoryID或CategoryCode"
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
  "DescribeMusic": {
    "params": [
      {
        "name": "ItemId",
        "desc": "歌曲ID"
      },
      {
        "name": "IdentityId",
        "desc": "User identity ID，用来唯一标识用户"
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
  }
}