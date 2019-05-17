# -*- coding: utf-8 -*-
DESC = "clb-2018-03-17"
INFO = {
  "RegisterTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerId",
        "desc": "负载均衡监听器 ID"
      },
      {
        "name": "Targets",
        "desc": "要注册的后端机器列表，数组长度最大支持20"
      },
      {
        "name": "LocationId",
        "desc": "转发规则的ID，当注册机器到七层转发规则时，必须提供此参数或Domain+Url两者之一"
      },
      {
        "name": "Domain",
        "desc": "目标规则的域名，提供LocationId参数时本参数不生效"
      },
      {
        "name": "Url",
        "desc": "目标规则的URL，提供LocationId参数时本参数不生效"
      }
    ],
    "desc": "RegisterTargets 接口用来将一台或多台后端机器注册到应用型负载均衡的监听器，对于四层监听器（TCP、UDP），只需指定监听器ID即可，对于七层监听器（HTTP、HTTPS），还需通过LocationId或者Domain+Url指定转发规则。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "SetLoadBalancerSecurityGroups": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "SecurityGroups",
        "desc": "安全组ID构成的数组，一个负载均衡实例最多关联50个安全组，如果要解绑所有安全组，可不传此参数。"
      }
    ],
    "desc": "SetLoadBalancerSecurityGroups 接口支持对一个负载均衡实例执行设置（绑定、解绑）安全组操作，查询一个负载均衡实例目前已绑定的安全组，可使用 DescribeLoadBalancers 接口。\n绑定操作时，入参需要传入负载均衡实例要绑定的所有安全组（已绑定的+新增绑定的）。\n解绑操作时，入参需要传入负载均衡实例执行解绑后所绑定的所有安全组；如果要解绑所有安全组，可传入空数组。"
  },
  "DescribeClassicalLBListeners": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerIds",
        "desc": "负载均衡监听器ID列表， 范围[1-65535]"
      },
      {
        "name": "Protocol",
        "desc": "负载均衡监听的协议, 'TCP', 'UDP', 'HTTP', 'HTTPS'"
      },
      {
        "name": "ListenerPort",
        "desc": "负载均衡监听端口"
      },
      {
        "name": "Status",
        "desc": "监听器的状态，0 表示创建中，1 表示运行中"
      }
    ],
    "desc": "DescribeClassicalLBListeners用于获取传统型负载均衡信息"
  },
  "DeleteListener": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "应用型负载均衡实例 ID"
      },
      {
        "name": "ListenerId",
        "desc": "要删除的监听器 ID"
      }
    ],
    "desc": "本接口用来删除应用型（四层和七层）负载均衡实例下的监听器。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "CreateRule": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerId",
        "desc": "监听器 ID"
      },
      {
        "name": "Rules",
        "desc": "新建转发规则的信息"
      }
    ],
    "desc": "CreateRule 接口用于在一个已存在的应用型负载均衡七层监听器下创建转发规则，七层监听器中，后端机器必须绑定到规则上而非监听器上。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "AutoRewrite": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID"
      },
      {
        "name": "ListenerId",
        "desc": "监听器ID"
      },
      {
        "name": "Domains",
        "desc": "需要重定向的域名"
      }
    ],
    "desc": "系统自动为已存在的HTTPS:443监听器创建HTTP监听器进行转发，默认使用80端口。创建成功后可以通过HTTP:80地址自动跳转为HTTPS:443地址进行访问。"
  },
  "ModifyDomain": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerId",
        "desc": "应用型负载均衡监听器 ID"
      },
      {
        "name": "Domain",
        "desc": "监听器下的某个旧域名。"
      },
      {
        "name": "NewDomain",
        "desc": "新域名，\t长度限制为：1-80。有三种使用格式：非正则表达式格式，通配符格式，正则表达式格式。非正则表达式格式只能使用字母、数字、‘-’、‘.’。通配符格式的使用 ‘*’ 只能在开头或者结尾。正则表达式以'~'开头。"
      }
    ],
    "desc": "ModifyDomain接口用来修改应用型负载均衡七层监听器下的域名。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "DescribeClassicalLBTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      }
    ],
    "desc": "DescribeClassicalLBTargets用于获取传统型负载均衡绑定的后端服务"
  },
  "DeregisterTargetsFromClassicalLB": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "InstanceIds",
        "desc": "后端实例ID列表"
      }
    ],
    "desc": "DeregisterTargetsFromClassicalLB用于解绑后端服务器"
  },
  "DescribeClassicalLBHealthStatus": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerId",
        "desc": "负载均衡监听器ID"
      }
    ],
    "desc": "DescribeClassicalLBHealthStatus用于获取传统型负载均衡后端的健康状态"
  },
  "ModifyListener": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerId",
        "desc": "负载均衡监听器 ID"
      },
      {
        "name": "ListenerName",
        "desc": "新的监听器名称"
      },
      {
        "name": "SessionExpireTime",
        "desc": "会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。"
      },
      {
        "name": "HealthCheck",
        "desc": "健康检查相关参数，此参数仅适用于TCP/UDP/TCP_SSL监听器"
      },
      {
        "name": "Certificate",
        "desc": "证书相关信息，此参数仅适用于HTTPS/TCP_SSL监听器"
      },
      {
        "name": "Scheduler",
        "desc": "监听器转发的方式。可选值：WRR、LEAST_CONN\n分别表示按权重轮询、最小连接数， 默认为 WRR。"
      }
    ],
    "desc": "ModifyListener接口用来修改应用型负载均衡监听器的属性，包括监听器名称、健康检查参数、证书信息、转发策略等。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "DeleteLoadBalancer": {
    "params": [
      {
        "name": "LoadBalancerIds",
        "desc": "要删除的负载均衡实例 ID数组"
      }
    ],
    "desc": "DeleteLoadBalancer 接口用来删除用户指定的一个负载均衡实例。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "DeleteRule": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerId",
        "desc": "应用型负载均衡监听器 ID"
      },
      {
        "name": "LocationIds",
        "desc": "要删除的转发规则的ID组成的数组"
      },
      {
        "name": "Domain",
        "desc": "要删除的转发规则的域名，已提供LocationIds参数时本参数不生效"
      },
      {
        "name": "Url",
        "desc": "要删除的转发规则的转发路径，已提供LocationIds参数时本参数不生效"
      }
    ],
    "desc": "DeleteRule 接口用来删除应用型负载均衡实例七层监听器下的转发规则。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "DescribeLoadBalancers": {
    "params": [
      {
        "name": "LoadBalancerIds",
        "desc": "负载均衡实例 ID。"
      },
      {
        "name": "LoadBalancerType",
        "desc": "负载均衡实例的网络类型：\nOPEN：公网属性， INTERNAL：内网属性。"
      },
      {
        "name": "Forward",
        "desc": "1：应用型，0：传统型。"
      },
      {
        "name": "LoadBalancerName",
        "desc": "负载均衡实例名称。"
      },
      {
        "name": "Domain",
        "desc": "腾讯云为负载均衡实例分配的域名，应用型负载均衡该字段无意义。"
      },
      {
        "name": "LoadBalancerVips",
        "desc": "负载均衡实例的 VIP 地址，支持多个。"
      },
      {
        "name": "BackendPublicIps",
        "desc": "后端云服务器的外网 IP。"
      },
      {
        "name": "BackendPrivateIps",
        "desc": "后端云服务器的内网 IP。"
      },
      {
        "name": "Offset",
        "desc": "数据偏移量，默认为 0。"
      },
      {
        "name": "Limit",
        "desc": "返回负载均衡个数，默认为 20。"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段，支持以下字段：LoadBalancerName，CreateTime，Domain，LoadBalancerType。"
      },
      {
        "name": "OrderType",
        "desc": "1：倒序，0：顺序，默认按照创建时间倒序。"
      },
      {
        "name": "SearchKey",
        "desc": "搜索字段，模糊匹配名称、域名、VIP。"
      },
      {
        "name": "ProjectId",
        "desc": "负载均衡实例所属的项目 ID，可以通过 DescribeProject 接口获取。"
      },
      {
        "name": "WithRs",
        "desc": "查询的负载均衡是否绑定后端服务器，0：没有绑定云服务器，1：绑定云服务器，-1：查询全部。"
      },
      {
        "name": "VpcId",
        "desc": "负载均衡实例所属私有网络，如 vpc-bhqkbhdx，\n基础网络不支持通过VpcId查询。"
      },
      {
        "name": "SecurityGroup",
        "desc": "安全组ID，如 sg-m1cc9123"
      }
    ],
    "desc": "查询负载均衡实例列表\n"
  },
  "DescribeListeners": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerIds",
        "desc": "要查询的应用型负载均衡监听器 ID数组"
      },
      {
        "name": "Protocol",
        "desc": "要查询的监听器协议类型，取值 TCP | UDP | HTTP | HTTPS | TCP_SSL"
      },
      {
        "name": "Port",
        "desc": "要查询的监听器的端口"
      }
    ],
    "desc": "DescribeListeners 接口可根据负载均衡器 ID，监听器的协议或者端口作为过滤条件获取监听器列表。如果不指定任何过滤条件，默认返该负载均衡器下的默认数据长度（20 个）的监听器。"
  },
  "CreateListener": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "Ports",
        "desc": "要将监听器创建到哪些端口，每个端口对应一个新的监听器"
      },
      {
        "name": "Protocol",
        "desc": "监听器协议： TCP | UDP | HTTP | HTTPS | TCP_SSL（TCP_SSL 正在内测中，如需使用请通过工单申请）"
      },
      {
        "name": "ListenerNames",
        "desc": "要创建的监听器名称列表，名称与Ports数组按序一一对应，如不需立即命名，则无需提供此参数"
      },
      {
        "name": "HealthCheck",
        "desc": "健康检查相关参数，此参数仅适用于TCP/UDP/TCP_SSL监听器"
      },
      {
        "name": "Certificate",
        "desc": "证书相关信息，此参数仅适用于HTTPS/TCP_SSL监听器"
      },
      {
        "name": "SessionExpireTime",
        "desc": "会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。"
      },
      {
        "name": "Scheduler",
        "desc": "监听器转发的方式。可选值：WRR、LEAST_CONN\n分别表示按权重轮询、最小连接数， 默认为 WRR。此参数仅适用于TCP/UDP/TCP_SSL监听器。"
      },
      {
        "name": "SniSwitch",
        "desc": "是否开启SNI特性，此参数仅适用于HTTPS监听器。"
      }
    ],
    "desc": "在一个负载均衡实例下创建监听器。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "ModifyTargetWeight": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerId",
        "desc": "负载均衡监听器 ID"
      },
      {
        "name": "Weight",
        "desc": "后端云服务器新的转发权重，取值范围：0~100。"
      },
      {
        "name": "LocationId",
        "desc": "转发规则的ID，当绑定机器到七层转发规则时，必须提供此参数或Domain+Url两者之一"
      },
      {
        "name": "Domain",
        "desc": "目标规则的域名，提供LocationId参数时本参数不生效"
      },
      {
        "name": "Url",
        "desc": "目标规则的URL，提供LocationId参数时本参数不生效"
      },
      {
        "name": "Targets",
        "desc": "要修改权重的后端机器列表"
      }
    ],
    "desc": "ModifyTargetWeight 接口用于修改监听器绑定的后端机器的转发权重。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "DescribeTaskStatus": {
    "params": [
      {
        "name": "TaskId",
        "desc": "请求ID，即接口返回的RequestId"
      }
    ],
    "desc": "本接口用于查询异步执行任务的状态，对于非查询类的接口（创建/删除负载均衡实例、监听器、规则以及绑定或解绑后端机器等），在调用成功后都需要使用本接口查询任务是否最终执行成功。"
  },
  "ModifyRule": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerId",
        "desc": "应用型负载均衡监听器 ID"
      },
      {
        "name": "LocationId",
        "desc": "要修改的转发规则的 ID。"
      },
      {
        "name": "Url",
        "desc": "转发规则的新的转发路径，如不需修改Url，则不需提供此参数"
      },
      {
        "name": "HealthCheck",
        "desc": "健康检查信息"
      },
      {
        "name": "Scheduler",
        "desc": "规则的请求转发方式"
      },
      {
        "name": "SessionExpireTime",
        "desc": "会话保持时间"
      }
    ],
    "desc": "ModifyRule 接口用来修改应用型负载均衡七层监听器下的转发规则的各项属性，包括转发路径、健康检查属性、转发策略等。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "DescribeTargetHealth": {
    "params": [
      {
        "name": "LoadBalancerIds",
        "desc": "要查询的负载均衡实例 ID列表"
      }
    ],
    "desc": "DescribeTargetHealth 接口用来获取应用型负载均衡后端的健康检查结果。"
  },
  "DescribeTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerIds",
        "desc": "监听器 ID列表"
      },
      {
        "name": "Protocol",
        "desc": "监听器协议类型"
      },
      {
        "name": "Port",
        "desc": "负载均衡监听器端口"
      }
    ],
    "desc": "DescribeTargets 接口用来查询应用型负载均衡实例的某些监听器后端绑定的机器列表。"
  },
  "DescribeRewrite": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID"
      },
      {
        "name": "SourceListenerIds",
        "desc": "负载均衡监听器ID数组"
      },
      {
        "name": "SourceLocationIds",
        "desc": "负载均衡转发规则的ID数组"
      }
    ],
    "desc": "DescribeRewrite 接口可根据负载均衡实例ID，查询一个负载均衡实例下转发规则的重定向关系。如果不指定监听器ID或转发规则ID，则返回该负载均衡实例下的所有重定向关系。"
  },
  "RegisterTargetsWithClassicalLB": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "Targets",
        "desc": "后端服务信息"
      }
    ],
    "desc": "RegisterTargetsWithClassicalLB用于绑定后端服务到传统型负载均衡"
  },
  "ModifyTargetPort": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerId",
        "desc": "负载均衡监听器 ID"
      },
      {
        "name": "Targets",
        "desc": "要修改端口的后端机器列表"
      },
      {
        "name": "NewPort",
        "desc": "后端机器绑定到监听器的新端口"
      },
      {
        "name": "LocationId",
        "desc": "转发规则的ID"
      },
      {
        "name": "Domain",
        "desc": "目标规则的域名，提供LocationId参数时本参数不生效"
      },
      {
        "name": "Url",
        "desc": "目标规则的URL，提供LocationId参数时本参数不生效"
      }
    ],
    "desc": "ModifyTargetPort接口用于修改监听器绑定的后端云服务器的端口。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "DeregisterTargets": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ListenerId",
        "desc": "监听器 ID"
      },
      {
        "name": "Targets",
        "desc": "要解绑的后端机器列表，数组长度最大支持20"
      },
      {
        "name": "LocationId",
        "desc": "转发规则的ID，当从七层转发规则解绑机器时，必须提供此参数或Domain+Url两者之一"
      },
      {
        "name": "Domain",
        "desc": "目标规则的域名，提供LocationId参数时本参数不生效"
      },
      {
        "name": "Url",
        "desc": "目标规则的URL，提供LocationId参数时本参数不生效"
      }
    ],
    "desc": "DeregisterTargets 接口用来将一台或多台后端机器从应用型负载均衡的监听器上解绑，对于四层监听器（TCP、UDP），只需指定监听器ID即可，对于七层监听器（HTTP、HTTPS），还需通过LocationId或者Domain+Url指定转发规则。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "ModifyLoadBalancerAttributes": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡的唯一ID"
      },
      {
        "name": "LoadBalancerName",
        "desc": "负载均衡实例名称"
      },
      {
        "name": "TargetRegionInfo",
        "desc": "负载均衡绑定的后端服务的地域信息"
      }
    ],
    "desc": "修改负载均衡实例的属性，支持修改负载均衡实例的名称、设置负载均衡的跨域属性。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "DescribeClassicalLBByInstanceId": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "后端实例ID列表"
      }
    ],
    "desc": "DescribeClassicalLBByInstanceId用于通过后端实例ID获取传统型负载均衡ID列表"
  },
  "BatchModifyTargetWeight": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例 ID"
      },
      {
        "name": "ModifyList",
        "desc": "要批量修改权重的列表"
      }
    ],
    "desc": "BatchModifyTargetWeight接口用于批量修改监听器绑定的后端机器的转发权重，当前接口只支持应用型HTTP/HTTPS监听器。\n本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。"
  },
  "DeleteRewrite": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID"
      },
      {
        "name": "SourceListenerId",
        "desc": "源监听器ID"
      },
      {
        "name": "TargetListenerId",
        "desc": "目标监听器ID"
      },
      {
        "name": "RewriteInfos",
        "desc": "转发规则之间的重定向关系"
      }
    ],
    "desc": "DeleteRewrite 接口支持删除指定转发规则之间的重定向关系。"
  },
  "CreateLoadBalancer": {
    "params": [
      {
        "name": "LoadBalancerType",
        "desc": "负载均衡实例的网络类型：\nOPEN：公网属性， INTERNAL：内网属性。"
      },
      {
        "name": "Forward",
        "desc": "负载均衡实例。1：应用型，0：传统型，默认为应用型负载均衡实例。"
      },
      {
        "name": "LoadBalancerName",
        "desc": "负载均衡实例的名称，只用来创建一个的时候生效。规则：1-50 个英文、汉字、数字、连接线“-”或下划线“_”。\n注意：如果名称与系统中已有负载均衡实例的名称重复的话，则系统将会自动生成此次创建的负载均衡实例的名称。"
      },
      {
        "name": "VpcId",
        "desc": "负载均衡后端实例所属网络 ID，可以通过 DescribeVpcEx 接口获取。 不填则默认为基础网络。"
      },
      {
        "name": "SubnetId",
        "desc": "在私有网络内购买内网负载均衡实例的时候需要指定子网 ID，内网负载均衡实例的 VIP 将从这个子网中产生。其他情况不用填写该字段。"
      },
      {
        "name": "ProjectId",
        "desc": "负载均衡实例所属的项目 ID，可以通过 DescribeProject 接口获取。不填则属于默认项目。"
      }
    ],
    "desc": "CreateLoadBalancer 接口用来创建负载均衡实例。为了使用负载均衡服务，您必须要购买一个或者多个负载均衡实例。通过成功调用该接口，会返回负载均衡实例的唯一 ID。用户可以购买的负载均衡实例类型分为：公网（应用型）、内网（应用型）。可以参考产品说明的产品类型。\n本接口成功返回后，可使用查询负载均衡实例列表接口DescribeLoadBalancers查询负载均衡实例的状态，以确定是否创建成功。"
  },
  "ManualRewrite": {
    "params": [
      {
        "name": "LoadBalancerId",
        "desc": "负载均衡实例ID"
      },
      {
        "name": "SourceListenerId",
        "desc": "源监听器ID"
      },
      {
        "name": "TargetListenerId",
        "desc": "目标监听器ID"
      },
      {
        "name": "RewriteInfos",
        "desc": "转发规则之间的重定向关系"
      }
    ],
    "desc": "用户手动配置原访问地址和重定向地址，系统自动将原访问地址的请求重定向至对应路径的目的地址。同一域名下可以配置多条路径作为重定向策略，实现http/https之间请求的自动跳转。"
  }
}