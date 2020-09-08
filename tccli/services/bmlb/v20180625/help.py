# -*- coding: utf-8 -*-
DESC = "bmlb-2018-06-25"
INFO = {
  "DescribeL7Listeners": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerIds",
        "desc": "七层监听器实例ID列表，可通过接口DescribeL7Listeners查询。"
      }
    ],
    "desc": "获取黑石负载均衡七层监听器列表信息。"
  },
  "UnbindTrafficMirrorReceivers": {
    "params": [
      {
        "name": "TrafficMirrorId",
        "desc": "流量镜像实例ID。"
      },
      {
        "name": "ReceiverSet",
        "desc": "待绑定的主机实例ID和端口数组。"
      }
    ],
    "desc": "从流量镜像实例上解绑流量镜像接收机。"
  },
  "ModifyL7BackendWeight": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "七层监听器实例ID，可通过接口DescribeL7Listeners查询。"
      },
      {
        "name": "DomainId",
        "desc": "转发域名实例ID，可通过接口DescribeL7Rules查询。"
      },
      {
        "name": "LocationId",
        "desc": "转发路径实例ID，可通过接口DescribeL7Rules查询。"
      },
      {
        "name": "InstanceId",
        "desc": "黑石物理机主机ID、虚拟机IP或者是半托管主机ID。"
      },
      {
        "name": "Weight",
        "desc": "权重信息，可选值0~100。"
      },
      {
        "name": "Port",
        "desc": "已绑定的主机端口。"
      },
      {
        "name": "BindType",
        "desc": "绑定类型。0：物理机 1：虚拟机 2：半托管机器"
      }
    ],
    "desc": "修改黑石负载均衡七层转发路径后端实例权重。"
  },
  "ModifyL4BackendWeight": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。"
      },
      {
        "name": "InstanceId",
        "desc": "黑石物理机主机ID、虚拟机IP或者是半托管主机ID。"
      },
      {
        "name": "Weight",
        "desc": "权重信息，可选值0~100。"
      },
      {
        "name": "Port",
        "desc": "已绑定的主机端口。"
      },
      {
        "name": "BindType",
        "desc": "绑定类型。0：物理机 1：虚拟机 2：半托管机器"
      }
    ],
    "desc": "修改黑石负载均衡四层监听器后端实例权重功能。"
  },
  "CreateL4Listeners": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerSet",
        "desc": "监听器信息数组，可以创建多个监听器。目前一个负载均衡下面最多允许创建50个监听器"
      }
    ],
    "desc": "创建黑石四层负载均衡监听器功能。黑石负载均衡四层监听器提供了转发用户请求的具体规则，包括端口、协议、会话保持、健康检查等参数。"
  },
  "UnbindL4Backends": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。"
      },
      {
        "name": "BackendSet",
        "desc": "待解绑的主机信息。可以绑定多个主机端口。目前一个四层监听器下面最多允许绑定255个主机端口。"
      },
      {
        "name": "BindType",
        "desc": "绑定类型。0：物理机 1：虚拟机 2：半托管机器"
      }
    ],
    "desc": "解绑黑石负载均衡四层监听器物理服务器。"
  },
  "ModifyL7Listener": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "七层监听器实例ID，可通过接口DescribeL7Listeners查询。"
      },
      {
        "name": "ListenerName",
        "desc": "七层监听器名称。"
      },
      {
        "name": "SslMode",
        "desc": "认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。"
      },
      {
        "name": "CertId",
        "desc": "服务端证书ID。"
      },
      {
        "name": "CertName",
        "desc": "服务端证书名称。"
      },
      {
        "name": "CertContent",
        "desc": "服务端证书内容。"
      },
      {
        "name": "CertKey",
        "desc": "服务端证书密钥。"
      },
      {
        "name": "CertCaId",
        "desc": "客户端证书ID。"
      },
      {
        "name": "CertCaName",
        "desc": "客户端证书名称。"
      },
      {
        "name": "CertCaContent",
        "desc": "客户端证书内容。"
      },
      {
        "name": "Bandwidth",
        "desc": "计费模式为按固定带宽方式时监听器的限速值，可选值：0-1000，单位：Mbps。"
      },
      {
        "name": "ForwardProtocol",
        "desc": "转发协议。当监听器Protocol为https时并且SslMode为1或2时，有意义。可选的值为0：https，1：spdy，2：http2，3：spdy+http2。"
      }
    ],
    "desc": "修改黑石负载均衡七层监听器。"
  },
  "DeleteTrafficMirror": {
    "params": [
      {
        "name": "TrafficMirrorIds",
        "desc": "流量镜像实例ID数组，可以批量删除，每次删除上限为20"
      }
    ],
    "desc": "删除已创建的黑石流量镜像实例，删除过程是异步执行的，因此需要使用查询任务接口获取删除的结果。"
  },
  "CreateL7Rules": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "七层监听器实例ID，可通过接口DescribeL7Listeners查询。"
      },
      {
        "name": "RuleSet",
        "desc": "七层转发规则信息数组，可以创建多个七层转发规则。目前一个七层监听器下面最多允许创建50个七层转发域名，而每一个转发域名下最多可以创建100个转发规则。目前只能单条创建，不能批量创建。"
      }
    ],
    "desc": "创建黑石负载均衡七层转发规则。"
  },
  "DescribeTrafficMirrorReceiverHealthStatus": {
    "params": [
      {
        "name": "TrafficMirrorId",
        "desc": "查询所在的流量镜像ID。"
      },
      {
        "name": "ReceiverSet",
        "desc": "流量镜像接收机实例ID和端口数组。"
      }
    ],
    "desc": "获取流量镜像接收机健康状态。"
  },
  "UnbindL7Backends": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "七层监听器实例ID，可通过接口DescribeL7Listeners查询。"
      },
      {
        "name": "DomainId",
        "desc": "转发域名实例ID，可通过接口DescribeL7Rules查询。"
      },
      {
        "name": "LocationId",
        "desc": "转发路径实例ID，可通过接口DescribeL7Rules查询。"
      },
      {
        "name": "BackendSet",
        "desc": "待绑定的主机信息。"
      },
      {
        "name": "BindType",
        "desc": "绑定类型。0：物理机  1：虚拟机 2：半托管机器"
      }
    ],
    "desc": "解绑黑石物理服务器或者托管服务器到七层转发路径功能。"
  },
  "DeleteL7Rules": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "七层监听器实例ID，可通过接口DescribeL7Listeners查询。"
      },
      {
        "name": "DomainId",
        "desc": "转发域名实例ID，可通过接口DescribeL7Rules查询。"
      },
      {
        "name": "LocationIds",
        "desc": "转发路径实例ID列表，可通过接口DescribeL7Rules查询。"
      }
    ],
    "desc": "删除黑石负载均衡七层转发规则。"
  },
  "DescribeL4ListenerInfo": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "SearchKey",
        "desc": "查找的键值，可用于模糊查找该名称的监听器。"
      },
      {
        "name": "InstanceIds",
        "desc": "主机ID或虚机IP列表，可用于获取绑定了该主机的监听器。"
      }
    ],
    "desc": "查找绑定了某主机或者指定监听器名称的黑石负载均衡四层监听器。"
  },
  "DescribeTrafficMirrorListeners": {
    "params": [
      {
        "name": "TrafficMirrorId",
        "desc": "流量镜像实例ID。"
      },
      {
        "name": "Offset",
        "desc": "分页的偏移量，也即从第几条记录开始查询"
      },
      {
        "name": "Limit",
        "desc": "单次查询返回的条目数，默认值：500。"
      },
      {
        "name": "SearchLoadBalancerIds",
        "desc": "待搜索的负载均衡Id。"
      },
      {
        "name": "SearchLoadBalancerNames",
        "desc": "待搜索的负载均衡名称。"
      },
      {
        "name": "SearchVips",
        "desc": "待搜索的Vip。"
      },
      {
        "name": "SearchListenerIds",
        "desc": "待搜索的监听器ID。"
      },
      {
        "name": "SearchListenerNames",
        "desc": "待搜索的监听器名称。"
      },
      {
        "name": "SearchProtocols",
        "desc": "待搜索的协议名称。"
      },
      {
        "name": "SearchLoadBalancerPorts",
        "desc": "待搜索的端口。"
      }
    ],
    "desc": "获取流量镜像的监听器列表信息。"
  },
  "ModifyL7Locations": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "七层监听器实例ID，可通过接口DescribeL7Listeners查询。"
      },
      {
        "name": "RuleSet",
        "desc": "待更新的七层转发规则信息数组。"
      }
    ],
    "desc": "修改黑石负载均衡七层转发路径。"
  },
  "DeleteLoadBalancer": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      }
    ],
    "desc": "删除用户指定的黑石负载均衡实例。"
  },
  "DescribeL7Rules": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "七层监听器ID，可通过接口DescribeL7Listeners查询。"
      },
      {
        "name": "DomainIds",
        "desc": "转发域名ID列表，可通过接口DescribeL7Rules查询。"
      }
    ],
    "desc": "获取黑石负载均衡七层转发规则。"
  },
  "DescribeLoadBalancerTaskResult": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID。由具体的异步操作接口提供。"
      }
    ],
    "desc": "查询负载均衡实例异步任务的执行情况。"
  },
  "DescribeL7ListenerInfo": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "SearchKey",
        "desc": "查找的键值，可用于模糊查找有该转发域名的监听器。"
      },
      {
        "name": "InstanceIds",
        "desc": "主机ID或虚机IP列表，可用于获取绑定了该主机的监听器。"
      },
      {
        "name": "IfGetBackendInfo",
        "desc": "是否获取转发规则下的主机信息。默认为0，不获取。"
      }
    ],
    "desc": "查找绑定了某主机或者有某转发域名黑石负载均衡七层监听器。"
  },
  "DescribeL4Listeners": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerIds",
        "desc": "四层监听器实例ID数组，可通过接口DescribeL4Listeners查询。"
      }
    ],
    "desc": "获取黑石负载均衡四层监听器。"
  },
  "SetTrafficMirrorHealthSwitch": {
    "params": [
      {
        "name": "TrafficMirrorId",
        "desc": "流量镜像实例ID。"
      },
      {
        "name": "HealthSwitch",
        "desc": "健康检查开关，0：关闭，1：打开"
      },
      {
        "name": "HealthNum",
        "desc": "健康检查判断健康的次数，最小值2，最大值10。"
      },
      {
        "name": "UnhealthNum",
        "desc": "健康检查判断不健康的次数，最小值2，最大值10。"
      },
      {
        "name": "IntervalTime",
        "desc": "健康检查间隔，单位：秒，最小值5，最大值300。"
      },
      {
        "name": "HttpCheckDomain",
        "desc": "检查的域名配置。"
      },
      {
        "name": "HttpCheckPath",
        "desc": "检查的路径配置。"
      },
      {
        "name": "HttpCodes",
        "desc": "健康检查中认为健康的HTTP返回码的组合。可选值为1~5的集合，1表示HTTP返回码为1xx认为健康。2表示HTTP返回码为2xx认为健康。3表示HTTP返回码为3xx认为健康。4表示HTTP返回码为4xx认为健康。5表示HTTP返回码为5xx认为健康。"
      }
    ],
    "desc": "设置流量镜像的健康检查参数。"
  },
  "DescribeLoadBalancers": {
    "params": [
      {
        "name": "LoadBalancerIds",
        "desc": "负载均衡器ID数组"
      },
      {
        "name": "LoadBalancerType",
        "desc": "负载均衡的类型 : open表示公网LB类型，internal表示内网LB类型"
      },
      {
        "name": "LoadBalancerName",
        "desc": "负载均衡器名称"
      },
      {
        "name": "Domain",
        "desc": "负载均衡域名。规则：1-60个小写英文字母、数字、点号“.”或连接线“-”。内网类型的负载均衡不能配置该字段"
      },
      {
        "name": "LoadBalancerVips",
        "desc": "负载均衡获得的公网IP地址,支持多个"
      },
      {
        "name": "Offset",
        "desc": "数据偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数据长度，默认为20"
      },
      {
        "name": "SearchKey",
        "desc": "模糊查找名称、域名、VIP"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段，支持：loadBalancerName,createTime,domain,loadBalancerType"
      },
      {
        "name": "OrderType",
        "desc": "1倒序，0顺序，默认顺序"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID"
      },
      {
        "name": "Exclusive",
        "desc": "是否筛选独占集群，0表示非独占集群，1表示四层独占集群，2表示七层独占集群，3表示四层和七层独占集群，4表示共享容灾"
      },
      {
        "name": "TgwSetType",
        "desc": "该负载均衡对应的tgw集群（fullnat,tunnel,dnat）"
      },
      {
        "name": "VpcId",
        "desc": "该负载均衡对应的所在的私有网络ID"
      },
      {
        "name": "QueryType",
        "desc": "'CONFLIST' 查询带confId的LB列表，'CONFID' 查询某个confId绑定的LB列表"
      },
      {
        "name": "ConfId",
        "desc": "个性化配置ID"
      }
    ],
    "desc": "获取黑石负载均衡实例列表"
  },
  "DeleteListeners": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerIds",
        "desc": "待删除的负载均衡四层和七层监听器ID列表，可通过接口DescribeL4Listeners和DescribeL7Listeners查询。目前同时只能删除一种类型的监听器，并且删除七层监听器的数量上限为一个。"
      }
    ],
    "desc": "删除黑石负载均衡监听器。"
  },
  "DescribeCertDetail": {
    "params": [
      {
        "name": "CertId",
        "desc": "证书ID。"
      }
    ],
    "desc": "获取黑石负载均衡证书详情。"
  },
  "UnbindTrafficMirrorListeners": {
    "params": [
      {
        "name": "TrafficMirrorId",
        "desc": "流量镜像实例ID。"
      },
      {
        "name": "ListenerIds",
        "desc": "七层监听器实例ID数组，可通过接口DescribeL7Listeners查询。"
      }
    ],
    "desc": "解绑流量镜像监听器。"
  },
  "ModifyL7BackendPort": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "七层监听器实例ID，可通过接口DescribeL7Listeners查询。"
      },
      {
        "name": "DomainId",
        "desc": "转发域名实例ID，可通过接口DescribeL7Rules查询。"
      },
      {
        "name": "LocationId",
        "desc": "转发路径实例ID，可通过接口DescribeL7Rules查询。"
      },
      {
        "name": "InstanceId",
        "desc": "黑石物理机主机ID、虚拟机IP或者是半托管主机ID。"
      },
      {
        "name": "Port",
        "desc": "已绑定的主机端口。"
      },
      {
        "name": "NewPort",
        "desc": "新的主机端口，可选值1~65535。"
      },
      {
        "name": "BindType",
        "desc": "绑定类型。0：物理机 1：虚拟机 2：半托管机器"
      }
    ],
    "desc": "修改黑石负载均衡七层转发路径后端实例端口。"
  },
  "DescribeL7Backends": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "七层监听器实例ID，可通过接口DescribeL7Listeners查询。"
      },
      {
        "name": "DomainId",
        "desc": "转发域名实例ID，可通过接口DescribeL7Rules查询。"
      },
      {
        "name": "LocationId",
        "desc": "转发路径实例ID，可通过接口DescribeL7Rules查询。"
      },
      {
        "name": "QueryType",
        "desc": "查询条件，传'all'则查询所有与规则绑定的主机信息。如果为all时，DomainId和LocationId参数没有意义不必传入，否则DomainId和LocationId参数必须传入。"
      }
    ],
    "desc": "获取黑石负载均衡七层监听器绑定的主机列表"
  },
  "CreateTrafficMirror": {
    "params": [
      {
        "name": "Alias",
        "desc": "流量镜像实例别名。"
      },
      {
        "name": "VpcId",
        "desc": "流量镜像实例所属的私有网络ID，形如：vpc-xxx。"
      }
    ],
    "desc": "创建流量镜像实例。"
  },
  "ModifyL4BackendProbePort": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "负载均衡四层监听器ID，可通过接口DescribeL7Listeners查询。"
      },
      {
        "name": "InstanceId",
        "desc": "黑石物理机主机ID、虚拟机IP或者是半托管主机ID。"
      },
      {
        "name": "Port",
        "desc": "已绑定的主机端口。"
      },
      {
        "name": "ProbePort",
        "desc": "新的探测端口，可选值1~65535。"
      },
      {
        "name": "BindType",
        "desc": "绑定类型。0：物理机 1：虚拟机IP 2：半托管机器"
      }
    ],
    "desc": "修改黑石负载均衡四层监听器后端探测端口。"
  },
  "BindL4Backends": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "四层监听器实例ID，可通过接口DescribeL4Listeners查询。"
      },
      {
        "name": "BackendSet",
        "desc": "待绑定的主机信息。可以绑定多个主机端口。目前一个四层监听器下面最多允许绑定255个主机端口。"
      },
      {
        "name": "BindType",
        "desc": "绑定类型。0：物理机 1：虚拟机 2：半托管机器"
      }
    ],
    "desc": "绑定黑石服务器到四层监听器。服务器包括物理服务器、虚拟机以及半托管机器。"
  },
  "BindTrafficMirrorReceivers": {
    "params": [
      {
        "name": "TrafficMirrorId",
        "desc": "流量镜像实例ID。"
      },
      {
        "name": "ReceiverSet",
        "desc": "待绑定的黑石物理机信息数组。"
      }
    ],
    "desc": "绑定黑石物理服务器成为流量镜像接收机。"
  },
  "ReplaceCert": {
    "params": [
      {
        "name": "OldCertId",
        "desc": "要被替换的证书ID"
      },
      {
        "name": "NewCert",
        "desc": "证书内容"
      },
      {
        "name": "NewAlias",
        "desc": "证书名称"
      },
      {
        "name": "NewKey",
        "desc": "私钥内容，证书类型为SVR时不需要传递"
      },
      {
        "name": "DeleteOld",
        "desc": "是否删除旧证书，0 表示不删除，1 表示删除"
      }
    ],
    "desc": "更新黑石负载均衡证书。"
  },
  "DeleteL7Domains": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "七层监听器实例ID，可通过接口DescribeL7Listeners查询。"
      },
      {
        "name": "DomainIds",
        "desc": "转发域名实例ID列表，可通过接口DescribeL7Rules查询。"
      }
    ],
    "desc": "删除黑石负载均衡七层转发域名。"
  },
  "DescribeDevicesBindInfo": {
    "params": [
      {
        "name": "VpcId",
        "desc": "黑石私有网络唯一ID。"
      },
      {
        "name": "InstanceIds",
        "desc": "主机ID或虚机IP列表，可用于获取绑定了该主机的负载均衡列表。"
      }
    ],
    "desc": "查询黑石物理机和虚机以及托管服务器绑定的黑石负载均衡详情。"
  },
  "DescribeTrafficMirrors": {
    "params": [
      {
        "name": "TrafficMirrorIds",
        "desc": "流量镜像实例ID的数组，支持批量查询"
      },
      {
        "name": "Aliases",
        "desc": "流量镜像实例别名数组。"
      },
      {
        "name": "VpcIds",
        "desc": "流量镜像实例所属的私有网络ID数组，形如：vpc-xxx。"
      },
      {
        "name": "Offset",
        "desc": "分页的偏移量，也即从第几条记录开始查询"
      },
      {
        "name": "Limit",
        "desc": "单次查询返回的条目数，默认值：500。"
      },
      {
        "name": "OrderField",
        "desc": "排序字段。trafficMirrorId或者createTime。"
      },
      {
        "name": "Order",
        "desc": "排序方式，取值：0:增序(默认)，1:降序"
      },
      {
        "name": "SearchKey",
        "desc": "模糊匹配trafficMirrorId或者alias字段。"
      }
    ],
    "desc": "获取流量镜像实例的列表信息。"
  },
  "ModifyL4BackendPort": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。"
      },
      {
        "name": "InstanceId",
        "desc": "黑石物理机主机ID、虚拟机IP或者是半托管主机ID。"
      },
      {
        "name": "Port",
        "desc": "已绑定的主机端口。"
      },
      {
        "name": "NewPort",
        "desc": "新的主机端口，可选值1~65535。"
      },
      {
        "name": "BindType",
        "desc": "绑定类型。0：物理机  1：虚拟机 2：半托管机器"
      }
    ],
    "desc": "修改黑石负载均衡四层监听器后端实例端口。"
  },
  "UploadCert": {
    "params": [
      {
        "name": "CertType",
        "desc": "证书类型，可选值：CA，SVR。"
      },
      {
        "name": "Cert",
        "desc": "证书内容。"
      },
      {
        "name": "Alias",
        "desc": "证书别名。"
      },
      {
        "name": "Key",
        "desc": "私钥内容，证书类型为SVR时不需要传递。"
      }
    ],
    "desc": "创建黑石负载均衡证书。"
  },
  "DescribeL7ListenersEx": {
    "params": [
      {
        "name": "TrafficMirrorId",
        "desc": "返回的监听器中标识是否绑定在此流量镜像中。"
      },
      {
        "name": "VpcId",
        "desc": "待获取监听器所在的VPC的ID。"
      },
      {
        "name": "Offset",
        "desc": "此VPC中获取负载均衡的偏移。"
      },
      {
        "name": "Limit",
        "desc": "此VPC中获取负载均衡的数量。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\nLoadBalancerId - String - （过滤条件）负载均衡ID。\nLoadBalancerName - String - （过滤条件）负载均衡名称。\nVip - String - （过滤条件）VIP。\nListenerId - String - （过滤条件）监听器ID。\nListenerName -  String - （过滤条件）监听器名称。\nProtocol -  String - （过滤条件）七层协议。\nLoadBalancerPort -  String - （过滤条件）监听器端口。"
      }
    ],
    "desc": "获取指定VPC下的7层监听器(支持模糊匹配)。"
  },
  "CreateL7Listeners": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID"
      },
      {
        "name": "ListenerSet",
        "desc": "七层监听器信息数组，可以创建多个七层监听器。目前一个负载均衡下面最多允许创建50个七层监听器。"
      }
    ],
    "desc": "创建黑石负载均衡七层监听器功能。负载均衡七层监听器提供了转发用户请求的具体规则，包括端口、协议等参数。"
  },
  "DescribeL4Backends": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "负载均衡四层监听器ID，可通过接口DescribeL4Listeners查询。"
      },
      {
        "name": "BackendSet",
        "desc": "待查询的主机信息。"
      }
    ],
    "desc": "获取黑石负载均衡四层监听器绑定的主机列表。"
  },
  "BindTrafficMirrorListeners": {
    "params": [
      {
        "name": "TrafficMirrorId",
        "desc": "流量镜像实例ID。"
      },
      {
        "name": "ListenerIds",
        "desc": "七层监听器实例ID数组，可通过接口DescribeL7Listeners查询。"
      }
    ],
    "desc": "绑定黑石服务器七层监听器到流量镜像实例。"
  },
  "ModifyLoadBalancer": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "LoadBalancerName",
        "desc": "负载均衡器名称，规则：1-20个英文、汉字、数字、连接线“-”或下划线“_”。"
      },
      {
        "name": "DomainPrefix",
        "desc": "域名前缀，负载均衡的域名由用户输入的域名前缀与配置文件中的域名后缀一起组合而成，保证是唯一的域名。规则：1-20个小写英文字母、数字或连接线“-”。内网类型的负载均衡不能配置该字段。"
      }
    ],
    "desc": "根据输入参数来修改黑石负载均衡实例的基本配置信息。可能的信息包括负载均衡实例的名称，域名前缀。"
  },
  "SetTrafficMirrorAlias": {
    "params": [
      {
        "name": "TrafficMirrorId",
        "desc": "流量镜像实例ID。"
      },
      {
        "name": "Alias",
        "desc": "流量镜像实例别名。"
      }
    ],
    "desc": "设置流量镜像的别名。"
  },
  "DescribeLoadBalancerPortInfo": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      }
    ],
    "desc": "获取黑石负载均衡端口相关信息。"
  },
  "ModifyLoadBalancerChargeMode": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID。"
      },
      {
        "name": "PayMode",
        "desc": "计费方式。flow或bandwidth。"
      },
      {
        "name": "ListenerSet",
        "desc": "监听器信息，当计费方式选为 bandwidth 且此负载均衡实例下存在监听器时需填入此字段，可以自定义每个监听器带宽上限。"
      }
    ],
    "desc": "更改黑石负载均衡的计费方式"
  },
  "BindL7Backends": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "七层监听器实例ID，可通过接口DescribeL7Listeners查询。"
      },
      {
        "name": "DomainId",
        "desc": "转发域名实例ID，可通过接口DescribeL7Rules查询。"
      },
      {
        "name": "LocationId",
        "desc": "转发路径实例ID，可通过接口DescribeL7Rules查询。"
      },
      {
        "name": "BackendSet",
        "desc": "待绑定的主机信息。可以绑定多个主机端口。目前一个七层转发路径下面最多允许绑定255个主机端口。"
      },
      {
        "name": "BindType",
        "desc": "绑定类型。0：物理机，1：虚拟机 2：半托管机器。"
      }
    ],
    "desc": "绑定黑石物理服务器或半托管服务器到七层转发路径。"
  },
  "CreateLoadBalancers": {
    "params": [
      {
        "name": "VpcId",
        "desc": "黑石负载均衡实例所属的私有网络ID。"
      },
      {
        "name": "LoadBalancerType",
        "desc": "负载均衡的类型，取值为open或internal。open表示公网(有日租)，internal表示内网。"
      },
      {
        "name": "SubnetId",
        "desc": "在私有网络内购买内网负载均衡实例的时候需要指定子网ID，内网负载均衡实例的VIP将从这个子网中产生。其他情况不用填写该字段。"
      },
      {
        "name": "ProjectId",
        "desc": "负载均衡所属项目ID。不填则属于默认项目。"
      },
      {
        "name": "GoodsNum",
        "desc": "购买黑石负载均衡实例的数量。默认值为1, 最大值为20。"
      },
      {
        "name": "PayMode",
        "desc": "黑石负载均衡的计费模式，取值为flow和bandwidth，其中flow模式表示流量模式，bandwidth表示带宽模式。默认值为flow。"
      },
      {
        "name": "TgwSetType",
        "desc": "负载均衡对应的TGW集群类别，取值为tunnel、fullnat或dnat。tunnel表示隧道集群，fullnat表示FULLNAT集群（普通外网负载均衡），dnat表示DNAT集群（增强型外网负载均衡）。默认值为fullnat。如需获取client IP，可以选择 tunnel 模式，fullnat 模式（tcp 通过toa 获取），dnat 模式。"
      },
      {
        "name": "Exclusive",
        "desc": "负载均衡的独占类别，取值为0表示非独占，1表示四层独占，2表示七层独占，3表示四层和七层独占，4表示共享容灾。"
      },
      {
        "name": "SpecifiedVips",
        "desc": "指定的VIP，如果指定，则数量必须与goodsNum一致。如果不指定，则由后台分配随机VIP。"
      },
      {
        "name": "BzConf",
        "desc": "（未全地域开放）保障型负载均衡设定参数，如果类别选择保障型则需传入此参数。"
      },
      {
        "name": "IpProtocolType",
        "desc": "IP协议类型。可取的值为“ipv4”或“ipv6”。"
      }
    ],
    "desc": "用来创建黑石负载均衡。为了使用黑石负载均衡服务，您必须要创建一个或者多个负载均衡实例。通过成功调用该接口，会返回负载均衡实例的唯一ID。用户可以购买的黑石负载均衡实例类型分为：公网类型、内网类型。公网类型负载均衡对应一个BGP VIP，可用于快速访问公网负载均衡绑定的物理服务器；内网类型负载均衡对应一个腾讯云内部的VIP，不能通过Internet访问，可快速访问内网负载均衡绑定的物理服务器。"
  },
  "ModifyL4Listener": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID，可通过接口DescribeLoadBalancers查询。"
      },
      {
        "name": "ListenerId",
        "desc": "四层监听器ID。可通过接口DescribeL4Listeners查询。"
      },
      {
        "name": "ListenerName",
        "desc": "四层监听器名称。"
      },
      {
        "name": "SessionExpire",
        "desc": "会话保持时间，单位：秒。可选值：900~3600。"
      },
      {
        "name": "HealthSwitch",
        "desc": "是否开启健康检查：1（开启）、0（关闭）。默认值0，表示关闭。"
      },
      {
        "name": "TimeOut",
        "desc": "健康检查的响应超时时间，可选值：2-60，默认值：2，单位:秒。<br><font color=\"red\">响应超时时间要小于检查间隔时间。</font>"
      },
      {
        "name": "IntervalTime",
        "desc": "健康检查间隔，默认值：5，可选值：5-300，单位：秒。"
      },
      {
        "name": "HealthNum",
        "desc": "健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。"
      },
      {
        "name": "UnhealthNum",
        "desc": "不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。"
      },
      {
        "name": "Bandwidth",
        "desc": "监听器最大带宽值，用于计费模式为固定带宽计费。可选值：0-1000，单位：Mbps。"
      },
      {
        "name": "CustomHealthSwitch",
        "desc": "是否开启自定义健康检查：1（开启）、0（关闭）。默认值0，表示关闭。（该字段在健康检查开启的情况下才生效）"
      },
      {
        "name": "InputType",
        "desc": "自定义健康探测内容类型，可选值：text（文本）、hexadecimal（十六进制）。"
      },
      {
        "name": "LineSeparatorType",
        "desc": "探测内容类型为文本方式时，针对请求文本中换行替换方式。可选值：1（替换为LF）、2（替换为CR）、3（替换为LF+CR）。"
      },
      {
        "name": "HealthRequest",
        "desc": "自定义探测请求内容。"
      },
      {
        "name": "HealthResponse",
        "desc": "自定义探测返回内容。"
      },
      {
        "name": "ToaFlag",
        "desc": "是否开启toa。可选值：0（关闭）、1（开启），默认关闭。（该字段在负载均衡为fullnat类型下才生效）"
      },
      {
        "name": "BalanceMode",
        "desc": "四层调度方式。wrr，wlc。"
      }
    ],
    "desc": "修改黑石负载均衡四层监听器。"
  },
  "DescribeTrafficMirrorReceivers": {
    "params": [
      {
        "name": "TrafficMirrorId",
        "desc": "流量镜像实例ID。"
      },
      {
        "name": "InstanceIds",
        "desc": "接收机黑石物理机实例ID数组。"
      },
      {
        "name": "Ports",
        "desc": "接收机接收端口数组。"
      },
      {
        "name": "Weights",
        "desc": "接收机实例权重数组。"
      },
      {
        "name": "Offset",
        "desc": "分页的偏移量，也即从第几条记录开始查询"
      },
      {
        "name": "Limit",
        "desc": "单次查询返回的条目数，默认值：500。"
      },
      {
        "name": "VagueStr",
        "desc": "搜索instance或者alias"
      },
      {
        "name": "VagueIp",
        "desc": "搜索IP"
      }
    ],
    "desc": "获取指定流量镜像实例的接收机信息。"
  }
}