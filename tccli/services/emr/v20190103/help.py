# -*- coding: utf-8 -*-
DESC = "emr-2019-01-03"
INFO = {
  "ScaleOutInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "时间单位"
      },
      {
        "name": "TimeSpan",
        "desc": "时间长度"
      },
      {
        "name": "InstanceId",
        "desc": "扩容实例ID"
      },
      {
        "name": "PayMode",
        "desc": "付费类型"
      },
      {
        "name": "ClientToken",
        "desc": "Token"
      },
      {
        "name": "PreExecutedFileSettings",
        "desc": "预执行脚本设置"
      },
      {
        "name": "TaskCount",
        "desc": "扩容Task节点数量"
      },
      {
        "name": "CoreCount",
        "desc": "扩容Core节点数量"
      },
      {
        "name": "UnNecessaryNodeList",
        "desc": "扩容时不需要安装的进程"
      }
    ],
    "desc": "实例扩容"
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "DisplayStrategy",
        "desc": "集群展示策略，该字段取值根据所选页面不同输入不同，集群列表页：clusterList，集群监控：monitorManage，云硬件管理：cloudHardwareManage，组件管理页：componentManage"
      },
      {
        "name": "InstanceIds",
        "desc": "查询列表,  如果不填写，返回该AppId下所有实例列表"
      },
      {
        "name": "Offset",
        "desc": "查询偏移量，默认0"
      },
      {
        "name": "Limit",
        "desc": "查询结果限制，默认值10"
      },
      {
        "name": "ProjectId",
        "desc": "项目列表，默认值-1"
      },
      {
        "name": "OrderField",
        "desc": "排序字段，当前支持以下排序字段：clusterId、addTime、status"
      },
      {
        "name": "Asc",
        "desc": "排序方法，0降序，1升序"
      }
    ],
    "desc": "查询EMR实例"
  },
  "TerminateInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "被销毁的实例ID"
      },
      {
        "name": "ResourceIds",
        "desc": "销毁节点ID"
      }
    ],
    "desc": "销毁EMR实例"
  },
  "InquiryPriceUpdateInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "时间单位。s:按量用例单位。m:包年包月用例单位"
      },
      {
        "name": "TimeSpan",
        "desc": "时间长度。按量用例长度为3600。"
      },
      {
        "name": "UpdateSpec",
        "desc": "变配参数"
      },
      {
        "name": "PayMode",
        "desc": "计费类型"
      },
      {
        "name": "Placement",
        "desc": "位置信息"
      },
      {
        "name": "Currency",
        "desc": "货币种类"
      }
    ],
    "desc": "变配询价"
  },
  "InquiryPriceRenewInstance": {
    "params": [
      {
        "name": "TimeSpan",
        "desc": "时间长度"
      },
      {
        "name": "ResourceIds",
        "desc": "资源ID列表"
      },
      {
        "name": "Placement",
        "desc": "位置信息"
      },
      {
        "name": "PayMode",
        "desc": "计费模式，0表示按量，1表示包年报月，此处只能为包年包月"
      },
      {
        "name": "TimeUnit",
        "desc": "时间单位，默认为m"
      },
      {
        "name": "Currency",
        "desc": "货币种类"
      }
    ],
    "desc": "续费询价。"
  },
  "CreateInstance": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "VPCSettings",
        "desc": "VPC设置参数"
      },
      {
        "name": "Software",
        "desc": "软件列表"
      },
      {
        "name": "ResourceSpec",
        "desc": "资源描述"
      },
      {
        "name": "SupportHA",
        "desc": "支持HA"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称"
      },
      {
        "name": "PayMode",
        "desc": "计费类型"
      },
      {
        "name": "Placement",
        "desc": "集群位置信息"
      },
      {
        "name": "TimeSpan",
        "desc": "时间长度"
      },
      {
        "name": "TimeUnit",
        "desc": "时间单位"
      },
      {
        "name": "LoginSettings",
        "desc": "登录配置"
      },
      {
        "name": "COSSettings",
        "desc": "COS设置参数"
      },
      {
        "name": "SgId",
        "desc": "安全组ID"
      },
      {
        "name": "PreExecutedFileSettings",
        "desc": "预执行脚本设置"
      },
      {
        "name": "AutoRenew",
        "desc": "自动续费"
      },
      {
        "name": "ClientToken",
        "desc": "客户端Token"
      },
      {
        "name": "NeedMasterWan",
        "desc": "是否需要外网Ip。支持填NEED_MASTER_WAN，不支持使用NOT_NEED_MASTER_WAN，默认使用NEED_MASTER_WAN"
      },
      {
        "name": "RemoteLoginAtCreate",
        "desc": "是否需要开启外网远程登录，即22号端口，在SgId不为空时，该选项无效"
      },
      {
        "name": "CheckSecurity",
        "desc": "是否开启安全集群，0表示不开启，非0表示开启"
      },
      {
        "name": "ExtendFsField",
        "desc": "访问外部文件系统"
      }
    ],
    "desc": "创建EMR实例"
  },
  "InquiryPriceCreateInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "时间单位"
      },
      {
        "name": "TimeSpan",
        "desc": "时间长度"
      },
      {
        "name": "ResourceSpec",
        "desc": "询价资源描述"
      },
      {
        "name": "Currency",
        "desc": "货币种类"
      },
      {
        "name": "PayMode",
        "desc": "计费类型"
      },
      {
        "name": "SupportHA",
        "desc": "是否支持HA， 1 支持，0 不支持"
      },
      {
        "name": "Software",
        "desc": "软件列表"
      },
      {
        "name": "Placement",
        "desc": "位置信息"
      },
      {
        "name": "VPCSettings",
        "desc": "VPC信息"
      }
    ],
    "desc": "创建实例询价"
  },
  "InquiryPriceScaleOutInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "时间单位。s:按量用例单位。m:包年包月用例单位"
      },
      {
        "name": "TimeSpan",
        "desc": "时间长度。按量用例长度为3600。"
      },
      {
        "name": "ZoneId",
        "desc": "Zone ID"
      },
      {
        "name": "PayMode",
        "desc": "计费类型"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "CoreCount",
        "desc": "扩容Core节点个数"
      },
      {
        "name": "TaskCount",
        "desc": "扩容Task节点个数"
      },
      {
        "name": "Currency",
        "desc": "货币种类"
      }
    ],
    "desc": "扩容询价. 当扩容时候，请通过该接口查询价格。"
  },
  "TerminateTasks": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "销毁节点所属实例ID"
      },
      {
        "name": "ResourceIds",
        "desc": "销毁节点ID"
      }
    ],
    "desc": "缩容Task节点"
  }
}