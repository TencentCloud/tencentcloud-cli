# -*- coding: utf-8 -*-
DESC = "iottid-2019-04-11"
INFO = {
  "DescribePermission": {
    "params": [],
    "desc": "查询企业用户TID平台控制台权限"
  },
  "DeliverTids": {
    "params": [
      {
        "name": "OrderId",
        "desc": "订单ID"
      },
      {
        "name": "Quantity",
        "desc": "数量，1~10"
      }
    ],
    "desc": "设备服务商请求空发产品订单的TID信息"
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
    "desc": "安全芯片TID烧录回执"
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
    "desc": "安全芯片为载体的TID空发回执，绑定TID与订单号。"
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
    "desc": "下载芯片订单的TID"
  }
}