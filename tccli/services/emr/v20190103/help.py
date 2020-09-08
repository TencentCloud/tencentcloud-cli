# -*- coding: utf-8 -*-
DESC = "emr-2019-01-03"
INFO = {
  "ScaleOutInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "扩容的时间单位。取值范围：\n<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>\n<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>"
      },
      {
        "name": "TimeSpan",
        "desc": "扩容的时长。结合TimeUnit一起使用。\n<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>\n<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID。"
      },
      {
        "name": "PayMode",
        "desc": "实例计费模式。取值范围：\n<li>0：表示按量计费。</li>\n<li>1：表示包年包月。</li>"
      },
      {
        "name": "ClientToken",
        "desc": "客户端Token。"
      },
      {
        "name": "PreExecutedFileSettings",
        "desc": "引导操作脚本设置。"
      },
      {
        "name": "TaskCount",
        "desc": "扩容的Task节点数量。"
      },
      {
        "name": "CoreCount",
        "desc": "扩容的Core节点数量。"
      },
      {
        "name": "UnNecessaryNodeList",
        "desc": "扩容时不需要安装的进程。"
      },
      {
        "name": "RouterCount",
        "desc": "扩容的Router节点数量。"
      },
      {
        "name": "SoftDeployInfo",
        "desc": "部署的服务。\n<li>SoftDeployInfo和ServiceNodeInfo是同组参数，和UnNecessaryNodeList参数互斥。</li>\n<li>建议使用SoftDeployInfo和ServiceNodeInfo组合。</li>"
      },
      {
        "name": "ServiceNodeInfo",
        "desc": "启动的进程。"
      },
      {
        "name": "DisasterRecoverGroupIds",
        "desc": "分散置放群组ID列表，当前仅支持指定一个。"
      },
      {
        "name": "Tags",
        "desc": "扩容节点绑定标签列表。"
      },
      {
        "name": "HardwareResourceType",
        "desc": "扩容所选资源类型，可选范围为\"host\",\"pod\"，host为普通的CVM资源，Pod为TKE集群提供的资源"
      },
      {
        "name": "PodSpec",
        "desc": "使用Pod资源扩容时，指定的Pod规格以及来源等信息"
      }
    ],
    "desc": "实例扩容"
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "DisplayStrategy",
        "desc": "集群筛选策略。取值范围：\n<li>clusterList：表示查询除了已销毁集群之外的集群列表。</li>\n<li>monitorManage：表示查询除了已销毁、创建中以及创建失败的集群之外的集群列表。</li>\n<li>cloudHardwareManage/componentManage：目前这两个取值为预留取值，暂时和monitorManage表示同样的含义。</li>"
      },
      {
        "name": "InstanceIds",
        "desc": "按照一个或者多个实例ID查询。实例ID形如: emr-xxxxxxxx 。(此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的 Ids.N 一节)。如果不填写实例ID，返回该APPID下所有实例列表。"
      },
      {
        "name": "Offset",
        "desc": "页编号，默认值为0，表示第一页。"
      },
      {
        "name": "Limit",
        "desc": "每页返回数量，默认值为10，最大值为100。"
      },
      {
        "name": "ProjectId",
        "desc": "建议必填-1，表示拉取所有项目下的集群。\n不填默认值为0，表示拉取默认项目下的集群。\n实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/378/4400) 的返回值中的 projectId 字段来获取。"
      },
      {
        "name": "OrderField",
        "desc": "排序字段。取值范围：\n<li>clusterId：表示按照实例ID排序。</li>\n<li>addTime：表示按照实例创建时间排序。</li>\n<li>status：表示按照实例的状态码排序。</li>"
      },
      {
        "name": "Asc",
        "desc": "按照OrderField升序或者降序进行排序。取值范围：\n<li>0：表示降序。</li>\n<li>1：表示升序。</li>默认值为0。\u0007"
      }
    ],
    "desc": "查询EMR实例"
  },
  "InquiryPriceUpdateInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "变配的时间单位。取值范围：\n<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>\n<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>"
      },
      {
        "name": "TimeSpan",
        "desc": "变配的时长。结合TimeUnit一起使用。\n<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>\n<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>"
      },
      {
        "name": "UpdateSpec",
        "desc": "节点变配的目标配置。"
      },
      {
        "name": "PayMode",
        "desc": "实例计费模式。取值范围：\n<li>0：表示按量计费。</li>\n<li>1：表示包年包月。</li>"
      },
      {
        "name": "Placement",
        "desc": "实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。"
      },
      {
        "name": "Currency",
        "desc": "货币种类。取值范围：\n<li>CNY：表示人民币。</li>"
      }
    ],
    "desc": "变配询价"
  },
  "DescribeClusterNodes": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "集群实例ID,实例ID形如: emr-xxxxxxxx"
      },
      {
        "name": "NodeFlag",
        "desc": "节点标识，取值为：\n<li>all：表示获取全部类型节点，cdb信息除外。</li>\n<li>master：表示获取master节点信息。</li>\n<li>core：表示获取core节点信息。</li>\n<li>task：表示获取task节点信息。</li>\n<li>common：表示获取common节点信息。</li>\n<li>router：表示获取router节点信息。</li>\n<li>db：表示获取正常状态的cdb信息。</li>\n<li>recyle：表示获取回收站隔离中的节点信息，包括cdb信息。</li>\n<li>renew：表示获取所有待续费的节点信息，包括cdb信息，自动续费节点不会返回。</li>\n注意：现在只支持以上取值，输入其他值会导致错误。"
      },
      {
        "name": "Offset",
        "desc": "页编号，默认值为0，表示第一页。"
      },
      {
        "name": "Limit",
        "desc": "每页返回数量，默认值为100，最大值为100。"
      },
      {
        "name": "HardwareResourceType",
        "desc": "资源类型:支持all/host/pod，默认为all"
      },
      {
        "name": "SearchFields",
        "desc": "支持搜索的字段"
      }
    ],
    "desc": "查询硬件节点信息"
  },
  "InquiryPriceRenewInstance": {
    "params": [
      {
        "name": "TimeSpan",
        "desc": "实例续费的时长。需要结合TimeUnit一起使用。1表示续费1一个月"
      },
      {
        "name": "ResourceIds",
        "desc": "待续费节点的资源ID列表。资源ID形如：emr-vm-xxxxxxxx。有效的资源ID可通过登录[控制台](https://console.cloud.tencent.com/emr/static/hardware)查询。"
      },
      {
        "name": "Placement",
        "desc": "实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。"
      },
      {
        "name": "PayMode",
        "desc": "实例计费模式。此处只支持取值为1，表示包年包月。"
      },
      {
        "name": "TimeUnit",
        "desc": "实例续费的时间单位。取值范围：\n<li>m：表示月份。</li>"
      },
      {
        "name": "Currency",
        "desc": "货币种类。取值范围：\n<li>CNY：表示人民币。\u0007</li>"
      }
    ],
    "desc": "续费询价。"
  },
  "CreateInstance": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID，不同产品ID表示不同的EMR产品版本。取值范围：\n<li>1：表示EMR-V1.3.1。</li>\n<li>2：表示EMR-V2.0.1。</li>\n<li>4：表示EMR-V2.1.0。</li>\n<li>7：表示EMR-V3.0.0。</li>"
      },
      {
        "name": "VPCSettings",
        "desc": "私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。"
      },
      {
        "name": "Software",
        "desc": "部署的组件列表。不同的EMR产品ID（ProductId：具体含义参考入参ProductId字段）需要选择不同的必选组件：\n<li>ProductId为1的时候，必选组件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>\n<li>ProductId为2的时候，必选组件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>\n<li>ProductId为4的时候，必选组件包括：hadoop-2.8.4、knox-1.2.0、zookeeper-3.4.9</li>\n<li>ProductId为7的时候，必选组件包括：hadoop-3.1.2、knox-1.2.0、zookeeper-3.4.9</li>"
      },
      {
        "name": "ResourceSpec",
        "desc": "节点资源的规格。"
      },
      {
        "name": "SupportHA",
        "desc": "是否开启节点高可用。取值范围：\n<li>0：表示不开启节点高可用。</li>\n<li>1：表示开启节点高可用。</li>"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称。\n<li>长度限制为6-36个字符。</li>\n<li>只允许包含中文、字母、数字、-、_。</li>"
      },
      {
        "name": "PayMode",
        "desc": "实例计费模式。取值范围：\n<li>0：表示按量计费。</li>\n<li>1：表示包年包月。</li>"
      },
      {
        "name": "Placement",
        "desc": "实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。"
      },
      {
        "name": "TimeSpan",
        "desc": "购买实例的时长。结合TimeUnit一起使用。\n<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>\n<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>"
      },
      {
        "name": "TimeUnit",
        "desc": "购买实例的时间单位。取值范围：\n<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>\n<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>"
      },
      {
        "name": "LoginSettings",
        "desc": "实例登录设置。通过该参数可以设置所购买节点的登录方式密码或者密钥。\n<li>设置密钥时，密码仅用于组件原生WebUI快捷入口登录。</li>\n<li>未设置密钥时，密码用于登录所购节点以及组件原生WebUI快捷入口登录。</li>"
      },
      {
        "name": "COSSettings",
        "desc": "开启COS访问需要设置的参数。"
      },
      {
        "name": "SgId",
        "desc": "实例所属安全组的ID，形如sg-xxxxxxxx。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的SecurityGroupId字段来获取。"
      },
      {
        "name": "PreExecutedFileSettings",
        "desc": "引导操作脚本设置。"
      },
      {
        "name": "AutoRenew",
        "desc": "包年包月实例是否自动续费。取值范围：\n<li>0：表示不自动续费。</li>\n<li>1：表示自动续费。</li>"
      },
      {
        "name": "ClientToken",
        "desc": "客户端Token。"
      },
      {
        "name": "NeedMasterWan",
        "desc": "是否开启集群Master节点公网。取值范围：\n<li>NEED_MASTER_WAN：表示开启集群Master节点公网。</li>\n<li>NOT_NEED_MASTER_WAN：表示不开启。</li>默认开启集群Master节点公网。"
      },
      {
        "name": "RemoteLoginAtCreate",
        "desc": "是否需要开启外网远程登录，即22号端口。在SgId不为空时，该参数无效。"
      },
      {
        "name": "CheckSecurity",
        "desc": "是否开启安全集群。0表示不开启，非0表示开启。"
      },
      {
        "name": "ExtendFsField",
        "desc": "访问外部文件系统。"
      },
      {
        "name": "Tags",
        "desc": "标签描述列表。通过指定该参数可以同时绑定标签到相应的实例。"
      },
      {
        "name": "DisasterRecoverGroupIds",
        "desc": "分散置放群组ID列表，当前只支持指定一个。"
      },
      {
        "name": "CbsEncrypt",
        "desc": "集群维度CBS加密盘，默认0表示不加密，1表示加密"
      },
      {
        "name": "MetaType",
        "desc": "hive共享元数据库类型。取值范围：\n<li>EMR_NEW_META：表示集群默认创建</li>\n<li>EMR_EXIT_METE：表示集群使用指定EMR-MetaDB。</li>\n<li>USER_CUSTOM_META：表示集群使用自定义MetaDB。</li>"
      },
      {
        "name": "UnifyMetaInstanceId",
        "desc": "EMR-MetaDB实例"
      },
      {
        "name": "MetaDBInfo",
        "desc": "自定义MetaDB信息"
      }
    ],
    "desc": "创建EMR实例"
  },
  "InquiryPriceCreateInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "购买实例的时间单位。取值范围：\n<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>\n<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>"
      },
      {
        "name": "TimeSpan",
        "desc": "购买实例的时长。结合TimeUnit一起使用。\n<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>\n<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>"
      },
      {
        "name": "ResourceSpec",
        "desc": "询价的节点规格。"
      },
      {
        "name": "Currency",
        "desc": "货币种类。取值范围：\n<li>CNY：表示人民币。\u0007</li>"
      },
      {
        "name": "PayMode",
        "desc": "实例计费模式。取值范围：\n<li>0：表示按量计费。</li>\n<li>1：表示包年包月。</li>"
      },
      {
        "name": "SupportHA",
        "desc": "是否开启节点高可用。取值范围：\n<li>0：表示不开启节点高可用。</li>\n<li>1：表示开启节点高可用。\u0007</li>"
      },
      {
        "name": "Software",
        "desc": "部署的组件列表。不同的EMR产品ID（ProductId：具体含义参考入参ProductId字段）需要选择不同的必选组件：\n<li>ProductId为1的时候，必选组件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>\n<li>ProductId为2的时候，必选组件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>\n<li>ProductId为4的时候，必选组件包括：hadoop-2.8.4、knox-1.2.0、zookeeper-3.4.9</li>\n<li>ProductId为7的时候，必选组件包括：hadoop-3.1.2、knox-1.2.0、zookeeper-3.4.9</li>"
      },
      {
        "name": "Placement",
        "desc": "实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。"
      },
      {
        "name": "VPCSettings",
        "desc": "私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。"
      },
      {
        "name": "MetaType",
        "desc": "hive共享元数据库类型。取值范围：\n<li>EMR_NEW_META：表示集群默认创建</li>\n<li>EMR_EXIT_METE：表示集群使用指定EMR-MetaDB。</li>\n<li>USER_CUSTOM_META：表示集群使用自定义MetaDB。</li>"
      },
      {
        "name": "UnifyMetaInstanceId",
        "desc": "EMR-MetaDB实例"
      },
      {
        "name": "MetaDBInfo",
        "desc": "自定义MetaDB信息"
      },
      {
        "name": "ProductId",
        "desc": "产品ID，不同产品ID表示不同的EMR产品版本。取值范围：\n<li>1：表示EMR-V1.3.1。</li>\n<li>2：表示EMR-V2.0.1。</li>\n<li>4：表示EMR-V2.1.0。</li>\n<li>7：表示EMR-V3.0.0。</li>"
      }
    ],
    "desc": "创建实例询价"
  },
  "InquiryPriceScaleOutInstance": {
    "params": [
      {
        "name": "TimeUnit",
        "desc": "扩容的时间单位。取值范围：\n<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>\n<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>"
      },
      {
        "name": "TimeSpan",
        "desc": "扩容的时长。结合TimeUnit一起使用。\n<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>\n<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>"
      },
      {
        "name": "ZoneId",
        "desc": "实例所属的可用区ID，例如100003。该参数可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/213/15707) 的返回值中的ZoneId字段来获取。"
      },
      {
        "name": "PayMode",
        "desc": "实例计费模式。取值范围：\n<li>0：表示按量计费。</li>\n<li>1：表示包年包月。</li>"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID。"
      },
      {
        "name": "CoreCount",
        "desc": "扩容的Core节点数量。"
      },
      {
        "name": "TaskCount",
        "desc": "扩容的Task节点数量。"
      },
      {
        "name": "Currency",
        "desc": "货币种类。取值范围：\n<li>CNY：表示人民币。\u0007</li>"
      },
      {
        "name": "RouterCount",
        "desc": "扩容的Router节点数量。"
      }
    ],
    "desc": "扩容询价. 当扩容时候，请通过该接口查询价格。"
  },
  "TerminateTasks": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID。"
      },
      {
        "name": "ResourceIds",
        "desc": "待销毁节点的资源ID列表。资源ID形如：emr-vm-xxxxxxxx。有效的资源ID可通过登录[控制台](https://console.cloud.tencent.com/emr/static/hardware)查询。"
      }
    ],
    "desc": "缩容Task节点"
  },
  "TerminateInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID。"
      },
      {
        "name": "ResourceIds",
        "desc": "销毁节点ID。该参数为预留参数，用户无需配置。"
      }
    ],
    "desc": "销毁EMR实例。此接口仅支持弹性MapReduce正式计费版本。"
  }
}