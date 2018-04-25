# -*- coding: utf-8 -*-
DESC = "postgres-2017-03-12"
INFO = {
  "InitDBInstances": {
    "params": [
      {
        "name": "DBInstanceIdSet",
        "desc": "实例ID集合。"
      },
      {
        "name": "AdminName",
        "desc": "实例根账号用户名。"
      },
      {
        "name": "AdminPassword",
        "desc": "实例根账号用户名对应的密码。"
      },
      {
        "name": "Charset",
        "desc": "实例字符集，目前只支持：UTF8、LATIN1。"
      }
    ],
    "desc": "本接口 (InitDBInstances) 用于初始化云数据库PostgreSQL实例。"
  },
  "DescribeZones": {
    "params": [],
    "desc": "本接口 (DescribeZones) 用于查询支持的可用区信息。"
  },
  "DescribeRegions": {
    "params": [],
    "desc": "本接口 (DescribeRegions) 用于查询售卖地域信息。"
  },
  "DescribeDBInstanceAttribute": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID。"
      }
    ],
    "desc": "本接口 (DescribeDBInstanceAttribute) 用于查询某个实例的详情信息。"
  },
  "CreateDBInstances": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID。"
      },
      {
        "name": "SpecCode",
        "desc": "售卖规格ID。该参数可以通过调用DescribeProductConfig的返回值中的SpecCode字段来获取。"
      },
      {
        "name": "DBVersion",
        "desc": "PostgreSQL内核版本，目前只支持：9.3.5、9.5.4两种版本。"
      },
      {
        "name": "Storage",
        "desc": "实例容量大小，单位：GB。"
      },
      {
        "name": "InstanceCount",
        "desc": "一次性购买的实例数量。"
      },
      {
        "name": "Period",
        "desc": "购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值。"
      },
      {
        "name": "InstanceChargeType",
        "desc": "实例计费类型。目前只支持：PREPAID（预付费，即包年包月）。"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券。1（是），0（否），默认不使用。"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表，目前仅支持指定一张代金券。"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID。"
      },
      {
        "name": "SubnetId",
        "desc": "私有网络子网ID。"
      },
      {
        "name": "Zone",
        "desc": "可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。"
      }
    ],
    "desc": "本接口 (CreateDBInstances) 用于创建一个或者多个PostgreSQL实例。"
  },
  "DescribeProductConfig": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区名称"
      }
    ],
    "desc": "本接口 (DescribeProductConfig) 用于查询售卖规格配置。"
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "PageSize",
        "desc": "每页显示数量，默认返回10条。"
      },
      {
        "name": "PageNumber",
        "desc": "分页序号，从1开始。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，目前支持：db-instance-id、db-instance-name两种。"
      }
    ],
    "desc": "本接口 (DescribeDBInstances) 用于查询一个或多个实例的详细信息。"
  },
  "InquiryPriceCreateDBInstances": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。"
      },
      {
        "name": "SpecCode",
        "desc": "规格ID。该参数可以通过调用DescribeProductConfig接口的返回值中的SpecCode字段来获取。"
      },
      {
        "name": "Storage",
        "desc": "存储容量大小，单位：GB。"
      },
      {
        "name": "InstanceCount",
        "desc": "实例数量。目前最大数量不超过100，如需一次性创建更多实例，请联系客服支持。"
      },
      {
        "name": "Period",
        "desc": "购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值。"
      },
      {
        "name": "Pid",
        "desc": "计费ID。该参数可以通过调用DescribeProductConfig接口的返回值中的Pid字段来获取。"
      },
      {
        "name": "InstanceChargeType",
        "desc": "实例计费类型。目前只支持：PREPAID（预付费，即包年包月）。"
      }
    ],
    "desc": "本接口 (InquiryPriceCreateDBInstances) 用于查询购买一个或多个实例的价格信息。"
  }
}