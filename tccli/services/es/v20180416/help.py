# -*- coding: utf-8 -*-
DESC = "es-2018-04-16"
INFO = {
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
        "desc": "实例版本,当前只支持5.6.4"
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
        "desc": "节点存储类型,取值范围:  \nLOCAL_BASIC: 本地硬盘  \nLOCAL_SSD: 本地SSD硬盘，默认值  \nCLOUD_BASIC: 普通云硬盘  \nCLOUD_PREMIUM: 高硬能云硬盘  \nCLOUD_SSD: SSD云硬盘"
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
        "desc": "修改后的配置项, JSON格式字符串"
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
      }
    ],
    "desc": "对已存在的集群进行扩缩容，修改实例名称，修改配置，重置密码， 添加Kibana黑白名单等操作 "
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
      }
    ],
    "desc": "重启ES集群实例(用于系统版本更新等操作) "
  }
}