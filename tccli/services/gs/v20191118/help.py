# -*- coding: utf-8 -*-
DESC = "gs-2019-11-18"
INFO = {
  "CreateSession": {
    "params": [
      {
        "name": "ClientSession",
        "desc": "客户端session信息，从JSSDK请求中获得"
      },
      {
        "name": "UserId",
        "desc": "游戏用户ID"
      },
      {
        "name": "GameId",
        "desc": "游戏ID"
      },
      {
        "name": "GameRegion",
        "desc": "游戏区域，ap-guangzhou、ap-shanghai、ap-beijing等"
      },
      {
        "name": "GameParas",
        "desc": "游戏参数"
      },
      {
        "name": "Resolution",
        "desc": "分辨率,，可设置为1080p或720p"
      },
      {
        "name": "ImageUrl",
        "desc": "背景图url，格式为png或jpeg，宽高1920*1080"
      },
      {
        "name": "SetNo",
        "desc": "资源池编号，1表示正式，2表示测试"
      },
      {
        "name": "Bitrate",
        "desc": "单位Mbps，固定码率，后端不动态调整(MaxBitrate和MinBitrate将无效)"
      },
      {
        "name": "MaxBitrate",
        "desc": "单位Mbps，动态调整最大码率"
      },
      {
        "name": "MinBitrate",
        "desc": "单位Mbps，动态调整最小码率"
      },
      {
        "name": "Fps",
        "desc": "帧率，可设置为30、45或60"
      },
      {
        "name": "UserIp",
        "desc": "游戏用户IP，用于就近调度，例如125.127.178.228"
      },
      {
        "name": "Optimization",
        "desc": "优化项，便于客户灰度开启新的优化项，默认为0"
      }
    ],
    "desc": "创建会话"
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
  "TrylockWorker": {
    "params": [
      {
        "name": "UserId",
        "desc": "游戏用户ID"
      },
      {
        "name": "GameId",
        "desc": "游戏ID"
      },
      {
        "name": "GameRegion",
        "desc": "游戏区域，ap-guangzhou、ap-shanghai、ap-beijing等"
      },
      {
        "name": "SetNo",
        "desc": "资源池编号，1表示共用，2表示测试"
      },
      {
        "name": "UserIp",
        "desc": "游戏用户IP，用于就近调度，例如125.127.178.228"
      },
      {
        "name": "GroupId",
        "desc": "分组ID"
      }
    ],
    "desc": "尝试锁定机器"
  }
}