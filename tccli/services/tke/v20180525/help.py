# -*- coding: utf-8 -*-
DESC = "tke-2018-05-25"
INFO = {
  "DeleteClusterRoute": {
    "params": [
      {
        "name": "RouteTableName",
        "desc": "路由表名称。"
      },
      {
        "name": "GatewayIp",
        "desc": "下一跳地址。"
      },
      {
        "name": "DestinationCidrBlock",
        "desc": "目的端CIDR。"
      }
    ],
    "desc": "删除集群路由"
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
  "DescribeRouteTableConflicts": {
    "params": [
      {
        "name": "RouteTableCidrBlock",
        "desc": "路由表CIDR"
      },
      {
        "name": "VpcId",
        "desc": "路由表绑定的VPC"
      }
    ],
    "desc": "查询路由表冲突列表"
  },
  "CreateClusterInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群 ID，请填写 查询集群列表 接口中返回的 clusterId 字段"
      },
      {
        "name": "RunInstancePara",
        "desc": "CVM创建透传参数，json化字符串格式，详见[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口。"
      },
      {
        "name": "InstanceAdvancedSettings",
        "desc": "实例额外需要设置参数信息"
      }
    ],
    "desc": "扩展(新建)集群节点"
  },
  "DescribeExistedInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群 ID，请填写查询集群列表 接口中返回的 ClusterId 字段（仅通过ClusterId获取需要过滤条件中的VPCID，比较状态时会使用该地域下所有集群中的节点进行比较。参数不支持同时指定InstanceIds和ClusterId。"
      },
      {
        "name": "InstanceIds",
        "desc": "按照一个或者多个实例ID查询。实例ID形如：ins-xxxxxxxx。（此参数的具体格式可参考API简介的id.N一节）。每次请求的实例的上限为100。参数不支持同时指定InstanceIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件,字段和详见[CVM查询实例](https://cloud.tencent.com/document/api/213/15728)如果设置了ClusterId，会附加集群的VPCID作为查询字段，在此情况下如果在Filter中指定了\"vpc-id\"作为过滤字段，指定的VPCID必须与集群的VPCID相同。"
      },
      {
        "name": "VagueIpAddress",
        "desc": "实例IP进行过滤(同时支持内网IP和外网IP)"
      },
      {
        "name": "VagueInstanceName",
        "desc": "实例名称进行过滤"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      }
    ],
    "desc": "查询已经存在的节点，判断是否可以加入集群"
  },
  "CreateClusterRoute": {
    "params": [
      {
        "name": "RouteTableName",
        "desc": "路由表名称。"
      },
      {
        "name": "DestinationCidrBlock",
        "desc": "目的端CIDR。"
      },
      {
        "name": "GatewayIp",
        "desc": "下一跳地址。"
      }
    ],
    "desc": "创建集群路由"
  },
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
  "CreateClusterRouteTable": {
    "params": [
      {
        "name": "RouteTableName",
        "desc": "路由表名称"
      },
      {
        "name": "RouteTableCidrBlock",
        "desc": "路由表CIDR"
      },
      {
        "name": "VpcId",
        "desc": "路由表绑定的VPC"
      },
      {
        "name": "IgnoreClusterCidrConflict",
        "desc": "是否忽略CIDR冲突"
      }
    ],
    "desc": "创建集群路由表"
  },
  "DescribeClusterRouteTables": {
    "params": [],
    "desc": "查询集群路由表"
  },
  "DescribeClusterRoutes": {
    "params": [
      {
        "name": "RouteTableName",
        "desc": "路由表名称。"
      }
    ],
    "desc": "查询集群路由"
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
  "DeleteClusterRouteTable": {
    "params": [
      {
        "name": "RouteTableName",
        "desc": "路由表名称"
      }
    ],
    "desc": "删除集群路由表"
  },
  "DeleteCluster": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "InstanceDeleteMode",
        "desc": "集群实例删除时的策略：terminate（销毁实例，仅支持按量计费云主机实例） retain （仅移除，保留实例）"
      }
    ],
    "desc": "删除集群(YUNAPI V3版本)"
  },
  "DescribeClusterSecurity": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群 ID，请填写 查询集群列表 接口中返回的 clusterId 字段"
      }
    ],
    "desc": "集群的密钥信息"
  }
}