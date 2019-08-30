# -*- coding: utf-8 -*-
DESC = "trtc-2019-07-22"
INFO = {
  "DissolveRoom": {
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
    "desc": "接口说明：把房间所有用户从房间踢出，解散房间。支持 TRTC SDK 6.6及以上版本，包括Android、iOS、Windows 和 macOS。"
  },
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
    "desc": "接口说明：将用户从房间踢出。支持 TRTC SDK 6.6及以上版本，包括Android、iOS、Windows 和 macOS。"
  }
}