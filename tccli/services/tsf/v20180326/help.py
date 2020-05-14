# -*- coding: utf-8 -*-
DESC = "tsf-2018-03-26"
INFO = {
  "DeletePublicConfig": {
    "params": [
      {
        "name": "ConfigId",
        "desc": "配置项ID"
      }
    ],
    "desc": "删除公共配置项"
  },
  "DescribeSimpleGroups": {
    "params": [
      {
        "name": "GroupIdList",
        "desc": "部署组ID列表，不填写时查询全量"
      },
      {
        "name": "ApplicationId",
        "desc": "应用ID，不填写时查询全量"
      },
      {
        "name": "ClusterId",
        "desc": "集群ID，不填写时查询全量"
      },
      {
        "name": "NamespaceId",
        "desc": "命名空间ID，不填写时查询全量"
      },
      {
        "name": "Limit",
        "desc": "每页条数"
      },
      {
        "name": "Offset",
        "desc": "起始偏移量"
      },
      {
        "name": "GroupId",
        "desc": "部署组ID，不填写时查询全量"
      },
      {
        "name": "SearchWord",
        "desc": "模糊查询，部署组名称，不填写时查询全量"
      },
      {
        "name": "AppMicroServiceType",
        "desc": "部署组类型，精确过滤字段，M：service mesh, P：原生应用， M：网关应用"
      }
    ],
    "desc": "查询简单部署组列表"
  },
  "CreateNamespace": {
    "params": [
      {
        "name": "NamespaceName",
        "desc": "命名空间名称"
      },
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "NamespaceDesc",
        "desc": "命名空间描述"
      },
      {
        "name": "NamespaceResourceType",
        "desc": "命名空间资源类型(默认值为DEF)"
      },
      {
        "name": "NamespaceType",
        "desc": "是否是全局命名空间(默认是DEF，表示普通命名空间；GLOBAL表示全局命名空间)"
      },
      {
        "name": "NamespaceId",
        "desc": "命名空间ID"
      }
    ],
    "desc": "创建命名空间"
  },
  "DescribeLaneRules": {
    "params": [
      {
        "name": "Limit",
        "desc": "每页展示的条数"
      },
      {
        "name": "Offset",
        "desc": "翻页偏移量"
      },
      {
        "name": "SearchWord",
        "desc": "搜索关键词"
      },
      {
        "name": "RuleId",
        "desc": "泳道规则ID（用于精确搜索）"
      }
    ],
    "desc": "查询泳道规则列表"
  },
  "CreateCluster": {
    "params": [
      {
        "name": "ClusterName",
        "desc": "集群名称"
      },
      {
        "name": "ClusterType",
        "desc": "集群类型"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID"
      },
      {
        "name": "ClusterCIDR",
        "desc": "分配给集群容器和服务IP的CIDR"
      },
      {
        "name": "ClusterDesc",
        "desc": "集群备注"
      },
      {
        "name": "TsfRegionId",
        "desc": "集群所属TSF地域"
      },
      {
        "name": "TsfZoneId",
        "desc": "集群所属TSF可用区"
      },
      {
        "name": "SubnetId",
        "desc": "私有网络子网ID"
      }
    ],
    "desc": "创建集群"
  },
  "DescribePkgs": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "应用ID（只传入应用ID，返回该应用下所有软件包信息）"
      },
      {
        "name": "SearchWord",
        "desc": "查询关键字（支持根据包ID，包名，包版本号搜索）"
      },
      {
        "name": "OrderBy",
        "desc": "排序关键字（默认为\"UploadTime\"：上传时间）"
      },
      {
        "name": "OrderType",
        "desc": "升序：0/降序：1（默认降序）"
      },
      {
        "name": "Offset",
        "desc": "查询起始偏移"
      },
      {
        "name": "Limit",
        "desc": "返回数量限制"
      }
    ],
    "desc": "无"
  },
  "ModifyContainerReplicas": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID，部署组唯一标识"
      },
      {
        "name": "InstanceNum",
        "desc": "实例数量"
      }
    ],
    "desc": "修改容器部署组实例数"
  },
  "DescribeConfigSummary": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "应用ID，不传入时查询全量"
      },
      {
        "name": "SearchWord",
        "desc": "查询关键字，模糊查询：应用名称，配置项名称，不传入时查询全量"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "每页条数，默认为20"
      }
    ],
    "desc": "查询配置汇总列表"
  },
  "DeployContainerGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID，分组唯一标识"
      },
      {
        "name": "Server",
        "desc": "镜像server"
      },
      {
        "name": "TagName",
        "desc": "镜像版本名称,如v1"
      },
      {
        "name": "InstanceNum",
        "desc": "实例数量"
      },
      {
        "name": "Reponame",
        "desc": "旧版镜像名，如/tsf/nginx"
      },
      {
        "name": "CpuLimit",
        "desc": "业务容器最大的 CPU 核数，对应 K8S 的 limit；不填时默认为 request 的 2 倍"
      },
      {
        "name": "MemLimit",
        "desc": "业务容器最大的内存 MiB 数，对应 K8S 的 limit；不填时默认为 request 的 2 倍"
      },
      {
        "name": "JvmOpts",
        "desc": "jvm参数"
      },
      {
        "name": "CpuRequest",
        "desc": "业务容器分配的 CPU 核数，对应 K8S 的 request"
      },
      {
        "name": "MemRequest",
        "desc": "业务容器分配的内存 MiB 数，对应 K8S 的 request"
      },
      {
        "name": "DoNotStart",
        "desc": "是否不立即启动"
      },
      {
        "name": "RepoName",
        "desc": "（优先使用）新版镜像名，如/tsf/nginx"
      },
      {
        "name": "UpdateType",
        "desc": "更新方式：0:快速更新 1:滚动更新"
      },
      {
        "name": "UpdateIvl",
        "desc": "滚动更新必填，更新间隔"
      },
      {
        "name": "AgentCpuRequest",
        "desc": "agent 容器分配的 CPU 核数，对应 K8S 的 request"
      },
      {
        "name": "AgentCpuLimit",
        "desc": "agent 容器最大的 CPU 核数，对应 K8S 的 limit"
      },
      {
        "name": "AgentMemRequest",
        "desc": "agent 容器分配的内存 MiB 数，对应 K8S 的 request"
      },
      {
        "name": "AgentMemLimit",
        "desc": "agent 容器最大的内存 MiB 数，对应 K8S 的 limit"
      },
      {
        "name": "IstioCpuRequest",
        "desc": "istioproxy 容器分配的 CPU 核数，对应 K8S 的 request"
      },
      {
        "name": "IstioCpuLimit",
        "desc": "istioproxy 容器最大的 CPU 核数，对应 K8S 的 limit"
      },
      {
        "name": "IstioMemRequest",
        "desc": "istioproxy 容器分配的内存 MiB 数，对应 K8S 的 request"
      },
      {
        "name": "IstioMemLimit",
        "desc": "istioproxy 容器最大的内存 MiB 数，对应 K8S 的 limit"
      }
    ],
    "desc": "部署容器应用"
  },
  "DescribeConfigReleases": {
    "params": [
      {
        "name": "ConfigName",
        "desc": "配置项名称，不传入时查询全量"
      },
      {
        "name": "GroupId",
        "desc": "部署组ID，不传入时查询全量"
      },
      {
        "name": "NamespaceId",
        "desc": "命名空间ID，不传入时查询全量"
      },
      {
        "name": "ClusterId",
        "desc": "集群ID，不传入时查询全量"
      },
      {
        "name": "Limit",
        "desc": "每页条数"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "ConfigId",
        "desc": "配置ID，不传入时查询全量"
      },
      {
        "name": "ApplicationId",
        "desc": "应用ID，不传入时查询全量"
      }
    ],
    "desc": "查询配置发布信息"
  },
  "AddClusterInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "InstanceIdList",
        "desc": "云主机ID列表"
      },
      {
        "name": "OsName",
        "desc": "操作系统名称"
      },
      {
        "name": "ImageId",
        "desc": "操作系统镜像ID"
      },
      {
        "name": "Password",
        "desc": "重装系统密码设置"
      },
      {
        "name": "KeyId",
        "desc": "重装系统，关联密钥设置"
      },
      {
        "name": "SgId",
        "desc": "安全组设置"
      },
      {
        "name": "InstanceImportMode",
        "desc": "云主机导入方式，虚拟机集群必填，容器集群不填写此字段，R：重装TSF系统镜像，M：手动安装agent"
      }
    ],
    "desc": "添加云主机节点至TSF集群"
  },
  "DescribePodInstances": {
    "params": [
      {
        "name": "GroupId",
        "desc": "实例所属groupId"
      },
      {
        "name": "Offset",
        "desc": "偏移量，取值从0开始"
      },
      {
        "name": "Limit",
        "desc": "分页个数，默认为20， 取值应为1~50"
      }
    ],
    "desc": "获取部署组实例列表"
  },
  "DescribeServerlessGroups": {
    "params": [
      {
        "name": "SearchWord",
        "desc": "搜索字段，模糊搜索groupName字段"
      },
      {
        "name": "ApplicationId",
        "desc": "分组所属应用ID"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段，默认为 createTime字段，支持id， name， createTime"
      },
      {
        "name": "OrderType",
        "desc": "排序方式，默认为1：倒序排序，0：正序，1：倒序"
      },
      {
        "name": "Offset",
        "desc": "偏移量，取值从0开始"
      },
      {
        "name": "Limit",
        "desc": "分页个数，默认为20， 取值应为1~50"
      },
      {
        "name": "NamespaceId",
        "desc": "分组所属名字空间ID"
      },
      {
        "name": "ClusterId",
        "desc": "分组所属集群ID"
      }
    ],
    "desc": "查询Serverless部署组列表"
  },
  "CreateGroup": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "部署组所属的应用ID"
      },
      {
        "name": "NamespaceId",
        "desc": "部署组所属命名空间ID"
      },
      {
        "name": "GroupName",
        "desc": "部署组名称"
      },
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "GroupDesc",
        "desc": "部署组描述"
      },
      {
        "name": "GroupResourceType",
        "desc": "部署组资源类型"
      }
    ],
    "desc": "创建虚拟机部署组"
  },
  "DeleteApplication": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "应用ID"
      }
    ],
    "desc": "删除应用"
  },
  "DeleteMicroservice": {
    "params": [
      {
        "name": "MicroserviceId",
        "desc": "微服务ID"
      }
    ],
    "desc": "删除微服务"
  },
  "StartGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      }
    ],
    "desc": "启动分组"
  },
  "CreateLaneRule": {
    "params": [
      {
        "name": "RuleName",
        "desc": "泳道规则名称"
      },
      {
        "name": "Remark",
        "desc": "泳道规则备注"
      },
      {
        "name": "RuleTagList",
        "desc": "泳道规则标签列表"
      },
      {
        "name": "RuleTagRelationship",
        "desc": "泳道规则标签关系"
      },
      {
        "name": "LaneId",
        "desc": "泳道Id"
      }
    ],
    "desc": "创建泳道规则"
  },
  "DeleteNamespace": {
    "params": [
      {
        "name": "NamespaceId",
        "desc": "命名空间ID"
      },
      {
        "name": "ClusterId",
        "desc": "集群ID"
      }
    ],
    "desc": "删除命名空间"
  },
  "DescribeGroupInstances": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      },
      {
        "name": "SearchWord",
        "desc": "搜索字段"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段"
      },
      {
        "name": "OrderType",
        "desc": "排序类型"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "分页个数"
      }
    ],
    "desc": "查询虚拟机部署组云主机列表"
  },
  "DeleteConfig": {
    "params": [
      {
        "name": "ConfigId",
        "desc": "配置项ID"
      }
    ],
    "desc": "删除配置项"
  },
  "ReleasePublicConfig": {
    "params": [
      {
        "name": "ConfigId",
        "desc": "配置ID"
      },
      {
        "name": "NamespaceId",
        "desc": "命名空间ID"
      },
      {
        "name": "ReleaseDesc",
        "desc": "发布描述"
      }
    ],
    "desc": "发布公共配置"
  },
  "DeletePkgs": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "应用ID"
      },
      {
        "name": "PkgIds",
        "desc": "需要删除的程序包ID列表"
      }
    ],
    "desc": "从软件仓库批量删除程序包。\n一次最多支持删除1000个包，数量超过1000，返回UpperDeleteLimit错误。"
  },
  "RevocationPublicConfig": {
    "params": [
      {
        "name": "ConfigReleaseId",
        "desc": "配置项发布ID"
      }
    ],
    "desc": "撤回已发布的公共配置"
  },
  "DescribePublicConfigs": {
    "params": [
      {
        "name": "ConfigId",
        "desc": "配置项ID，不传入时查询全量，高优先级"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "每页条数，默认为20"
      },
      {
        "name": "ConfigIdList",
        "desc": "配置项ID列表，不传入时查询全量，低优先级"
      },
      {
        "name": "ConfigName",
        "desc": "配置项名称，精确查询，不传入时查询全量"
      },
      {
        "name": "ConfigVersion",
        "desc": "配置项版本，精确查询，不传入时查询全量"
      }
    ],
    "desc": "查询公共配置项列表"
  },
  "DescribeSimpleClusters": {
    "params": [
      {
        "name": "ClusterIdList",
        "desc": "需要查询的集群ID列表，不填或不传入时查询所有内容"
      },
      {
        "name": "ClusterType",
        "desc": "需要查询的集群类型，不填或不传入时查询所有内容"
      },
      {
        "name": "Offset",
        "desc": "查询偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "分页个数，默认为20， 取值应为1~50"
      },
      {
        "name": "SearchWord",
        "desc": "对id和name进行关键词过滤"
      }
    ],
    "desc": "查询简单集群列表"
  },
  "CreateServerlessGroup": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "分组所属应用ID"
      },
      {
        "name": "GroupName",
        "desc": "分组名称字段，长度1~60，字母或下划线开头，可包含字母数字下划线"
      },
      {
        "name": "NamespaceId",
        "desc": "分组所属名字空间ID"
      },
      {
        "name": "ClusterId",
        "desc": "分组所属集群ID"
      }
    ],
    "desc": "创建Serverless部署组"
  },
  "DescribeConfigs": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "应用ID，不传入时查询全量"
      },
      {
        "name": "ConfigId",
        "desc": "配置项ID，不传入时查询全量，高优先级"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "每页条数"
      },
      {
        "name": "ConfigIdList",
        "desc": "配置项ID列表，不传入时查询全量，低优先级"
      },
      {
        "name": "ConfigName",
        "desc": "配置项名称，精确查询，不传入时查询全量"
      },
      {
        "name": "ConfigVersion",
        "desc": "配置项版本，精确查询，不传入时查询全量"
      }
    ],
    "desc": "查询配置项列表"
  },
  "ModifyMicroservice": {
    "params": [
      {
        "name": "MicroserviceId",
        "desc": "微服务 ID"
      },
      {
        "name": "MicroserviceDesc",
        "desc": "微服务备注信息"
      }
    ],
    "desc": "修改微服务详情"
  },
  "DescribeConfig": {
    "params": [
      {
        "name": "ConfigId",
        "desc": "配置项ID"
      }
    ],
    "desc": "查询配置"
  },
  "DescribeMicroservices": {
    "params": [
      {
        "name": "NamespaceId",
        "desc": "命名空间ID"
      },
      {
        "name": "SearchWord",
        "desc": "搜索字段"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段"
      },
      {
        "name": "OrderType",
        "desc": "排序类型"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "分页个数"
      }
    ],
    "desc": "获取微服务列表"
  },
  "StartContainerGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      }
    ],
    "desc": "启动容器部署组"
  },
  "RemoveInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群 ID"
      },
      {
        "name": "InstanceIdList",
        "desc": "云主机 ID 列表"
      }
    ],
    "desc": "从 TSF 集群中批量移除云主机节点"
  },
  "ModifyLaneRule": {
    "params": [
      {
        "name": "RuleId",
        "desc": "泳道规则ID"
      },
      {
        "name": "RuleName",
        "desc": "泳道规则名称"
      },
      {
        "name": "Remark",
        "desc": "泳道规则备注"
      },
      {
        "name": "RuleTagList",
        "desc": "泳道规则标签列表"
      },
      {
        "name": "RuleTagRelationship",
        "desc": "泳道规则标签关系"
      },
      {
        "name": "LaneId",
        "desc": "泳道ID"
      },
      {
        "name": "Enable",
        "desc": "开启状态"
      }
    ],
    "desc": "更新泳道规则"
  },
  "ExpandGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      },
      {
        "name": "InstanceIdList",
        "desc": "扩容的机器实例ID列表"
      }
    ],
    "desc": "虚拟机部署组添加实例"
  },
  "DeleteGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      }
    ],
    "desc": "删除容器部署组"
  },
  "DescribeContainerGroupDetail": {
    "params": [
      {
        "name": "GroupId",
        "desc": "分组ID"
      }
    ],
    "desc": " 容器部署组详情"
  },
  "DeleteContainerGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID，分组唯一标识"
      }
    ],
    "desc": "删除容器部署组"
  },
  "RollbackConfig": {
    "params": [
      {
        "name": "ConfigReleaseLogId",
        "desc": "配置项发布历史ID"
      },
      {
        "name": "ReleaseDesc",
        "desc": "回滚描述"
      }
    ],
    "desc": "回滚配置"
  },
  "DeleteLane": {
    "params": [
      {
        "name": "LaneId",
        "desc": "泳道Idl"
      }
    ],
    "desc": "删除泳道"
  },
  "CreatePublicConfig": {
    "params": [
      {
        "name": "ConfigName",
        "desc": "配置项名称"
      },
      {
        "name": "ConfigVersion",
        "desc": "配置项版本"
      },
      {
        "name": "ConfigValue",
        "desc": "配置项值，总是接收yaml格式的内容"
      },
      {
        "name": "ConfigVersionDesc",
        "desc": "配置项版本描述"
      },
      {
        "name": "ConfigType",
        "desc": "配置项类型"
      },
      {
        "name": "EncodeWithBase64",
        "desc": "Base64编码的配置项"
      }
    ],
    "desc": "创建公共配置项"
  },
  "DescribeImageTags": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "应用Id"
      },
      {
        "name": "Offset",
        "desc": "偏移量，取值从0开始"
      },
      {
        "name": "Limit",
        "desc": "分页个数，默认为20， 取值应为1~100"
      },
      {
        "name": "QueryImageIdFlag",
        "desc": "不填和0:查询 1:不查询"
      },
      {
        "name": "SearchWord",
        "desc": "可用于搜索的 tag 名字"
      }
    ],
    "desc": "镜像版本列表"
  },
  "DescribeServerlessGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      }
    ],
    "desc": "查询Serverless部署组明细"
  },
  "CreateLane": {
    "params": [
      {
        "name": "LaneName",
        "desc": "泳道名称"
      },
      {
        "name": "Remark",
        "desc": "泳道备注"
      },
      {
        "name": "LaneGroupList",
        "desc": "泳道部署组信息"
      }
    ],
    "desc": "创建泳道"
  },
  "DescribePublicConfigReleaseLogs": {
    "params": [
      {
        "name": "NamespaceId",
        "desc": "命名空间ID，不传入时查询全量"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "每页条数，默认为20"
      }
    ],
    "desc": "查询公共配置发布历史"
  },
  "DescribeApplicationAttribute": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "应用ID"
      }
    ],
    "desc": "获取应用列表其它字段，如实例数量信息等"
  },
  "RevocationConfig": {
    "params": [
      {
        "name": "ConfigReleaseId",
        "desc": "配置项发布ID"
      }
    ],
    "desc": "撤回已发布的配置"
  },
  "DescribePublicConfigSummary": {
    "params": [
      {
        "name": "SearchWord",
        "desc": "查询关键字，模糊查询：配置项名称，不传入时查询全量"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "每页条数，默认为20"
      }
    ],
    "desc": "查询公共配置汇总列表"
  },
  "ReleaseConfig": {
    "params": [
      {
        "name": "ConfigId",
        "desc": "配置ID"
      },
      {
        "name": "GroupId",
        "desc": "部署组ID"
      },
      {
        "name": "ReleaseDesc",
        "desc": "发布描述"
      }
    ],
    "desc": "发布配置"
  },
  "DescribeReleasedConfig": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      }
    ],
    "desc": "查询group发布的配置"
  },
  "CreateContainGroup": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "分组所属应用ID"
      },
      {
        "name": "NamespaceId",
        "desc": "分组所属命名空间ID"
      },
      {
        "name": "GroupName",
        "desc": "分组名称字段，长度1~60，字母或下划线开头，可包含字母数字下划线"
      },
      {
        "name": "InstanceNum",
        "desc": "实例数量"
      },
      {
        "name": "AccessType",
        "desc": "0:公网 1:集群内访问 2：NodePort"
      },
      {
        "name": "ProtocolPorts",
        "desc": "数组对象，见下方定义"
      },
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "CpuLimit",
        "desc": "最大分配 CPU 核数，对应 K8S limit"
      },
      {
        "name": "MemLimit",
        "desc": "最大分配内存 MiB 数，对应 K8S limit"
      },
      {
        "name": "GroupComment",
        "desc": "分组备注字段，长度应不大于200字符"
      },
      {
        "name": "UpdateType",
        "desc": "更新方式：0:快速更新 1:滚动更新"
      },
      {
        "name": "UpdateIvl",
        "desc": "滚动更新必填，更新间隔"
      },
      {
        "name": "CpuRequest",
        "desc": "初始分配的 CPU 核数，对应 K8S request"
      },
      {
        "name": "MemRequest",
        "desc": "初始分配的内存 MiB 数，对应 K8S request"
      },
      {
        "name": "GroupResourceType",
        "desc": "部署组资源类型"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID"
      },
      {
        "name": "AgentCpuRequest",
        "desc": "agent 容器分配的 CPU 核数，对应 K8S 的 request"
      },
      {
        "name": "AgentCpuLimit",
        "desc": "agent 容器最大的 CPU 核数，对应 K8S 的 limit"
      },
      {
        "name": "AgentMemRequest",
        "desc": "agent 容器分配的内存 MiB 数，对应 K8S 的 request"
      },
      {
        "name": "AgentMemLimit",
        "desc": "agent 容器最大的内存 MiB 数，对应 K8S 的 limit"
      },
      {
        "name": "IstioCpuRequest",
        "desc": "istioproxy 容器分配的 CPU 核数，对应 K8S 的 request"
      },
      {
        "name": "IstioCpuLimit",
        "desc": "istioproxy 容器最大的 CPU 核数，对应 K8S 的 limit"
      },
      {
        "name": "IstioMemRequest",
        "desc": "istioproxy 容器分配的内存 MiB 数，对应 K8S 的 request"
      },
      {
        "name": "IstioMemLimit",
        "desc": "istioproxy 容器最大的内存 MiB 数，对应 K8S 的 limit"
      }
    ],
    "desc": "创建容器部署组"
  },
  "DescribePublicConfigReleases": {
    "params": [
      {
        "name": "ConfigName",
        "desc": "配置项名称，不传入时查询全量"
      },
      {
        "name": "NamespaceId",
        "desc": "命名空间ID，不传入时查询全量"
      },
      {
        "name": "Limit",
        "desc": "每页条数"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "ConfigId",
        "desc": "配置项ID，不传入时查询全量"
      }
    ],
    "desc": "查询公共配置发布信息"
  },
  "DescribeGroups": {
    "params": [
      {
        "name": "SearchWord",
        "desc": "搜索字段"
      },
      {
        "name": "ApplicationId",
        "desc": "应用ID"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段"
      },
      {
        "name": "OrderType",
        "desc": "排序方式"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "分页个数"
      },
      {
        "name": "NamespaceId",
        "desc": "命名空间ID"
      },
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "GroupResourceTypeList",
        "desc": "部署组资源类型列表"
      }
    ],
    "desc": "获取虚拟机部署组列表"
  },
  "ModifyLane": {
    "params": [
      {
        "name": "LaneId",
        "desc": "泳道ID"
      },
      {
        "name": "LaneName",
        "desc": "泳道名称"
      },
      {
        "name": "Remark",
        "desc": "备注"
      }
    ],
    "desc": "更新泳道信息"
  },
  "DescribeSimpleNamespaces": {
    "params": [
      {
        "name": "NamespaceIdList",
        "desc": "命名空间ID列表，不传入时查询全量"
      },
      {
        "name": "ClusterId",
        "desc": "集群ID，不传入时查询全量"
      },
      {
        "name": "Limit",
        "desc": "每页条数"
      },
      {
        "name": "Offset",
        "desc": "起始偏移量"
      },
      {
        "name": "NamespaceId",
        "desc": "命名空间ID，不传入时查询全量"
      },
      {
        "name": "NamespaceResourceTypeList",
        "desc": "查询资源类型列表"
      },
      {
        "name": "SearchWord",
        "desc": "通过id和name进行过滤"
      },
      {
        "name": "NamespaceTypeList",
        "desc": "查询的命名空间类型列表"
      },
      {
        "name": "NamespaceName",
        "desc": "通过命名空间名精确过滤"
      },
      {
        "name": "IsDefault",
        "desc": "通过是否是默认命名空间过滤，不传表示拉取全部命名空间。0：默认，命名空间。1：非默认命名空间"
      }
    ],
    "desc": "查询简单命名空间列表 "
  },
  "DescribeLanes": {
    "params": [
      {
        "name": "Limit",
        "desc": "每页展示的条数"
      },
      {
        "name": "Offset",
        "desc": "翻页偏移量"
      },
      {
        "name": "SearchWord",
        "desc": "搜索关键字"
      }
    ],
    "desc": "查询泳道列表"
  },
  "DescribeConfigReleaseLogs": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID，不传入时查询全量"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "每页条数，默认为20"
      },
      {
        "name": "NamespaceId",
        "desc": "命名空间ID，不传入时查询全量"
      },
      {
        "name": "ClusterId",
        "desc": "集群ID，不传入时查询全量"
      },
      {
        "name": "ApplicationId",
        "desc": "应用ID，不传入时查询全量"
      }
    ],
    "desc": "查询配置发布历史"
  },
  "CreateMicroservice": {
    "params": [
      {
        "name": "NamespaceId",
        "desc": "命名空间ID"
      },
      {
        "name": "MicroserviceName",
        "desc": "微服务名称"
      },
      {
        "name": "MicroserviceDesc",
        "desc": "微服务描述信息"
      }
    ],
    "desc": "新增微服务"
  },
  "DescribeDownloadInfo": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "应用ID"
      },
      {
        "name": "PkgId",
        "desc": "程序包ID"
      }
    ],
    "desc": "TSF上传的程序包存放在腾讯云对象存储（COS）中，通过该API可以获取从COS下载程序包需要的信息，包括包所在的桶、存储路径、鉴权信息等，之后使用COS API（或SDK）进行下载。\nCOS相关文档请查阅：https://cloud.tencent.com/document/product/436"
  },
  "DeployServerlessGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      },
      {
        "name": "PkgId",
        "desc": "程序包ID"
      },
      {
        "name": "Memory",
        "desc": "所需实例内存大小，取值为 1Gi 2Gi 4Gi 8Gi 16Gi，缺省为 1Gi，不传表示维持原态"
      },
      {
        "name": "InstanceRequest",
        "desc": "要求最小实例数，取值范围 [1, 4]，缺省为 1，不传表示维持原态"
      },
      {
        "name": "StartupParameters",
        "desc": "部署组启动参数，不传表示维持原态"
      }
    ],
    "desc": "部署Serverless应用"
  },
  "DescribeGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      }
    ],
    "desc": "查询虚拟机部署组详情"
  },
  "CreateConfig": {
    "params": [
      {
        "name": "ConfigName",
        "desc": "配置项名称"
      },
      {
        "name": "ConfigVersion",
        "desc": "配置项版本"
      },
      {
        "name": "ConfigValue",
        "desc": "配置项值"
      },
      {
        "name": "ApplicationId",
        "desc": "应用ID"
      },
      {
        "name": "ConfigVersionDesc",
        "desc": "配置项版本描述"
      },
      {
        "name": "ConfigType",
        "desc": "配置项值类型"
      },
      {
        "name": "EncodeWithBase64",
        "desc": "Base64编码的配置项"
      }
    ],
    "desc": "创建配置项"
  },
  "DescribeContainerGroups": {
    "params": [
      {
        "name": "SearchWord",
        "desc": "搜索字段，模糊搜索groupName字段"
      },
      {
        "name": "ApplicationId",
        "desc": "分组所属应用ID"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段，默认为 createTime字段，支持id， name， createTime"
      },
      {
        "name": "OrderType",
        "desc": "排序方式，默认为1：倒序排序，0：正序，1：倒序"
      },
      {
        "name": "Offset",
        "desc": "偏移量，取值从0开始"
      },
      {
        "name": "Limit",
        "desc": "分页个数，默认为20， 取值应为1~50"
      },
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "NamespaceId",
        "desc": "命名空间 ID"
      }
    ],
    "desc": "容器部署组列表"
  },
  "DeleteImageTags": {
    "params": [
      {
        "name": "ImageTags",
        "desc": "镜像版本数组"
      }
    ],
    "desc": "批量删除镜像版本"
  },
  "DescribeClusterInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "SearchWord",
        "desc": "搜索字段"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段"
      },
      {
        "name": "OrderType",
        "desc": "排序类型"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "分页个数"
      }
    ],
    "desc": "查询集群实例"
  },
  "CreateApplication": {
    "params": [
      {
        "name": "ApplicationName",
        "desc": "应用名称"
      },
      {
        "name": "ApplicationType",
        "desc": "应用类型，V：虚拟机应用；C：容器应用；S：serverless应用"
      },
      {
        "name": "MicroserviceType",
        "desc": "应用微服务类型，M：service mesh应用；N：普通应用；G：网关应用"
      },
      {
        "name": "ApplicationDesc",
        "desc": "应用描述"
      },
      {
        "name": "ApplicationLogConfig",
        "desc": "应用日志配置项，废弃参数"
      },
      {
        "name": "ApplicationResourceType",
        "desc": "应用资源类型，废弃参数"
      },
      {
        "name": "ApplicationRuntimeType",
        "desc": "应用runtime类型"
      }
    ],
    "desc": "创建应用"
  },
  "StopGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      }
    ],
    "desc": "停止虚拟机部署组"
  },
  "ShrinkGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      }
    ],
    "desc": "下线部署组所有机器实例"
  },
  "DescribeMicroservice": {
    "params": [
      {
        "name": "MicroserviceId",
        "desc": "微服务ID"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "分页个数"
      }
    ],
    "desc": "查询微服务详情"
  },
  "DeployGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      },
      {
        "name": "PkgId",
        "desc": "程序包ID"
      },
      {
        "name": "StartupParameters",
        "desc": "部署组启动参数"
      }
    ],
    "desc": "部署虚拟机部署组应用"
  },
  "DescribeApplications": {
    "params": [
      {
        "name": "SearchWord",
        "desc": "搜索字段"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段"
      },
      {
        "name": "OrderType",
        "desc": "排序类型"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "分页个数"
      },
      {
        "name": "ApplicationType",
        "desc": "应用类型"
      },
      {
        "name": "MicroserviceType",
        "desc": "应用的微服务类型"
      },
      {
        "name": "ApplicationResourceTypeList",
        "desc": "应用资源类型数组"
      }
    ],
    "desc": "获取应用列表"
  },
  "DescribeUploadInfo": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "应用ID"
      },
      {
        "name": "PkgName",
        "desc": "程序包名"
      },
      {
        "name": "PkgVersion",
        "desc": "程序包版本"
      },
      {
        "name": "PkgType",
        "desc": "程序包类型"
      },
      {
        "name": "PkgDesc",
        "desc": "程序包介绍"
      }
    ],
    "desc": "TSF会将软件包上传到腾讯云对象存储（COS）。调用此接口获取上传信息，如目标地域，桶，包Id，存储路径，鉴权信息等，之后请使用COS API（或SDK）进行上传。\nCOS相关文档请查阅：https://cloud.tencent.com/document/product/436"
  },
  "ModifyUploadInfo": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "应用ID"
      },
      {
        "name": "PkgId",
        "desc": "调用DescribeUploadInfo接口时返回的软件包ID"
      },
      {
        "name": "Result",
        "desc": "COS返回上传结果（默认为0：成功，其他值表示失败）"
      },
      {
        "name": "Md5",
        "desc": "程序包MD5"
      },
      {
        "name": "Size",
        "desc": "程序包大小（单位字节）"
      }
    ],
    "desc": "调用该接口和COS的上传接口后，需要调用此接口更新TSF中保存的程序包状态。\n调用此接口完成后，才标志上传包流程结束。"
  },
  "StopContainerGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      }
    ],
    "desc": "停止容器部署组"
  },
  "DescribeSimpleApplications": {
    "params": [
      {
        "name": "ApplicationIdList",
        "desc": "应用ID列表"
      },
      {
        "name": "ApplicationType",
        "desc": "应用类型"
      },
      {
        "name": "Limit",
        "desc": "每页条数"
      },
      {
        "name": "Offset",
        "desc": "起始偏移量"
      },
      {
        "name": "MicroserviceType",
        "desc": "微服务类型"
      },
      {
        "name": "ApplicationResourceTypeList",
        "desc": "资源类型数组"
      },
      {
        "name": "SearchWord",
        "desc": "通过id和name进行关键词过滤"
      }
    ],
    "desc": "查询简单应用列表"
  },
  "DescribePublicConfig": {
    "params": [
      {
        "name": "ConfigId",
        "desc": "需要查询的配置项ID"
      }
    ],
    "desc": "查询公共配置（单条）"
  },
  "ModifyContainerGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      },
      {
        "name": "AccessType",
        "desc": "0:公网 1:集群内访问 2：NodePort"
      },
      {
        "name": "ProtocolPorts",
        "desc": "ProtocolPorts数组"
      },
      {
        "name": "UpdateType",
        "desc": "更新方式：0:快速更新 1:滚动更新"
      },
      {
        "name": "UpdateIvl",
        "desc": "更新间隔,单位秒"
      }
    ],
    "desc": "修改容器部署组"
  },
  "DescribeApplication": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "应用ID"
      }
    ],
    "desc": "获取应用详情"
  },
  "ShrinkInstances": {
    "params": [
      {
        "name": "GroupId",
        "desc": "部署组ID"
      },
      {
        "name": "InstanceIdList",
        "desc": "下线机器实例ID列表"
      }
    ],
    "desc": "虚拟机部署组下线实例"
  },
  "DeleteServerlessGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "groupId，分组唯一标识"
      }
    ],
    "desc": "删除Serverless部署组"
  },
  "AddInstances": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "集群ID"
      },
      {
        "name": "InstanceIdList",
        "desc": "云主机ID列表"
      },
      {
        "name": "OsName",
        "desc": "操作系统名称"
      },
      {
        "name": "ImageId",
        "desc": "操作系统镜像ID"
      },
      {
        "name": "Password",
        "desc": "重装系统密码设置"
      },
      {
        "name": "KeyId",
        "desc": "重装系统，关联密钥设置"
      },
      {
        "name": "SgId",
        "desc": "安全组设置"
      },
      {
        "name": "InstanceImportMode",
        "desc": "云主机导入方式，虚拟机集群必填，容器集群不填写此字段，R：重装TSF系统镜像，M：手动安装agent"
      }
    ],
    "desc": "添加云主机节点至TSF集群"
  }
}