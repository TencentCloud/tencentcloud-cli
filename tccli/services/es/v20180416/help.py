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
        "desc": "起始时间, e.g. \"2019-03-07 16:30:39\""
      },
      {
        "name": "EndTime",
        "desc": "结束时间, e.g. \"2019-03-30 20:18:03\""
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
        "desc": "集群实例ID列表"
      },
      {
        "name": "InstanceNames",
        "desc": "集群实例名称列表"
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
        "desc": "排序字段<li>1：实例ID</li><li>2：实例名称</li><li>3：可用区</li><li>4：创建时间</li>若orderKey未传递则按创建时间降序排序"
      },
      {
        "name": "OrderByType",
        "desc": "排序方式<li>0：升序</li><li>1：降序</li>若传递了orderByKey未传递orderByType, 则默认升序"
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
        "desc": "节点数量（2-50个）"
      },
      {
        "name": "EsVersion",
        "desc": "实例版本（支持\"5.6.4\"、\"6.4.3\"）"
      },
      {
        "name": "NodeType",
        "desc": "节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>"
      },
      {
        "name": "DiskSize",
        "desc": "节点磁盘容量（单位GB）"
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
        "desc": "访问密码（密码需8到16位，至少包括两项（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号）"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）"
      },
      {
        "name": "ChargeType",
        "desc": "计费类型<li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li>默认值POSTPAID_BY_HOUR"
      },
      {
        "name": "ChargePeriod",
        "desc": "包年包月购买时长（单位由参数TimeUint决定）"
      },
      {
        "name": "RenewFlag",
        "desc": "自动续费标识<li>RENEW_FLAG_AUTO：自动续费</li><li>RENEW_FLAG_MANUAL：不自动续费，用户手动续费</li>ChargeType为PREPAID时需要设置，如不传递该参数，普通用于默认不自动续费，SVIP用户自动续费"
      },
      {
        "name": "DiskType",
        "desc": "节点磁盘类型<li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高硬能云硬盘</li>默认值CLOUD_SSD"
      },
      {
        "name": "TimeUnit",
        "desc": "计费时长单位（ChargeType为PREPAID时需要设置，默认值为“m”，表示月，当前只支持“m”）"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券<li>0：不自动使用</li><li>1：自动使用</li>默认值0"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表（目前仅支持指定一张代金券）"
      },
      {
        "name": "EnableDedicatedMaster",
        "desc": "是否创建专用主节点<li>true：开启专用主节点</li><li>false：不开启专用主节点</li>默认值false"
      },
      {
        "name": "MasterNodeNum",
        "desc": "专用主节点个数（只支持3个和5个，EnableDedicatedMaster为true时该值必传）"
      },
      {
        "name": "MasterNodeType",
        "desc": "专用主节点类型（EnableDedicatedMaster为true时必传）<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>"
      },
      {
        "name": "MasterNodeDiskSize",
        "desc": "专用主节点磁盘大小（单位GB，非必传，若传递则必须为50，暂不支持自定义）"
      },
      {
        "name": "ClusterNameInConf",
        "desc": "集群配置文件中的ClusterName（系统默认配置为实例ID，暂不支持自定义）"
      },
      {
        "name": "DeployMode",
        "desc": "集群部署方式<li>0：单可用区部署</li><li>1：多可用区部署</li>默认为0"
      },
      {
        "name": "MultiZoneInfo",
        "desc": "多可用区部署时可用区的详细信息(DeployMode为1时必传)"
      },
      {
        "name": "LicenseType",
        "desc": "License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum"
      }
    ],
    "desc": "创建指定规格的ES集群实例"
  },
  "UpdateInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）"
      },
      {
        "name": "NodeNum",
        "desc": "节点个数（2-50个）"
      },
      {
        "name": "EsConfig",
        "desc": "配置项（JSON格式字符串）。当前仅支持以下配置项：<li>action.destructive_requires_name</li><li>indices.fielddata.cache.size</li><li>indices.query.bool.max_clause_count</li>"
      },
      {
        "name": "Password",
        "desc": "默认用户elastic的密码（8到16位，至少包括两项（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号）"
      },
      {
        "name": "EsAcl",
        "desc": "访问控制列表"
      },
      {
        "name": "DiskSize",
        "desc": "磁盘大小（单位GB）"
      },
      {
        "name": "NodeType",
        "desc": "节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>"
      },
      {
        "name": "MasterNodeNum",
        "desc": "专用主节点个数（只支持3个或5个）"
      },
      {
        "name": "MasterNodeType",
        "desc": "专用主节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>"
      },
      {
        "name": "MasterNodeDiskSize",
        "desc": "专用主节点磁盘大小（单位GB系统默认配置为50GB,暂不支持自定义）"
      },
      {
        "name": "ForceRestart",
        "desc": "更新配置时是否强制重启<li>true强制重启</li><li>false不强制重启</li>当前仅更新EsConfig时需要设置，默认值为false"
      },
      {
        "name": "CosBackup",
        "desc": "COS自动备份信息"
      }
    ],
    "desc": "对集群进行扩缩容，修改实例名称，修改配置，重置密码， 添加Kibana黑白名单等操作。参数中InstanceId为必传参数，ForceRestart为选填参数，剩余参数传递组合及含义如下：\n- InstanceName：修改实例名称(仅用于标识实例)\n- NodeNum：集群数据节点横向扩缩容\n- NodeType, DiskSize：集群数据节点纵向扩缩容\n- MasterNodeNum: 集群专用主节点横向扩缩容\n- MasterNodeType, MasterNodeDiskSize: 集群专用主节点纵向扩缩容\n- EsConfig：修改集群配置\n- Password：修改默认用户elastic的密码\n- EsAcl：修改访问控制列表\n- CosBackUp: 设置集群COS自动备份信息\n以上参数组合只能传递一种，多传或少传均会导致请求失败"
  },
  "DeleteInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      }
    ],
    "desc": "销毁集群实例 "
  },
  "RestartInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "ForceRestart",
        "desc": "是否强制重启<li>true：强制重启</li><li>false：不强制重启</li>默认false"
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
        "desc": "日志类型，默认值为1\n<li>1, 主日志</li>\n<li>2, 搜索慢日志</li>\n<li>3, 索引慢日志</li>\n<li>4, GC日志</li>"
      },
      {
        "name": "SearchKey",
        "desc": "搜索词，支持LUCENE语法，如 level:WARN、ip:1.1.1.1、message:test-index等"
      },
      {
        "name": "StartTime",
        "desc": "日志开始时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53"
      },
      {
        "name": "EndTime",
        "desc": "日志结束时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53"
      },
      {
        "name": "Offset",
        "desc": "分页起始值, 默认值为0"
      },
      {
        "name": "Limit",
        "desc": "分页大小，默认值为100，最大值100"
      },
      {
        "name": "OrderByType",
        "desc": "时间排序方式，默认值为0\n<li>0, 降序</li>\n<li>1, 升序</li>"
      }
    ],
    "desc": "查询用户该地域下符合条件的ES集群的日志"
  }
}