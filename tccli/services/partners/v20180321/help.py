# -*- coding: utf-8 -*-
DESC = "partners-2018-03-21"
INFO = {
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
      }
    ],
    "desc": "查询已审核客户列表"
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