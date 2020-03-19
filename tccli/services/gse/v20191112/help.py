# -*- coding: utf-8 -*-
DESC = "gse-2019-11-12"
INFO = {
  "UpdateGameServerSession": {
    "params": [
      {
        "name": "GameServerSessionId",
        "desc": "游戏服务器会话ID"
      },
      {
        "name": "MaximumPlayerSessionCount",
        "desc": "最大玩家数量"
      },
      {
        "name": "Name",
        "desc": "游戏服务器会话名称"
      },
      {
        "name": "PlayerSessionCreationPolicy",
        "desc": "玩家会话创建策略（ACCEPT_ALL,DENY_ALL）"
      },
      {
        "name": "ProtectionPolicy",
        "desc": "保护策略(NoProtection,TimeLimitProtection,FullProtection)"
      }
    ],
    "desc": "本接口（UpdateGameServerSession）用于更新游戏服务器会话"
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "FleetId",
        "desc": "服务部署ID"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "Offset",
        "desc": "结果返回最大数量"
      },
      {
        "name": "Limit",
        "desc": "返回结果偏移"
      }
    ],
    "desc": "用于查询服务器实例列表"
  },
  "DescribeGameServerSessions": {
    "params": [
      {
        "name": "AliasId",
        "desc": "别名ID"
      },
      {
        "name": "FleetId",
        "desc": "舰队ID"
      },
      {
        "name": "GameServerSessionId",
        "desc": "游戏服务器会话ID"
      },
      {
        "name": "Limit",
        "desc": "单次查询记录数上限"
      },
      {
        "name": "NextToken",
        "desc": "页偏移，用于查询下一页"
      },
      {
        "name": "StatusFilter",
        "desc": "游戏服务器会话状态"
      }
    ],
    "desc": "本接口（DescribeGameServerSessions）用于查询游戏服务器会话列表"
  },
  "GetInstanceAccess": {
    "params": [
      {
        "name": "FleetId",
        "desc": "服务部署Id"
      },
      {
        "name": "InstanceId",
        "desc": "实例Id"
      }
    ],
    "desc": "获取实例登录所需要的凭据"
  },
  "JoinGameServerSession": {
    "params": [
      {
        "name": "GameServerSessionId",
        "desc": "游戏服务器会话ID"
      },
      {
        "name": "PlayerId",
        "desc": "玩家ID"
      },
      {
        "name": "PlayerData",
        "desc": "玩家自定义信息"
      }
    ],
    "desc": "本接口（JoinGameServerSession）用于加入游戏服务器会话"
  },
  "DescribeGameServerSessionPlacement": {
    "params": [
      {
        "name": "PlacementId",
        "desc": "游戏服务器会话放置的唯一标识符"
      }
    ],
    "desc": "本接口（DescribeGameServerSessionPlacement）用于查询游戏服务器会话的放置"
  },
  "DescribeGameServerSessionDetails": {
    "params": [
      {
        "name": "AliasId",
        "desc": "别名ID"
      },
      {
        "name": "FleetId",
        "desc": "舰队ID"
      },
      {
        "name": "GameServerSessionId",
        "desc": "游戏服务器会话ID"
      },
      {
        "name": "Limit",
        "desc": "单次查询记录数上限"
      },
      {
        "name": "NextToken",
        "desc": "页偏移，用于查询下一页"
      },
      {
        "name": "StatusFilter",
        "desc": "游戏服务器会话状态(ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR)"
      }
    ],
    "desc": "本接口（DescribeGameServerSessionDetails）用于查询游戏服务器会话详情列表"
  },
  "StartGameServerSessionPlacement": {
    "params": [
      {
        "name": "PlacementId",
        "desc": "开始部署游戏服务器会话的唯一标识符"
      },
      {
        "name": "GameServerSessionQueueName",
        "desc": "游戏服务器会话队列名称"
      },
      {
        "name": "MaximumPlayerSessionCount",
        "desc": "游戏服务器允许同时连接到游戏会话的最大玩家数量"
      },
      {
        "name": "DesiredPlayerSessions",
        "desc": "玩家游戏会话信息"
      },
      {
        "name": "GameProperties",
        "desc": "玩家游戏会话属性"
      },
      {
        "name": "GameServerSessionData",
        "desc": "游戏服务器会话数据"
      },
      {
        "name": "GameServerSessionName",
        "desc": "游戏服务器会话名称"
      },
      {
        "name": "PlayerLatencies",
        "desc": "玩家延迟"
      }
    ],
    "desc": "本接口（StartGameServerSessionPlacement）用于开始放置游戏服务器会话"
  },
  "DescribePlayerSessions": {
    "params": [
      {
        "name": "GameServerSessionId",
        "desc": "游戏服务器会话ID"
      },
      {
        "name": "Limit",
        "desc": "单次查询记录数上限"
      },
      {
        "name": "NextToken",
        "desc": "页偏移，用于查询下一页"
      },
      {
        "name": "PlayerId",
        "desc": "玩家ID"
      },
      {
        "name": "PlayerSessionId",
        "desc": "玩家会话ID"
      },
      {
        "name": "PlayerSessionStatusFilter",
        "desc": "玩家会话状态（RESERVED,ACTIVE,COMPLETED,TIMEDOUT）"
      }
    ],
    "desc": "本接口（DescribePlayerSessions）用于获取玩家会话列表"
  },
  "GetGameServerSessionLogUrl": {
    "params": [
      {
        "name": "GameServerSessionId",
        "desc": "游戏服务器会话ID"
      }
    ],
    "desc": "本接口（GetGameServerSessionLogUrl）用于获取游戏服务器会话的日志URL"
  },
  "StopGameServerSessionPlacement": {
    "params": [
      {
        "name": "PlacementId",
        "desc": "游戏服务器会话放置的唯一标识符"
      }
    ],
    "desc": "本接口（StopGameServerSessionPlacement）用于停止放置游戏服务器会话"
  },
  "CreateGameServerSession": {
    "params": [
      {
        "name": "MaximumPlayerSessionCount",
        "desc": "最大玩家数量"
      },
      {
        "name": "AliasId",
        "desc": "别名ID"
      },
      {
        "name": "CreatorId",
        "desc": "创建者ID"
      },
      {
        "name": "FleetId",
        "desc": "舰队ID"
      },
      {
        "name": "GameProperties",
        "desc": "游戏属性"
      },
      {
        "name": "GameServerSessionData",
        "desc": "游戏服务器会话属性详情"
      },
      {
        "name": "GameServerSessionId",
        "desc": "游戏服务器会话自定义ID"
      },
      {
        "name": "IdempotencyToken",
        "desc": "幂等token"
      },
      {
        "name": "Name",
        "desc": "游戏服务器会话名称"
      }
    ],
    "desc": "本接口（CreateGameServerSession）用于创建游戏服务会话"
  }
}