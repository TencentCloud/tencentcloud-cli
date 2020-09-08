# -*- coding: utf-8 -*-
DESC = "domain-2018-08-08"
INFO = {
  "DescribeDomainPriceList": {
    "params": [
      {
        "name": "TldList",
        "desc": "查询价格的后缀列表。默认则为全部后缀"
      },
      {
        "name": "Year",
        "desc": "查询购买的年份，默认会列出所有年份的价格"
      },
      {
        "name": "Operation",
        "desc": "域名的购买类型：new  新购，renew 续费，redem 赎回，tran 转入"
      }
    ],
    "desc": "按照域名后缀获取对应的价格列表"
  },
  "CheckDomain": {
    "params": [
      {
        "name": "DomainName",
        "desc": "所查询域名名称"
      },
      {
        "name": "Period",
        "desc": "年限"
      }
    ],
    "desc": "检查域名是否可以注册。"
  }
}