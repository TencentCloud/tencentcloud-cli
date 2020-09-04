# -*- coding: utf-8 -*-
DESC = "cynosdb-2019-01-07"
INFO = {
  "ModifyBackupConfig": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "BackupTimeBeg",
        "desc": "表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200"
      },
      {
        "name": "BackupTimeEnd",
        "desc": "表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200"
      },
      {
        "name": "ReserveDuration",
        "desc": "表示保留备份时长, 单位秒，超过该时间将被清理, 七天表示为3600*24*7=604800"
      },
      {
        "name": "BackupFreq",
        "desc": "备份频率，长度为7的数组，分别对应周一到周日的备份方式，full-全量备份，increment-增量备份"
      },
      {
        "name": "BackupType",
        "desc": "备份方式，logic-逻辑备份，snapshot-快照备份"
      }
    ],
    "desc": "修改指定集群的备份配置"
  },
  "SetRenewFlag": {
    "params": [
      {
        "name": "ResourceIds",
        "desc": "需操作的实例ID"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "自动续费标志位"
      }
    ],
    "desc": "SetRenewFlag设置实例的自动续费功能"
  },
  "UpgradeInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "Cpu",
        "desc": "数据库CPU"
      },
      {
        "name": "Memory",
        "desc": "数据库内存"
      },
      {
        "name": "UpgradeType",
        "desc": "升级类型：upgradeImmediate，upgradeInMaintain"
      },
      {
        "name": "StorageLimit",
        "desc": "存储上限，为0表示使用标准配置"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动选择代金券 1是 0否 默认为0"
      },
      {
        "name": "DbType",
        "desc": "数据库类型，取值范围: \n<li> MYSQL </li>"
      }
    ],
    "desc": "升级实例"
  },
  "CreateClusters": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区"
      },
      {
        "name": "VpcId",
        "desc": "所属VPC网络ID"
      },
      {
        "name": "SubnetId",
        "desc": "所属子网ID"
      },
      {
        "name": "DbType",
        "desc": "数据库类型，取值范围: \n<li> MYSQL </li>"
      },
      {
        "name": "DbVersion",
        "desc": "数据库版本，取值范围: \n<li> MYSQL可选值：5.7 </li>"
      },
      {
        "name": "Cpu",
        "desc": "Cpu核数"
      },
      {
        "name": "Memory",
        "desc": "内存"
      },
      {
        "name": "StorageLimit",
        "desc": "存储上限，单位GB"
      },
      {
        "name": "ProjectId",
        "desc": "所属项目ID"
      },
      {
        "name": "Storage",
        "desc": "存储"
      },
      {
        "name": "ClusterName",
        "desc": "集群名称"
      },
      {
        "name": "AdminPassword",
        "desc": "账号密码(8-64个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()~）中的两种)"
      },
      {
        "name": "Port",
        "desc": "端口，默认5432"
      },
      {
        "name": "PayMode",
        "desc": "计费模式，按量计费：0，包年包月：1。默认按量计费。"
      },
      {
        "name": "Count",
        "desc": "购买个数，目前只支持传1（不传默认为1）"
      },
      {
        "name": "RollbackStrategy",
        "desc": "回档类型：\nnoneRollback：不回档；\nsnapRollback，快照回档；\ntimeRollback，时间点回档"
      },
      {
        "name": "RollbackId",
        "desc": "快照回档，表示snapshotId；时间点回档，表示queryId，为0，表示需要判断时间点是否有效"
      },
      {
        "name": "OriginalClusterId",
        "desc": "回档时，传入源集群ID，用于查找源poolId"
      },
      {
        "name": "ExpectTime",
        "desc": "时间点回档，指定时间；快照回档，快照时间"
      },
      {
        "name": "ExpectTimeThresh",
        "desc": "时间点回档，指定时间允许范围"
      },
      {
        "name": "InstanceCount",
        "desc": "实例数量"
      },
      {
        "name": "TimeSpan",
        "desc": "包年包月购买时长"
      },
      {
        "name": "TimeUnit",
        "desc": "包年包月购买时长单位"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "包年包月购买是否自动续费"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动选择代金券 1是 0否 默认为0"
      },
      {
        "name": "HaCount",
        "desc": "实例数量（该参数已不再使用，只做存量兼容处理）"
      },
      {
        "name": "OrderSource",
        "desc": "订单来源"
      }
    ],
    "desc": "创建集群"
  },
  "DescribeMaintainPeriod": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      }
    ],
    "desc": "查询实例维护时间窗"
  },
  "DescribeRollbackTimeValidity": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "ExpectTime",
        "desc": "期望回滚的时间点"
      },
      {
        "name": "ExpectTimeThresh",
        "desc": "回滚时间点的允许误差范围"
      }
    ],
    "desc": "指定时间和集群查询是否可回滚"
  },
  "DescribeBackupConfig": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      }
    ],
    "desc": "获取指定集群的备份配置信息，包括全量备份时间段，备份文件保留时间"
  },
  "DescribeClusterDetail": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群Id"
      }
    ],
    "desc": "显示集群详情"
  },
  "ModifyDBInstanceSecurityGroups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例组ID"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "要修改的安全组ID列表，一个或者多个安全组Id组成的数组。"
      },
      {
        "name": "Zone",
        "desc": "可用区"
      }
    ],
    "desc": "本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。"
  },
  "OfflineCluster": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      }
    ],
    "desc": "下线集群"
  },
  "IsolateInstance": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "InstanceIdList",
        "desc": "实例ID数组"
      },
      {
        "name": "DbType",
        "desc": "数据库类型，取值范围: \n<li> MYSQL </li>"
      }
    ],
    "desc": "本接口(IsolateInstance)用于隔离实例访问。"
  },
  "DescribeInstanceSpecs": {
    "params": [
      {
        "name": "DbType",
        "desc": "数据库类型，取值范围: \n<li> MYSQL </li>"
      }
    ],
    "desc": "本接口（DescribeInstanceSpecs）用于查询实例规格"
  },
  "AddInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "Cpu",
        "desc": "Cpu核数"
      },
      {
        "name": "Memory",
        "desc": "内存"
      },
      {
        "name": "ReadOnlyCount",
        "desc": "新增只读实例数"
      },
      {
        "name": "InstanceGrpId",
        "desc": "实例组ID，在已有RO组中新增实例时使用，不传则新增RO组"
      },
      {
        "name": "VpcId",
        "desc": "所属VPC网络ID"
      },
      {
        "name": "SubnetId",
        "desc": "所属子网ID"
      },
      {
        "name": "Port",
        "desc": "新增RO组时使用的Port"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动选择代金券 1是 0否 默认为0"
      },
      {
        "name": "DbType",
        "desc": "数据库类型，取值范围: \n<li> MYSQL </li>"
      },
      {
        "name": "OrderSource",
        "desc": "订单来源"
      }
    ],
    "desc": "本接口（AddInstances）用于集群添加实例"
  },
  "DescribeClusters": {
    "params": [
      {
        "name": "DbType",
        "desc": "引擎类型：目前支持“MYSQL”， “POSTGRESQL”"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100"
      },
      {
        "name": "Offset",
        "desc": "记录偏移量，默认值为0"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段，取值范围：\n<li> CREATETIME：创建时间</li>\n<li> PERIODENDTIME：过期时间</li>"
      },
      {
        "name": "OrderByType",
        "desc": "排序类型，取值范围：\n<li> ASC：升序排序 </li>\n<li> DESC：降序排序 </li>"
      },
      {
        "name": "Filters",
        "desc": "搜索条件，若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。"
      }
    ],
    "desc": "查询集群列表"
  },
  "DescribeAccounts": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "AccountNames",
        "desc": "需要过滤的账户列表"
      },
      {
        "name": "DbType",
        "desc": "数据库类型，取值范围: \n<li> MYSQL </li>"
      }
    ],
    "desc": "本接口(DescribeAccounts)用于查询数据库管理账号。"
  },
  "DescribeBackupList": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "Limit",
        "desc": "备份文件列表偏移"
      },
      {
        "name": "Offset",
        "desc": "备份文件列表起始"
      }
    ],
    "desc": "查询备份文件列表"
  },
  "ModifyMaintainPeriodConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "MaintainStartTime",
        "desc": "维护开始时间，单位为秒，如3:00为10800"
      },
      {
        "name": "MaintainDuration",
        "desc": "维护持续时间，单位为秒，如1小时为3600"
      },
      {
        "name": "MaintainWeekDays",
        "desc": "每周维护日期"
      }
    ],
    "desc": "修改维护时间配置"
  },
  "DescribeRollbackTimeRange": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      }
    ],
    "desc": "查询指定集群有效回滚时间范围"
  },
  "IsolateCluster": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "DbType",
        "desc": "数据库类型，取值范围: \n<li> MYSQL </li>"
      }
    ],
    "desc": "隔离集群"
  }
}