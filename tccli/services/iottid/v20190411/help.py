# -*- coding: utf-8 -*-
DESC = "iottid-2019-04-11"
INFO = {
  "AuthTestTid": {
    "params": [
      {
        "name": "Data",
        "desc": "设备端SDK填入测试TID参数后生成的加密数据串"
      }
    ],
    "desc": "单向认证测试TID "
  },
  "UploadDeviceUniqueCode": {
    "params": [
      {
        "name": "CodeSet",
        "desc": "硬件唯一标识码"
      },
      {
        "name": "OrderId",
        "desc": "硬件标识码绑定的申请编号"
      }
    ],
    "desc": "上传硬件唯一标识码，是软加固设备身份参数。本接口如遇到错误数据，则所有当次上传数据失效。"
  },
  "VerifyChipBurnInfo": {
    "params": [
      {
        "name": "Data",
        "desc": "验证数据"
      }
    ],
    "desc": "下载控制台验证芯片烧录信息，保证TID与中心信息一致 "
  },
  "DeliverTids": {
    "params": [
      {
        "name": "OrderId",
        "desc": "订单ID"
      },
      {
        "name": "Quantity",
        "desc": "数量，1~100"
      }
    ],
    "desc": "设备服务商请求空发产品订单的TID信息 "
  },
  "BurnTidNotify": {
    "params": [
      {
        "name": "OrderId",
        "desc": "订单编号"
      },
      {
        "name": "Tid",
        "desc": "TID编号"
      }
    ],
    "desc": "安全芯片TID烧录回执 "
  },
  "DescribePermission": {
    "params": [],
    "desc": "查询企业用户TID平台控制台权限 "
  },
  "DeliverTidNotify": {
    "params": [
      {
        "name": "OrderId",
        "desc": "订单编号"
      },
      {
        "name": "Tid",
        "desc": "TID编号"
      }
    ],
    "desc": "安全芯片为载体的TID空发回执，绑定TID与订单号。 "
  },
  "DownloadTids": {
    "params": [
      {
        "name": "OrderId",
        "desc": "订单编号"
      },
      {
        "name": "Quantity",
        "desc": "下载数量：1~10"
      }
    ],
    "desc": "下载芯片订单的TID "
  },
  "DescribeAvailableLibCount": {
    "params": [
      {
        "name": "OrderId",
        "desc": "订单编号"
      }
    ],
    "desc": "查询指定订单的可空发的白盒密钥数量"
  }
}