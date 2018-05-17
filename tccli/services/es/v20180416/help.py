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
        "name": "InstanceName",
        "desc": "实例名称"
      },
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
        "name": "ChargeType",
        "desc": "计费类型: \n* PREPAID：预付费，即包年包月 \n* POSTPAID_BY_HOUR：按小时后付费，默认值"
      },
      {
        "name": "ChargePeriod",
        "desc": "包年包月购买时长，单位：月"
      },
      {
        "name": "RenewFlag",
        "desc": "自动续费标识，取值范围： \n* NOTIFY_AND_AUTO_RENEW：通知过期且自动续费，默认值 \n* NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费 \n* DISABLE_NOTIFY_AND_MANUAL_RENEW： 不通知过期不自动续费"
      },
      {
        "name": "NodeType",
        "desc": "节点规格 \n* ES.S1.SMALL2: 1核2G\n* ES.S1.MEDIUM4: 2核4G\n* ES.S1.MEDIUM8: 2核8G\n* ES.S1.LARGE16: 4核16G\n* ES.S1.2XLARGE32: 8核32G\n* ES.S1.3XLARGE32: 12核32G\n* ES.S1.6XLARGE32: 24核32G"
      },
      {
        "name": "DiskType",
        "desc": "节点存储类型,取值范围:  \n* LOCAL_BASIC: 本地硬盘  \n* LOCAL_SSD: 本地SSD硬盘，默认值  \n* CLOUD_BASIC: 普通云硬盘  \n* CLOUD_PREMIUM: 高硬能云硬盘  \n* CLOUD_SSD: SSD云硬盘"
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
        "desc": "修改后的实例名称"
      },
      {
        "name": "NodeNum",
        "desc": "横向扩缩容后的节点个数"
      },
      {
        "name": "EsConfig",
        "desc": "修改后的配置项"
      },
      {
        "name": "Password",
        "desc": "重置后的用户密码"
      },
      {
        "name": "EsAcl",
        "desc": "修改后的访问控制列表"
      }
    ],
    "desc": "对已存在的集群进行扩缩容，修改实例名称，修改配置，重置密码， 添加Kibana黑白名单等操作"
  },
  "DeleteInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "要销毁的实例ID"
      }
    ],
    "desc": "销毁集群实例"
  },
  "RestartInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "要重启的实例ID"
      }
    ],
    "desc": "重启ES集群实例(用于系统版本更新等操作)"
  }
}