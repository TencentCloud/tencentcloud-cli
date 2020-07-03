# -*- coding: utf-8 -*-
DESC = "billing-2018-07-09"
INFO = {
  "DescribeAccountBalance": {
    "params": [],
    "desc": "获取云账户余额信息。"
  },
  "DescribeDosageDetailByDate": {
    "params": [
      {
        "name": "StartDate",
        "desc": "查询账单开始日期，如 2019-01-01"
      },
      {
        "name": "EndDate",
        "desc": "查询账单结束日期，如 2019-01-01， 时间跨度不超过7天"
      },
      {
        "name": "ProductCode",
        "desc": "互动直播：\n10194   互动直播-核心机房           :\n10195   互动直播-边缘机房\n\ncdn业务：\n10180：CDN静态加速流量(国内)\n10181：CDN静态加速带宽(国内)\n10182：CDN静态加速普通流量\n10183：CDN静态加速普通带宽\n10231：CDN静态加速流量(海外)\n10232：CDN静态加速带宽(海外)\n\n100967：弹性公网IP-按流量计费\n101065：公网负载均衡-按流量计费\n\n视频直播\n10226 视频直播流量(国内)\n10227 视频直播带宽(国内)\n100763 视频直播流量(海外)\n100762 视频直播宽带(海外)"
      },
      {
        "name": "Domain",
        "desc": "查询域名 例如 www.qq.com\n非CDN业务查询时值为空"
      },
      {
        "name": "InstanceID",
        "desc": "1、如果为空，则返回EIP或CLB所有实例的明细；\n2、如果传入实例名，则返回该实例明细"
      }
    ],
    "desc": "按日期获取产品用量明细"
  },
  "DescribeCostSummaryByResource": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "查询账单数据的用户UIN"
      },
      {
        "name": "BeginTime",
        "desc": "目前只支持传当月1号 00:00:00，且必须和EndTime为相同月份，不支持跨月查询，例 2018-09-01 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "目前只支持传当月最后一天 23:59:59，且必须和BeginTime为相同月份，不支持跨月查询，例 2018-09-30 23:59:59"
      },
      {
        "name": "Limit",
        "desc": "每次获取数据量"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "NeedRecordNum",
        "desc": "是否需要返回记录数量，0不需要，1需要，默认不需要"
      },
      {
        "name": "NeedConditionValue",
        "desc": "是否需要返回过滤条件，0不需要，1需要，默认不需要"
      },
      {
        "name": "Conditions",
        "desc": "过滤条件，只支持ResourceKeyword(资源关键字，支持资源id及资源名称模糊查询)，ProjectIds（项目id），RegionIds(地域id)，PayModes(付费模式，可选prePay和postPay)，HideFreeCost（是否隐藏0元流水，可选0和1），OrderByCost（按费用排序规则，可选desc和asc）"
      }
    ],
    "desc": "获取按资源汇总消耗详情"
  },
  "DescribeBillList": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询范围的起始时间（包含）"
      },
      {
        "name": "EndTime",
        "desc": "查询范围的结束时间（包含）"
      },
      {
        "name": "Offset",
        "desc": "翻页偏移量，初始值为0"
      },
      {
        "name": "Limit",
        "desc": "每页的限制数量"
      },
      {
        "name": "PayType",
        "desc": "交易类型： all所有交易类型，recharge充值，return退款，unblock解冻，agentin资金转入，advanced垫付，cash提现，deduct扣费，block冻结，agentout资金转出，repay垫付回款，repayment还款(仅国际信用账户)，adj_refund调增(仅国际信用账户)，adj_deduct调减(仅国际信用账户)"
      },
      {
        "name": "SubPayType",
        "desc": "扣费模式，当所选的交易类型中包含扣费deduct时有意义： all所有扣费类型，trade预付费支付，hour_h按量小时结，hour_d按量日结，hour_m按量月结，decompensate调账扣费，other其他扣费"
      },
      {
        "name": "WithZeroAmount",
        "desc": "是否返回0元交易金额的交易项，取值：0-不返回，1-返回。不传该参数则不返回"
      }
    ],
    "desc": "获取收支明细列表，支持翻页和参数过滤"
  },
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
        "desc": "周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。"
      },
      {
        "name": "Month",
        "desc": "月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。"
      },
      {
        "name": "BeginTime",
        "desc": "周期开始时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。(不支持跨月查询)"
      },
      {
        "name": "EndTime",
        "desc": "周期结束时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。（不支持跨月查询）"
      },
      {
        "name": "NeedRecordNum",
        "desc": "是否需要访问列表的总记录数，用于前端分页\n1-表示需要， 0-表示不需要"
      },
      {
        "name": "ProductCode",
        "desc": "查询指定产品信息（暂时未开放获取）"
      },
      {
        "name": "PayMode",
        "desc": "付费模式 prePay/postPay"
      },
      {
        "name": "ResourceId",
        "desc": "查询指定资源信息"
      },
      {
        "name": "ActionType",
        "desc": "查询交易类型。如 按量计费日结，按量计费小时结 等"
      }
    ],
    "desc": "查询账单明细数据"
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
      },
      {
        "name": "BigDealId",
        "desc": "大订单号"
      }
    ],
    "desc": "查询订单"
  },
  "DescribeCostSummaryByProject": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "查询账单数据的用户UIN"
      },
      {
        "name": "BeginTime",
        "desc": "目前只支持传当月1号 00:00:00，且必须和EndTime为相同月份，不支持跨月查询，例 2018-09-01 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "目前只支持传当月最后一天 23:59:59，且必须和BeginTime为相同月份，不支持跨月查询，例 2018-09-30 23:59:59"
      },
      {
        "name": "Limit",
        "desc": "每次获取数据量"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "NeedRecordNum",
        "desc": "是否需要返回记录数量，0不需要，1需要，默认不需要"
      }
    ],
    "desc": "获取按项目汇总消耗详情"
  },
  "DescribeBillSummaryByPayMode": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "查询账单数据的用户UIN"
      },
      {
        "name": "BeginTime",
        "desc": "目前只支持传当月开始，且必须和EndTime为相同月份，例 2018-09-01 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "目前只支持传当月结束，且必须和BeginTime为相同月份，例 2018-09-30 23:59:59"
      }
    ],
    "desc": "获取按付费模式汇总费用分布"
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
        "desc": "周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。您可前往[账单概览](https://console.cloud.tencent.com/expense/bill/overview)页面顶部查看确认您的账单统计周期类型。"
      },
      {
        "name": "Month",
        "desc": "月份，格式为yyyy-mm。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。"
      },
      {
        "name": "NeedRecordNum",
        "desc": "是否需要访问列表的总记录数，用于前端分页\n1-表示需要， 0-表示不需要"
      },
      {
        "name": "ActionType",
        "desc": "查询交易类型。如 按量计费日结，按量计费小时结 等"
      }
    ],
    "desc": "查询账单资源汇总数据 "
  },
  "DescribeCostSummaryByRegion": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "查询账单数据的用户UIN"
      },
      {
        "name": "BeginTime",
        "desc": "目前只支持传当月1号 00:00:00，且必须和EndTime为相同月份，不支持跨月查询，例 2018-09-01 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "目前只支持传当月最后一天 23:59:59，且必须和BeginTime为相同月份，不支持跨月查询，例 2018-09-30 23:59:59"
      },
      {
        "name": "Limit",
        "desc": "每次获取数据量"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "NeedRecordNum",
        "desc": "是否需要返回记录数量，0不需要，1需要，默认不需要"
      }
    ],
    "desc": "获取按地域汇总消耗详情"
  },
  "DescribeBillSummaryByRegion": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "查询账单数据的用户UIN"
      },
      {
        "name": "BeginTime",
        "desc": "目前只支持传当月开始，且必须和EndTime为相同月份，例 2018-09-01 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "目前只支持传当月结束，且必须和BeginTime为相同月份，例 2018-09-30 23:59:59"
      }
    ],
    "desc": "获取按地域汇总费用分布"
  },
  "DescribeBillSummaryByProject": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "查询账单数据的用户UIN"
      },
      {
        "name": "BeginTime",
        "desc": "目前只支持传当月开始，且必须和EndTime为相同月份，例 2018-09-01 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "目前只支持传当月结束，且必须和BeginTime为相同月份，例 2018-09-30 23:59:59"
      }
    ],
    "desc": "获取按项目汇总费用分布"
  },
  "DescribeBillSummaryByProduct": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "查询账单数据的用户UIN"
      },
      {
        "name": "BeginTime",
        "desc": "目前只支持传当月开始，且必须和EndTime为相同月份，例 2018-09-01 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "目前只支持传当月结束，且必须和BeginTime为相同月份，例 2018-09-30 23:59:59"
      }
    ],
    "desc": "获取产品汇总费用分布"
  },
  "DescribeBillSummaryByTag": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "查询账单数据的用户UIN"
      },
      {
        "name": "BeginTime",
        "desc": "目前只支持传当月开始，且必须和EndTime为相同月份，例 2018-09-01 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "目前只支持传当月结束，且必须和BeginTime为相同月份，例 2018-09-30 23:59:59"
      },
      {
        "name": "TagKey",
        "desc": "分账标签键"
      }
    ],
    "desc": "获取按标签汇总费用分布"
  },
  "DescribeCostSummaryByProduct": {
    "params": [
      {
        "name": "PayerUin",
        "desc": "查询账单数据的用户UIN"
      },
      {
        "name": "BeginTime",
        "desc": "目前只支持传当月1号 00:00:00，且必须和EndTime为相同月份，不支持跨月查询，例 2018-09-01 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "目前只支持传当月最后一天 23:59:59，且必须和BeginTime为相同月份，不支持跨月查询，例 2018-09-30 23:59:59"
      },
      {
        "name": "Limit",
        "desc": "每次获取数据量"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "NeedRecordNum",
        "desc": "是否需要返回记录数量，0不需要，1需要，默认不需要"
      }
    ],
    "desc": "获取按产品汇总消耗详情"
  },
  "DescribeCostDetail": {
    "params": [
      {
        "name": "Limit",
        "desc": "数量，最大值为100"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "BeginTime",
        "desc": "周期开始时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通成本分析的月份，最多可拉取24个月内的数据。"
      },
      {
        "name": "EndTime",
        "desc": "周期结束时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通成本分析的月份，最多可拉取24个月内的数据。"
      },
      {
        "name": "NeedRecordNum",
        "desc": "是否需要访问列表的总记录数，用于前端分页\n1-表示需要， 0-表示不需要"
      },
      {
        "name": "Month",
        "desc": "月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通成本分析的月份，最多可拉取24个月内的数据。"
      },
      {
        "name": "ProductCode",
        "desc": "查询指定产品信息"
      },
      {
        "name": "PayMode",
        "desc": "付费模式 prePay/postPay"
      },
      {
        "name": "ResourceId",
        "desc": "查询指定资源信息"
      }
    ],
    "desc": "查询消耗明细"
  },
  "PayDeals": {
    "params": [
      {
        "name": "OrderIds",
        "desc": "需要支付的一个或者多个子订单号，与BigDealIds字段两者必须且仅传一个参数"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券,1:是,0否,默认0"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表,目前仅支持指定一张代金券"
      },
      {
        "name": "BigDealIds",
        "desc": "需要支付的一个或者多个大订单号，与OrderIds字段两者必须且仅传一个参数"
      }
    ],
    "desc": "支付订单"
  }
}