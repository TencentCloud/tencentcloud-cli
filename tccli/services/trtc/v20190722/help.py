# -*- coding: utf-8 -*-
DESC = "trtc-2019-07-22"
INFO = {
  "DescribeRealtimeQuality": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      },
      {
        "name": "SdkAppId",
        "desc": "用户sdkappid"
      },
      {
        "name": "DataType",
        "desc": "查询的数据类型\nenterTotalSuccPercent：进房成功率\nfistFreamInSecRate：首帧秒开率\nblockPercent：视频卡顿率\naudioBlockPercent：音频卡顿率"
      }
    ],
    "desc": "查询sdkappid维度下实时质量数据，包括：进房成功率，首帧秒开率，音频卡顿率，视频卡顿率。可查询24小时内数据，查询起止时间不超过1个小时。"
  },
  "DescribeHistoryScale": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "用户sdkappid"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      }
    ],
    "desc": "查询历史房间和用户数，每分钟1次，可查询最近5天的数据"
  },
  "DescribeRealtimeScale": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      },
      {
        "name": "SdkAppId",
        "desc": "用户sdkappid"
      },
      {
        "name": "DataType",
        "desc": "查询的数据类型\nUserNum：通话人数；\nRoomNum：房间数"
      }
    ],
    "desc": "查询sdkappid维度下实时规模，可查询24小时内数据，查询起止时间不超过1个小时。"
  },
  "DescribeRealtimeNetwork": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      },
      {
        "name": "SdkAppId",
        "desc": "用户sdkappid"
      },
      {
        "name": "DataType",
        "desc": "需查询的数据类型\nsendLossRateRaw：上行丢包率；\nrecvLossRateRaw：下行丢包率"
      }
    ],
    "desc": "查询sdkappid维度下实时网络状态，包括上行丢包与下行丢包。可查询24小时内数据，查询起止时间不超过1个小时。"
  },
  "DescribeRoomInformation": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "用户sdkappid"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      },
      {
        "name": "RoomId",
        "desc": "数字房间号"
      },
      {
        "name": "PageNumber",
        "desc": "分页index（不填默认只返回10个）"
      },
      {
        "name": "PageSize",
        "desc": "分页大小（不填默认返回10个,最多不超过100条）"
      }
    ],
    "desc": "查询sdkappid下的房间列表。默认返回10条通话，一次最多返回100条通话。可查询最近5天的数据。"
  },
  "RemoveUser": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "TRTC的SDKAppId。"
      },
      {
        "name": "RoomId",
        "desc": "房间号。"
      },
      {
        "name": "UserIds",
        "desc": "要移出的用户列表，最多10个。"
      }
    ],
    "desc": "接口说明：将用户从房间移出，适用于主播/房主/管理员踢人等场景。支持所有平台，Android、iOS、Windows 和 macOS 需升级到 TRTC SDK 6.6及以上版本。"
  },
  "DescribeCallDetail": {
    "params": [
      {
        "name": "CommId",
        "desc": "通话ID"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      },
      {
        "name": "SdkAppId",
        "desc": "用户sdkappid"
      },
      {
        "name": "UserIds",
        "desc": "需查询的用户数组，不填默认返回6个用户"
      },
      {
        "name": "DataType",
        "desc": "需查询的指标，不填则只返回用户列表，填all则返回所有指标。\nappCpu：APP CPU使用率；\nsysCpu：系统 CPU使用率；\naBit：上/下行音频码率；\naBlock：音频卡顿时长；\nvBit：上/下行视频码率；\nvCapFps：视频采集帧率；\nvEncFps：视频发送帧率；\nvDecFps：渲染帧率；\nvBlock：视频卡顿时长；\naLoss：上/下行音频丢包；\nvLoss：上/下行视频丢包；\nvWidth：上/下行分辨率宽；\nvHeight：上/下行分辨率高"
      }
    ],
    "desc": "查询指定时间内的用户列表及用户通话质量数据。"
  },
  "DismissRoom": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "TRTC的SDKAppId。"
      },
      {
        "name": "RoomId",
        "desc": "房间号。"
      }
    ],
    "desc": "接口说明：把房间所有用户从房间移出，解散房间。支持所有平台，Android、iOS、Windows 和 macOS 需升级到 TRTC SDK 6.6及以上版本。"
  }
}