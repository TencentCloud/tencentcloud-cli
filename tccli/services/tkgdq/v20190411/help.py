# -*- coding: utf-8 -*-
DESC = "tkgdq-2019-04-11"
INFO = {
  "DescribeEntity": {
    "params": [
      {
        "name": "EntityName",
        "desc": "实体名称"
      }
    ],
    "desc": "输入实体名称，返回实体相关的信息如实体别名、实体英文名、实体详细信息、相关实体等"
  },
  "DescribeTriple": {
    "params": [
      {
        "name": "TripleCondition",
        "desc": "三元组查询条件"
      }
    ],
    "desc": "三元组查询，主要分为两类，SP查询和PO查询。SP查询表示已知主语和谓语查询宾语，PO查询表示已知宾语和谓语查询主语。每一个SP或PO查询都是一个可独立执行的查询，TQL支持SP查询的嵌套查询，即主语可以是一个嵌套的子查询。其他复杂的三元组查询方法，请参考官网API文档示例。"
  },
  "DescribeRelation": {
    "params": [
      {
        "name": "LeftEntityName",
        "desc": "输入第一个实体"
      },
      {
        "name": "RightEntityName",
        "desc": "输入第二个实体"
      }
    ],
    "desc": "输入两个实体，返回两个实体间的关系，例如马化腾与腾讯公司不仅是相关实体，二者还存在隶属关系（马化腾属于腾讯公司）。"
  }
}