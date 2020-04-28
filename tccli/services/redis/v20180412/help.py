# -*- coding: utf-8 -*-
DESC = "redis-2018-04-12"
INFO = {
  "ClearInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "Password",
        "desc": "redis的实例密码（免密实例不需要传密码，非免密实例必传）"
      }
    ],
    "desc": "清空Redis实例的实例数据。"
  },
  "InquiryPriceRenewInstance": {
    "params": [
      {
        "name": "Period",
        "desc": "购买时长，单位：月"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID"
      }
    ],
    "desc": "查询实例续费价格（包年包月）"
  },
  "CreateInstanceAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "AccountName",
        "desc": "子账号名称"
      },
      {
        "name": "AccountPassword",
        "desc": "子账号密码"
      },
      {
        "name": "ReadonlyPolicy",
        "desc": "路由策略：填写master或者replication，表示主节点或者从节点"
      },
      {
        "name": "Privilege",
        "desc": "读写策略：填写r、w、rw，表示只读、只写、读写"
      },
      {
        "name": "Remark",
        "desc": "子账号描述信息"
      }
    ],
    "desc": "创建实例子账号"
  },
  "ModifyInstanceAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "AccountName",
        "desc": "子账号名称，如果要修改主账号，填root"
      },
      {
        "name": "AccountPassword",
        "desc": "子账号密码"
      },
      {
        "name": "Remark",
        "desc": "子账号描述信息"
      },
      {
        "name": "ReadonlyPolicy",
        "desc": "子账号路由策略：填写master或者slave，表示路由主节点，从节点"
      },
      {
        "name": "Privilege",
        "desc": "子账号读写策略：填写r、w、rw，表示只读，只写，读写策略"
      },
      {
        "name": "NoAuth",
        "desc": "true表示将主账号切换为免密账号，这里只适用于主账号，子账号不可免密"
      }
    ],
    "desc": "修改实例子账号"
  },
  "DescribeTaskList": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称"
      },
      {
        "name": "Limit",
        "desc": "分页大小"
      },
      {
        "name": "Offset",
        "desc": "偏移量，取Limit整数倍（自动向下取整）"
      },
      {
        "name": "ProjectIds",
        "desc": "项目Id"
      },
      {
        "name": "TaskTypes",
        "desc": "任务类型"
      },
      {
        "name": "BeginTime",
        "desc": "起始时间"
      },
      {
        "name": "EndTime",
        "desc": "终止时间"
      },
      {
        "name": "TaskStatus",
        "desc": "任务状态"
      }
    ],
    "desc": "查询任务列表信息"
  },
  "CleanUpInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      }
    ],
    "desc": "回收站实例立即下线"
  },
  "StartupInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例id"
      }
    ],
    "desc": "实例解隔离"
  },
  "DescribeInstanceAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "Limit",
        "desc": "分页大小"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量"
      }
    ],
    "desc": "查看实例子账号信息"
  },
  "DescribeInstanceDTSInfo": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      }
    ],
    "desc": "查询实例DTS信息"
  },
  "DescribeInstanceMonitorTopNCmdTook": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "SpanType",
        "desc": "时间范围：1——实时，2——近30分钟，3——近6小时，4——近24小时"
      }
    ],
    "desc": "查询实例CPU耗时"
  },
  "ModifyNetworkConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "Operation",
        "desc": "操作类型：changeVip——修改实例VIP；changeVpc——修改实例子网；changeBaseToVpc——基础网络转VPC网络"
      },
      {
        "name": "Vip",
        "desc": "VIP地址，changeVip的时候填写，不填则默认分配"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，changeVpc、changeBaseToVpc的时候需要提供"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID，changeVpc、changeBaseToVpc的时候需要提供"
      }
    ],
    "desc": "修改实例网络配置"
  },
  "ResetPassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "Redis实例ID"
      },
      {
        "name": "Password",
        "desc": "重置的密码（切换为免密实例时，可不传；其他情况必传）"
      },
      {
        "name": "NoAuth",
        "desc": "是否切换免密实例，false-切换为非免密码实例，true-切换为免密码实例；默认false"
      }
    ],
    "desc": "重置密码"
  },
  "DestroyPrepaidInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      }
    ],
    "desc": "包年包月实例退还"
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "Limit",
        "desc": "实例列表的大小，参数默认值20"
      },
      {
        "name": "Offset",
        "desc": "偏移量，取Limit整数倍"
      },
      {
        "name": "InstanceId",
        "desc": "实例Id，如：crs-6ubhgouj"
      },
      {
        "name": "OrderBy",
        "desc": "枚举范围： projectId,createtime,instancename,type,curDeadline"
      },
      {
        "name": "OrderType",
        "desc": "1倒序，0顺序，默认倒序"
      },
      {
        "name": "VpcIds",
        "desc": "私有网络ID数组，数组下标从0开始，如果不传则默认选择基础网络，如：47525"
      },
      {
        "name": "SubnetIds",
        "desc": "子网ID数组，数组下标从0开始，如：56854"
      },
      {
        "name": "ProjectIds",
        "desc": "项目ID 组成的数组，数组下标从0开始"
      },
      {
        "name": "SearchKey",
        "desc": "查找实例的ID。"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称"
      },
      {
        "name": "UniqVpcIds",
        "desc": "私有网络ID数组，数组下标从0开始，如果不传则默认选择基础网络，如：vpc-sad23jfdfk"
      },
      {
        "name": "UniqSubnetIds",
        "desc": "子网ID数组，数组下标从0开始，如：subnet-fdj24n34j2"
      },
      {
        "name": "RegionIds",
        "desc": "地域ID，已经弃用，可通过公共参数Region查询对应地域"
      },
      {
        "name": "Status",
        "desc": "实例状态：0-待初始化，1-流程中，2-运行中，-2-已隔离，-3-待删除"
      },
      {
        "name": "TypeVersion",
        "desc": "类型版本：1-单机版,2-主从版,3-集群版"
      },
      {
        "name": "EngineName",
        "desc": "引擎信息：Redis-2.8，Redis-4.0，CKV"
      },
      {
        "name": "AutoRenew",
        "desc": "续费模式：0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费"
      },
      {
        "name": "BillingMode",
        "desc": "计费模式：postpaid-按量计费；prepaid-包年包月"
      },
      {
        "name": "Type",
        "desc": "实例类型：1-Redis老集群版；2-Redis 2.8主从版；3-CKV主从版；4-CKV集群版；5-Redis 2.8单机版；6-Redis 4.0主从版；7-Redis 4.0集群版；8 – Redis5.0主从版，9 – Redis5.0集群版，"
      },
      {
        "name": "SearchKeys",
        "desc": "搜索关键词：支持实例Id、实例名称、完整IP"
      },
      {
        "name": "TypeList",
        "desc": "内部参数，用户可忽略"
      }
    ],
    "desc": "查询Redis实例列表"
  },
  "DescribeInstanceParamRecords": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "Limit",
        "desc": "分页大小"
      },
      {
        "name": "Offset",
        "desc": "偏移量，取Limit整数倍"
      }
    ],
    "desc": "查询参数修改历史列表"
  },
  "DescribeInstanceMonitorTopNCmd": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "SpanType",
        "desc": "时间范围：1——实时，2——近30分钟，3——近6小时，4——近24小时"
      }
    ],
    "desc": "查询实例访问命令"
  },
  "DisableReplicaReadonly": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例序号ID"
      }
    ],
    "desc": "禁用读写分离"
  },
  "DescribeAutoBackupConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      }
    ],
    "desc": "获取备份配置"
  },
  "ModifyAutoBackupConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "WeekDays",
        "desc": "日期 Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday"
      },
      {
        "name": "TimePeriod",
        "desc": "时间段 00:00-01:00, 01:00-02:00...... 23:00-00:00"
      },
      {
        "name": "AutoBackupType",
        "desc": "自动备份类型： 1 “定时回档”"
      }
    ],
    "desc": "设置自动备份时间"
  },
  "DescribeInstanceMonitorSIP": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      }
    ],
    "desc": "查询实例访问来源信息"
  },
  "DescribeInstanceParams": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      }
    ],
    "desc": "查询实例参数列表"
  },
  "DescribeInstanceMonitorBigKeySizeDist": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "Date",
        "desc": "时间；例如：\"20190219\""
      }
    ],
    "desc": "查询实例大Key大小分布"
  },
  "InquiryPriceUpgradeInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "MemSize",
        "desc": "分片大小 单位 MB"
      },
      {
        "name": "RedisShardNum",
        "desc": "分片数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写"
      },
      {
        "name": "RedisReplicasNum",
        "desc": "副本数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写"
      }
    ],
    "desc": "查询实例扩容价格"
  },
  "DescribeProjectSecurityGroup": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "0:默认项目；-1 所有项目; >0: 特定项目"
      },
      {
        "name": "SecurityGroupId",
        "desc": "安全组Id"
      }
    ],
    "desc": "查询项目安全组信息"
  },
  "DescribeInstanceShards": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例id"
      },
      {
        "name": "FilterSlave",
        "desc": "是否过滤掉从节信息"
      }
    ],
    "desc": "获取集群版实例分片信息"
  },
  "DescribeTaskInfo": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID"
      }
    ],
    "desc": "用于查询任务结果"
  },
  "DescribeInstanceDealDetail": {
    "params": [
      {
        "name": "DealIds",
        "desc": "订单ID数组"
      }
    ],
    "desc": "查询订单信息"
  },
  "EnableReplicaReadonly": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例序号ID"
      },
      {
        "name": "ReadonlyPolicy",
        "desc": "账号路由策略：填写master或者replication，表示路由主节点，从节点；不填路由策略默认为写主节点，读从节点"
      }
    ],
    "desc": "启用读写分离"
  },
  "DescribeProjectSecurityGroups": {
    "params": [
      {
        "name": "Product",
        "desc": "数据库引擎名称：mariadb,cdb,cynosdb,dcdb,redis,mongodb"
      },
      {
        "name": "ProjectId",
        "desc": "项目Id。"
      },
      {
        "name": "Offset",
        "desc": "偏移量。"
      },
      {
        "name": "Limit",
        "desc": "拉取数量限制。"
      },
      {
        "name": "SearchKey",
        "desc": "搜索条件，支持安全组id或者安全组名称。"
      }
    ],
    "desc": "本接口(DescribeProjectSecurityGroups)用于查询项目的安全组详情。"
  },
  "AssociateSecurityGroups": {
    "params": [
      {
        "name": "Product",
        "desc": "数据库引擎名称：mariadb,cdb,cynosdb,dcdb,redis,mongodb 等。"
      },
      {
        "name": "SecurityGroupId",
        "desc": "要绑定的安全组ID，类似sg-efil73jd。"
      },
      {
        "name": "InstanceIds",
        "desc": "被绑定的实例ID，类似ins-lesecurk，支持指定多个实例。"
      }
    ],
    "desc": "本接口 (AssociateSecurityGroups) 用于绑定安全组到指定实例。"
  },
  "InquiryPriceCreateInstance": {
    "params": [
      {
        "name": "ZoneId",
        "desc": "实例所属的可用区id"
      },
      {
        "name": "TypeId",
        "desc": "实例类型：2 – Redis2.8主从版，3 – Redis3.2主从版(CKV主从版)，4 – Redis3.2集群版(CKV集群版)，5-Redis2.8单机版，6 – Redis4.0主从版，7 – Redis4.0集群版，"
      },
      {
        "name": "MemSize",
        "desc": "实例容量，单位MB， 取值大小以 查询售卖规格接口返回的规格为准"
      },
      {
        "name": "GoodsNum",
        "desc": "实例数量，单次购买实例数量以 查询售卖规格接口返回的规格为准"
      },
      {
        "name": "Period",
        "desc": "购买时长，在创建包年包月实例的时候需要填写，按量计费实例填1即可，单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]"
      },
      {
        "name": "BillingMode",
        "desc": "付费方式:0-按量计费，1-包年包月。"
      },
      {
        "name": "RedisShardNum",
        "desc": "实例分片数量，Redis2.8主从版、CKV主从版和Redis2.8单机版、Redis4.0主从版不需要填写"
      },
      {
        "name": "RedisReplicasNum",
        "desc": "实例副本数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写"
      },
      {
        "name": "ReplicasReadonly",
        "desc": "是否支持副本只读，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写"
      }
    ],
    "desc": "查询新购实例价格"
  },
  "ModifyDBInstanceSecurityGroups": {
    "params": [
      {
        "name": "Product",
        "desc": "数据库引擎名称：mariadb,cdb,cynosdb,dcdb,redis,mongodb 等。"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "要修改的安全组ID列表，一个或者多个安全组Id组成的数组。"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同"
      }
    ],
    "desc": "本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组"
  },
  "DeleteInstanceAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "AccountName",
        "desc": "子账号名称"
      }
    ],
    "desc": "删除实例子账号"
  },
  "DescribeInstanceMonitorBigKey": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "ReqType",
        "desc": "请求类型：1——string类型，2——所有类型"
      },
      {
        "name": "Date",
        "desc": "时间；例如：\"20190219\""
      }
    ],
    "desc": "查询实例大Key"
  },
  "DescribeInstanceSecurityGroup": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例列表"
      }
    ],
    "desc": "查询实例安全组信息"
  },
  "DescribeInstanceMonitorBigKeyTypeDist": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "Date",
        "desc": "时间；例如：\"20190219\""
      }
    ],
    "desc": "查询实例大Key类型分布"
  },
  "DescribeProductInfo": {
    "params": [],
    "desc": "本接口查询指定可用区和实例类型下 Redis 的售卖规格， 如果用户不在购买白名单中，将不能查询该可用区或该类型的售卖规格详情。申请购买某地域白名单可以提交工单"
  },
  "UpgradeInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "MemSize",
        "desc": "分片大小 单位 MB"
      },
      {
        "name": "RedisShardNum",
        "desc": "分片数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写"
      },
      {
        "name": "RedisReplicasNum",
        "desc": "副本数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写"
      }
    ],
    "desc": "升级实例"
  },
  "DescribeInstanceMonitorHotKey": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "SpanType",
        "desc": "时间范围：1——实时，2——近30分钟，3——近6小时，4——近24小时"
      }
    ],
    "desc": "查询实例热Key"
  },
  "ManualBackupInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待操作的实例ID，可通过 DescribeInstance接口返回值中的 InstanceId 获取。"
      },
      {
        "name": "Remark",
        "desc": "备份的备注信息"
      }
    ],
    "desc": "手动备份Redis实例"
  },
  "ModfiyInstancePassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "OldPassword",
        "desc": "实例旧密码"
      },
      {
        "name": "Password",
        "desc": "实例新密码"
      }
    ],
    "desc": "修改redis密码"
  },
  "DescribeDBSecurityGroups": {
    "params": [
      {
        "name": "Product",
        "desc": "数据库引擎名称：mariadb,cdb,cynosdb,dcdb,redis,mongodb 等。"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。"
      }
    ],
    "desc": "本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。"
  },
  "DescribeSlowLog": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "BeginTime",
        "desc": "开始时间"
      },
      {
        "name": "EndTime",
        "desc": "结束时间"
      },
      {
        "name": "MinQueryTime",
        "desc": "慢查询阈值（单位：微秒）"
      },
      {
        "name": "Limit",
        "desc": "页面大小"
      },
      {
        "name": "Offset",
        "desc": "偏移量，取Limit整数倍"
      }
    ],
    "desc": "查询实例慢查询记录"
  },
  "RestoreInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待操作的实例ID，可通过 DescribeRedis 接口返回值中的 redisId 获取。"
      },
      {
        "name": "BackupId",
        "desc": "备份ID，可通过 GetRedisBackupList 接口返回值中的 backupId 获取"
      },
      {
        "name": "Password",
        "desc": "实例密码，恢复实例时，需要校验实例密码（免密实例不需要传密码）"
      }
    ],
    "desc": "恢复 CRS 实例"
  },
  "ModifyInstanceParams": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "InstanceParams",
        "desc": "实例修改的参数列表"
      }
    ],
    "desc": "修改实例参数"
  },
  "CreateInstances": {
    "params": [
      {
        "name": "ZoneId",
        "desc": "实例所属的可用区ID"
      },
      {
        "name": "TypeId",
        "desc": "实例类型：2 – Redis2.8主从版，3 – Redis3.2主从版(CKV主从版)，4 – Redis3.2集群版(CKV集群版)，5-Redis2.8单机版，6 – Redis4.0主从版，7 – Redis4.0集群版，8 – Redis5.0主从版，9 – Redis5.0集群版，"
      },
      {
        "name": "MemSize",
        "desc": "实例容量，单位MB， 取值大小以 查询售卖规格接口返回的规格为准"
      },
      {
        "name": "GoodsNum",
        "desc": "实例数量，单次购买实例数量以 查询售卖规格接口返回的规格为准"
      },
      {
        "name": "Period",
        "desc": "购买时长，在创建包年包月实例的时候需要填写，按量计费实例填1即可，单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]"
      },
      {
        "name": "BillingMode",
        "desc": "付费方式:0-按量计费，1-包年包月。"
      },
      {
        "name": "Password",
        "desc": "实例密码，密码规则：1.长度为8-16个字符；2:至少包含字母、数字和字符!@^*()中的两种（创建免密实例时，可不传入该字段，该字段内容会忽略）"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，如果不传则默认选择基础网络，请使用私有网络列表查询，如：vpc-sad23jfdfk"
      },
      {
        "name": "SubnetId",
        "desc": "基础网络下， subnetId无效； vpc子网下，取值以查询子网列表，如：subnet-fdj24n34j2"
      },
      {
        "name": "ProjectId",
        "desc": "项目id，取值以用户账户>用户账户相关接口查询>项目列表返回的projectId为准"
      },
      {
        "name": "AutoRenew",
        "desc": "自动续费标识。0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费"
      },
      {
        "name": "SecurityGroupIdList",
        "desc": "安全组id数组"
      },
      {
        "name": "VPort",
        "desc": "用户自定义的端口 不填则默认为6379，范围[1024,65535]"
      },
      {
        "name": "RedisShardNum",
        "desc": "实例分片数量，Redis2.8主从版、CKV主从版和Redis2.8单机版、Redis4.0主从版不需要填写"
      },
      {
        "name": "RedisReplicasNum",
        "desc": "实例副本数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写"
      },
      {
        "name": "ReplicasReadonly",
        "desc": "是否支持副本只读，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称"
      },
      {
        "name": "NoAuth",
        "desc": "是否支持免密，true-免密实例，false-非免密实例，默认为非免密实例"
      }
    ],
    "desc": "创建redis实例"
  },
  "DescribeBackupUrl": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "BackupId",
        "desc": "备份ID，通过DescribeInstanceBackups接口可查"
      }
    ],
    "desc": "查询备份Rdb下载地址(接口灰度中，需要加白名单使用)"
  },
  "DestroyPostpaidInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      }
    ],
    "desc": "按量计费实例销毁"
  },
  "DescribeInstanceBackups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待操作的实例ID，可通过 DescribeInstance 接口返回值中的 InstanceId 获取。"
      },
      {
        "name": "Limit",
        "desc": "实例列表大小，默认大小20"
      },
      {
        "name": "Offset",
        "desc": "偏移量，取Limit整数倍"
      },
      {
        "name": "BeginTime",
        "desc": "开始时间，格式如：2017-02-08 16:46:34。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，格式如：2017-02-08 19:09:26。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。"
      },
      {
        "name": "Status",
        "desc": "1：备份在流程中，2：备份正常，3：备份转RDB文件处理中，4：已完成RDB转换，-1：备份已过期，-2：备份已删除。"
      }
    ],
    "desc": "查询 CRS 实例备份列表"
  },
  "DisassociateSecurityGroups": {
    "params": [
      {
        "name": "Product",
        "desc": "数据库引擎名称：mariadb,cdb,cynosdb,dcdb,redis,mongodb 等。"
      },
      {
        "name": "SecurityGroupId",
        "desc": "安全组Id。"
      },
      {
        "name": "InstanceIds",
        "desc": "实例ID列表，一个或者多个实例Id组成的数组。"
      }
    ],
    "desc": "本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。"
  },
  "RenewInstance": {
    "params": [
      {
        "name": "Period",
        "desc": "购买时长，单位：月"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID"
      }
    ],
    "desc": "续费实例"
  },
  "ModifyInstance": {
    "params": [
      {
        "name": "Operation",
        "desc": "修改实例操作，如填写：rename-表示实例重命名；modifyProject-修改实例所属项目；modifyAutoRenew-修改实例续费标记"
      },
      {
        "name": "InstanceIds",
        "desc": "实例Id"
      },
      {
        "name": "InstanceNames",
        "desc": "实例的新名称"
      },
      {
        "name": "ProjectId",
        "desc": "项目Id"
      },
      {
        "name": "AutoRenews",
        "desc": "自动续费标识。0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费"
      },
      {
        "name": "InstanceId",
        "desc": "已经废弃"
      },
      {
        "name": "InstanceName",
        "desc": "已经废弃"
      },
      {
        "name": "AutoRenew",
        "desc": "已经废弃"
      }
    ],
    "desc": "修改实例相关信息"
  },
  "DescribeInstanceMonitorTookDist": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "Date",
        "desc": "时间；例如：\"20190219\""
      },
      {
        "name": "SpanType",
        "desc": "时间范围：1——实时，2——近30分钟，3——近6小时，4——近24小时"
      }
    ],
    "desc": "查询实例访问的耗时分布"
  },
  "SwitchInstanceVip": {
    "params": [
      {
        "name": "SrcInstanceId",
        "desc": "源实例ID"
      },
      {
        "name": "DstInstanceId",
        "desc": "目标实例ID"
      },
      {
        "name": "TimeDelay",
        "desc": "单位为秒。源实例与目标实例间DTS已断开时间，如果DTS断开时间大于TimeDelay，则不切换VIP，建议尽量根据业务设置一个可接受的值。"
      },
      {
        "name": "ForceSwitch",
        "desc": "在DTS断开的情况下是否强制切换。1：强制切换，0：不强制切换"
      },
      {
        "name": "SwitchTime",
        "desc": "now: 立即切换，syncComplete：等待同步完成后切换"
      }
    ],
    "desc": "在通过DTS支持跨可用区灾备的场景中，通过该接口交换实例VIP完成实例灾备切换。交换VIP后目标实例可写，源和目标实例VIP互换，同时源与目标实例间DTS同步任务断开"
  }
}