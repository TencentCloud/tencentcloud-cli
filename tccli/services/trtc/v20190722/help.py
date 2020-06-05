# -*- coding: utf-8 -*-
DESC = "trtc-2019-07-22"
INFO = {
  "DescribeRealtimeQuality": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询开始时间，24小时内。本地unix时间戳（1588031999s）"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，本地unix时间戳（1588031999s）"
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
        "desc": "查询开始时间，5天内。本地unix时间戳（1588031999s）"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，本地unix时间戳（1588031999s）"
      }
    ],
    "desc": "可查询sdkqppid 每天的房间数和用户数，每分钟1次，可查询最近5天的数据。当天未结束，无法查到当天的房间数与用户数。"
  },
  "StartMCUMixTranscode": {
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
        "name": "OutputParams",
        "desc": "混流输出控制参数。"
      },
      {
        "name": "EncodeParams",
        "desc": "混流输出编码参数。"
      },
      {
        "name": "LayoutParams",
        "desc": "混流输出布局参数。"
      }
    ],
    "desc": "接口说明：启动云端混流，并指定混流画面中各路画面的布局位置。\n\nTRTC 的一个房间中可能会同时存在多路音视频流，您可以通过此 API 接口，通知腾讯云服务端将多路视频画面合成一路，并指定每一路画面的位置，同时将多路声音进行混音，最终形成一路音视频流，以便用于录制和直播观看。\n\n您可以通过此接口实现如下目标：\n- 设置最终直播流的画质和音质，包括视频分辨率、视频码率、视频帧率、以及声音质量等。\n- 设置各路画面的位置和布局，您只需要在启动时设置一次，排版引擎会自动完成后续的画面排布。\n- 设置录制文件名，用于二次回放。\n- 设置 CDN 直播流 ID，用于在 CDN 进行直播观看。\n\n目前已经支持了如下几种布局模板：\n- 悬浮模板：第一个进入房间的用户的视频画面会铺满整个屏幕，其他用户的视频画面从左下角依次水平排列，显示为小画面，最多4行，每行4个，小画面悬浮于大画面之上。最多支持1个大画面和15个小画面，如果用户只发送音频，仍然会占用画面位置。\n- 九宫格模板：所有用户的视频画面大小一致，平分整个屏幕，人数越多，每个画面的尺寸越小。最多支持16个画面，如果用户只发送音频，仍然会占用画面位置。\n- 屏幕分享模板：适合视频会议和在线教育场景的布局，屏幕分享（或者主讲的摄像头）始终占据屏幕左侧的大画面位置，其他用户依次垂直排列于右侧，最多两列，每列最多8个小画面。最多支持1个大画面和15个小画面，如果用户只发送音频，仍然会占用画面位置。"
  },
  "DescribeRealtimeScale": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询开始时间，24小时内。本地unix时间戳（1588031999s）"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，本地unix时间戳（1588031999s）"
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
        "desc": "查询开始时间，24小时内，，本地unix时间戳（1588031999s）"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，本地unix时间戳（1588031999s）"
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
        "desc": "查询开始时间，5天内。本地unix时间戳（1588031999s）"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，本地unix时间戳（1588031999s）"
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
    "desc": "查询sdkappid下的房间列表。默认返回10条通话，一次最多返回100条通话。可查询5天内的数据。"
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
        "desc": "通话 ID（唯一标识一次通话）： sdkappid_roomgString（房间号_createTime（房间创建时间，unix时间戳，单位为s）。通过 DescribeRoomInformation（查询房间列表）接口获取。"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间，5天内。本地unix时间戳（1588031999s）"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，本地unix时间戳（1588031999s）"
      },
      {
        "name": "SdkAppId",
        "desc": "用户sdkappid"
      },
      {
        "name": "UserIds",
        "desc": "需查询的用户数组，不填默认返回6个用户,最多可填6个用户"
      },
      {
        "name": "DataType",
        "desc": "需查询的指标，不填则只返回用户列表，填all则返回所有指标。\nappCpu：APP CPU使用率；\nsysCpu：系统 CPU使用率；\naBit：上/下行音频码率；\naBlock：音频卡顿时长；\nvBit：上/下行视频码率；\nvCapFps：视频采集帧率；\nvEncFps：视频发送帧率；\nvDecFps：渲染帧率；\nvBlock：视频卡顿时长；\naLoss：上/下行音频丢包；\nvLoss：上/下行视频丢包；\nvWidth：上/下行分辨率宽；\nvHeight：上/下行分辨率高"
      }
    ],
    "desc": "查询指定时间内的用户列表及用户通话质量数据。可查询5天内数据，查询起止时间不超过1个小时，查询用户不超过6个"
  },
  "DescribeDetailEvent": {
    "params": [
      {
        "name": "CommId",
        "desc": "通话 ID（唯一标识一次通话）： sdkappid_roomgString（房间号_createTime（房间创建时间，unix时间戳，单位s）。通过 DescribeRoomInformation（查询房间列表）接口获取。"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间，5天内。本地unix时间戳（1588031999s）"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，本地unix时间戳（1588031999s）"
      },
      {
        "name": "UserId",
        "desc": "用户id"
      },
      {
        "name": "RoomId",
        "desc": "房间号"
      }
    ],
    "desc": "查询用户某次通话内的进退房，视频开关等详细事件。可查询5天内数据。"
  },
  "StopMCUMixTranscode": {
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
    "desc": "接口说明：结束云端混流"
  },
  "CreateTroubleInfo": {
    "params": [
      {
        "name": "SdkAppId",
        "desc": "应用的ID"
      },
      {
        "name": "RoomId",
        "desc": "房间ID"
      },
      {
        "name": "TeacherUserId",
        "desc": "老师用户ID"
      },
      {
        "name": "StudentUserId",
        "desc": "学生用户ID"
      },
      {
        "name": "TroubleUserId",
        "desc": "体验异常端（老师或学生）的用户 ID。"
      },
      {
        "name": "TroubleType",
        "desc": "异常类型。\n1. 仅视频异常\n2. 仅声音异常\n3. 音视频都异常\n5. 进房异常\n4. 切课\n6. 求助\n7. 问题反馈\n8. 投诉"
      },
      {
        "name": "TroubleTime",
        "desc": "异常发生的UNIX 时间戳，单位为秒。"
      },
      {
        "name": "TroubleMsg",
        "desc": "异常详情"
      }
    ],
    "desc": "创建异常信息"
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