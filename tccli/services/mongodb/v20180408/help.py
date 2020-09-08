# -*- coding: utf-8 -*-
DESC = "mongodb-2018-04-08"
INFO = {
  "AssignProject": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID"
      }
    ],
    "desc": "本接口(AssignProject)用于指定云数据库实例的所属项目。\n\n"
  },
  "RenameInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      },
      {
        "name": "NewName",
        "desc": "实例名称"
      }
    ],
    "desc": "本接口(RenameInstance)用于修改云数据库实例的名称。"
  },
  "CreateDBInstance": {
    "params": [
      {
        "name": "SecondaryNum",
        "desc": "每个副本集内从节点个数"
      },
      {
        "name": "Memory",
        "desc": "实例内存大小，单位：GB"
      },
      {
        "name": "Volume",
        "desc": "实例硬盘大小，单位：GB"
      },
      {
        "name": "MongoVersion",
        "desc": "版本号，当前支持 MONGO_3_WT、MONGO_3_ROCKS、MONGO_36_WT"
      },
      {
        "name": "MachineCode",
        "desc": "机器类型，GIO：高IO版；TGIO：高IO万兆"
      },
      {
        "name": "GoodsNum",
        "desc": "实例数量，默认值为1, 最小值1，最大值为10"
      },
      {
        "name": "Zone",
        "desc": "实例所属区域名称，格式如：ap-guangzhou-2"
      },
      {
        "name": "TimeSpan",
        "desc": "时长，购买月数"
      },
      {
        "name": "Password",
        "desc": "实例密码"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，不填为默认项目"
      },
      {
        "name": "SecurityGroup",
        "desc": "安全组参数"
      },
      {
        "name": "UniqVpcId",
        "desc": "私有网络ID，如果不传则默认选择基础网络"
      },
      {
        "name": "UniqSubnetId",
        "desc": "私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填"
      }
    ],
    "desc": "本接口(CreateDBInstance)用于创建包年包月的MongoDB云数据库实例。"
  },
  "DescribeClientConnections": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      }
    ],
    "desc": "本接口(DescribeClientConnections)用于查询实例客户端连接信息，包括连接IP和连接数量。目前只支持3.2版本的MongoDB实例。"
  },
  "CreateDBInstanceHour": {
    "params": [
      {
        "name": "Memory",
        "desc": "实例内存大小，单位：GB"
      },
      {
        "name": "Volume",
        "desc": "实例硬盘大小，单位：GB"
      },
      {
        "name": "ReplicateSetNum",
        "desc": "副本集个数，1为单副本集实例，大于1为分片集群实例，最大不超过10"
      },
      {
        "name": "SecondaryNum",
        "desc": "每个副本集内从节点个数，目前只支持从节点数为2"
      },
      {
        "name": "EngineVersion",
        "desc": "MongoDB引擎版本，值包括MONGO_3_WT 、MONGO_3_ROCKS和MONGO_36_WT"
      },
      {
        "name": "Machine",
        "desc": "实例类型，GIO：高IO版；TGIO：高IO万兆"
      },
      {
        "name": "GoodsNum",
        "desc": "实例数量，默认值为1, 最小值1，最大值为10"
      },
      {
        "name": "Zone",
        "desc": "可用区信息，格式如：ap-guangzhou-2"
      },
      {
        "name": "InstanceRole",
        "desc": "实例角色，支持值包括：MASTER-表示主实例，DR-表示灾备实例，RO-表示只读实例"
      },
      {
        "name": "InstanceType",
        "desc": "实例类型，REPLSET-副本集，SHARD-分片集群"
      },
      {
        "name": "Encrypt",
        "desc": "数据是否加密，当且仅当引擎版本为MONGO_3_ROCKS，可以选择加密"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，如果不传则默认选择基础网络"
      },
      {
        "name": "SubnetId",
        "desc": "私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，不填为默认项目"
      },
      {
        "name": "SecurityGroup",
        "desc": "安全组参数"
      }
    ],
    "desc": "本接口(CreateDBInstanceHour)用于创建按量计费的MongoDB云数据库实例（包括主实例、灾备实例和只读实例），可通过传入实例规格、实例类型、MongoDB版本、购买时长和数量等信息创建云数据库实例。"
  },
  "DescribeSlowLog": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      },
      {
        "name": "StartTime",
        "desc": "慢日志起始时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-01 10:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。"
      },
      {
        "name": "EndTime",
        "desc": "慢日志终止时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-02 12:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。"
      },
      {
        "name": "SlowMS",
        "desc": "慢日志执行时间阈值，返回执行时间超过该阈值的慢日志，单位为毫秒(ms)，最小为100毫秒。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，最小值为0，最大值为10000，默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "分页大小，最小值为1，最大值为100，默认值为20。"
      }
    ],
    "desc": "本接口(DescribeSlowLogs)用于获取云数据库实例的慢查询日志。"
  },
  "TerminateDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。"
      }
    ],
    "desc": "本接口(TerminateDBInstance)用于销毁按量计费的MongoDB云数据库实例"
  },
  "UpgradeDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      },
      {
        "name": "Memory",
        "desc": "升级后的内存大小，单位：GB"
      },
      {
        "name": "Volume",
        "desc": "升级后的硬盘大小，单位：GB"
      },
      {
        "name": "OplogSize",
        "desc": "升级后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%"
      }
    ],
    "desc": "本接口(UpgradeDBInstance)用于升级包年包月的MongoDB云数据库实例，可以扩容内存、存储以及Oplog"
  },
  "SetAutoRenew": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "续费选项，取值范围：0-手动续费，1-自动续费，2-确认不续费"
      }
    ],
    "desc": "本接口(SetAutoRenew)用于设置包年包月云数据库实例的续费选项。"
  },
  "DescribeSpecInfo": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区"
      }
    ],
    "desc": "本接口(DescribeSpecInfo)用于查询实例的售卖规格。"
  },
  "SetPassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      },
      {
        "name": "UserName",
        "desc": "实例账户名称"
      },
      {
        "name": "Password",
        "desc": "实例新密码，至少包含字母、数字和字符（!@#%^*()）中的两种，长度为8-16个字符"
      }
    ],
    "desc": "本接口(SetPassword)用于设置云数据库账户的密码。\n\n"
  },
  "UpgradeDBInstanceHour": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5"
      },
      {
        "name": "Memory",
        "desc": "升级后的内存大小，单位：GB"
      },
      {
        "name": "Volume",
        "desc": "升级后的硬盘大小，单位：GB"
      },
      {
        "name": "OplogSize",
        "desc": "升级后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%"
      }
    ],
    "desc": "本接口(UpgradeDBInstanceHour)用于升级按量计费的MongoDB云数据库实例，可以扩容内存、存储以及oplog"
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      },
      {
        "name": "InstanceType",
        "desc": "实例类型，取值范围：0-所有实例,1-正式实例，2-临时实例, 3-只读实例，-1-正式实例+只读+灾备实例"
      },
      {
        "name": "ClusterType",
        "desc": "集群类型，取值范围：0-副本集实例，1-分片实例，-1-所有实例"
      },
      {
        "name": "Status",
        "desc": "实例状态，取值范围：0-待初始化，1-流程执行中，2-实例有效，-2-实例已过期"
      },
      {
        "name": "VpcId",
        "desc": "私有网络的ID，基础网络则不传该参数"
      },
      {
        "name": "SubnetId",
        "desc": "私有网络的子网ID，基础网络则不传该参数。入参设置该参数的同时，必须设置相应的VpcId"
      },
      {
        "name": "PayMode",
        "desc": "付费类型，取值范围：0-按量计费，1-包年包月，-1-按量计费+包年包月"
      },
      {
        "name": "Limit",
        "desc": "单次请求返回的数量，最小值为1，最大值为100，默认值为20"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认值为0"
      },
      {
        "name": "OrderBy",
        "desc": "返回结果集排序的字段，目前支持：\"ProjectId\", \"InstanceName\", \"CreateTime\"，默认为升序排序"
      },
      {
        "name": "OrderByType",
        "desc": "返回结果集排序方式，目前支持：\"ASC\"或者\"DESC\""
      }
    ],
    "desc": "本接口(DescribeDBInstances)用于查询云数据库实例列表，支持通过项目ID、实例ID、实例状态等过滤条件来筛选实例。支持查询主实例、灾备实例和只读实例信息列表。"
  }
}