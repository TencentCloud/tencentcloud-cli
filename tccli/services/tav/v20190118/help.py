# -*- coding: utf-8 -*-
DESC = "tav-2019-01-18"
INFO = {
  "GetScanResult": {
    "params": [
      {
        "name": "Key",
        "desc": "购买服务后获得的授权信息，用于保证请求有效性"
      },
      {
        "name": "Md5",
        "desc": "需要获取扫描接口的md5（只允许单个md5）"
      }
    ],
    "desc": "tav文件上传扫描结果查询"
  },
  "ScanFile": {
    "params": [
      {
        "name": "Key",
        "desc": "购买服务后获得的授权信息，用于保证请求有效性"
      },
      {
        "name": "Sample",
        "desc": "文件下载url地址"
      },
      {
        "name": "Md5",
        "desc": "文件的md5值"
      }
    ],
    "desc": "tav文件上传扫描"
  },
  "GetLocalEngine": {
    "params": [
      {
        "name": "Key",
        "desc": "购买服务后获得的授权信息，用于保证请求有效性"
      }
    ],
    "desc": "获取TAV本地引擎"
  },
  "ScanFileHash": {
    "params": [
      {
        "name": "Key",
        "desc": "购买服务后获得的授权信息，用于保证请求有效性"
      },
      {
        "name": "Md5s",
        "desc": "需要查询的md5值（支持单个和多个，多个md5间用逗号分格）"
      },
      {
        "name": "WithCategory",
        "desc": "保留字段默认填0"
      },
      {
        "name": "SensitiveLevel",
        "desc": "松严规则控制字段默认填10（5-松、10-标准、15-严）"
      }
    ],
    "desc": "通过文件哈希值获取文件黑白属性"
  }
}