# -*- coding: utf-8 -*-
DESC = "emr-2019-01-03"
INFO = {
  "InquiryPriceCreateInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "时间单位"
      },
      {
        "name": "TimeSpan",
        "desc": "时间长度"
      },
      {
        "name": "ResourceSpec",
        "desc": "询价资源描述"
      },
      {
        "name": "Currency",
        "desc": "货币种类"
      },
      {
        "name": "PayMode",
        "desc": "计费类型"
      },
      {
        "name": "SupportHA",
        "desc": "是否支持HA， 1 支持，0 不支持"
      },
      {
        "name": "Software",
        "desc": "软件列表"
      },
      {
        "name": "Placement",
        "desc": "位置信息"
      },
      {
        "name": "VPCSettings",
        "desc": "VPC信息"
      }
    ],
    "desc": "创建实例询价"
  }
}