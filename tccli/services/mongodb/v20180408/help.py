# -*- coding: utf-8 -*-
DESC = "mongodb-2018-04-08"
INFO = {
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
        "desc": "版本号，当前仅支持 MONGO_3_WT"
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
        "desc": "MongoDB引擎版本，值包括：MONGO_2、MONGO_3_MMAP、MONGO_3_WT 、MONGO_3_ROCKS和MONGO_36_WT"
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
  }
}