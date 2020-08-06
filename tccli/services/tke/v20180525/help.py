# -*- coding: utf-8 -*-
DESC = "tke-2018-05-25"
INFO = {
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
        "desc": "CVM创建透传参数，json化字符串格式，详见[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口。总机型(包括地域)数量不超过10个，相同机型(地域)购买多台机器可以通过设置参数中RunInstances中InstanceCount来实现。"
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
        "desc": "已存在实例的配置信息。所有实例必须在同一个VPC中，最大数量不超过100。"
      },
      {
        "name": "InstanceDataDiskMountSettings",
        "desc": "CVM类型和其对应的数据盘挂载配置信息"
      }
    ],
    "desc": "创建集群"
  },
  "DescribeImages": {
    "params": [],
    "desc": "获取镜像信息"
  },
  "ModifyClusterAsGroupAttribute": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "ClusterAsGroupAttribute",
        "desc": "集群关联的伸缩组属性"
      }
    ],
    "desc": "修改集群伸缩组属性"
  },
  "DeleteClusterEndpoint": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "IsExtranet",
        "desc": "是否为外网访问（TRUE 外网访问 FALSE 内网访问，默认值： FALSE）"
      }
    ],
    "desc": "删除集群访问端口(独立集群开启内网/外网访问，托管集群支持开启内网访问)"
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
  "ModifyClusterAttribute": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "ProjectId",
        "desc": "集群所属项目"
      },
      {
        "name": "ClusterName",
        "desc": "集群名称"
      },
      {
        "name": "ClusterDesc",
        "desc": "集群描述"
      }
    ],
    "desc": "修改集群属性"
  },
  "DeleteClusterAsGroups": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID，通过[DescribeClusters](https://cloud.tencent.com/document/api/457/31862)接口获取。"
      },
      {
        "name": "AutoScalingGroupIds",
        "desc": "集群伸缩组ID的列表"
      },
      {
        "name": "KeepInstance",
        "desc": "是否保留伸缩组中的节点(默认值： false(不保留))"
      }
    ],
    "desc": "删除集群伸缩组"
  },
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
  "DescribeClusterEndpointVipStatus": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      }
    ],
    "desc": "查询集群开启端口流程状态(仅支持托管集群外网端口)"
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
      },
      {
        "name": "ResourceDeleteOptions",
        "desc": "集群删除时资源的删除策略，目前支持CBS（默认保留CBS）"
      }
    ],
    "desc": "删除集群(YUNAPI V3版本)"
  },
  "CreateClusterAsGroup": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "AutoScalingGroupPara",
        "desc": "伸缩组创建透传参数，json化字符串格式，详见[伸缩组创建实例](https://cloud.tencent.com/document/api/377/20440)接口。LaunchConfigurationId由LaunchConfigurePara参数创建，不支持填写"
      },
      {
        "name": "LaunchConfigurePara",
        "desc": "启动配置创建透传参数，json化字符串格式，详见[创建启动配置](https://cloud.tencent.com/document/api/377/20447)接口。另外ImageId参数由于集群维度已经有的ImageId信息，这个字段不需要填写。UserData字段设置通过UserScript设置，这个字段不需要填写。"
      },
      {
        "name": "InstanceAdvancedSettings",
        "desc": "节点高级配置信息"
      },
      {
        "name": "Labels",
        "desc": "节点Label数组"
      }
    ],
    "desc": "为已经存在的集群创建伸缩组"
  },
  "DescribeExistedInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群 ID，请填写查询集群列表 接口中返回的 ClusterId 字段（仅通过ClusterId获取需要过滤条件中的VPCID。节点状态比较时会使用该地域下所有集群中的节点进行比较。参数不支持同时指定InstanceIds和ClusterId。"
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
  "DescribeClusterAsGroupOption": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      }
    ],
    "desc": "集群弹性伸缩配置"
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
        "desc": "最大输出条数，默认20，最大为100"
      },
      {
        "name": "Filters",
        "desc": "过滤条件,当前只支持按照单个条件ClusterName进行过滤"
      }
    ],
    "desc": "查询集群列表"
  },
  "DescribeClusterEndpointStatus": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "IsExtranet",
        "desc": "是否为外网访问（TRUE 外网访问 FALSE 内网访问，默认值： FALSE）"
      }
    ],
    "desc": "查询集群访问端口状态(独立集群开启内网/外网访问，托管集群支持开启内网访问)"
  },
  "DescribeClusterAsGroups": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "AutoScalingGroupIds",
        "desc": "伸缩组ID列表，如果为空，表示拉取集群关联的所有伸缩组。"
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
    "desc": "集群关联的伸缩组列表"
  },
  "CreateClusterEndpoint": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "SubnetId",
        "desc": "集群端口所在的子网ID  (仅在开启非外网访问时需要填，必须为集群所在VPC内的子网)"
      },
      {
        "name": "IsExtranet",
        "desc": "是否为外网访问（TRUE 外网访问 FALSE 内网访问，默认值： FALSE）"
      }
    ],
    "desc": "创建集群访问端口(独立集群开启内网/外网访问，托管集群支持开启内网访问)"
  },
  "DescribeClusterRouteTables": {
    "params": [],
    "desc": "查询集群路由表"
  },
  "DescribeRegions": {
    "params": [],
    "desc": "获取容器服务支持的所有地域"
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
      },
      {
        "name": "HostName",
        "desc": "重装系统时，可以指定修改实例的HostName(集群为HostName模式时，此参数必传，规则名称除不支持大写字符外与[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口HostName一致)"
      }
    ],
    "desc": "添加已经存在的实例到集群"
  },
  "DescribeClusterSecurity": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群 ID，请填写 查询集群列表 接口中返回的 clusterId 字段"
      }
    ],
    "desc": "集群的密钥信息"
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
  "DescribeClusterInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "InstanceIds",
        "desc": "需要获取的节点实例Id列表。如果为空，表示拉取集群下所有节点实例。"
      },
      {
        "name": "InstanceRole",
        "desc": "节点角色, MASTER, WORKER, ETCD, MASTER_ETCD,ALL, 默认为WORKER。默认为WORKER类型。"
      }
    ],
    "desc": " 查询集群下节点实例信息 "
  },
  "DeleteClusterEndpointVip": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      }
    ],
    "desc": "删除托管集群外网访问端口（老的方式，仅支持托管集群外网端口）"
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
      },
      {
        "name": "ForceDelete",
        "desc": "是否强制删除(当节点在初始化时，可以指定参数为TRUE)"
      }
    ],
    "desc": "删除集群中的实例"
  },
  "ModifyClusterEndpointSP": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "SecurityPolicies",
        "desc": "安全策略放通单个IP或CIDR(例如: \"192.168.1.0/24\",默认为拒绝所有)"
      }
    ],
    "desc": "修改托管集群外网端口的安全策略（老的方式，仅支持托管集群外网端口）"
  },
  "CreateClusterEndpointVip": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "SecurityPolicies",
        "desc": "安全策略放通单个IP或CIDR(例如: \"192.168.1.0/24\",默认为拒绝所有)"
      }
    ],
    "desc": "创建托管集群外网访问端口（老的方式，仅支持托管集群外网端口）"
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
  "DescribeClusterRoutes": {
    "params": [
      {
        "name": "RouteTableName",
        "desc": "路由表名称。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件,当前只支持按照单个条件GatewayIP进行过滤（可选）"
      }
    ],
    "desc": "查询集群路由"
  }
}