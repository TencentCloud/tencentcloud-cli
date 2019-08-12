# -*- coding: utf-8 -*-
DESC = "trtc-2019-07-22"
INFO = {
  "KickOutUser": {
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
        "desc": "要踢的用户列表，最多10个。"
      }
    ],
    "desc": "接口说明：将用户从房间踢出。"
  },
  "DissloveRoom": {
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
    "desc": "接口说明：把房间所有用户从房间踢出，解散房间。"
  }
}