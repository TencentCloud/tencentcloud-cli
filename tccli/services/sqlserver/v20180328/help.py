# -*- coding: utf-8 -*-
DESC = "sqlserver-2018-03-28"
INFO = {
  "ModifyMigration": {
    "params": [
      {
        "name": "MigrateId",
        "desc": "迁移任务ID"
      },
      {
        "name": "MigrateName",
        "desc": "新的迁移任务的名称，若不填则不修改"
      },
      {
        "name": "MigrateType",
        "desc": "新的迁移类型（1:结构迁移 2:数据迁移 3:增量同步），若不填则不修改"
      },
      {
        "name": "SourceType",
        "desc": "迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式），若不填则不修改"
      },
      {
        "name": "Source",
        "desc": "迁移源，若不填则不修改"
      },
      {
        "name": "Target",
        "desc": "迁移目标，若不填则不修改"
      },
      {
        "name": "MigrateDBSet",
        "desc": "迁移DB对象 ，离线迁移（SourceType=4或SourceType=5）不使用，若不填则不修改"
      }
    ],
    "desc": "本接口（ModifyMigration）可以修改已有的迁移任务信息"
  },
  "DescribeOrders": {
    "params": [
      {
        "name": "DealNames",
        "desc": "订单数组。发货时会返回订单名字，利用该订单名字调用DescribeOrders接口查询发货情况"
      }
    ],
    "desc": "本接口（DescribeOrders）用于查询订单信息"
  },
  "DescribeMigrations": {
    "params": [
      {
        "name": "StatusSet",
        "desc": "状态集合。只要符合集合中某一状态的迁移任务，就会查出来"
      },
      {
        "name": "MigrateName",
        "desc": "迁移任务的名称，模糊匹配"
      },
      {
        "name": "Limit",
        "desc": "分页返回，每页返回的数目，取值为1-100，默认值为100"
      },
      {
        "name": "Offset",
        "desc": "分页返回，页编号，默认值为第0页"
      },
      {
        "name": "OrderBy",
        "desc": "查询结果按照关键字排序，可选值为name、createTime、startTime，endTime，status"
      },
      {
        "name": "OrderByType",
        "desc": "排序方式，可选值为desc、asc"
      }
    ],
    "desc": "本接口（DescribeMigrations）根据输入的限定条件，查询符合条件的迁移任务列表"
  },
  "ModifyDBName": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "OldDBName",
        "desc": "旧数据库名"
      },
      {
        "name": "NewDBName",
        "desc": "新数据库名"
      }
    ],
    "desc": "本接口（ModifyDBName）用于更新数据库名。"
  },
  "ResetAccountPassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "数据库实例ID，形如mssql-njj2mtpl"
      },
      {
        "name": "Accounts",
        "desc": "更新后的账户密码信息数组"
      }
    ],
    "desc": "本接口（ResetAccountPassword）用于重置实例的账户密码。"
  },
  "InquiryPriceCreateDBInstances": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。"
      },
      {
        "name": "Memory",
        "desc": "内存大小，单位：GB"
      },
      {
        "name": "Storage",
        "desc": "实例容量大小，单位：GB。"
      },
      {
        "name": "InstanceChargeType",
        "desc": "计费类型，取值支持 PREPAID，POSTPAID。"
      },
      {
        "name": "Period",
        "desc": "购买时长，单位：月。取值为1到48，默认为1"
      },
      {
        "name": "GoodsNum",
        "desc": "一次性购买的实例数量。取值1-100，默认取值为1"
      },
      {
        "name": "DBVersion",
        "desc": "sqlserver版本，目前只支持：2008R2（SQL Server 2008 Enterprise），2012SP3（SQL Server 2012 Enterprise），2016SP1（SQL Server 2016 Enterprise），201602（SQL Server 2016 Standard）2017（SQL Server 2017 Enterprise）版本。默认为2008R2版本"
      }
    ],
    "desc": "本接口（InquiryPriceCreateDBInstances）用于查询申请实例价格。"
  },
  "ModifyDBInstanceProject": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "实例ID数组，形如mssql-j8kv137v"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，为0的话表示默认项目"
      }
    ],
    "desc": "本接口（ModifyDBInstanceProject）用于修改数据库实例所属项目。"
  },
  "DescribeSlowlogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，形如mssql-k8voqdlz"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      },
      {
        "name": "Limit",
        "desc": "分页返回，每页返回的数目，取值为1-100，默认值为20"
      },
      {
        "name": "Offset",
        "desc": "分页返回，页编号，默认值为第0页"
      }
    ],
    "desc": "本接口（DescribeSlowlogs）用于获取慢查询日志文件信息"
  },
  "DescribeBackups": {
    "params": [
      {
        "name": "StartTime",
        "desc": "开始时间(yyyy-MM-dd HH:mm:ss)"
      },
      {
        "name": "EndTime",
        "desc": "结束时间(yyyy-MM-dd HH:mm:ss)"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID，形如mssql-njj2mtpl"
      },
      {
        "name": "Limit",
        "desc": "分页返回，每页返回的数目，取值为1-100，默认值为20"
      },
      {
        "name": "Offset",
        "desc": "分页返回，页编号，默认值为第0页"
      }
    ],
    "desc": "本接口(DescribeBackups)用于查询备份列表。"
  },
  "DescribeFlowStatus": {
    "params": [
      {
        "name": "FlowId",
        "desc": "流程ID"
      }
    ],
    "desc": "本接口(DescribeFlowStatus)用于查询流程状态。"
  },
  "ModifyAccountRemark": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，形如mssql-j8kv137v"
      },
      {
        "name": "Accounts",
        "desc": "修改备注的账户信息"
      }
    ],
    "desc": "本接口（ModifyAccountRemark）用于修改账户备注。"
  },
  "ModifyAccountPrivilege": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "数据库实例ID，形如mssql-njj2mtpl"
      },
      {
        "name": "Accounts",
        "desc": "账号权限变更信息"
      }
    ],
    "desc": "本接口（ModifyAccountPrivilege）用于修改实例账户权限。"
  },
  "RestartDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "数据库实例ID，形如mssql-njj2mtpl"
      }
    ],
    "desc": "本接口（RestartDBInstance）用于重启数据库实例。"
  },
  "ModifyDBInstanceName": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "数据库实例ID，形如mssql-njj2mtpl"
      },
      {
        "name": "InstanceName",
        "desc": "新的数据库实例名字"
      }
    ],
    "desc": "本接口（ModifyDBInstanceName）用于修改实例名字。"
  },
  "TerminateDBInstance": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "主动销毁的实例ID列表，格式如：[mssql-3l3fgqn7]。与云数据库控制台页面中显示的实例ID相同"
      }
    ],
    "desc": "本接口(TerminateDBInstance)用于主动销毁按量计费实例。"
  },
  "CreateBackup": {
    "params": [
      {
        "name": "Strategy",
        "desc": "备份策略(0-实例备份 1-多库备份)"
      },
      {
        "name": "DBNames",
        "desc": "需要备份库名的列表(多库备份才填写)"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID，形如mssql-i1z41iwd"
      }
    ],
    "desc": "本接口(CreateBackup)用于创建备份。"
  },
  "CreateDBInstances": {
    "params": [
      {
        "name": "Zone",
        "desc": "实例可用区，类似ap-guangzhou-1（广州一区）；实例可售卖区域可以通过接口DescribeZones获取"
      },
      {
        "name": "Memory",
        "desc": "实例内存大小，单位GB"
      },
      {
        "name": "Storage",
        "desc": "实例磁盘大小，单位GB"
      },
      {
        "name": "InstanceChargeType",
        "desc": "付费模式，取值支持 PREPAID（预付费），POSTPAID（后付费）。"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID"
      },
      {
        "name": "GoodsNum",
        "desc": "本次购买几个实例，默认值为1。取值不超过10"
      },
      {
        "name": "SubnetId",
        "desc": "VPC子网ID，形如subnet-bdoe83fa；SubnetId和VpcId需同时设置或者同时不设置"
      },
      {
        "name": "VpcId",
        "desc": "VPC网络ID，形如vpc-dsp338hz；SubnetId和VpcId需同时设置或者同时不设置"
      },
      {
        "name": "Period",
        "desc": "购买实例周期，默认取值为1，表示一个月。取值不超过48"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券；1 - 是，0 - 否，默认不使用"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID数组，目前单个订单只能使用一张"
      },
      {
        "name": "DBVersion",
        "desc": "sqlserver版本，目前只支持：2008R2（SQL Server 2008 Enterprise），2012SP3（SQL Server 2012 Enterprise），2016SP1（SQL Server 2016 Enterprise），201602（SQL Server 2016 Standard）2017（SQL Server 2017 Enterprise）版本。每个地域支持售卖的版本不同，可通过DescribeProductConfig接口来拉取每个地域可售卖的版本信息。不填，默认为版本2008R2。"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "自动续费标志：0-正常续费  1-自动续费，默认为1自动续费。只在购买预付费实例时有效。"
      }
    ],
    "desc": "本接口（CreateDBInstances）用于创建实例。"
  },
  "RollbackInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "Type",
        "desc": "回档类型，0-回档的数据库覆盖原库；1-回档的数据库以重命名的形式生成，不覆盖原库"
      },
      {
        "name": "DBs",
        "desc": "需要回档的数据库"
      },
      {
        "name": "Time",
        "desc": "回档目标时间点"
      }
    ],
    "desc": "本接口（RollbackInstance）用于回档实例"
  },
  "DescribeDBs": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "实例ID"
      },
      {
        "name": "Limit",
        "desc": "分页返回，每页返回的数目，取值为1-100，默认值为20"
      },
      {
        "name": "Offset",
        "desc": "分页返回，页编号，默认值为第0页"
      }
    ],
    "desc": "本接口（DescribeDBs）用于查询数据库列表。"
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      },
      {
        "name": "Status",
        "desc": "实例状态。取值范围：\n<li>1：申请中</li>\n<li>2：运行中</li>\n<li>3：受限运行中 (主备切换中)</li>\n<li>4：已隔离</li>\n<li>5：回收中</li>\n<li>6：已回收</li>\n<li>7：任务执行中 (实例做备份、回档等操作)</li>\n<li>8：已下线</li>\n<li>9：实例扩容中</li>\n<li>10：实例迁移中</li>\n<li>11：只读</li>\n<li>12：重启中</li>"
      },
      {
        "name": "Offset",
        "desc": "分页返回，页编号，默认值为第0页"
      },
      {
        "name": "Limit",
        "desc": "分页返回，每页返回的数目，取值为1-100，默认值为100"
      },
      {
        "name": "InstanceIdSet",
        "desc": "一个或者多个实例ID。实例ID，格式如：mssql-si2823jyl"
      },
      {
        "name": "PayMode",
        "desc": "付费类型检索 1-包年包月，0-按量计费"
      },
      {
        "name": "VpcId",
        "desc": "实例所属VPC的唯一字符串ID，格式如：vpc-xxx，传空字符串(“”)则按照基础网络筛选。"
      },
      {
        "name": "SubnetId",
        "desc": "实例所属子网的唯一字符串ID，格式如： subnet-xxx，传空字符串(“”)则按照基础网络筛选。"
      }
    ],
    "desc": "本接口(DescribeDBInstances)用于查询实例列表。"
  },
  "DescribeZones": {
    "params": [],
    "desc": "本接口 (DescribeZones) 用于查询当前可售卖的可用区信息。"
  },
  "ModifyDBRemark": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，形如mssql-rljoi3bf"
      },
      {
        "name": "DBRemarks",
        "desc": "数据库名称及备注数组，每个元素包含数据库名和对应的备注"
      }
    ],
    "desc": "本接口（ModifyDBRemark）用于修改数据库备注。"
  },
  "RenewDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，形如mssql-j8kv137v"
      },
      {
        "name": "Period",
        "desc": "续费多少个月，取值范围为1-48，默认为1"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券，0-不使用；1-使用；默认不实用"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID数组，目前只支持使用1张代金券"
      }
    ],
    "desc": "本接口（RenewDBInstance）用于续费实例。"
  },
  "CreateAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "数据库实例ID，形如mssql-njj2mtpl"
      },
      {
        "name": "Accounts",
        "desc": "数据库实例账户信息"
      }
    ],
    "desc": "本接口（CreateAccount）用于创建实例账号"
  },
  "InquiryPriceUpgradeDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，形如mssql-njj2mtpl"
      },
      {
        "name": "Memory",
        "desc": "实例升级后的内存大小，单位GB，其值不能比当前实例内存小"
      },
      {
        "name": "Storage",
        "desc": "实例升级后的磁盘大小，单位GB，其值不能比当前实例磁盘小"
      }
    ],
    "desc": "本接口（InquiryPriceUpgradeDBInstance）用于查询升级实例的价格。"
  },
  "CreateMigration": {
    "params": [
      {
        "name": "MigrateName",
        "desc": "迁移任务的名称"
      },
      {
        "name": "MigrateType",
        "desc": "迁移类型（1:结构迁移 2:数据迁移 3:增量同步）"
      },
      {
        "name": "SourceType",
        "desc": "迁移源的类型 1:TencentDB for SQLServer 2:云服务器自建SQLServer数据库 4:SQLServer备份还原 5:SQLServer备份还原（COS方式）"
      },
      {
        "name": "Source",
        "desc": "迁移源"
      },
      {
        "name": "Target",
        "desc": "迁移目标"
      },
      {
        "name": "MigrateDBSet",
        "desc": "迁移DB对象 ，离线迁移不使用（SourceType=4或SourceType=5）。"
      }
    ],
    "desc": "本接口（CreateMigration）作用是创建一个迁移任务"
  },
  "DescribeRegions": {
    "params": [],
    "desc": "本接口 (DescribeRegions) 用于查询售卖地域信息。"
  },
  "InquiryPriceRenewDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "Period",
        "desc": "续费周期。按月续费最多48个月。默认查询续费一个月的价格"
      },
      {
        "name": "TimeUnit",
        "desc": "续费周期单位。month表示按月续费，当前只支持按月付费查询价格"
      }
    ],
    "desc": "本接口（InquiryPriceRenewDBInstance）用于查询续费实例的价格。"
  },
  "DeleteMigration": {
    "params": [
      {
        "name": "MigrateId",
        "desc": "迁移任务ID"
      }
    ],
    "desc": "本接口（DeleteMigration）用于删除迁移任务"
  },
  "DescribeAccounts": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "Limit",
        "desc": "分页返回，每页返回的数目，取值为1-100，默认值为20"
      },
      {
        "name": "Offset",
        "desc": "分页返回，页编号，默认值为第0页"
      }
    ],
    "desc": "本接口（DescribeAccounts）用于拉取实例账户列表。"
  },
  "DescribeRollbackTime": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "DBs",
        "desc": "需要查询的数据库列表"
      }
    ],
    "desc": "本接口（DescribeRollbackTime）用于查询实例可回档时间范围"
  },
  "DeleteDB": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，形如mssql-rljoi3bf"
      },
      {
        "name": "Names",
        "desc": "数据库名数组"
      }
    ],
    "desc": "本接口(DeleteDB)用于删除数据库。"
  },
  "CreateDB": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "DBs",
        "desc": "数据库创建信息"
      }
    ],
    "desc": "本接口（CreateDB）用于创建数据库。"
  },
  "DeleteAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "数据库实例ID，形如mssql-njj2mtpl"
      },
      {
        "name": "UserNames",
        "desc": "实例用户名数组"
      }
    ],
    "desc": "本接口（DeleteAccount）用于删除实例账号。"
  },
  "DescribeMigrationDetail": {
    "params": [
      {
        "name": "MigrateId",
        "desc": "迁移任务ID"
      }
    ],
    "desc": "本接口（DescribeMigrationDetail）用于查询迁移任务的详细情况"
  },
  "RestoreInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，形如mssql-j8kv137v"
      },
      {
        "name": "BackupId",
        "desc": "备份文件ID，该ID可以通过DescribeBackups接口返回数据中的Id字段获得"
      }
    ],
    "desc": "本接口（RestoreInstance）用于根据备份文件恢复实例。"
  },
  "UpgradeDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，形如mssql-j8kv137v"
      },
      {
        "name": "Memory",
        "desc": "实例升级后内存大小，单位GB，其值不能小于当前实例内存大小"
      },
      {
        "name": "Storage",
        "desc": "实例升级后磁盘大小，单位GB，其值不能小于当前实例磁盘大小"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券，0 - 不使用；1 - 默认使用。取值默认为0"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID，目前单个订单只能使用一张代金券"
      }
    ],
    "desc": "本接口（UpgradeDBInstance）用于升级实例"
  },
  "RunMigration": {
    "params": [
      {
        "name": "MigrateId",
        "desc": "迁移任务ID"
      }
    ],
    "desc": "本接口（RunMigration）用于启动迁移任务，开始迁移"
  },
  "DescribeProductConfig": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区英文ID，形如ap-guangzhou-1"
      }
    ],
    "desc": "本接口 (DescribeProductConfig) 用于查询售卖规格配置。"
  },
  "ModifyDBInstanceRenewFlag": {
    "params": [
      {
        "name": "RenewFlags",
        "desc": "实例续费状态标记信息"
      }
    ],
    "desc": "本接口（ModifyDBInstanceRenewFlag）用于修改实例续费标记"
  }
}