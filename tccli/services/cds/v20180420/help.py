# -*- coding: utf-8 -*-
DESC = "cds-2018-04-20"
INFO = {
  "DescribeDasbImageIds": {
    "params": [],
    "desc": "获取镜像列表"
  },
  "ModifyDbauditInstancesRenewFlag": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "0，表示默认状态(用户未设置，即初始状态)；1，表示自动续费；2，表示明确不自动续费"
      }
    ],
    "desc": "本接口 (ModifyDbauditInstancesRenewFlag) 用于修改数据安全审计产品实例续费标识"
  },
  "DescribeDbauditInstances": {
    "params": [
      {
        "name": "SearchRegion",
        "desc": "查询条件地域"
      },
      {
        "name": "Limit",
        "desc": "限制数目，默认10， 最大50"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认1"
      }
    ],
    "desc": "本接口 (DescribeDbauditInstances) 用于查询数据安全审计实例列表"
  },
  "InquiryPriceDbauditInstance": {
    "params": [
      {
        "name": "InstanceVersion",
        "desc": "实例规格，取值范围： cdsaudit，cdsaudit_adv， cdsaudit_ent 分别为合规版，高级版，企业版"
      },
      {
        "name": "InquiryType",
        "desc": "询价类型： renew，续费；newbuy，新购"
      },
      {
        "name": "TimeSpan",
        "desc": "购买实例的时长。取值范围：1（y/m），2（y/m）,，3（y/m），4（m）， 5（m），6（m）， 7（m），8（m），9（m）， 10（m）"
      },
      {
        "name": "TimeUnit",
        "desc": "购买时长单位，y：年；m：月"
      },
      {
        "name": "ServiceRegion",
        "desc": "实例所在地域"
      }
    ],
    "desc": "用于查询数据安全审计产品实例价格"
  },
  "DescribeDbauditUsedRegions": {
    "params": [],
    "desc": "本接口 (DescribeDbauditUsedRegions) 用于查询可售卖地域列表。"
  },
  "DescribeDbauditInstanceType": {
    "params": [],
    "desc": "本接口 (DescribeDbauditInstanceType) 用于查询可售卖的产品规格列表。"
  }
}