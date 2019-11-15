# -*- coding: utf-8 -*-
DESC = "dayu-2018-07-09"
INFO = {
  "DescribeResourceList": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版；shield表示棋牌）"
      },
      {
        "name": "RegionList",
        "desc": "地域码搜索，可选，当不指定地域时空数组，当指定地域时，填地域码。例如：[\"gz\", \"sh\"]"
      },
      {
        "name": "Line",
        "desc": "线路搜索，可选，只有当获取高防IP资源列表是可以选填，取值为[1（BGP线路），2（南京电信），3（南京联通），99（第三方合作线路）]，当获取其他产品时请填空数组；"
      },
      {
        "name": "IdList",
        "desc": "资源ID搜索，可选，当不为空数组时表示获取指定资源的资源列表；"
      },
      {
        "name": "Name",
        "desc": "资源名称搜索，可选，当不为空字符串时表示按名称搜索资源；"
      },
      {
        "name": "IpList",
        "desc": "IP搜索列表，可选，当不为空时表示安装IP搜索资源；"
      },
      {
        "name": "Status",
        "desc": "资源状态搜索列表，可选，取值为[0（运行中）, 1（清洗中）, 2（封堵中）]，当填空数组时不进行状态搜索；"
      },
      {
        "name": "Expire",
        "desc": "即将到期搜索；可选，取值为[0（不搜索），1（搜索即将到期的资源）]"
      },
      {
        "name": "OderBy",
        "desc": "排序字段，可选"
      },
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      },
      {
        "name": "CName",
        "desc": "高防IP专业版资源的CNAME，可选，只对高防IP专业版资源列表有效；"
      },
      {
        "name": "Domain",
        "desc": "高防IP专业版资源的域名，可选，只对高防IP专业版资源列表有效；"
      }
    ],
    "desc": "获取资源列表"
  }
}