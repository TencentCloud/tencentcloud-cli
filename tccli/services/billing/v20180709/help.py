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
        "desc": "查询账单结束日期，如 2019-01-01"
      },
      {
        "name": "ProductCode",
        "desc": "视频业务：\n10194   互动直播-核心机房           :\n10195   互动直播-边缘机房\n\ncdn业务：\n10180：CDN静态加速流量(国内)\n10181：CDN静态加速带宽(国内)\n10182：CDN静态加速普通流量\n10183：CDN静态加速普通带宽\n10231：CDN静态加速流量(海外)\n10232：CDN静态加速带宽(海外)\n\n100967：弹性公网IP-按流量计费\n101065：公网负载均衡-按流量计费"
      },
      {
        "name": "Domain",
        "desc": "查询域名 例如 www.qq.com\n非CDN业务查询时可以设置为空"
      },
      {
        "name": "InstanceID",
        "desc": "1、如果为空，则返回EIP或CLB所有实例的明细；\n2、如果传入实例名，则返回该实例明细"
      }
    ],
    "desc": "按日期获取产品用量明细"
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
        "desc": "周期类型，byPayTime按扣费周期/byUsedTime按计费周期。需要与费用中心该月份账单的周期保持一致。"
      },
      {
        "name": "Month",
        "desc": "月份，格式为yyyy-mm，Month和BeginTime&EndTime必传一个，如果有传BeginTime&EndTime则Month字段无效。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。"
      },
      {
        "name": "BeginTime",
        "desc": "周期开始时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。"
      },
      {
        "name": "EndTime",
        "desc": "周期结束时间，格式为Y-m-d H:i:s，Month和BeginTime&EndTime必传一个，如果有该字段则Month字段无效。BeginTime和EndTime必须一起传。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。"
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
      }
    ],
    "desc": "查询订单"
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
        "desc": "周期类型，byUsedTime按计费周期/byPayTime按扣费周期。需要与费用中心该月份账单的周期保持一致。"
      },
      {
        "name": "Month",
        "desc": "月份，格式为yyyy-mm。不能早于开通账单2.0的月份，最多可拉取24个月内的数据。"
      }
    ],
    "desc": "查询账单资源汇总数据"
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