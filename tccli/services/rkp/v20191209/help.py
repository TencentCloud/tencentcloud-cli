# -*- coding: utf-8 -*-
DESC = "rkp-2019-12-09"
INFO = {
  "GetOpenId": {
    "params": [
      {
        "name": "DeviceToken",
        "desc": "dev临时token，通过sdk接口获取"
      },
      {
        "name": "BusinessId",
        "desc": "业务ID"
      },
      {
        "name": "BusinessUserId",
        "desc": "业务侧账号体系下的用户ID"
      },
      {
        "name": "Platform",
        "desc": "平台：0-Android， 1-iOS， 2-web"
      },
      {
        "name": "Option",
        "desc": "选项"
      }
    ],
    "desc": "根据DevicceToken查询OpenID。"
  },
  "GetToken": {
    "params": [
      {
        "name": "BusinessId",
        "desc": "业务ID"
      },
      {
        "name": "Scene",
        "desc": "业务子场景"
      },
      {
        "name": "BusinessUserId",
        "desc": "业务侧账号体系下的用户ID"
      },
      {
        "name": "AppClientIp",
        "desc": "用户侧的IP"
      },
      {
        "name": "ExpireTime",
        "desc": "过期时间"
      },
      {
        "name": "OldToken",
        "desc": "上一个token"
      }
    ],
    "desc": "获取token接口。"
  },
  "QueryDevAndRisk": {
    "params": [
      {
        "name": "DevType",
        "desc": "设备类型 0表示Android， 1表示IOS"
      },
      {
        "name": "Imei",
        "desc": "Android Imei号"
      },
      {
        "name": "Mac",
        "desc": "Mac地址"
      },
      {
        "name": "Aid",
        "desc": "android  Aid"
      },
      {
        "name": "Cid",
        "desc": "Android Cid"
      },
      {
        "name": "Imsi",
        "desc": "手机Imsi"
      },
      {
        "name": "Df",
        "desc": "Df 磁盘分区信息"
      },
      {
        "name": "KernelVer",
        "desc": "内核版本"
      },
      {
        "name": "Storage",
        "desc": "存储大小"
      },
      {
        "name": "Dfp",
        "desc": "设备驱动指纹"
      },
      {
        "name": "BootTime",
        "desc": "启动时间"
      },
      {
        "name": "Resolution",
        "desc": "分辨率 水平*垂直 格式"
      },
      {
        "name": "RingList",
        "desc": "铃声列表"
      },
      {
        "name": "FontList",
        "desc": "字体列表"
      },
      {
        "name": "SensorList",
        "desc": "传感器列表"
      },
      {
        "name": "CpuType",
        "desc": "CPU型号"
      },
      {
        "name": "Battery",
        "desc": "电池容量"
      },
      {
        "name": "Oaid",
        "desc": "信通院广告ID"
      },
      {
        "name": "Idfa",
        "desc": "IOS 广告ID"
      },
      {
        "name": "Idfv",
        "desc": "IOS 应用ID"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      },
      {
        "name": "IphoneModel",
        "desc": "IOS手机型号"
      },
      {
        "name": "Fingerprint",
        "desc": "Android 指纹"
      },
      {
        "name": "SerialId",
        "desc": "Android序列号"
      }
    ],
    "desc": "腾讯天御设备风险查询接口，输入由客户应用自主采集的设备信息， 通过腾讯大数据风控能力，可以准确根据输入设备信息，还原设备库中的设备ID，并且识别设备的风险，解决客户业务过程中的设备风险，降低企业损失。"
  }
}