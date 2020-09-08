# -*- coding: utf-8 -*-
DESC = "habo-2018-12-03"
INFO = {
  "StartAnalyse": {
    "params": [
      {
        "name": "Pk",
        "desc": "购买服务后获得的授权帐号，用于保证请求有效性"
      },
      {
        "name": "Md5",
        "desc": "样本md5，用于对下载获得的样本完整性进行校验"
      },
      {
        "name": "DlUrl",
        "desc": "待分析样本下载地址"
      }
    ],
    "desc": "上传样本到哈勃进行分析，异步生成分析日志。"
  },
  "DescribeStatus": {
    "params": [
      {
        "name": "Pk",
        "desc": "购买服务后获得的授权帐号，用于保证请求有效性"
      },
      {
        "name": "Md5",
        "desc": "需要获取分析结果的样本md5"
      }
    ],
    "desc": "查询指定md5样本是否分析完成，并获取分析日志下载地址。"
  }
}