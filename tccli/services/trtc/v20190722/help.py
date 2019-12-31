# -*- coding: utf-8 -*-
DESC = "trtc-2019-07-22"
INFO = {
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