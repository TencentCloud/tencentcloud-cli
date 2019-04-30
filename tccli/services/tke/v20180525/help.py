# -*- coding: utf-8 -*-
DESC = "tke-2018-05-25"
INFO = {
  "AddExistedInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "InstanceIds",
        "desc": "实例列表"
      },
      {
        "name": "InstanceAdvancedSettings",
        "desc": "实例额外需要设置参数信息"
      },
      {
        "name": "EnhancedService",
        "desc": "增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。"
      },
      {
        "name": "LoginSettings",
        "desc": "节点登录信息（目前仅支持使用Password或者单个KeyIds）"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。（目前仅支持设置单个sgId）"
      }
    ],
    "desc": "添加已经存在的实例到集群"
  },
  "DescribeClusters": {
    "params": [
      {
        "name": "ClusterIds",
        "desc": "集群ID列表(为空时，\n表示获取账号下所有集群)"
      },
      {
        "name": "Offset",
        "desc": "偏移量,默认0"
      },
      {
        "name": "Limit",
        "desc": "最大输出条数，默认20"
      },
      {
        "name": "Filters",
        "desc": "过滤条件,当前只支持按照单个条件ClusterName进行过滤"
      }
    ],
    "desc": "查询集群列表"
  },
  "CreateCluster": {
    "params": [
      {
        "name": "ClusterCIDRSettings",
        "desc": "集群容器网络配置信息"
      },
      {
        "name": "ClusterType",
        "desc": "集群类型，托管集群：MANAGED_CLUSTER，独立集群：INDEPENDENT_CLUSTER。"
      },
      {
        "name": "RunInstancesForNode",
        "desc": "CVM创建透传参数，json化字符串格式，详见[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口。"
      },
      {
        "name": "ClusterBasicSettings",
        "desc": "集群的基本配置信息"
      },
      {
        "name": "ClusterAdvancedSettings",
        "desc": "集群高级配置信息"
      },
      {
        "name": "InstanceAdvancedSettings",
        "desc": "节点高级配置信息"
      },
      {
        "name": "ExistedInstancesForNode",
        "desc": "已存在实例的配置信息"
      }
    ],
    "desc": "创建集群"
  },
  "DescribeClusterInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "Offset",
        "desc": "偏移量,默认0"
      },
      {
        "name": "Limit",
        "desc": "最大输出条数，默认20"
      },
      {
        "name": "InstanceIds",
        "desc": "需要获取的节点实例Id列表(默认为空，表示拉取集群下所有节点实例)"
      }
    ],
    "desc": " 查询集群下节点实例信息 "
  },
  "DeleteClusterInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "InstanceIds",
        "desc": "主机InstanceId列表"
      },
      {
        "name": "InstanceDeleteMode",
        "desc": "集群实例删除时的策略：terminate（销毁实例，仅支持按量计费云主机实例） retain （仅移除，保留实例）"
      }
    ],
    "desc": "删除集群中的实例"
  }
}