# -*- coding: utf-8 -*-
DESC = "bmvpc-2018-06-25"
INFO = {
  "DownloadCustomerGatewayConfiguration": {
    "params": [
      {
        "name": "VpnConnectionId",
        "desc": "VPN通道实例ID。形如：bmvpnx-f49l6u0z。"
      },
      {
        "name": "VendorName",
        "desc": "厂商,取值 h3c，cisco"
      }
    ],
    "desc": "本接口(DownloadCustomerGatewayConfiguration)用于下载VPN通道配置。"
  },
  "DescribeCustomerGateways": {
    "params": [
      {
        "name": "CustomerGatewayIds",
        "desc": "对端网关ID，例如：bmcgw-2wqq41m9。每次请求的实例的上限为100。参数不支持同时指定CustomerGatewayIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定CustomerGatewayIds和Filters。\n<li>customergateway-name - String - （过滤条件）对端网关名称。</li>\n<li>ip-address - String - （过滤条件)对端网关地址。</li>\n<li>customergateway-id - String - （过滤条件）对端网关唯一ID。</li>\n<li>zone - String - （过滤条件）对端所在可用区，形如：ap-guangzhou-2。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      },
      {
        "name": "OrderField",
        "desc": "排序字段, 支持\"CreateTime\"排序"
      },
      {
        "name": "OrderDirection",
        "desc": "排序方向, “asc”、“desc”"
      }
    ],
    "desc": "本接口（DescribeCustomerGateways）用于查询对端网关列表。"
  },
  "CreateVpcPeerConnection": {
    "params": [
      {
        "name": "VpcId",
        "desc": "本端VPC唯一ID"
      },
      {
        "name": "PeerVpcId",
        "desc": "对端VPC唯一ID"
      },
      {
        "name": "PeerRegion",
        "desc": "对端地域，取值范围为gz,sh,bj,hk,cd,de,sh_bm,gz_bm,bj_bm,cq_bm等"
      },
      {
        "name": "VpcPeerConnectionName",
        "desc": "对等连接名称"
      },
      {
        "name": "PeerUin",
        "desc": "对端账户OwnerUin（默认值为本端账户）"
      },
      {
        "name": "Bandwidth",
        "desc": "跨地域必传，带宽上限值"
      }
    ],
    "desc": "创建对等连接"
  },
  "AsyncRegisterIps": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私有网络的唯一ID。"
      },
      {
        "name": "SubnetId",
        "desc": "子网唯一ID。"
      },
      {
        "name": "Ips",
        "desc": "需要注册的IP列表。"
      }
    ],
    "desc": "批量注册虚拟IP，异步接口。通过接口来查询任务进度。每次请求最多注册256个IP"
  },
  "DescribeRouteTables": {
    "params": [
      {
        "name": "RouteTableIds",
        "desc": "路由表实例ID，例如：rtb-azd4dt1c。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定RouteTableIds和Filters。\nroute-table-id - String - （过滤条件）路由表实例ID。\nroute-table-name - String - （过滤条件）路由表名称。\nroute-table-id-like - String - （模糊过滤条件）路由表实例ID。\nroute-table-name-like - String - （模糊过滤条件）路由表名称。\nvpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。\nzone - String - （过滤条件）可用区。"
      },
      {
        "name": "Offset",
        "desc": "初始行的偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "每页行数，默认为20。"
      },
      {
        "name": "OrderField",
        "desc": "排序字段, 支持按“RouteTableId”，“VpcId”, \"RouteTableName\", \"CreateTime\""
      },
      {
        "name": "OrderDirection",
        "desc": "排序方向, “asc”、“desc”"
      }
    ],
    "desc": "本接口（DescribeRouteTables）用于查询路由表。"
  },
  "DeleteHostedInterfaces": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "物理机ID"
      },
      {
        "name": "SubnetIds",
        "desc": "物理机ID"
      }
    ],
    "desc": "托管机器移除子网批量接口，传入一台托管机器和多个子网，批量移除这些子网。异步接口，接口返回TaskId。"
  },
  "UnbindEipsFromNatGateway": {
    "params": [
      {
        "name": "NatId",
        "desc": "NAT网关ID，例如：nat-kdm476mp"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，例如：vpc-kd7d06of"
      },
      {
        "name": "AssignedEips",
        "desc": "已分配的EIP列表"
      }
    ],
    "desc": "NAT网关解绑该EIP后，NAT网关将不会使用该EIP作为访问外网的源IP地址\n"
  },
  "BindEipsToNatGateway": {
    "params": [
      {
        "name": "NatId",
        "desc": "NAT网关ID，例如：nat-kdm476mp"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，例如：vpc-kd7d06of"
      },
      {
        "name": "AssignedEips",
        "desc": "已分配的EIP列表；AssignedEips和AutoAllocEipNum至少输入一个"
      },
      {
        "name": "AutoAllocEipNum",
        "desc": "新建EIP数目，系统将会按您的要求生产该数目个数EIP；AssignedEips和AutoAllocEipNum至少输入一个"
      }
    ],
    "desc": "NAT网关绑定EIP接口，可将EIP绑定到NAT网关，该EIP作为访问外网的源IP地址，将流量发送到Internet"
  },
  "ModifyVpcPeerConnection": {
    "params": [
      {
        "name": "VpcPeerConnectionId",
        "desc": "黑石对等连接唯一ID"
      },
      {
        "name": "Bandwidth",
        "desc": "对等连接带宽"
      },
      {
        "name": "VpcPeerConnectionName",
        "desc": "对等连接名称"
      }
    ],
    "desc": "修改黑石对等连接"
  },
  "CreateVpc": {
    "params": [
      {
        "name": "VpcName",
        "desc": "私有网络的名称"
      },
      {
        "name": "CidrBlock",
        "desc": "私有网络的CIDR"
      },
      {
        "name": "Zone",
        "desc": "私有网络的可用区"
      },
      {
        "name": "SubnetSet",
        "desc": "子网信息"
      },
      {
        "name": "EnableMonitoring",
        "desc": "是否启用内网监控"
      }
    ],
    "desc": "创建黑石私有网络"
  },
  "CreateNatGateway": {
    "params": [
      {
        "name": "ForwardMode",
        "desc": "转发模式，其中0表示IP方式，1表示网段方式；通过cidr方式可支持更多的IP接入到NAT网关"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，例如：vpc-kd7d06of"
      },
      {
        "name": "NatName",
        "desc": "NAT名称"
      },
      {
        "name": "MaxConcurrent",
        "desc": "并发连接数规格；取值为1000000、3000000、10000000，分别对应小型、中型、大型NAT网关"
      },
      {
        "name": "SubnetIds",
        "desc": "子网ID列表，子网下全部IP将加入NAT，不区分网关转发方式"
      },
      {
        "name": "IpInfoSet",
        "desc": "部分IP信息，子网下只有该部分IP将加入NAT，仅当网关转发模式为IP方式有效；IpInfoSet和SubnetIds中的子网ID不能同时存在"
      },
      {
        "name": "AssignedEips",
        "desc": "已分配的EIP列表, AssignedEips和AutoAllocEipNum至少输入一个"
      },
      {
        "name": "AutoAllocEipNum",
        "desc": "新建EIP数目，系统将会按您的要求生产该数目个数EIP, AssignedEips和AutoAllocEipNum至少输入一个"
      },
      {
        "name": "Exclusive",
        "desc": "独占标识，取值为0和1，默认值为0；0和1分别表示创建共享型NAT网关和独占NAT型网关；由于同一个VPC网络内，指向NAT集群的默认路由只有一条，因此VPC内只能创建一种类型NAT网关；创建独占型NAT网关时，需联系对应架构师进行独占NAT集群搭建，否则无法创建独占型NAT网关。"
      }
    ],
    "desc": "创建NAT网关接口，可针对网段方式、子网全部IP、子网部分IP这三种方式创建NAT网关"
  },
  "DeleteVpnGateway": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID。"
      }
    ],
    "desc": "本接口（DeleteVpnGateway）用于删除VPN网关。"
  },
  "DescribeRoutePolicies": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表实例ID，例如：rtb-afg8md3c。"
      },
      {
        "name": "RoutePolicyIds",
        "desc": "路由策略实例ID，例如：rti-azd4dt1c。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定RoutePolicyIds和Filters。\nroute-table-id - String - （过滤条件）路由表实例ID。\nvpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。\nroute-policy-id - String - （过滤条件）路由策略ID。\nroute-policy-description-like - String -（过滤条件）路由项备注。\nroute-policy-type - String - （过滤条件）路由项策略类型。\ndestination-cidr-like - String - （过滤条件）路由项目的地址。\ngateway-id-like - String - （过滤条件）路由项下一跳网关。\ngateway-type - String - （过滤条件）路由项下一条网关类型。\nenable - Bool - （过滤条件）路由策略是否启用。"
      },
      {
        "name": "Offset",
        "desc": "初始行的偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "每页行数，默认为20。"
      }
    ],
    "desc": "本接口（DescribeRoutePolicies）用于查询路由表条目。"
  },
  "DeleteVpc": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      }
    ],
    "desc": "本接口(DeleteVpc)用于删除黑石私有网络(VPC)。\n\n删除私有网络前，请清理该私有网络下所有资源，包括子网、负载均衡、弹性 IP、对等连接、NAT 网关、专线通道、SSLVPN 等资源。"
  },
  "DeleteHostedInterface": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "托管机器唯一ID 数组"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID或者私有网络统一ID，建议使用统一ID"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID或者子网统一ID，建议使用统一ID"
      }
    ],
    "desc": "本接口用于托管机器从VLANID不为5的子网中移除。\n1) 不能从vlanId 为5的子网中移除。\n2) 每次调用最多能支持传入10台物理机。"
  },
  "DeregisterIps": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私有网络ID"
      },
      {
        "name": "IpSet",
        "desc": "注销指定IP的列表"
      },
      {
        "name": "SubnetId",
        "desc": "私有网络子网ID"
      }
    ],
    "desc": "注销私有网络IP为空闲"
  },
  "ModifyRoutePolicy": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表ID"
      },
      {
        "name": "RoutePolicy",
        "desc": "修改的路由"
      }
    ],
    "desc": "修改自定义路由"
  },
  "CreateInterfaces": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "物理机实例ID列表"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID"
      }
    ],
    "desc": "物理机加入子网"
  },
  "ModifyCustomerGatewayAttribute": {
    "params": [
      {
        "name": "CustomerGatewayId",
        "desc": "对端网关ID，例如：bmcgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。"
      },
      {
        "name": "CustomerGatewayName",
        "desc": "对端网关名称，可任意命名，但不得超过60个字符。"
      }
    ],
    "desc": "本接口（ModifyCustomerGatewayAttribute）用于修改对端网关信息。"
  },
  "DeleteRoutePolicy": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表ID"
      },
      {
        "name": "RoutePolicyId",
        "desc": "路由表策略ID"
      }
    ],
    "desc": "删除黑石路由表路由规则"
  },
  "CreateVirtualSubnetWithVlan": {
    "params": [
      {
        "name": "VpcId",
        "desc": "系统分配的私有网络ID，例如：vpc-kd7d06of"
      },
      {
        "name": "SubnetSet",
        "desc": "子网信息"
      }
    ],
    "desc": "创建黑石虚拟子网， 虚拟子网用于在黑石上创建虚拟网络，与黑石子网要做好规划。虚拟子网会分配2000-2999的VlanId。"
  },
  "ModifyVpnConnectionAttribute": {
    "params": [
      {
        "name": "VpnConnectionId",
        "desc": "VPN通道实例ID。形如：bmvpnx-f49l6u0z。"
      },
      {
        "name": "VpcId",
        "desc": "VPC实例ID"
      },
      {
        "name": "VpnConnectionName",
        "desc": "VPN通道名称，可任意命名，但不得超过60个字符。"
      },
      {
        "name": "PreShareKey",
        "desc": "预共享密钥。"
      },
      {
        "name": "SecurityPolicyDatabases",
        "desc": "SPD策略组，例如：{\"10.0.0.5/24\":[\"172.123.10.5/16\"]}，10.0.0.5/24是vpc内网段172.123.10.5/16是IDC网段。用户指定VPC内哪些网段可以和您IDC中哪些网段通信。"
      },
      {
        "name": "IKEOptionsSpecification",
        "desc": "IKE配置（Internet Key Exchange，因特网密钥交换），IKE具有一套自我保护机制，用户配置网络安全协议。"
      },
      {
        "name": "IPSECOptionsSpecification",
        "desc": "IPSec配置，腾讯云提供IPSec安全会话设置。"
      }
    ],
    "desc": "本接口（ModifyVpnConnectionAttribute）用于修改VPN通道。"
  },
  "DeleteVpnConnection": {
    "params": [
      {
        "name": "VpnConnectionId",
        "desc": "VPN通道实例ID。形如：bmvpnx-f49l6u0z。"
      }
    ],
    "desc": "本接口(DeleteVpnConnection)用于删除VPN通道。"
  },
  "DescribeSubnetAvailableIps": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "私有网络子网ID"
      },
      {
        "name": "Cidr",
        "desc": "CIDR前缀，例如10.0.1"
      }
    ],
    "desc": "获取子网内可用IP列表"
  },
  "DescribeVpcs": {
    "params": [
      {
        "name": "VpcIds",
        "desc": "VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定VpcIds和Filters。\nvpc-name - String - （过滤条件）VPC实例名称。\nvpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。\ncidr-block - String - （过滤条件）vpc的cidr。\nstate - String - （过滤条件）VPC状态。(pending | available).\nzone -  String - （过滤条件）VPC的可用区。"
      },
      {
        "name": "Offset",
        "desc": "初始行的偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "每页行数，默认为20。"
      }
    ],
    "desc": "本接口（DescribeVpcs）用于查询私有网络列表。\n本接口不传参数时，返回默认排序下的前20条VPC信息。"
  },
  "UnbindIpsFromNatGateway": {
    "params": [
      {
        "name": "NatId",
        "desc": "NAT网关ID，例如：nat-kdm476mp"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，例如：vpc-kd7d06of"
      },
      {
        "name": "IpInfoSet",
        "desc": "部分IP信息；子网须以部分IP将加入NAT网关"
      }
    ],
    "desc": "NAT网关解绑IP接口，可将子网的部分IP从NAT网关中解绑"
  },
  "ModifyVpnGatewayAttribute": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID。"
      },
      {
        "name": "VpnGatewayName",
        "desc": "VPN网关名称，最大长度不能超过60个字节。"
      }
    ],
    "desc": "本接口（ModifyVpnGatewayAttribute）用于修改VPN网关属性。"
  },
  "DeleteSubnet": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私有网络ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "SubnetId",
        "desc": "子网实例ID。可通过DescribeSubnets接口返回值中的SubnetId获取。"
      }
    ],
    "desc": "本接口（DeleteSubnet）用于删除黑石私有网络子网。\n删除子网前，请清理该子网下所有资源，包括物理机、负载均衡、黑石数据库、弹性IP、NAT网关等资源"
  },
  "DescribeNatSubnets": {
    "params": [
      {
        "name": "NatId",
        "desc": "NAT网关ID，例如：nat-kdm476mp"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，例如：vpc-kd7d06of"
      }
    ],
    "desc": "可获取NAT网关绑定的子网信息"
  },
  "RejectVpcPeerConnection": {
    "params": [
      {
        "name": "VpcPeerConnectionId",
        "desc": "黑石对等连接实例ID"
      }
    ],
    "desc": "拒绝黑石对等连接申请"
  },
  "DescribeSubnets": {
    "params": [
      {
        "name": "SubnetIds",
        "desc": "子网实例ID查询。形如：subnet-pxir56ns。参数不支持同时指定SubnetIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定SubnetIds和Filters。\nsubnet-id - String - （过滤条件）Subnet实例名称。\nvpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。\ncidr-block - String - （过滤条件）vpc的cidr。\nsubnet-name - String - （过滤条件）子网名称。\nzone - String - （过滤条件）可用区。"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      },
      {
        "name": "OrderField",
        "desc": "排序字段, 支持按“CreateTime”，“VlanId”"
      },
      {
        "name": "OrderDirection",
        "desc": "排序方向, “asc”、“desc”"
      }
    ],
    "desc": "本接口（DescribeSubnets）用于查询黑石子网列表。"
  },
  "CreateCustomerGateway": {
    "params": [
      {
        "name": "CustomerGatewayName",
        "desc": "对端网关名称，可任意命名，但不得超过60个字符。"
      },
      {
        "name": "IpAddress",
        "desc": "对端网关公网IP。"
      },
      {
        "name": "Zone",
        "desc": "可用区ID"
      }
    ],
    "desc": "本接口（CreateCustomerGateway）用于创建对端网关。"
  },
  "DeleteNatGateway": {
    "params": [
      {
        "name": "NatId",
        "desc": "NAT网关ID，例如：nat-kdm476mp"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，例如：vpc-kd7d06of"
      }
    ],
    "desc": "删除NAT网关"
  },
  "ModifySubnetDHCPRelay": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私有网络ID"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID"
      },
      {
        "name": "EnableDHCP",
        "desc": "是否开启DHCP Relay"
      },
      {
        "name": "ServerIps",
        "desc": "DHCP服务器IP"
      },
      {
        "name": "ReservedIpCount",
        "desc": "预留IP个数"
      }
    ],
    "desc": "修改子网DHCP Relay属性"
  },
  "DescribeVpcView": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私有网络唯一ID"
      }
    ],
    "desc": "本接口（DescribeVpcView）用于查询VPC网络拓扑视图。"
  },
  "DeleteVirtualIp": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私有网络唯一ID。"
      },
      {
        "name": "Ips",
        "desc": "退还的IP列表。"
      }
    ],
    "desc": "退还虚拟IP。此接口只能退还虚拟IP，物理机IP不能退还。"
  },
  "DescribeSubnetByDevice": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "物理机ID"
      },
      {
        "name": "Types",
        "desc": "子网类型。0: 物理机子网; 7: DOCKER子网 8: 虚拟子网"
      },
      {
        "name": "Offset",
        "desc": "查询的起始位置。"
      },
      {
        "name": "Limit",
        "desc": "查询的个数。"
      }
    ],
    "desc": "物理机可以加入物理机子网，虚拟子网，DOCKER子网，通过此接口可以查询物理机加入的子网。"
  },
  "DescribeTaskStatus": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID"
      }
    ],
    "desc": "根据任务ID，获取任务的执行状态"
  },
  "AcceptVpcPeerConnection": {
    "params": [
      {
        "name": "VpcPeerConnectionId",
        "desc": "黑石对等连接实例ID"
      }
    ],
    "desc": "接受黑石对等连接"
  },
  "UpgradeNatGateway": {
    "params": [
      {
        "name": "NatId",
        "desc": "NAT网关ID，例如：nat-kdm476mp"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，例如：vpc-kd7d06of"
      },
      {
        "name": "MaxConcurrent",
        "desc": "并发连接数规格；取值为1000000、3000000、10000000，分别对应小型、中型、大型NAT网关"
      }
    ],
    "desc": "升级NAT网关接口，可NAT网关修改为小型NAT网关、中型NAT网关、以及大型NAT网关\n"
  },
  "DeleteCustomerGateway": {
    "params": [
      {
        "name": "CustomerGatewayId",
        "desc": "对端网关ID，例如：bmcgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。"
      }
    ],
    "desc": "本接口（DeleteCustomerGateway）用于删除对端网关。"
  },
  "CreateRoutePolicies": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表ID"
      },
      {
        "name": "RoutePolicySet",
        "desc": "新增的路由"
      }
    ],
    "desc": "创建黑石路由表的路由规则"
  },
  "ModifyRouteTable": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表ID"
      },
      {
        "name": "RouteTableName",
        "desc": "路由表名称"
      }
    ],
    "desc": "修改路由表"
  },
  "UnbindSubnetsFromNatGateway": {
    "params": [
      {
        "name": "NatId",
        "desc": "NAT网关ID，例如：nat-kdm476mp"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，例如：vpc-kd7d06of"
      },
      {
        "name": "SubnetIds",
        "desc": "子网ID列表，子网不区分加入NAT网关的转发方式"
      }
    ],
    "desc": "NAT网关解绑子网接口，可将子网解绑NAT网关"
  },
  "ResetVpnConnection": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC唯一ID"
      },
      {
        "name": "VpnConnectionId",
        "desc": "VPN通道实例ID。形如：bmvpnx-f49l6u0z。"
      }
    ],
    "desc": "本接口(ResetVpnConnection)用于重置VPN通道。"
  },
  "DescribeVpnGateways": {
    "params": [
      {
        "name": "VpnGatewayIds",
        "desc": "VPN网关实例ID。形如：bmvpngw-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpnGatewayIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定VpnGatewayIds和Filters。\n<li>vpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。</li>\n<li>state - String - （过滤条件 VPN状态：creating，available，createfailed，changing，changefailed，deleting，deletefailed。</li>\n<li>zone - String - （过滤条件）VPN所在可用区，形如：ap-guangzhou-2。</li>\n<li>vpngw-name - String - （过滤条件）vpn网关名称。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "请求对象个数"
      },
      {
        "name": "OrderField",
        "desc": "排序字段, 支持\"CreateTime\"排序"
      },
      {
        "name": "OrderDirection",
        "desc": "排序方向, “asc”、“desc”"
      }
    ],
    "desc": "本接口（DescribeVpnGateways）用于查询VPN网关列表。"
  },
  "ModifySubnetAttribute": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私有网络ID"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID"
      },
      {
        "name": "SubnetName",
        "desc": "子网名称"
      }
    ],
    "desc": "修改子网属性"
  },
  "CreateDockerSubnetWithVlan": {
    "params": [
      {
        "name": "VpcId",
        "desc": "系统分配的私有网络ID，例如：vpc-kd7d06of"
      },
      {
        "name": "SubnetSet",
        "desc": "子网信息"
      }
    ],
    "desc": "创建黑石Docker子网， 如果不指定VlanId，将会分配2000--2999范围的VlanId; 子网会关闭分布式网关"
  },
  "DescribeNatGateways": {
    "params": [
      {
        "name": "NatId",
        "desc": "NAT网关ID，例如：nat-kdm476mp"
      },
      {
        "name": "NatName",
        "desc": "NAT名称"
      },
      {
        "name": "SearchKey",
        "desc": "搜索字段"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，例如：vpc-kd7d06of"
      },
      {
        "name": "Offset",
        "desc": "起始值"
      },
      {
        "name": "Limit",
        "desc": "偏移值，默认值为 20"
      },
      {
        "name": "Zone",
        "desc": "NAT所在可用区，形如：ap-guangzhou-2。"
      },
      {
        "name": "OrderField",
        "desc": "排序字段, 支持\"CreateTime\"排序"
      },
      {
        "name": "OrderDirection",
        "desc": "排序方向, “asc”、“desc”"
      }
    ],
    "desc": "获取NAT网关信息，包括NAT网关 ID、网关名称、私有网络、网关并发连接上限、绑定EIP列表等"
  },
  "BindSubnetsToNatGateway": {
    "params": [
      {
        "name": "NatId",
        "desc": "NAT网关ID，例如：nat-kdm476mp"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，例如：vpc-kd7d06of"
      },
      {
        "name": "SubnetIds",
        "desc": "子网ID列表，子网下全部IP将加入NAT，不区分网关转发方式"
      }
    ],
    "desc": "NAT网关绑定子网后，该子网内全部IP可出公网"
  },
  "DescribeVpcQuota": {
    "params": [
      {
        "name": "TypeIds",
        "desc": "类型"
      }
    ],
    "desc": "本接口（DescribeVpcQuota）用于查询用户VPC相关配额限制。"
  },
  "CreateHostedInterface": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "托管机器唯一ID 数组"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID或者私有网络统一ID，建议使用统一ID"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID或者子网统一ID，建议使用统一ID"
      }
    ],
    "desc": "本接口（CreateHostedInterface）用于黑石托管机器加入带VLANID不为5的子网。\n\n1) 不能加入vlanId 为5的子网，只能加入VLANID范围为2000-2999的子网。\n2) 每台托管机器最多可以加入20个子网。\n3) 每次调用最多能支持传入10台托管机器。"
  },
  "DescribeSubnetByHostedDevice": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "托管机器ID, 如chm-xasdfx2j"
      },
      {
        "name": "Types",
        "desc": "子网类型。0: 物理机子网; 7: DOCKER子网 8: 虚拟子网"
      },
      {
        "name": "Offset",
        "desc": "查询的起始位置。"
      },
      {
        "name": "Limit",
        "desc": "查询的个数。"
      }
    ],
    "desc": "托管可以加入物理机子网，虚拟子网，DOCKER子网，通过此接口可以查询托管加入的子网。"
  },
  "DescribeVpcPeerConnections": {
    "params": [
      {
        "name": "VpcPeerConnectionIds",
        "desc": "对等连接实例ID"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定VpcPeerConnectionIds和Filters。\n过滤条件，参数不支持同时指定VpcPeerConnectionIds和Filters。\n<li>peer-name - String - （过滤条件）对等连接名称。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID"
      }
    ],
    "desc": "获取对等连接列表"
  },
  "DescribeVpcResource": {
    "params": [
      {
        "name": "VpcIds",
        "desc": "私有网络实例ID"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定SubnetIds和Filters。\nvpc-id - String - （过滤条件）私有网络实例ID，形如：vpc-f49l6u0z。\nvpc-name - String - （过滤条件）私有网络名称。\nzone - String - （过滤条件）可用区。\nstate - String - （过滤条件）VPC状态。available: 运营中; pending: 创建中; failed: 创建失败; deleting: 删除中"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      },
      {
        "name": "OrderField",
        "desc": "排序字段"
      },
      {
        "name": "OrderDirection",
        "desc": "排序方向, “asc”、“desc”"
      }
    ],
    "desc": "查询黑石私有网络关联资源"
  },
  "DeleteVpcPeerConnection": {
    "params": [
      {
        "name": "VpcPeerConnectionId",
        "desc": "黑石对等连接实例ID"
      }
    ],
    "desc": "删除黑石对等连接"
  },
  "DeleteInterfaces": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "物理机ID"
      },
      {
        "name": "SubnetIds",
        "desc": "子网的唯一ID列表"
      }
    ],
    "desc": "物理机移除子网批量接口，传入一台物理机和多个子网，批量移除这些子网。异步接口，接口返回TaskId。"
  },
  "ModifyVpcAttribute": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私有网络ID"
      },
      {
        "name": "VpcName",
        "desc": "私有网络名称"
      },
      {
        "name": "EnableMonitor",
        "desc": "是否开启内网监控，0为关闭，1为开启"
      }
    ],
    "desc": "本接口（ModifyVpcAttribute）用于修改VPC的标识名称和控制VPC的监控起停。"
  },
  "BindIpsToNatGateway": {
    "params": [
      {
        "name": "NatId",
        "desc": "NAT网关ID，例如：nat-kdm476mp"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，例如：vpc-kd7d06of"
      },
      {
        "name": "IpInfoSet",
        "desc": "部分IP信息，子网下只有该部分IP将加入NAT，仅当网关转发模式为IP方式有效"
      }
    ],
    "desc": "可用于将子网的部分IP绑定到NAT网关"
  },
  "DescribeVpnConnections": {
    "params": [
      {
        "name": "VpnConnectionIds",
        "desc": "VPN通道实例ID。形如：bmvpnx-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpnConnectionIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定VpnConnectionIds和Filters。\n<li>vpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。</li>\n<li>state - String - （过滤条件 VPN状态：creating，available，createfailed，changing，changefailed，deleting，deletefailed。</li>\n<li>zone - String - （过滤条件）VPN所在可用区，形如：ap-guangzhou-2。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      },
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID"
      },
      {
        "name": "VpnConnectionName",
        "desc": "VPN通道名称"
      },
      {
        "name": "OrderField",
        "desc": "排序字段, 支持\"CreateTime\"排序"
      },
      {
        "name": "OrderDirection",
        "desc": "排序方向, “asc”、“desc”"
      }
    ],
    "desc": " 本接口（DescribeVpnConnections）查询VPN通道列表。"
  },
  "CreateSubnet": {
    "params": [
      {
        "name": "VpcId",
        "desc": "系统分配的私有网络ID，例如：vpc-kd7d06of"
      },
      {
        "name": "SubnetSet",
        "desc": "子网信息"
      }
    ],
    "desc": "创建黑石私有网络的子网\n访问管理: 用户可以对VpcId进行授权操作。例如设置资源为[\"qcs::bmvpc:::unVpc/vpc-xxxxx\"]"
  }
}