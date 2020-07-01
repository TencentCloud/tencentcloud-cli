# -*- coding: utf-8 -*-
DESC = "postgres-2017-03-12"
INFO = {
  "DescribeOrders": {
    "params": [
      {
        "name": "DealNames",
        "desc": "订单名集合"
      }
    ],
    "desc": "本接口（DescribeOrders）用于获取订单信息。"
  },
  "DestroyDBInstance": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "待删除实例标识符"
      }
    ],
    "desc": "本接口 (DestroyDBInstance) 用于销毁指定DBInstanceId对应的实例。"
  },
  "DescribeDBBackups": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-4wdeb0zv。"
      },
      {
        "name": "Type",
        "desc": "备份方式（1-全量）。目前只支持全量，取值为1。"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，形如2018-06-10 17:06:38"
      },
      {
        "name": "Limit",
        "desc": "备份列表分页返回，每页返回数量，默认为 20，最小为1，最大值为 100。（当该参数不传或者传0时按默认值处理）"
      },
      {
        "name": "Offset",
        "desc": "返回结果中的第几页，从第0页开始。默认为0。"
      }
    ],
    "desc": "本接口（DescribeDBBackups）用于查询实例备份列表。"
  },
  "ResetAccountPassword": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-4wdeb0zv"
      },
      {
        "name": "UserName",
        "desc": "实例账户名"
      },
      {
        "name": "Password",
        "desc": "UserName账户对应的新密码"
      }
    ],
    "desc": "本接口（ResetAccountPassword）用于重置实例的账户密码。"
  },
  "DescribeDBErrlogs": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-5bq3wfjd"
      },
      {
        "name": "StartTime",
        "desc": "查询起始时间，形如2018-01-01 00:00:00，起始时间不得小于7天以前"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，形如2018-01-01 00:00:00"
      },
      {
        "name": "DatabaseName",
        "desc": "数据库名字"
      },
      {
        "name": "SearchKeys",
        "desc": "搜索关键字"
      },
      {
        "name": "Limit",
        "desc": "分页返回，每页返回的最大数量。取值为1-100"
      },
      {
        "name": "Offset",
        "desc": "分页返回，返回第几页的数据，从第0页开始计数"
      }
    ],
    "desc": "本接口（DescribeDBErrlogs）用于获取错误日志。"
  },
  "DescribeDBInstanceAttribute": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID"
      }
    ],
    "desc": "本接口 (DescribeDBInstanceAttribute) 用于查询某个实例的详情信息。"
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
  },
  "OpenDBExtranetAccess": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-hez4fh0v"
      },
      {
        "name": "IsIpv6",
        "desc": "是否开通Ipv6外网，1：是，0：否"
      }
    ],
    "desc": "本接口（OpenDBExtranetAccess）用于开通外网。"
  },
  "CloseServerlessDBExtranetAccess": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例唯一标识符"
      },
      {
        "name": "DBInstanceName",
        "desc": "实例名称"
      }
    ],
    "desc": "关闭serverlessDB实例外网"
  },
  "ModifyDBInstancesProject": {
    "params": [
      {
        "name": "DBInstanceIdSet",
        "desc": "postgresql实例ID数组"
      },
      {
        "name": "ProjectId",
        "desc": "postgresql实例所属新项目的ID"
      }
    ],
    "desc": "本接口（ModifyDBInstancesProject）用于将实例转至其他项目。"
  },
  "ModifyAccountRemark": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-4wdeb0zv"
      },
      {
        "name": "UserName",
        "desc": "实例用户名"
      },
      {
        "name": "Remark",
        "desc": "用户UserName对应的新备注"
      }
    ],
    "desc": "本接口（ModifyAccountRemark）用于修改帐号备注。"
  },
  "DescribeDBXlogs": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-4wdeb0zv。"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，形如2018-06-10 17:06:38"
      },
      {
        "name": "Offset",
        "desc": "分页返回，表示返回第几页的条目。从第0页开始计数。"
      },
      {
        "name": "Limit",
        "desc": "分页返回，表示每页有多少条目。取值为1-100。"
      }
    ],
    "desc": "本接口（DescribeDBXlogs）用于获取实例Xlog列表。"
  },
  "SetAutoRenewFlag": {
    "params": [
      {
        "name": "DBInstanceIdSet",
        "desc": "实例ID数组"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "续费标记。0-正常续费；1-自动续费；2-到期不续费"
      }
    ],
    "desc": "本接口（SetAutoRenewFlag）用于设置自动续费。"
  },
  "RestartDBInstance": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-6r233v55"
      }
    ],
    "desc": "本接口（RestartDBInstance）用于重启实例。"
  },
  "ModifyDBInstanceName": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "数据库实例ID，形如postgres-6fego161"
      },
      {
        "name": "InstanceName",
        "desc": "新的数据库实例名字"
      }
    ],
    "desc": "本接口（ModifyDBInstanceName）用于修改postgresql实例名字。"
  },
  "CreateDBInstances": {
    "params": [
      {
        "name": "SpecCode",
        "desc": "售卖规格ID。该参数可以通过调用DescribeProductConfig的返回值中的SpecCode字段来获取。"
      },
      {
        "name": "DBVersion",
        "desc": "PostgreSQL内核版本，目前支持：9.3.5、9.5.4、10.4三种版本。"
      },
      {
        "name": "Storage",
        "desc": "实例容量大小，单位：GB。"
      },
      {
        "name": "InstanceCount",
        "desc": "一次性购买的实例数量。取值1-100"
      },
      {
        "name": "Period",
        "desc": "购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值，按量计费模式下该参数传1。"
      },
      {
        "name": "Zone",
        "desc": "可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID。"
      },
      {
        "name": "InstanceChargeType",
        "desc": "实例计费类型。目前支持：PREPAID（预付费，即包年包月），POSTPAID_BY_HOUR（后付费，即按量计费）。"
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
        "name": "AutoRenewFlag",
        "desc": "续费标记：0-正常续费（默认）；1-自动续费；"
      },
      {
        "name": "ActivityId",
        "desc": "活动ID"
      },
      {
        "name": "Name",
        "desc": "实例名(后续支持)"
      },
      {
        "name": "NeedSupportIpv6",
        "desc": "是否需要支持Ipv6，1：是，0：否"
      }
    ],
    "desc": "本接口 (CreateDBInstances) 用于创建一个或者多个PostgreSQL实例。"
  },
  "CreateServerlessDBInstance": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区ID。公测阶段仅支持ap-shanghai-2、ap-beijing-1,ap-guangzhou-2."
      },
      {
        "name": "DBInstanceName",
        "desc": "DB实例名称，同一个账号下该值必须唯一。"
      },
      {
        "name": "DBVersion",
        "desc": "PostgreSQL内核版本，目前只支持：10.4。"
      },
      {
        "name": "DBCharset",
        "desc": "PostgreSQL数据库字符集，目前支持UTF8。"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID。"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID。"
      },
      {
        "name": "SubnetId",
        "desc": "私有网络子网ID。"
      }
    ],
    "desc": "本接口 (CreateServerlessDBInstance) 用于创建一个ServerlessDB实例，创建成功返回实例ID。"
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件，目前支持：db-instance-id、db-instance-name、db-project-id、db-pay-mode。"
      },
      {
        "name": "Limit",
        "desc": "每页显示数量，默认返回10条。"
      },
      {
        "name": "Offset",
        "desc": "分页序号，从0开始。"
      },
      {
        "name": "OrderBy",
        "desc": "排序指标，如实例名、创建时间等，支持DBInstanceId,CreateTime,Name,EndTime"
      },
      {
        "name": "OrderByType",
        "desc": "排序方式，包括升序、降序"
      }
    ],
    "desc": "本接口 (DescribeDBInstances) 用于查询一个或多个实例的详细信息。"
  },
  "DescribeZones": {
    "params": [],
    "desc": "本接口 (DescribeZones) 用于查询支持的可用区信息。"
  },
  "DeleteServerlessDBInstance": {
    "params": [
      {
        "name": "DBInstanceName",
        "desc": "DB实例名称，实例名和实例ID必须至少传一个，如果同时存在，将只以实例ID为准。"
      },
      {
        "name": "DBInstanceId",
        "desc": "DB实例ID，实例名和实例ID必须至少传一个，如果同时存在，将只以实例ID为准。"
      }
    ],
    "desc": "本接口 (DeleteServerlessDBInstance) 用于删除一个ServerlessDB实例。"
  },
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
  "InquiryPriceUpgradeDBInstance": {
    "params": [
      {
        "name": "Storage",
        "desc": "实例的磁盘大小，单位GB"
      },
      {
        "name": "Memory",
        "desc": "实例的内存大小，单位GB"
      },
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-hez4fh0v"
      },
      {
        "name": "InstanceChargeType",
        "desc": "实例计费类型，预付费或者后付费。PREPAID-预付费。目前只支持预付费。"
      }
    ],
    "desc": "本接口（InquiryPriceUpgradeDBInstance）用于查询升级实例的价格。"
  },
  "DescribeRegions": {
    "params": [],
    "desc": "本接口 (DescribeRegions) 用于查询售卖地域信息。"
  },
  "InquiryPriceRenewDBInstance": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID"
      },
      {
        "name": "Period",
        "desc": "续费周期，按月计算，最大不超过48"
      }
    ],
    "desc": "本接口（InquiryPriceRenewDBInstance）用于查询续费实例的价格。"
  },
  "CloseDBExtranetAccess": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-6r233v55"
      },
      {
        "name": "IsIpv6",
        "desc": "是否关闭Ipv6外网，1：是，0：否"
      }
    ],
    "desc": "本接口（CloseDBExtranetAccess）用于关闭实例外网链接。"
  },
  "DescribeAccounts": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-6fego161"
      },
      {
        "name": "Limit",
        "desc": "分页返回，每页最大返回数目，默认20，取值范围为1-100"
      },
      {
        "name": "Offset",
        "desc": "分页返回，返回第几页的用户数据。页码从0开始计数"
      },
      {
        "name": "OrderBy",
        "desc": "返回数据按照创建时间或者用户名排序。取值只能为createTime或者name。createTime-按照创建时间排序；name-按照用户名排序"
      },
      {
        "name": "OrderByType",
        "desc": "返回结果是升序还是降序。取值只能为desc或者asc。desc-降序；asc-升序"
      }
    ],
    "desc": "本接口（DescribeAccounts）用于获取实例用户列表。"
  },
  "OpenServerlessDBExtranetAccess": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例的唯一标识符"
      },
      {
        "name": "DBInstanceName",
        "desc": "实例名称"
      }
    ],
    "desc": "开通serverlessDB实例外网"
  },
  "DescribeServerlessDBInstances": {
    "params": [
      {
        "name": "Filter",
        "desc": "查询条件"
      },
      {
        "name": "Limit",
        "desc": "查询个数"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      }
    ],
    "desc": "用于查询一个或多个serverlessDB实例的详细信息"
  },
  "RenewInstance": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-6fego161"
      },
      {
        "name": "Period",
        "desc": "续费多少个月"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券,1是,0否，默认不使用"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表，目前仅支持指定一张代金券"
      }
    ],
    "desc": "本接口（RenewInstance）用于续费实例。"
  },
  "DescribeDatabases": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID"
      }
    ],
    "desc": "接口（DescribeDatabases）用来拉取数据库列表"
  },
  "UpgradeDBInstance": {
    "params": [
      {
        "name": "Memory",
        "desc": "升级后的实例内存大小，单位GB"
      },
      {
        "name": "Storage",
        "desc": "升级后的实例磁盘大小，单位GB"
      },
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-lnp6j617"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券,1是,0否，默认不使用"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表，目前仅支持指定一张代金券"
      },
      {
        "name": "ActivityId",
        "desc": "活动ID"
      }
    ],
    "desc": "本接口（UpgradeDBInstance）用于升级实例。"
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
  "DescribeDBSlowlogs": {
    "params": [
      {
        "name": "DBInstanceId",
        "desc": "实例ID，形如postgres-lnp6j617"
      },
      {
        "name": "StartTime",
        "desc": "查询起始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，形如2018-06-10 17:06:38"
      },
      {
        "name": "DatabaseName",
        "desc": "数据库名字"
      },
      {
        "name": "OrderBy",
        "desc": "按照何种指标排序，取值为sum_calls或者sum_cost_time。sum_calls-总调用次数；sum_cost_time-总的花费时间"
      },
      {
        "name": "OrderByType",
        "desc": "排序规则。desc-降序；asc-升序"
      },
      {
        "name": "Limit",
        "desc": "分页返回结果，每页最大返回数量，取值为1-100，默认20"
      },
      {
        "name": "Offset",
        "desc": "分页返回结果，返回结果的第几页，从0开始计数"
      }
    ],
    "desc": "本接口（DescribeDBSlowlogs）用于获取慢查询日志。"
  }
}