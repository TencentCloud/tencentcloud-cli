# -*- coding: utf-8 -*-
DESC = "billing-2018-07-09"
INFO = {
  "DescribeBillDetail": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "数量，最大值为100"
      },
      {
        "name": "PeriodType",
        "desc": "周期类型，byPayTime按扣费周期/byUsedTime按计费周期"
      },
      {
        "name": "Month",
        "desc": "月份，格式为yyyy-mm"
      }
    ],
    "desc": "查询账单明细数据"
  },
  "DescribeAccountBalance": {
    "params": [],
    "desc": "获取云账户余额信息。"
  },
  "DescribeBillResourceSummary": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "数量，最大值为1000"
      },
      {
        "name": "PeriodType",
        "desc": "周期类型，byUsedTime按计费周期/byPayTime按扣费周期"
      },
      {
        "name": "Month",
        "desc": "月份，格式为yyyy-mm"
      }
    ],
    "desc": "查询账单资源汇总数据"
  },
  "DescribeDealsByCond": {
    "params": [
      {
        "name": "StartTime",
        "desc": "开始时间"
      },
      {
        "name": "EndTime",
        "desc": "结束时间"
      },
      {
        "name": "Limit",
        "desc": "一页多少条数据，默认是20条，最大不超过1000"
      },
      {
        "name": "Offset",
        "desc": "第多少页，从0开始，默认是0"
      },
      {
        "name": "Status",
        "desc": "订单状态,默认为4（成功的订单）\n订单的状态\n1：未支付\n2：已支付3：发货中\n4：已发货\n5：发货失败\n6：已退款\n7：已关单\n8：订单过期\n9：订单已失效\n10：产品已失效\n11：代付拒绝\n12：支付中"
      },
      {
        "name": "OrderId",
        "desc": "订单号"
      }
    ],
    "desc": "查询订单"
  },
  "PayDeals": {
    "params": [
      {
        "name": "OrderIds",
        "desc": "需要支付的一个或者多个订单号"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券,1:是,0否,默认0"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表,目前仅支持指定一张代金券"
      }
    ],
    "desc": "支付订单"
  }
}