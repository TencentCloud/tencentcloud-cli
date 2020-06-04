# -*- coding: utf-8 -*-
DESC = "partners-2018-03-21"
INFO = {
  "DescribeAgentDealsCache": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      },
      {
        "name": "CreatTimeRangeStart",
        "desc": "下单时间范围起始点"
      },
      {
        "name": "CreatTimeRangeEnd",
        "desc": "下单时间范围终止点"
      },
      {
        "name": "Order",
        "desc": "0:下单时间降序；其他：下单时间升序"
      },
      {
        "name": "Status",
        "desc": "订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)"
      },
      {
        "name": "OwnerUins",
        "desc": "下单人账号ID列表"
      },
      {
        "name": "DealNames",
        "desc": "订单号列表"
      },
      {
        "name": "PayerMode",
        "desc": "支付方式，0：自付；1：代付"
      }
    ],
    "desc": "供超大型代理商（代客数量>=3000 ）拉取缓存的全量客户订单。"
  },
  "AgentPayDeals": {
    "params": [
      {
        "name": "OwnerUin",
        "desc": "订单所有者uin"
      },
      {
        "name": "AgentPay",
        "desc": "代付标志，1：代付；0：自付"
      },
      {
        "name": "DealNames",
        "desc": "订单号数组"
      }
    ],
    "desc": "代理商支付订单接口，支持自付/代付"
  },
  "DescribeAgentBills": {
    "params": [
      {
        "name": "SettleMonth",
        "desc": "支付月份，如2018-02"
      },
      {
        "name": "ClientUin",
        "desc": "客户账号ID"
      },
      {
        "name": "PayMode",
        "desc": "支付方式，prepay/postpay"
      },
      {
        "name": "OrderId",
        "desc": "预付费订单号"
      },
      {
        "name": "ClientRemark",
        "desc": "客户备注名称"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      }
    ],
    "desc": "代理商可查询自己及名下代客所有业务明细"
  },
  "AgentTransferMoney": {
    "params": [
      {
        "name": "ClientUin",
        "desc": "客户账号ID"
      },
      {
        "name": "Amount",
        "desc": "转账金额，单位分"
      }
    ],
    "desc": "为合作伙伴提供转账给客户能力。仅支持合作伙伴为自己名下客户转账。"
  },
  "DescribeRebateInfos": {
    "params": [
      {
        "name": "RebateMonth",
        "desc": "返佣月份，如2018-02"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      }
    ],
    "desc": "代理商可查询自己名下全部返佣信息"
  },
  "DescribeSalesmans": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      },
      {
        "name": "SalesName",
        "desc": "业务员姓名(模糊查询)"
      },
      {
        "name": "SalesUin",
        "desc": "业务员ID"
      },
      {
        "name": "OrderDirection",
        "desc": "ASC/DESC， 不区分大小写，按创建通过时间排序"
      }
    ],
    "desc": "代理商查询名下业务员列表信息"
  },
  "RemovePayRelationForClient": {
    "params": [
      {
        "name": "ClientUin",
        "desc": "客户账号ID"
      }
    ],
    "desc": "合作伙伴为客户消除强代付关系"
  },
  "ModifyClientRemark": {
    "params": [
      {
        "name": "ClientRemark",
        "desc": "客户备注名称"
      },
      {
        "name": "ClientUin",
        "desc": "客户账号ID"
      }
    ],
    "desc": "代理商可以对名下客户添加备注、修改备注"
  },
  "DescribeAgentPayDeals": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      },
      {
        "name": "CreatTimeRangeStart",
        "desc": "下单时间范围起始点(不传时会默认查15天内订单，传值时需要传15天内的起始时间)"
      },
      {
        "name": "CreatTimeRangeEnd",
        "desc": "下单时间范围终止点"
      },
      {
        "name": "Order",
        "desc": "0:下单时间降序；其他：下单时间升序"
      },
      {
        "name": "Status",
        "desc": "订单的状态(1：未支付;2：已支付;3：发货中;4：已发货;5：发货失败;6：已退款;7：已关单;8：订单过期;9：订单已失效;10：产品已失效;11：代付拒绝;12：支付中)"
      },
      {
        "name": "OwnerUins",
        "desc": "下单人账号ID列表"
      },
      {
        "name": "DealNames",
        "desc": "订单号列表"
      }
    ],
    "desc": "可以查询代理商代付的所有订单"
  },
  "DescribeAgentClients": {
    "params": [
      {
        "name": "ClientUin",
        "desc": "客户账号ID"
      },
      {
        "name": "ClientName",
        "desc": "客户名称。由于涉及隐私，名称打码显示，故名称仅支持打码后的模糊搜索"
      },
      {
        "name": "ClientFlag",
        "desc": "客户类型，a/b，类型定义参考代理商相关政策文档"
      },
      {
        "name": "OrderDirection",
        "desc": "ASC/DESC， 不区分大小写，按申请时间排序"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      },
      {
        "name": "SalesUin",
        "desc": "业务员ID"
      },
      {
        "name": "SalesName",
        "desc": "业务员姓名（模糊查询）"
      }
    ],
    "desc": "代理商可查询自己名下待审核客户列表"
  },
  "DescribeClientBalance": {
    "params": [
      {
        "name": "ClientUin",
        "desc": "客户(代客)账号ID"
      }
    ],
    "desc": "为合作伙伴提供查询客户余额能力。调用者必须是合作伙伴，只能查询自己名下客户余额"
  },
  "DescribeAgentClientGrade": {
    "params": [
      {
        "name": "ClientUin",
        "desc": "代客uin"
      }
    ],
    "desc": "传入代客uin，查客户级别，客户审核状态，客户实名认证状态"
  },
  "DescribeAgentAuditedClients": {
    "params": [
      {
        "name": "ClientUin",
        "desc": "客户账号ID"
      },
      {
        "name": "ClientName",
        "desc": "客户名称。由于涉及隐私，名称打码显示，故名称仅支持打码后的模糊搜索"
      },
      {
        "name": "ClientFlag",
        "desc": "客户类型，a/b，类型定义参考代理商相关政策文档"
      },
      {
        "name": "OrderDirection",
        "desc": "ASC/DESC， 不区分大小写，按审核通过时间排序"
      },
      {
        "name": "ClientUins",
        "desc": "客户账号ID列表"
      },
      {
        "name": "HasOverdueBill",
        "desc": "是否欠费。0：不欠费；1：欠费"
      },
      {
        "name": "ClientRemark",
        "desc": "客户备注"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      },
      {
        "name": "ClientType",
        "desc": "客户类型：可以为new(新拓)/assign(指定)/old(存量)/空"
      },
      {
        "name": "ProjectType",
        "desc": "项目类型：可以为self(自拓项目)/platform(合作项目)/repeat(复算项目  )/空"
      },
      {
        "name": "SalesUin",
        "desc": "业务员ID"
      },
      {
        "name": "SalesName",
        "desc": "业务员姓名（模糊查询）"
      }
    ],
    "desc": "查询已审核客户列表"
  },
  "CreatePayRelationForClient": {
    "params": [
      {
        "name": "ClientUin",
        "desc": "客户账号ID"
      }
    ],
    "desc": "合作伙伴为客户创建强代付关系"
  },
  "AuditApplyClient": {
    "params": [
      {
        "name": "ClientUin",
        "desc": "待审核客户账号ID"
      },
      {
        "name": "AuditResult",
        "desc": "审核结果，可能的取值：accept/reject"
      },
      {
        "name": "Note",
        "desc": "申请理由，B类客户审核通过时必须填写申请理由"
      }
    ],
    "desc": "代理商可以审核其名下申请中代客"
  }
}