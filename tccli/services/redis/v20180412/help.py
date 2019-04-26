# -*- coding: utf-8 -*-
DESC = "redis-2018-04-12"
INFO = {
  "CleanUpInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      }
    ],
    "desc": "回收站实例立即下线"
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
        "name": "Password",
        "desc": "重置的密码"
      },
      {
        "name": "InstanceId",
        "desc": "Redis实例ID"
      }
    ],
    "desc": "重置密码"
  },
  "DestroyPrepaidInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
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
        "desc": "实例类型：1-Redis老集群版；2-Redis 2.8主从版；3-CKV主从版；4-CKV集群版；5-Redis 2.8单机版；7-Redis 4.0集群版"
      },
      {
        "name": "SearchKeys",
        "desc": "搜索关键词：支持实例Id、实例名称、完整IP"
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
  "ClearInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "Password",
        "desc": "redis的实例密码"
      }
    ],
    "desc": "清空Redis实例的实例数据。"
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
      }
    ],
    "desc": "启用读写分离"
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
  "DescribeInstanceSecurityGroup": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例列表"
      }
    ],
    "desc": "查询实例安全组信息"
  },
  "DescribeProductInfo": {
    "params": [],
    "desc": "本接口查询指定可用区和实例类型下 Redis 的售卖规格， 如果用户不在购买白名单中，将不能查询该可用区或该类型的售卖规格详情。申请购买某地域白名单可以提交工单"
  },
  "UpgradeInstance": {
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
    "desc": "升级实例"
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
  "DescribeTaskInfo": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID"
      }
    ],
    "desc": "用于查询任务结果"
  },
  "RestoreInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待操作的实例ID，可通过 DescribeRedis 接口返回值中的 redisId 获取。"
      },
      {
        "name": "Password",
        "desc": "实例密码，恢复实例时，需要校验实例密码"
      },
      {
        "name": "BackupId",
        "desc": "备份ID，可通过 GetRedisBackupList 接口返回值中的 backupId 获取"
      }
    ],
    "desc": "恢复 CRS 实例"
  },
  "ModifyInstanceParams": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
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
        "desc": "实例所属的可用区id"
      },
      {
        "name": "TypeId",
        "desc": "实例类型：2 – Redis2.8主从版，3 – Redis3.2主从版(CKV主从版)，4 – Redis3.2集群版(CKV集群版)，5-Redis2.8单机版，7 – Redis4.0集群版，"
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
        "name": "Password",
        "desc": "实例密码，密码规则：1.长度为8-16个字符；2:至少包含字母、数字和字符!@^*()中的两种"
      },
      {
        "name": "BillingMode",
        "desc": "付费方式:0-按量计费，1-包年包月。"
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
        "desc": "用户自定义的端口 不填则默认为6379"
      },
      {
        "name": "RedisShardNum",
        "desc": "实例分片数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写"
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
      }
    ],
    "desc": "创建redis实例"
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
  "DescribeBackupUrl": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "BackupId",
        "desc": "备份Id，通过DescribeInstanceBackups接口可查"
      }
    ],
    "desc": "查询备份Rdb下载地址"
  },
  "DestroyPostpaidInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      }
    ],
    "desc": "按量计费实例销毁"
  },
  "ModifyInstance": {
    "params": [
      {
        "name": "Operation",
        "desc": "修改实例操作，如填写：rename-表示实例重命名；modifyProject-修改实例所属项目；modifyAutoRenew-修改实例续费标记"
      },
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "InstanceName",
        "desc": "实例的新名称"
      },
      {
        "name": "ProjectId",
        "desc": "项目Id"
      },
      {
        "name": "AutoRenew",
        "desc": "自动续费标识。0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费"
      }
    ],
    "desc": "修改实例相关信息（目前支持：实例重命名）"
  }
}