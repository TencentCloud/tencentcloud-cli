# -*- coding: utf-8 -*-
DESC = "es-2018-04-16"
INFO = {
  "DescribeInstanceOperations": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "集群实例ID"
      },
      {
        "name": "StartTime",
        "desc": "起始时间"
      },
      {
        "name": "EndTime",
        "desc": "结束时间"
      },
      {
        "name": "Offset",
        "desc": "分页起始值"
      },
      {
        "name": "Limit",
        "desc": "分页大小"
      }
    ],
    "desc": "查询实例指定条件下的操作记录"
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "Zone",
        "desc": "集群实例所属可用区，不传则默认所有可用区"
      },
      {
        "name": "InstanceIds",
        "desc": "一个或多个集群实例ID"
      },
      {
        "name": "InstanceNames",
        "desc": "一个或多个集群实例名称"
      },
      {
        "name": "Offset",
        "desc": "分页起始值, 默认值0"
      },
      {
        "name": "Limit",
        "desc": "分页大小，默认值20"
      },
      {
        "name": "OrderByKey",
        "desc": "排序字段：1，实例ID；2，实例名称；3，可用区；4，创建时间，若orderKey未传递则按创建时间降序排序"
      },
      {
        "name": "OrderByType",
        "desc": "排序方式：0，升序；1，降序；若传递了orderByKey未传递orderByType, 则默认升序"
      }
    ],
    "desc": "查询用户该地域下符合条件的所有实例"
  },
  "CreateInstance": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区"
      },
      {
        "name": "NodeNum",
        "desc": "节点数量"
      },
      {
        "name": "EsVersion",
        "desc": "实例版本,支持\"5.6.4\"、\"6.4.3\""
      },
      {
        "name": "NodeType",
        "desc": "节点规格： \nES.S1.SMALL2: 1核2G\nES.S1.MEDIUM4: 2核4G\nES.S1.MEDIUM8: 2核8G\nES.S1.LARGE16: 4核16G\nES.S1.2XLARGE32: 8核32G\nES.S1.4XLARGE64: 16核64G"
      },
      {
        "name": "DiskSize",
        "desc": "节点存储容量，单位GB"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID"
      },
      {
        "name": "Password",
        "desc": "访问密码，密码需8到16位，至少包括两项（[a-z,A-Z],[0-9]和[()`~!@#$%^&*-+=_|{}:;' <>,.?/]的特殊符号"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称，1-50 个英文、汉字、数字、连接线-或下划线_"
      },
      {
        "name": "ChargeType",
        "desc": "计费类型: \nPREPAID：预付费，即包年包月 \nPOSTPAID_BY_HOUR：按小时后付费，默认值"
      },
      {
        "name": "ChargePeriod",
        "desc": "包年包月购买时长，单位由TimeUint决定，默认为月"
      },
      {
        "name": "RenewFlag",
        "desc": "自动续费标识，取值范围： \nRENEW_FLAG_AUTO：自动续费\nRENEW_FLAG_MANUAL：不自动续费，用户手动续费\n如不传递该参数，普通用于默认不自动续费，SVIP用户自动续费"
      },
      {
        "name": "DiskType",
        "desc": "节点存储类型,取值范围:    \nCLOUD_PREMIUM: 高硬能云硬盘  \nCLOUD_SSD: SSD云硬盘"
      },
      {
        "name": "TimeUnit",
        "desc": "计费时长单位，当前只支持“m”，表示月"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券，1是，0否，默认不使用"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表，目前仅支持指定一张代金券"
      },
      {
        "name": "EnableDedicatedMaster",
        "desc": "是否创建专用主节点"
      },
      {
        "name": "MasterNodeNum",
        "desc": "专用主节点个数"
      },
      {
        "name": "MasterNodeType",
        "desc": "专用主节点类型，与NodeType支持的规格相同"
      },
      {
        "name": "MasterNodeDiskSize",
        "desc": "专用主节点磁盘大小，单位GB（系统默认配置50GB，暂不支持自定义）"
      },
      {
        "name": "ClusterNameInConf",
        "desc": "配置文件中的ClusterName（系统默认配置为实例ID，暂不支持自定义）"
      }
    ],
    "desc": "创建指定规格的ES集群实例"
  },
  "UpdateInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "要操作的实例ID"
      },
      {
        "name": "InstanceName",
        "desc": "修改后的实例名称, 1-50 个英文、汉字、数字、连接线-或下划线_"
      },
      {
        "name": "NodeNum",
        "desc": "横向扩缩容后的节点个数"
      },
      {
        "name": "EsConfig",
        "desc": "修改后的配置项, JSON格式字符串。当前仅支持以下配置项：\naction.destructive_requires_name\nindices.fielddata.cache.size\nindices.query.bool.max_clause_count"
      },
      {
        "name": "Password",
        "desc": "重置后的Kibana密码, 8到16位，至少包括两项（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号"
      },
      {
        "name": "EsAcl",
        "desc": "修改后的访问控制列表"
      },
      {
        "name": "DiskSize",
        "desc": "磁盘大小,单位GB"
      },
      {
        "name": "NodeType",
        "desc": "节点规格: \nES.S1.SMALL2: 1 核 2G\nES.S1.MEDIUM4: 2 核 4G \nES.S1.MEDIUM8: 2 核 8G \nES.S1.LARGE16: 4 核 16G \nES.S1.2XLARGE32: 8 核 32G \nES.S1.4XLARGE64: 16 核 64G"
      },
      {
        "name": "MasterNodeNum",
        "desc": "专用主节点个数"
      },
      {
        "name": "MasterNodeType",
        "desc": "专用主节点规格，与NodeType支持的规格相同"
      },
      {
        "name": "MasterNodeDiskSize",
        "desc": "专用主节点磁盘大小， 单位GB（系统默认配置为50GB,暂不支持自定义）"
      },
      {
        "name": "ForceRestart",
        "desc": "更新配置时是否强制重启"
      },
      {
        "name": "CosBackup",
        "desc": "COS自动备份信息"
      }
    ],
    "desc": "对集群进行扩缩容，修改实例名称，修改配置，重置密码， 添加Kibana黑白名单等操作。参数中InstanceId为必传参数，ForceRestart为选填参数，剩余参数传递组合及含义如下：<br>\n  InstanceName：修改实例名称(仅用于标识实例)<br>\n  NodeNum：集群数据节点横向扩缩容<br>\n  NodeType, DiskSize：集群数据节点纵向扩缩容<br>\n  MasterNodeNum: 集群专用主节点横向扩缩容<br>\n  MasterNodeType, MasterNodeDiskSize: 集群专用主节点纵向扩缩容<br>\n  EsConfig：修改集群配置<br>\n  Password：修改集群密码<br>\n  EsAcl：修改Kibana密码<br>\n  CosBackUp: 设置集群COS自动备份信息<br>\n以上参数组合只能传递一种，多传或少传均会导致请求失败<br>"
  },
  "DeleteInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "要销毁的实例ID"
      }
    ],
    "desc": "销毁集群实例 "
  },
  "RestartInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "要重启的实例ID"
      },
      {
        "name": "ForceRestart",
        "desc": "是否强制重启"
      }
    ],
    "desc": "重启ES集群实例(用于系统版本更新等操作) "
  },
  "DescribeInstanceLogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "集群实例ID"
      },
      {
        "name": "LogType",
        "desc": "日志类型"
      },
      {
        "name": "SearchKey",
        "desc": "搜索词"
      },
      {
        "name": "StartTime",
        "desc": "日志开始时间"
      },
      {
        "name": "EndTime",
        "desc": "日志结束时间"
      },
      {
        "name": "Offset",
        "desc": "分页起始值"
      },
      {
        "name": "Limit",
        "desc": "分页大小"
      },
      {
        "name": "OrderByType",
        "desc": "时间排序方式"
      }
    ],
    "desc": "查询用户该地域下符合条件的ES集群的日志"
  }
}