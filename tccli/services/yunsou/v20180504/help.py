# -*- coding: utf-8 -*-
DESC = "yunsou-2018-05-04"
INFO = {
  "DataManipulation": {
    "params": [
      {
        "name": "OpType",
        "desc": "操作类型，add或del"
      },
      {
        "name": "Encoding",
        "desc": "数据编码类型"
      },
      {
        "name": "Contents",
        "desc": "数据"
      },
      {
        "name": "ResourceId",
        "desc": "应用Id"
      }
    ],
    "desc": "上传云搜数据的API接口"
  },
  "DataSearch": {
    "params": [
      {
        "name": "ResourceId",
        "desc": "云搜的业务ID，用以表明当前数据请求的业务"
      },
      {
        "name": "SearchQuery",
        "desc": "检索串"
      },
      {
        "name": "PageId",
        "desc": "当前页，从第0页开始计算"
      },
      {
        "name": "NumPerPage",
        "desc": "每页结果数"
      },
      {
        "name": "SearchId",
        "desc": "当前检索号，用于定位问题，建议指定并且全局唯一"
      },
      {
        "name": "QueryEncode",
        "desc": "请求编码，0表示utf8，1表示gbk，建议指定"
      },
      {
        "name": "RankType",
        "desc": "排序类型"
      },
      {
        "name": "NumFilter",
        "desc": "数值过滤，结果中按属性过滤"
      },
      {
        "name": "ClFilter",
        "desc": "分类过滤，导航类检索请求"
      },
      {
        "name": "Extra",
        "desc": "检索用户相关字段"
      },
      {
        "name": "SourceId",
        "desc": "检索来源"
      },
      {
        "name": "SecondSearch",
        "desc": "是否进行二次检索，0关闭，1打开"
      },
      {
        "name": "MaxDocReturn",
        "desc": "指定返回最大篇数，无特殊原因不建议指定"
      },
      {
        "name": "IsSmartbox",
        "desc": "是否smartbox检索，0关闭，1打开"
      },
      {
        "name": "EnableAbsHighlight",
        "desc": "是否打开高红标亮，0关闭，1打开"
      },
      {
        "name": "QcBid",
        "desc": "指定访问QC纠错业务ID"
      },
      {
        "name": "GroupBy",
        "desc": "按指定字段进行group by，只能对数值字段进行操作"
      },
      {
        "name": "Distinct",
        "desc": "按指定字段进行distinct，只能对数值字段进行操作"
      },
      {
        "name": "L4RankExpression",
        "desc": "高级排序参数，具体参见高级排序说明"
      },
      {
        "name": "MatchValue",
        "desc": "高级排序参数，具体参见高级排序说明"
      },
      {
        "name": "Longitude",
        "desc": "经度信息"
      },
      {
        "name": "Latitude",
        "desc": "纬度信息"
      },
      {
        "name": "MultiFilter",
        "desc": "分类过滤并集"
      }
    ],
    "desc": "用于检索云搜中的数据"
  }
}