# -*- coding: utf-8 -*-
DESC = "ic-2019-03-07"
INFO = {
  "DescribeApp": {
    "params": [
      {
        "name": "Sdkappid",
        "desc": "物联卡应用ID"
      }
    ],
    "desc": "根据应用id查询物联卡应用详情"
  },
  "DescribeCard": {
    "params": [
      {
        "name": "Sdkappid",
        "desc": "应用ID"
      },
      {
        "name": "Iccid",
        "desc": "卡片ID"
      }
    ],
    "desc": "查询卡片详细信息"
  },
  "SendSms": {
    "params": [
      {
        "name": "Sdkappid",
        "desc": "应用ID"
      },
      {
        "name": "Iccid",
        "desc": "卡片ID"
      },
      {
        "name": "Content",
        "desc": "短信内容长度70限制"
      }
    ],
    "desc": "发送短信息接口"
  },
  "SendMultiSms": {
    "params": [
      {
        "name": "Sdkappid",
        "desc": "应用ID"
      },
      {
        "name": "Iccids",
        "desc": "卡片列表"
      },
      {
        "name": "Content",
        "desc": "短信内容 长度限制 70"
      }
    ],
    "desc": "群发短信"
  },
  "RenewCards": {
    "params": [
      {
        "name": "Sdkappid",
        "desc": "应用ID"
      },
      {
        "name": "Iccids",
        "desc": "续费的iccid"
      },
      {
        "name": "RenewNum",
        "desc": "续费的周期（单位：月）"
      }
    ],
    "desc": "批量为卡片续费，此接口建议调用至少间隔10s,如果出现返回deal lock failed相关的错误，请过10s再重试。\n续费的必要条件：\n1、单次续费的卡片不可以超过 100张。\n2、接口只支持在控制台购买的卡片进行续费\n3、销户和未激活的卡片不支持续费。\n4、每张物联网卡，续费总周期不能超过24个月"
  },
  "DescribeCards": {
    "params": [
      {
        "name": "Sdkappid",
        "desc": "应用ID"
      },
      {
        "name": "Offset",
        "desc": "偏移值"
      },
      {
        "name": "Limit",
        "desc": "列表限制"
      }
    ],
    "desc": "查询卡片列表信息"
  }
}