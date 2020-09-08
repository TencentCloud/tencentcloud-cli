# -*- coding: utf-8 -*-
DESC = "tics-2018-11-15"
INFO = {
  "DescribeFileInfo": {
    "params": [
      {
        "name": "Key",
        "desc": "要查询文件的MD5"
      },
      {
        "name": "Option",
        "desc": "附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。"
      }
    ],
    "desc": "提供文件相关的基础信息以及与攻击事件（团伙、家族）、恶意文件等相关联信息。"
  },
  "DescribeIpInfo": {
    "params": [
      {
        "name": "Key",
        "desc": "要查询的IP"
      },
      {
        "name": "Option",
        "desc": "附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。"
      }
    ],
    "desc": "提供IP相关的基础信息以及与攻击事件（团伙、家族）、恶意文件等相关联信息。"
  },
  "DescribeDomainInfo": {
    "params": [
      {
        "name": "Key",
        "desc": "要查询的域名"
      },
      {
        "name": "Option",
        "desc": "附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。"
      }
    ],
    "desc": "提供域名相关的基础信息以及与攻击事件（团伙、家族）、恶意文件等相关联信息。"
  },
  "DescribeThreatInfo": {
    "params": [
      {
        "name": "Key",
        "desc": "查询对象，域名或IP"
      },
      {
        "name": "Type",
        "desc": "查询类型，当前取值为domain或ip"
      },
      {
        "name": "Option",
        "desc": "附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。"
      }
    ],
    "desc": "提供IP和域名相关威胁情报信息查询，这些信息可以辅助检测失陷主机、帮助SIEM/SOC等系统做研判决策、帮助运营团队对设备报警的编排处理。"
  }
}