# -*- coding: utf-8 -*-
DESC = "gs-2019-11-18"
INFO = {
  "DescribeWorkers": {
    "params": [
      {
        "name": "SetNo",
        "desc": "资源池编号，值为2的幂，1表示共用，2表示测试"
      }
    ],
    "desc": "查询空闲机器数量"
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
      }
    ],
    "desc": "尝试锁定机器"
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
        "desc": "游戏区域"
      },
      {
        "name": "GameParas",
        "desc": "游戏参数"
      },
      {
        "name": "Resolution",
        "desc": "分辨率"
      },
      {
        "name": "ImageUrl",
        "desc": "背景图url"
      },
      {
        "name": "SetNo",
        "desc": "资源池编号"
      }
    ],
    "desc": "创建会话"
  }
}