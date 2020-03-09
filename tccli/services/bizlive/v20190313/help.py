# -*- coding: utf-8 -*-
DESC = "bizlive-2019-03-13"
INFO = {
  "ForbidLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的推流域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "ResumeTime",
        "desc": "恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。\n注意：默认禁播90天，且最长支持禁播90天。"
      }
    ],
    "desc": "禁止某条流的推送，可以预设某个时刻将流恢复。"
  },
  "StopGame": {
    "params": [
      {
        "name": "UserId",
        "desc": "游戏用户ID"
      }
    ],
    "desc": "强制退出游戏"
  },
  "RegisterIM": {
    "params": [
      {
        "name": "Nickname",
        "desc": "用户昵称"
      },
      {
        "name": "UserId",
        "desc": "用户唯一ID，建议采用用户小程序OpenID加盐形式"
      },
      {
        "name": "HeadImgUrl",
        "desc": "用户头像URL"
      },
      {
        "name": "Level",
        "desc": "用户身份，默认值：0，表示无特殊身份"
      }
    ],
    "desc": "注册聊天室"
  },
  "DescribeWorkers": {
    "params": [],
    "desc": "查询空闲机器数量"
  },
  "DescribeStreamPlayInfoList": {
    "params": [
      {
        "name": "EndTime",
        "desc": "结束时间，北京时间，格式：2019-04-28 10:36:00\n结束时间 和 开始时间  必须在同一天内。"
      },
      {
        "name": "PlayDomain",
        "desc": "播放域名。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间，北京时间，格式：2019-04-28 10:36:00\n当前时间 和 开始时间 间隔不超过30天。"
      },
      {
        "name": "StreamName",
        "desc": "流名称，精确匹配。\n若不填，则为查询总体播放数据。"
      }
    ],
    "desc": "查询播放数据，支持按流名称查询详细播放数据，也可按播放域名查询详细总数据。"
  },
  "CreateSession": {
    "params": [
      {
        "name": "ClientSession",
        "desc": "客户端session信息，从JSSDK请求中获得"
      },
      {
        "name": "GameId",
        "desc": "游戏ID"
      },
      {
        "name": "UserId",
        "desc": "游戏用户ID"
      },
      {
        "name": "GameParas",
        "desc": "游戏参数"
      },
      {
        "name": "GameRegion",
        "desc": "游戏区域"
      },
      {
        "name": "ImageUrl",
        "desc": "背景图url"
      },
      {
        "name": "Resolution",
        "desc": "分辨率"
      }
    ],
    "desc": "创建会话"
  }
}