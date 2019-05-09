# -*- coding: utf-8 -*-
DESC = "mariadb-2017-03-12"
INFO = {
  "DescribeAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "UserName",
        "desc": "登录用户名。"
      },
      {
        "name": "Host",
        "desc": "用户允许的访问 host，用户名+host唯一确定一个账号。"
      },
      {
        "name": "DbName",
        "desc": "数据库名。如果为 \\*，表示查询全局权限（即 \\*.\\*），此时忽略 Type 和 Object 参数"
      },
      {
        "name": "Type",
        "desc": "类型,可以填入 table 、 view 、 proc 、 func 和 \\*。当 DbName 为具体数据库名，Type为 \\* 时，表示查询该数据库权限（即db.\\*），此时忽略 Object 参数"
      },
      {
        "name": "Object",
        "desc": "具体的 Type 的名称，比如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \\* 或者为空"
      },
      {
        "name": "ColName",
        "desc": "当 Type=table 时，ColName 为 \\* 表示查询表的权限，如果为具体字段名，表示查询对应字段的权限"
      }
    ],
    "desc": "本接口（DescribeAccountPrivileges）用于查询云数据库账号权限。\n注意：注意：相同用户名，不同Host是不同的账号。"
  },
  "DescribeRenewalPrice": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待续费的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "Period",
        "desc": "续费时长，单位：月。不传则默认为1个月。"
      }
    ],
    "desc": "本接口（DescribeRenewalPrice）用于在续费云数据库实例时，查询续费的价格。"
  },
  "DescribeOrders": {
    "params": [
      {
        "name": "DealNames",
        "desc": "待查询的长订单号列表，创建实例、续费实例、扩容实例接口返回。"
      }
    ],
    "desc": "本接口（DescribeOrders）用于查询云数据库订单信息。传入订单Id来查询订单关联的云数据库实例，和对应的任务流程ID。"
  },
  "DescribeSaleInfo": {
    "params": [],
    "desc": "本接口(DescribeSaleInfo)用于查询云数据库可售卖的地域和可用区信息。"
  },
  "ModifyAccountDescription": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "UserName",
        "desc": "登录用户名。"
      },
      {
        "name": "Host",
        "desc": "用户允许的访问 host，用户名+host唯一确定一个账号。"
      },
      {
        "name": "Description",
        "desc": "新的账号备注，长度 0~256。"
      }
    ],
    "desc": "本接口（ModifyAccountDescription）用于修改云数据库账号备注。\n注意：相同用户名，不同Host是不同的账号。"
  },
  "DescribeBackupTime": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      }
    ],
    "desc": "本接口（DescribeBackupTime）用于获取云数据库的备份时间。后台系统将根据此配置定期进行实例备份。"
  },
  "DescribeDBResourceUsageDetails": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc。"
      },
      {
        "name": "StartTime",
        "desc": "开始日期，格式yyyy-mm-dd"
      },
      {
        "name": "EndTime",
        "desc": "结束日期，格式yyyy-mm-dd"
      },
      {
        "name": "MetricName",
        "desc": "拉取的指标名称，支持的值为：data_disk_available,binlog_disk_available,mem_available,cpu_usage_rate"
      }
    ],
    "desc": "本接口(DescribeDBResourceUsageDetails)用于查看数据库实例当前性能数据。"
  },
  "ResetAccountPassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "UserName",
        "desc": "登录用户名。"
      },
      {
        "name": "Host",
        "desc": "用户允许的访问 host，用户名+host唯一确定一个账号。"
      },
      {
        "name": "Password",
        "desc": "新密码，由字母、数字或常见符号组成，不能包含分号、单引号和双引号，长度为6~32位。"
      }
    ],
    "desc": "本接口（ResetAccountPassword）用于重置云数据库账号的密码。\n注意：相同用户名，不同Host是不同的账号。"
  },
  "ModifyDBParameters": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc。"
      },
      {
        "name": "Params",
        "desc": "参数列表，每一个元素是Param和Value的组合"
      }
    ],
    "desc": "本接口(ModifyDBParameters)用于修改数据库参数。"
  },
  "ModifyLogFileRetentionPeriod": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc。"
      },
      {
        "name": "Days",
        "desc": "保存的天数,不能超过30"
      }
    ],
    "desc": "本接口(ModifyLogFileRetentionPeriod)用于修改数据库备份日志保存天数。"
  },
  "DescribeDBPerformanceDetails": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc。"
      },
      {
        "name": "StartTime",
        "desc": "开始日期，格式yyyy-mm-dd"
      },
      {
        "name": "EndTime",
        "desc": "结束日期，格式yyyy-mm-dd"
      },
      {
        "name": "MetricName",
        "desc": "拉取的指标名，支持的值为：long_query,select_total,update_total,insert_total,delete_total,mem_hit_rate,disk_iops,conn_active,is_master_switched,slave_delay"
      }
    ],
    "desc": "本接口(DescribeDBPerformanceDetails)用于查看实例性能数据详情。"
  },
  "DescribeFlow": {
    "params": [
      {
        "name": "FlowId",
        "desc": "异步请求接口返回的任务流程号。"
      }
    ],
    "desc": "本接口（DescribeFlow）用于查询流程状态。"
  },
  "DescribeDBLogFiles": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc。"
      },
      {
        "name": "Type",
        "desc": "请求日志类型，取值只能为1、2、3或者4。1-binlog，2-冷备，3-errlog，4-slowlog。"
      }
    ],
    "desc": "本接口(DescribeDBLogFiles)用于获取数据库的各种日志列表，包括冷备、binlog、errlog和slowlog。"
  },
  "GrantAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "UserName",
        "desc": "登录用户名。"
      },
      {
        "name": "Host",
        "desc": "用户允许的访问 host，用户名+host唯一确定一个账号。"
      },
      {
        "name": "DbName",
        "desc": "数据库名。如果为 \\*，表示设置全局权限（即 \\*.\\*），此时忽略 Type 和 Object 参数。当DbName不为\\*时，需要传入参 Type。"
      },
      {
        "name": "Privileges",
        "desc": "全局权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER，SHOW DATABASES \n库权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER \n表/视图权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE VIEW，SHOW VIEW，TRIGGER \n存储过程/函数权限： ALTER ROUTINE，EXECUTE \n字段权限： INSERT，REFERENCES，SELECT，UPDATE"
      },
      {
        "name": "Type",
        "desc": "类型,可以填入 table 、 view 、 proc 、 func 和 \\*。当 DbName 为具体数据库名，Type为 \\* 时，表示设置该数据库权限（即db.\\*），此时忽略 Object 参数"
      },
      {
        "name": "Object",
        "desc": "具体的 Type 的名称，比如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \\* 或者为空"
      },
      {
        "name": "ColName",
        "desc": "当 Type=table 时，ColName 为 \\* 表示对表授权，如果为具体字段名，表示对字段授权"
      }
    ],
    "desc": "本接口（GrantAccountPrivileges）用于给云数据库账号赋权。\n注意：相同用户名，不同Host是不同的账号。"
  },
  "DeleteAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "UserName",
        "desc": "用户名"
      },
      {
        "name": "Host",
        "desc": "用户允许的访问 host"
      }
    ],
    "desc": "本接口（DeleteAccount）用于删除云数据库账号。用户名+host唯一确定一个账号。"
  },
  "DescribeDBParameters": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc。"
      }
    ],
    "desc": "本接口(DescribeDBParameters)用于获取数据库的当前参数设置。"
  },
  "ModifyDBInstancesProject": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "待修改的实例ID列表。实例 ID 形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "ProjectId",
        "desc": "要分配的项目 ID，可以通过 DescribeProjects 查询项目列表接口获取。"
      }
    ],
    "desc": "本接口（ModifyDBInstancesProject）用于修改云数据库实例所属项目。"
  },
  "DescribeSqlLogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "Offset",
        "desc": "SQL日志偏移。"
      },
      {
        "name": "Limit",
        "desc": "拉取数量（0-10000，为0时拉取总数信息）。"
      }
    ],
    "desc": "本接口（DescribeSqlLogs）用于获取实例SQL日志。"
  },
  "ModifyDBInstanceName": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待修改的实例 ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "InstanceName",
        "desc": "新的实例名称。允许的字符为字母、数字、下划线、连字符和中文。"
      }
    ],
    "desc": "本接口（ModifyDBInstanceName）用于修改云数据库实例的名称。"
  },
  "DescribeDBInstanceSpecs": {
    "params": [],
    "desc": "本接口(DescribeDBInstanceSpecs)用于查询可创建的云数据库可售卖的规格配置。"
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "按照一个或者多个实例 ID 查询。实例 ID 形如：tdsql-ow728lmc。每次请求的实例的上限为100。"
      },
      {
        "name": "SearchName",
        "desc": "搜索的字段名，当前支持的值有：instancename、vip、all。传 instancename 表示按实例名进行搜索；传 vip 表示按内网IP进行搜索；传 all 将会按实例ID、实例名和内网IP进行搜索。"
      },
      {
        "name": "SearchKey",
        "desc": "搜索的关键字，支持模糊搜索。多个关键字使用换行符（'\\n'）分割。"
      },
      {
        "name": "ProjectIds",
        "desc": "按项目 ID 查询"
      },
      {
        "name": "IsFilterVpc",
        "desc": "是否根据 VPC 网络来搜索"
      },
      {
        "name": "VpcId",
        "desc": "私有网络 ID， IsFilterVpc 为 1 时有效"
      },
      {
        "name": "SubnetId",
        "desc": "私有网络的子网 ID， IsFilterVpc 为 1 时有效"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段， projectId， createtime， instancename 三者之一"
      },
      {
        "name": "OrderByType",
        "desc": "排序类型， desc 或者 asc"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "OriginSerialIds",
        "desc": "按 OriginSerialId 查询"
      },
      {
        "name": "IsFilterExcluster",
        "desc": "标识是否使用ExclusterType字段, false不使用，true使用"
      },
      {
        "name": "ExclusterType",
        "desc": "实例所属独享集群类型。取值范围：1-非独享集群，2-独享集群， 0-全部"
      },
      {
        "name": "ExclusterIds",
        "desc": "按独享集群Id过滤实例，独享集群Id形如dbdc-4ih6uct9"
      }
    ],
    "desc": "本接口（DescribeDBInstances）用于查询云数据库实例列表，支持通过项目ID、实例ID、内网地址、实例名称等来筛选实例。\n如果不指定任何筛选条件，则默认返回20条实例记录，单次请求最多支持返回100条实例记录。"
  },
  "RenewDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待续费的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "Period",
        "desc": "续费时长，单位：月。"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券进行支付，默认不使用。"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表，目前仅支持指定一张代金券。"
      }
    ],
    "desc": "本接口（RenewDBInstance）用于续费云数据库实例。"
  },
  "DescribeUpgradePrice": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待升级的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "Memory",
        "desc": "内存大小，单位：GB，可以通过 DescribeDBInstanceSpecs\n 查询实例规格获得。"
      },
      {
        "name": "Storage",
        "desc": "存储空间大小，单位：GB，可以通过 DescribeDBInstanceSpecs\n 查询实例规格获得不同内存大小对应的磁盘规格下限和上限。"
      }
    ],
    "desc": "本接口（DescribeUpgradePrice）用于在扩容云数据库实例时，查询扩容的价格。"
  },
  "CreateDBInstance": {
    "params": [
      {
        "name": "Zones",
        "desc": "实例节点可用区分布，最多可填两个可用区。当分片规格为一主两从时，其中两个节点在第一个可用区。"
      },
      {
        "name": "NodeCount",
        "desc": "节点个数大小，可以通过 DescribeDBInstanceSpecs\n 查询实例规格获得。"
      },
      {
        "name": "Memory",
        "desc": "内存大小，单位：GB，可以通过 DescribeDBInstanceSpecs\n 查询实例规格获得。"
      },
      {
        "name": "Storage",
        "desc": "存储空间大小，单位：GB，可以通过 DescribeDBInstanceSpecs\n 查询实例规格获得不同内存大小对应的磁盘规格下限和上限。"
      },
      {
        "name": "Period",
        "desc": "欲购买的时长，单位：月。"
      },
      {
        "name": "Count",
        "desc": "欲购买的数量，默认查询购买1个实例的价格。"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券进行支付，默认不使用。"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表，目前仅支持指定一张代金券。"
      },
      {
        "name": "VpcId",
        "desc": "虚拟私有网络 ID，不传表示创建为基础网络"
      },
      {
        "name": "SubnetId",
        "desc": "虚拟私有网络子网 ID，VpcId 不为空时必填"
      },
      {
        "name": "ProjectId",
        "desc": "项目 ID，可以通过查看项目列表获取，不传则关联到默认项目"
      },
      {
        "name": "DbVersionId",
        "desc": "数据库引擎版本，当前可选：10.0.10，10.1.9，5.7.17。如果不传的话，默认为 Mariadb 10.1.9。"
      }
    ],
    "desc": "本接口（CreateDBInstance）用于创建包年包月的云数据库实例，可通过传入实例规格、数据库版本号、购买时长和数量等信息创建云数据库实例。"
  },
  "CreateAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "UserName",
        "desc": "登录用户名，由字幕、数字、下划线和连字符组成，长度为1~32位。"
      },
      {
        "name": "Host",
        "desc": "可以登录的主机，与mysql 账号的 host 格式一致，可以支持通配符，例如 %，10.%，10.20.%。"
      },
      {
        "name": "Password",
        "desc": "账号密码，由字母、数字或常见符号组成，不能包含分号、单引号和双引号，长度为6~32位。"
      },
      {
        "name": "ReadOnly",
        "desc": "是否创建为只读账号，0：否， 1：该账号的sql请求优先选择备机执行，备机不可用时选择主机执行，2：优先选择备机执行，备机不可用时操作失败。"
      },
      {
        "name": "Description",
        "desc": "账号备注，可以包含中文、英文字符、常见符号和数字，长度为0~256字符"
      },
      {
        "name": "DelayThresh",
        "desc": "根据传入时间判断备机不可用"
      }
    ],
    "desc": "本接口（CreateAccount）用于创建云数据库账号。一个实例可以创建多个不同的账号，相同的用户名+不同的host是不同的账号。"
  },
  "OpenDBExtranetAccess": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待开放外网访问的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      }
    ],
    "desc": "本接口（OpenDBExtranetAccess）用于开通云数据库实例的外网访问。开通外网访问后，您可通过外网域名和端口访问实例，可使用查询实例列表接口获取外网域名和端口信息。"
  },
  "InitDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "待初始化的实例Id列表，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "Params",
        "desc": "参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步）。"
      }
    ],
    "desc": "本接口(InitDBInstances)用于初始化云数据库实例，包括设置默认字符集、表名大小写敏感等。"
  },
  "ModifyBackupTime": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "StartBackupTime",
        "desc": "每天备份执行的区间的开始时间，格式 mm:ss，形如 22:00"
      },
      {
        "name": "EndBackupTime",
        "desc": "每天备份执行的区间的结束时间，格式 mm:ss，形如 23:59"
      }
    ],
    "desc": "本接口（ModifyBackupTime）用于设置云数据库实例的备份时间。后台系统将根据此配置定期进行实例备份。"
  },
  "DescribeDBSlowLogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc。"
      },
      {
        "name": "Offset",
        "desc": "从结果的第几条数据开始返回"
      },
      {
        "name": "Limit",
        "desc": "返回的结果条数"
      },
      {
        "name": "StartTime",
        "desc": "查询的起始时间，形如2016-07-23 14:55:20"
      },
      {
        "name": "EndTime",
        "desc": "查询的结束时间，形如2016-08-22 14:55:20"
      },
      {
        "name": "Db",
        "desc": "要查询的具体数据库名称"
      },
      {
        "name": "OrderBy",
        "desc": "排序指标，取值为query_time_sum或者query_count"
      },
      {
        "name": "OrderByType",
        "desc": "排序类型，desc或者asc"
      },
      {
        "name": "Slave",
        "desc": "是否查询从机的慢查询，0-主机; 1-从机"
      }
    ],
    "desc": "本接口(DescribeDBSlowLogs)用于查询慢查询日志列表。"
  },
  "CloseDBExtranetAccess": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待关闭外网访问的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      }
    ],
    "desc": "本接口(CloseDBExtranetAccess)用于关闭云数据库实例的外网访问。关闭外网访问后，外网地址将不可访问，查询实例列表接口将不返回对应实例的外网域名和端口信息。"
  },
  "DescribeAccounts": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      }
    ],
    "desc": "本接口（DescribeAccounts）用于查询指定云数据库实例的账号列表。"
  },
  "CopyAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "SrcUserName",
        "desc": "源用户名"
      },
      {
        "name": "SrcHost",
        "desc": "源用户允许的访问 host"
      },
      {
        "name": "DstUserName",
        "desc": "目的用户名"
      },
      {
        "name": "DstHost",
        "desc": "目的用户允许的访问 host"
      },
      {
        "name": "SrcReadOnly",
        "desc": "源账号的 ReadOnly 属性"
      },
      {
        "name": "DstReadOnly",
        "desc": "目的账号的 ReadOnly 属性"
      }
    ],
    "desc": "本接口（CopyAccountPrivileges）用于复制云数据库账号的权限。\n注意：相同用户名，不同Host是不同的账号，Readonly属性相同的账号之间才能复制权限。"
  },
  "DescribePrice": {
    "params": [
      {
        "name": "Zone",
        "desc": "欲新购实例的可用区ID。"
      },
      {
        "name": "NodeCount",
        "desc": "实例节点个数，可以通过 DescribeDBInstanceSpecs\n 查询实例规格获得。"
      },
      {
        "name": "Memory",
        "desc": "内存大小，单位：GB，可以通过 DescribeDBInstanceSpecs\n 查询实例规格获得。"
      },
      {
        "name": "Storage",
        "desc": "存储空间大小，单位：GB，可以通过 DescribeDBInstanceSpecs\n 查询实例规格获得不同内存大小对应的磁盘规格下限和上限。"
      },
      {
        "name": "Period",
        "desc": "欲购买的时长，单位：月。"
      },
      {
        "name": "Count",
        "desc": "欲购买的数量，默认查询购买1个实例的价格。"
      }
    ],
    "desc": "本接口（DescribePrice）用于在购买实例前，查询实例的价格。"
  },
  "CloneAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "SrcUser",
        "desc": "源用户账户名"
      },
      {
        "name": "SrcHost",
        "desc": "源用户HOST"
      },
      {
        "name": "DstUser",
        "desc": "目的用户账户名"
      },
      {
        "name": "DstHost",
        "desc": "目的用户HOST"
      },
      {
        "name": "DstDesc",
        "desc": "目的用户账户描述"
      }
    ],
    "desc": "本接口（CloneAccount）用于克隆实例账户。"
  },
  "UpgradeDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待升级的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。"
      },
      {
        "name": "Memory",
        "desc": "内存大小，单位：GB，可以通过 DescribeDBInstanceSpecs\n 查询实例规格获得。"
      },
      {
        "name": "Storage",
        "desc": "存储空间大小，单位：GB，可以通过 DescribeDBInstanceSpecs\n 查询实例规格获得不同内存大小对应的磁盘规格下限和上限。"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券进行支付，默认不使用。"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表，目前仅支持指定一张代金券。"
      }
    ],
    "desc": "本接口(UpgradeDBInstance)用于扩容云数据库实例。本接口完成下单和支付两个动作，如果发生支付失败的错误，调用用户账户相关接口中的支付订单接口（PayDeals）重新支付即可。"
  },
  "DescribeDBPerformance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc。"
      },
      {
        "name": "StartTime",
        "desc": "开始日期，格式yyyy-mm-dd"
      },
      {
        "name": "EndTime",
        "desc": "结束日期，格式yyyy-mm-dd"
      },
      {
        "name": "MetricName",
        "desc": "拉取的指标名，支持的值为：long_query,select_total,update_total,insert_total,delete_total,mem_hit_rate,disk_iops,conn_active,is_master_switched,slave_delay"
      }
    ],
    "desc": "本接口(DescribeDBPerformance)用于查看数据库实例当前性能数据。"
  },
  "DescribeLogFileRetentionPeriod": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc。"
      }
    ],
    "desc": "本接口(DescribeLogFileRetentionPeriod)用于查看数据库备份日志的备份天数的设置情况。"
  },
  "DescribeDBResourceUsage": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：tdsql-ow728lmc。"
      },
      {
        "name": "StartTime",
        "desc": "开始日期，格式yyyy-mm-dd"
      },
      {
        "name": "EndTime",
        "desc": "结束日期，格式yyyy-mm-dd"
      },
      {
        "name": "MetricName",
        "desc": "拉取的指标名称，支持的值为：data_disk_available,binlog_disk_available,mem_available,cpu_usage_rate"
      }
    ],
    "desc": "本接口(DescribeDBResourceUsage)用于查看数据库实例资源的使用情况。"
  }
}