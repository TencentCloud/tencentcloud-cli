# -*- coding: utf-8 -*-
DESC = "vpc-2017-03-12"
INFO = {
  "DescribeVpcResourceDashboard": {
    "params": [
      {
        "name": "VpcIds",
        "desc": "Vpc实例ID，例如：vpc-f1xjkw1b。"
      }
    ],
    "desc": "本接口(DescribeVpcResourceDashboard)用于查看VPC资源信息。"
  },
  "CreateDefaultSecurityGroup": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID，默认0。可在qcloud控制台项目管理页面查询到。"
      }
    ],
    "desc": "本接口（CreateDefaultSecurityGroup）用于创建（如果项目下未存在默认安全组，则创建；已存在则获取。）默认安全组（SecurityGroup）。\n* 每个账户下每个地域的每个项目的<a href=\"https://cloud.tencent.com/document/product/213/12453\">安全组数量限制</a>。\n* 新建的安全组的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用CreateSecurityGroupPolicies将安全组的规则设置为需要的规则。\n* 创建安全组同时可以绑定标签, 应答里的标签列表代表添加成功的标签。"
  },
  "DescribeCustomerGateways": {
    "params": [
      {
        "name": "CustomerGatewayIds",
        "desc": "对端网关ID，例如：cgw-2wqq41m9。每次请求的实例的上限为100。参数不支持同时指定CustomerGatewayIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定CustomerGatewayIds和Filters。\n<li>customer-gateway-id - String - （过滤条件）用户网关唯一ID形如：`cgw-mgp33pll`。</li>\n<li>customer-gateway-name - String - （过滤条件）用户网关名称形如：`test-cgw`。</li>\n<li>ip-address - String - （过滤条件）公网地址形如：`58.211.1.12`。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeCustomerGateways）用于查询对端网关列表。"
  },
  "ReplaceSecurityGroupPolicy": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。"
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "安全组规则集合对象。"
      }
    ],
    "desc": "本接口（ReplaceSecurityGroupPolicy）用于替换单条安全组规则（SecurityGroupPolicy）。\n单个请求中只能替换单个方向的一条规则, 必须要指定索引（PolicyIndex）。"
  },
  "CreateFlowLog": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私用网络ID或者统一ID，建议使用统一ID"
      },
      {
        "name": "FlowLogName",
        "desc": "流日志实例名字"
      },
      {
        "name": "ResourceType",
        "desc": "流日志所属资源类型，VPC|SUBNET|NETWORKINTERFACE"
      },
      {
        "name": "ResourceId",
        "desc": "资源唯一ID"
      },
      {
        "name": "TrafficType",
        "desc": "流日志采集类型，ACCEPT|REJECT|ALL"
      },
      {
        "name": "CloudLogId",
        "desc": "流日志存储ID"
      },
      {
        "name": "FlowLogDescription",
        "desc": "流日志实例描述"
      }
    ],
    "desc": "本接口（CreateFlowLog）用于创建流日志"
  },
  "ModifyNatGatewayAttribute": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "NAT网关的ID，形如：`nat-df45454`。"
      },
      {
        "name": "NatGatewayName",
        "desc": "NAT网关的名称，形如：`test_nat`。"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "NAT网关最大外网出带宽(单位:Mbps)。"
      }
    ],
    "desc": "本接口（ModifyNatGatewayAttribute）用于修改NAT网关的属性。"
  },
  "DescribeTaskResult": {
    "params": [
      {
        "name": "TaskId",
        "desc": "异步任务ID。TaskId和DealName必填一个参数"
      },
      {
        "name": "DealName",
        "desc": "计费订单号。TaskId和DealName必填一个参数"
      }
    ],
    "desc": "查询EIP异步任务执行结果"
  },
  "CreateNetworkAcl": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "NetworkAclName",
        "desc": "网络ACL名称，最大长度不能超过60个字节。"
      }
    ],
    "desc": "本接口（CreateNetworkAcl）用于创建新的<a href=\"https://cloud.tencent.com/document/product/215/20088\">网络ACL</a>。\n* 新建的网络ACL的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用ModifyNetworkAclEntries将网络ACL的规则设置为需要的规则。"
  },
  "DescribeServiceTemplateGroups": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>service-template-group-name - String - （过滤条件）协议端口模板集合名称。</li>\n<li>service-template-group-id - String - （过滤条件）协议端口模板集合实例ID，例如：ppmg-e6dy460g。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeServiceTemplateGroups）用于查询协议端口模板集合"
  },
  "DescribeRouteTables": {
    "params": [
      {
        "name": "RouteTableIds",
        "desc": "路由表实例ID，例如：rtb-azd4dt1c。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定RouteTableIds和Filters。\n<li>route-table-id - String - （过滤条件）路由表实例ID。</li>\n<li>route-table-name - String - （过滤条件）路由表名称。</li>\n<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>\n<li>association.main - String - （过滤条件）是否主路由表。</li>\n<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。</li>\n<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例2。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量。"
      },
      {
        "name": "Limit",
        "desc": "请求对象个数。"
      }
    ],
    "desc": " 本接口（DescribeRouteTables）用于查询路由表。"
  },
  "CreateBandwidthPackage": {
    "params": [
      {
        "name": "NetworkType",
        "desc": "带宽包类型，包括'BGP'，'SINGLEISP'，'ANYCAST'"
      },
      {
        "name": "ChargeType",
        "desc": "带宽包计费类型，包括‘TOP5_POSTPAID_BY_MONTH’，‘PERCENT95_POSTPAID_BY_MONTH’"
      },
      {
        "name": "BandwidthPackageName",
        "desc": "带宽包名字"
      },
      {
        "name": "BandwidthPackageCount",
        "desc": "带宽包数量(非上移账户只能填1)"
      },
      {
        "name": "InternetMaxBandwidth",
        "desc": "带宽包限速大小。单位：Mbps，-1表示不限速。"
      },
      {
        "name": "Tags",
        "desc": "需要关联的标签列表。"
      },
      {
        "name": "Protocol",
        "desc": "带宽包协议类型。当前支持'ipv4'和'ipv6'协议带宽包，默认值是'ipv4'。"
      }
    ],
    "desc": "接口支持创建[设备带宽包](https://cloud.tencent.com/document/product/684/15246#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85)和[IP带宽包](https://cloud.tencent.com/document/product/684/15246#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85)"
  },
  "DeleteFlowLog": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私用网络ID或者统一ID，建议使用统一ID"
      },
      {
        "name": "FlowLogId",
        "desc": "流日志唯一ID"
      }
    ],
    "desc": "本接口（DeleteFlowLog）用于删除流日志"
  },
  "CreateRouteTable": {
    "params": [
      {
        "name": "VpcId",
        "desc": "待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "RouteTableName",
        "desc": "路由表名称，最大长度不能超过60个字节。"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "本接口(CreateRouteTable)用于创建路由表。\n* 创建了VPC后，系统会创建一个默认路由表，所有新建的子网都会关联到默认路由表。默认情况下您可以直接使用默认路由表来管理您的路由策略。当您的路由策略较多时，您可以调用创建路由表接口创建更多路由表管理您的路由策略。\n* 创建路由表同时可以绑定标签, 应答里的标签列表代表添加成功的标签。"
  },
  "AssignIpv6CidrBlock": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC`实例`ID`，形如：`vpc-f49l6u0z`。"
      }
    ],
    "desc": "本接口（AssignIpv6CidrBlock）用于分配IPv6网段。\n* 使用本接口前，您需要已有VPC实例，如果没有可通过接口<a href=\"https://cloud.tencent.com/document/api/215/15774\" title=\"CreateVpc\" target=\"_blank\">CreateVpc</a>创建。\n* 每个VPC只能申请一个IPv6网段"
  },
  "DeleteNetworkAcl": {
    "params": [
      {
        "name": "NetworkAclId",
        "desc": "网络ACL实例ID。例如：acl-12345678。"
      }
    ],
    "desc": "本接口（DeleteNetworkAcl）用于删除网络ACL。"
  },
  "DescribeNatGatewayDestinationIpPortTranslationNatRules": {
    "params": [
      {
        "name": "NatGatewayIds",
        "desc": "NAT网关ID。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件:\n参数不支持同时指定NatGatewayIds和Filters。\n<li> nat-gateway-id，NAT网关的ID，如`nat-0yi4hekt`</li>\n<li> vpc-id，私有网络VPC的ID，如`vpc-0yi4hekt`</li>\n<li> public-ip-address， 弹性IP，如`139.199.232.238`。</li>\n<li>public-port， 公网端口。</li>\n<li>private-ip-address， 内网IP，如`10.0.0.1`。</li>\n<li>private-port， 内网端口。</li>\n<li>description，规则描述。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeNatGatewayDestinationIpPortTranslationNatRules）用于查询NAT网关端口转发规则对象数组。"
  },
  "ModifyFlowLogAttribute": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私用网络ID或者统一ID，建议使用统一ID"
      },
      {
        "name": "FlowLogId",
        "desc": "流日志唯一ID"
      },
      {
        "name": "FlowLogName",
        "desc": "流日志实例名字"
      },
      {
        "name": "FlowLogDescription",
        "desc": "流日志实例描述"
      }
    ],
    "desc": "本接口（ModifyFlowLogAttribute）用于修改流日志属性"
  },
  "DisassociateNetworkInterfaceSecurityGroups": {
    "params": [
      {
        "name": "NetworkInterfaceIds",
        "desc": "弹性网卡实例ID。形如：eni-pxir56ns。每次请求的实例的上限为100。"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "安全组实例ID，例如：sg-33ocnj9n，可通过DescribeSecurityGroups获取。每次请求的实例的上限为100。"
      }
    ],
    "desc": "本接口（DisassociateNetworkInterfaceSecurityGroups）用于弹性网卡解绑安全组。支持弹性网卡完全解绑安全组。"
  },
  "ModifyAddressInternetChargeType": {
    "params": [
      {
        "name": "AddressId",
        "desc": "弹性公网IP的唯一ID，形如eip-xxx"
      },
      {
        "name": "InternetChargeType",
        "desc": "弹性公网IP调整目标计费模式，只支持\"BANDWIDTH_PREPAID_BY_MONTH\"和\"TRAFFIC_POSTPAID_BY_HOUR\""
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "弹性公网IP调整目标带宽值"
      },
      {
        "name": "AddressChargePrepaid",
        "desc": "包月带宽网络计费模式参数。弹性公网IP的调整目标计费模式是\"BANDWIDTH_PREPAID_BY_MONTH\"时，必传该参数。"
      }
    ],
    "desc": "该接口用于调整具有带宽属性弹性公网IP的网络计费模式\n* 支持BANDWIDTH_PREPAID_BY_MONTH和TRAFFIC_POSTPAID_BY_HOUR两种网络计费模式之间的切换。\n* 每个弹性公网IP支持调整两次，次数超出则无法调整。"
  },
  "DescribeCcnAttachedInstances": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      },
      {
        "name": "Filters",
        "desc": "过滤条件：\n<li>ccn-id - String -（过滤条件）CCN实例ID。</li>\n<li>instance-type - String -（过滤条件）关联实例类型。</li>\n<li>instance-region - String -（过滤条件）关联实例所属地域。</li>\n<li>instance-id - String -（过滤条件）关联实例实例ID。</li>"
      },
      {
        "name": "CcnId",
        "desc": "云联网实例ID"
      },
      {
        "name": "OrderField",
        "desc": "排序字段。支持：`CcnId` `InstanceType` `InstanceId` `InstanceName` `InstanceRegion` `AttachedTime` `State`。"
      },
      {
        "name": "OrderDirection",
        "desc": "排序方法。顺序：`ASC`，倒序：`DESC`。"
      }
    ],
    "desc": "本接口（DescribeCcnAttachedInstances）用于查询云联网实例下已关联的网络实例。"
  },
  "ResetRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表实例ID，例如：rtb-azd4dt1c。"
      },
      {
        "name": "RouteTableName",
        "desc": "路由表名称，最大长度不能超过60个字节。"
      },
      {
        "name": "Routes",
        "desc": "路由策略。"
      }
    ],
    "desc": "本接口（ResetRoutes）用于对某个路由表名称和所有路由策略（Route）进行重新设置。<br />\n注意: 调用本接口是先删除当前路由表中所有路由策略, 再保存新提交的路由策略内容, 会引起网络中断。"
  },
  "DeleteServiceTemplate": {
    "params": [
      {
        "name": "ServiceTemplateId",
        "desc": "协议端口模板实例ID，例如：ppm-e6dy460g。"
      }
    ],
    "desc": "本接口（DeleteServiceTemplate）用于删除协议端口模板"
  },
  "DescribeNetworkInterfaceLimit": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "要查询的CVM实例ID或弹性网卡ID"
      }
    ],
    "desc": "本接口（DescribeNetworkInterfaceLimit）根据CVM实例ID或弹性网卡ID查询弹性网卡配额，返回该CVM实例或弹性网卡能绑定的弹性网卡配额，以及弹性网卡可以分配的IP配额"
  },
  "DescribeNetDetects": {
    "params": [
      {
        "name": "NetDetectIds",
        "desc": "网络探测实例`ID`数组。形如：[`netd-12345678`]"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定NetDetectIds和Filters。\n<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-12345678</li>\n<li>net-detect-id - String - （过滤条件）网络探测实例ID，形如：netd-12345678</li>\n<li>subnet-id - String - （过滤条件）子网实例ID，形如：subnet-12345678</li>\n<li>net-detect-name - String - （过滤条件）网络探测名称</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeNetDetects）用于查询网络探测列表。"
  },
  "ModifyCcnRegionBandwidthLimitsType": {
    "params": [
      {
        "name": "CcnId",
        "desc": "云联网实例ID。"
      },
      {
        "name": "BandwidthLimitType",
        "desc": "云联网限速类型，INTER_REGION_LIMIT：地域间限速，OUTER_REGION_LIMIT：地域出口限速。"
      }
    ],
    "desc": "本接口（ModifyCcnRegionBandwidthLimitsType）用于修改后付费云联网实例修改带宽限速策略。"
  },
  "DescribeGatewayFlowMonitorDetail": {
    "params": [
      {
        "name": "TimePoint",
        "desc": "时间点。表示要查询这分钟内的明细。如：`2019-02-28 18:15:20`，将查询 `18:15` 这一分钟内的明细。"
      },
      {
        "name": "VpnId",
        "desc": "VPN网关实例ID，形如：`vpn-ltjahce6`。"
      },
      {
        "name": "DirectConnectGatewayId",
        "desc": "专线网关实例ID，形如：`dcg-ltjahce6`。"
      },
      {
        "name": "PeeringConnectionId",
        "desc": "对等连接实例ID，形如：`pcx-ltjahce6`。"
      },
      {
        "name": "NatId",
        "desc": "NAT网关实例ID，形如：`nat-ltjahce6`。"
      },
      {
        "name": "Offset",
        "desc": "偏移量。"
      },
      {
        "name": "Limit",
        "desc": "返回数量。"
      },
      {
        "name": "OrderField",
        "desc": "排序字段。支持 `InPkg` `OutPkg` `InTraffic` `OutTraffic`。"
      },
      {
        "name": "OrderDirection",
        "desc": "排序方法。顺序：`ASC`，倒序：`DESC`。"
      }
    ],
    "desc": "本接口（DescribeGatewayFlowMonitorDetail）用于查询网关流量监控明细。\n* 只支持单个网关实例查询。即入参 `VpnId` `DirectConnectGatewayId` `PeeringConnectionId` `NatId` 最多只支持传一个，且必须传一个。\n* 如果网关有流量，但调用本接口没有返回数据，请在控制台对应网关详情页确认是否开启网关流量监控。"
  },
  "EnableGatewayFlowMonitor": {
    "params": [
      {
        "name": "GatewayId",
        "desc": "网关实例ID，目前我们支持的网关实例有，\n专线网关实例ID，形如，`dcg-ltjahce6`；\nNat网关实例ID，形如，`nat-ltjahce6`；\nVPN网关实例ID，形如，`vpn-ltjahce6`。"
      }
    ],
    "desc": "本接口（EnableGatewayFlowMonitor）用于开启网关流量监控。"
  },
  "UnassignIpv6Addresses": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例`ID`，形如：`eni-m6dyj72l`。"
      },
      {
        "name": "Ipv6Addresses",
        "desc": "指定的`IPv6`地址列表，单次最多指定10个。"
      }
    ],
    "desc": "本接口（UnassignIpv6Addresses）用于释放弹性网卡`IPv6`地址。<br />\n本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口。"
  },
  "AssociateDirectConnectGatewayNatGateway": {
    "params": [
      {
        "name": "VpcId",
        "desc": "专线网关ID。"
      },
      {
        "name": "NatGatewayId",
        "desc": "NAT网关ID。"
      },
      {
        "name": "DirectConnectGatewayId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      }
    ],
    "desc": "将专线网关与NAT网关绑定，专线网关默认路由指向NAT网关"
  },
  "DeleteVpnConnection": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID。"
      },
      {
        "name": "VpnConnectionId",
        "desc": "VPN通道实例ID。形如：vpnx-f49l6u0z。"
      }
    ],
    "desc": "本接口(DeleteVpnConnection)用于删除VPN通道。"
  },
  "DeleteAddressTemplateGroup": {
    "params": [
      {
        "name": "AddressTemplateGroupId",
        "desc": "IP地址模板集合实例ID，例如：ipmg-90cex8mq。"
      }
    ],
    "desc": "本接口（DeleteAddressTemplateGroup）用于删除IP地址模板集合"
  },
  "DescribeCustomerGatewayVendors": {
    "params": [],
    "desc": "本接口（DescribeCustomerGatewayVendors）用于查询可支持的对端网关厂商信息。"
  },
  "DescribeAddresses": {
    "params": [
      {
        "name": "AddressIds",
        "desc": "标识 EIP 的唯一 ID 列表。EIP 唯一 ID 形如：`eip-11112222`。参数不支持同时指定`AddressIds`和`Filters`。"
      },
      {
        "name": "Filters",
        "desc": "每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AddressIds`和`Filters`。详细的过滤条件如下：\n<li> address-id - String - 是否必填：否 - （过滤条件）按照 EIP 的唯一 ID 过滤。EIP 唯一 ID 形如：eip-11112222。</li>\n<li> address-name - String - 是否必填：否 - （过滤条件）按照 EIP 名称过滤。不支持模糊过滤。</li>\n<li> address-ip - String - 是否必填：否 - （过滤条件）按照 EIP 的 IP 地址过滤。</li>\n<li> address-status - String - 是否必填：否 - （过滤条件）按照 EIP 的状态过滤。状态包含：'CREATING'，'BINDING'，'BIND'，'UNBINDING'，'UNBIND'，'OFFLINING'，'BIND_ENI'。</li>\n<li> instance-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的实例 ID 过滤。实例 ID 形如：ins-11112222。</li>\n<li> private-ip-address - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的内网 IP 过滤。</li>\n<li> network-interface-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的弹性网卡 ID 过滤。弹性网卡 ID 形如：eni-11112222。</li>\n<li> is-arrears - String - 是否必填：否 - （过滤条件）按照 EIP 是否欠费进行过滤。（TRUE：EIP 处于欠费状态|FALSE：EIP 费用状态正常）</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。"
      }
    ],
    "desc": "本接口 (DescribeAddresses) 用于查询一个或多个[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）的详细信息。\n* 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的 EIP。"
  },
  "DescribeClassicLinkInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>vpc-id - String - （过滤条件）VPC实例ID。</li>\n<li>vm-ip - String - （过滤条件）基础网络云服务器IP。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      }
    ],
    "desc": "本接口(DescribeClassicLinkInstances)用于查询私有网络和基础网络设备互通列表。"
  },
  "DescribeSecurityGroupPolicies": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "安全组实例ID，例如：sg-33ocnj9n，可通过DescribeSecurityGroups获取。"
      }
    ],
    "desc": "本接口（DescribeSecurityGroupPolicies）用于查询安全组规则。"
  },
  "ModifyServiceTemplateAttribute": {
    "params": [
      {
        "name": "ServiceTemplateId",
        "desc": "协议端口模板实例ID，例如：ppm-529nwwj8。"
      },
      {
        "name": "ServiceTemplateName",
        "desc": "协议端口模板名称。"
      },
      {
        "name": "Services",
        "desc": "支持单个端口、多个端口、连续端口及所有端口，协议支持：TCP、UDP、ICMP、GRE 协议。"
      }
    ],
    "desc": "本接口（ModifyServiceTemplateAttribute）用于修改协议端口模板"
  },
  "AssociateNatGatewayAddress": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "NAT网关的ID，形如：`nat-df45454`。"
      },
      {
        "name": "AddressCount",
        "desc": "需要申请的弹性IP个数，系统会按您的要求生产N个弹性IP, 其中AddressCount和PublicAddresses至少传递一个。"
      },
      {
        "name": "PublicIpAddresses",
        "desc": "绑定NAT网关的弹性IP数组，其中AddressCount和PublicAddresses至少传递一个。。"
      },
      {
        "name": "Zone",
        "desc": "弹性IP可以区，自动分配弹性IP时传递。"
      }
    ],
    "desc": "本接口(AssociateNatGatewayAddress)用于NAT网关绑定弹性IP（EIP）。"
  },
  "CreateVpnConnection": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID。"
      },
      {
        "name": "CustomerGatewayId",
        "desc": "对端网关ID，例如：cgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。"
      },
      {
        "name": "VpnConnectionName",
        "desc": "通道名称，可任意命名，但不得超过60个字符。"
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
        "desc": "IKE配置（Internet Key Exchange，因特网密钥交换），IKE具有一套自我保护机制，用户配置网络安全协议"
      },
      {
        "name": "IPSECOptionsSpecification",
        "desc": "IPSec配置，腾讯云提供IPSec安全会话设置"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "本接口（CreateVpnConnection）用于创建VPN通道。"
  },
  "DeleteRouteTable": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表实例ID，例如：rtb-azd4dt1c。"
      }
    ],
    "desc": "删除路由表"
  },
  "RemoveBandwidthPackageResources": {
    "params": [
      {
        "name": "BandwidthPackageId",
        "desc": "带宽包唯一标识ID，形如'bwp-xxxx'"
      },
      {
        "name": "ResourceType",
        "desc": "资源类型，包括‘Address’, ‘LoadBalance’"
      },
      {
        "name": "ResourceIds",
        "desc": "资源ID，可支持资源形如'eip-xxxx', 'lb-xxxx'"
      }
    ],
    "desc": "接口用于删除带宽包资源，包括[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)和[负载均衡](https://cloud.tencent.com/document/product/214/517)等"
  },
  "InquiryPriceRenewVpnGateway": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID。"
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。"
      }
    ],
    "desc": "本接口（InquiryPriceRenewVpnGateway）用于续费VPN网关询价。目前仅支持IPSEC类型网关的询价。"
  },
  "AssignPrivateIpAddresses": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-m6dyj72l。"
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "指定的内网IP信息，单次最多指定10个。与SecondaryPrivateIpAddressCount至少提供一个。"
      },
      {
        "name": "SecondaryPrivateIpAddressCount",
        "desc": "新申请的内网IP地址个数，与PrivateIpAddresses至少提供一个。内网IP地址个数总和不能超过配额数，详见<a href=\"/document/product/576/18527\">弹性网卡使用限制</a>。"
      }
    ],
    "desc": "本接口（AssignPrivateIpAddresses）用于弹性网卡申请内网 IP。\n* 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href=\"/document/product/576/18527\">弹性网卡使用限制</a>。\n* 可以指定内网IP地址申请，内网IP地址类型不能为主IP，主IP已存在，不能修改，内网IP必须要弹性网卡所在子网内，而且不能被占用。\n* 在弹性网卡上申请一个到多个辅助内网IP，接口会在弹性网卡所在子网网段内返回指定数量的辅助内网IP。"
  },
  "CreateAndAttachNetworkInterface": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "NetworkInterfaceName",
        "desc": "弹性网卡名称，最大长度不能超过60个字节。"
      },
      {
        "name": "SubnetId",
        "desc": "弹性网卡所在的子网实例ID，例如：subnet-0ap8nwca。"
      },
      {
        "name": "InstanceId",
        "desc": "云主机实例ID。"
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "指定的内网IP信息，单次最多指定10个。"
      },
      {
        "name": "SecondaryPrivateIpAddressCount",
        "desc": "新申请的内网IP地址个数，内网IP地址个数总和不能超过配数。"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "指定绑定的安全组，例如：['sg-1dd51d']。"
      },
      {
        "name": "NetworkInterfaceDescription",
        "desc": "弹性网卡描述，可任意命名，但不得超过60个字符。"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "本接口（CreateAndAttachNetworkInterface）用于创建弹性网卡并绑定云主机。\n* 创建弹性网卡时可以指定内网IP，并且可以指定一个主IP，指定的内网IP必须在弹性网卡所在子网内，而且不能被占用。\n* 创建弹性网卡时可以指定需要申请的内网IP数量，系统会随机生成内网IP地址。\n* 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href=\"/document/product/576/18527\">弹性网卡使用限制</a>。\n* 创建弹性网卡同时可以绑定已有安全组。\n* 创建弹性网卡同时可以绑定标签, 应答里的标签列表代表添加成功的标签。"
  },
  "DescribeNatGateways": {
    "params": [
      {
        "name": "NatGatewayIds",
        "desc": "NAT网关统一 ID，形如：`nat-123xx454`。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定NatGatewayIds和Filters。\n<li>nat-gateway-id - String - （过滤条件）协议端口模板实例ID，形如：`nat-123xx454`。</li>\n<li>vpc-id - String - （过滤条件）私有网络 唯一ID，形如：`vpc-123xx454`。</li>\n<li>nat-gateway-name - String - （过滤条件）协议端口模板实例ID，形如：`test_nat`。</li>\n<li>tag-key - String - （过滤条件）标签键，形如：`test-key`。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeNatGateways）用于查询 NAT 网关。"
  },
  "CreateSubnets": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC`实例`ID`。形如：`vpc-6v2ht8q5`"
      },
      {
        "name": "Subnets",
        "desc": "子网对象列表。"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，注意这里的标签集合为列表中所有子网对象所共享，不能为每个子网对象单独指定标签，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "本接口(CreateSubnets)用于批量创建子网。\n* 创建子网前必须创建好 VPC。\n* 子网创建成功后，子网网段不能修改。子网网段必须在VPC网段内，可以和VPC网段相同（VPC有且只有一个子网时），建议子网网段在VPC网段内，预留网段给其他子网使用。\n* 您可以创建的最小网段子网掩码为28（有16个IP地址），最大网段子网掩码为16（65,536个IP地址）。\n* 同一个VPC内，多个子网的网段不能重叠。\n* 子网创建后会自动关联到默认路由表。\n* 创建子网同时可以绑定标签, 应答里的标签列表代表添加成功的标签。"
  },
  "DisassociateDhcpIpWithAddressIp": {
    "params": [
      {
        "name": "DhcpIpId",
        "desc": "`DhcpIp`唯一`ID`，形如：`dhcpip-9o233uri`。必须是已绑定`EIP`的`DhcpIp`。"
      }
    ],
    "desc": "本接口（DisassociateDhcpIpWithAddressIp）用于将DhcpIp已绑定的弹性公网IP（EIP）解除绑定。<br />"
  },
  "ReplaceRouteTableAssociation": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "子网实例ID，例如：subnet-3x5lf5q0。可通过DescribeSubnets接口查询。"
      },
      {
        "name": "RouteTableId",
        "desc": "路由表实例ID，例如：rtb-azd4dt1c。"
      }
    ],
    "desc": "本接口（ReplaceRouteTableAssociation)用于修改子网（Subnet）关联的路由表（RouteTable）。\n* 一个子网只能关联一个路由表。"
  },
  "DescribeTemplateLimits": {
    "params": [],
    "desc": "本接口（DescribeTemplateLimits）用于查询参数模板配额列表。"
  },
  "CheckNetDetectState": {
    "params": [
      {
        "name": "DetectDestinationIp",
        "desc": "探测目的IPv4地址数组，最多两个。"
      },
      {
        "name": "NextHopType",
        "desc": "下一跳类型，目前我们支持的类型有：\nVPN：VPN网关；\nDIRECTCONNECT：专线网关；\nPEERCONNECTION：对等连接；\nNAT：NAT网关；\nNORMAL_CVM：普通云服务器；"
      },
      {
        "name": "NextHopDestination",
        "desc": "下一跳目的网关，取值与“下一跳类型”相关：\n下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；\n下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；\n下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；\n下一跳类型为NAT，取值Nat网关，形如：nat-12345678；\n下一跳类型为NORMAL_CVM，取值云服务器IPv4地址，形如：10.0.0.12；"
      },
      {
        "name": "NetDetectId",
        "desc": "网络探测实例ID。形如：netd-12345678。该参数与（VpcId，SubnetId，NetDetectName），至少要有一个。当NetDetectId存在时，使用NetDetectId。"
      },
      {
        "name": "VpcId",
        "desc": "`VPC`实例`ID`。形如：`vpc-12345678`。该参数与（SubnetId，NetDetectName）配合使用，与NetDetectId至少要有一个。当NetDetectId存在时，使用NetDetectId。"
      },
      {
        "name": "SubnetId",
        "desc": "子网实例ID。形如：subnet-12345678。该参数与（VpcId，NetDetectName）配合使用，与NetDetectId至少要有一个。当NetDetectId存在时，使用NetDetectId。"
      },
      {
        "name": "NetDetectName",
        "desc": "网络探测名称，最大长度不能超过60个字节。该参数与（VpcId，SubnetId）配合使用，与NetDetectId至少要有一个。当NetDetectId存在时，使用NetDetectId。"
      }
    ],
    "desc": "本接口(CheckNetDetectState)用于验证网络探测。"
  },
  "DescribeVpcs": {
    "params": [
      {
        "name": "VpcIds",
        "desc": "VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定VpcIds和Filters。\n<li>vpc-name - String - （过滤条件）VPC实例名称。</li>\n<li>is-default - String - （过滤条件）是否默认VPC。</li>\n<li>vpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。</li>\n<li>cidr-block - String - （过滤条件）vpc的cidr。</li>\n<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。</li>\n<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例2。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeVpcs）用于查询私有网络列表。"
  },
  "InquiryPriceResetVpnGatewayInternetMaxBandwidth": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID。"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "公网带宽设置。可选带宽规格：5, 10, 20, 50, 100；单位：Mbps。"
      }
    ],
    "desc": "本接口（InquiryPriceResetVpnGatewayInternetMaxBandwidth）调整VPN网关带宽上限询价。"
  },
  "DeleteDirectConnectGatewayCcnRoutes": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "专线网关ID，形如：dcg-prpqlmg1"
      },
      {
        "name": "RouteIds",
        "desc": "路由ID。形如：ccnr-f49l6u0z。"
      }
    ],
    "desc": "本接口（DeleteDirectConnectGatewayCcnRoutes）用于删除专线网关的云联网路由（IDC网段）"
  },
  "RejectAttachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。"
      },
      {
        "name": "Instances",
        "desc": "拒绝关联实例列表。"
      }
    ],
    "desc": "本接口（RejectAttachCcnInstances）用于跨账号关联实例时，云联网所有者拒绝关联操作。\n"
  },
  "DeleteSecurityGroup": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。"
      }
    ],
    "desc": "本接口（DeleteSecurityGroup）用于删除安全组（SecurityGroup）。\n* 只有当前账号下的安全组允许被删除。\n* 安全组实例ID如果在其他安全组的规则中被引用，则无法直接删除。这种情况下，需要先进行规则修改，再删除安全组。\n* 删除的安全组无法再找回，请谨慎调用。"
  },
  "ModifyAddressesBandwidth": {
    "params": [
      {
        "name": "AddressIds",
        "desc": "EIP唯一标识ID，形如'eip-xxxx'"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "调整带宽目标值"
      },
      {
        "name": "StartTime",
        "desc": "包月带宽起始时间"
      },
      {
        "name": "EndTime",
        "desc": "包月带宽结束时间"
      }
    ],
    "desc": "本接口（ModifyAddressesBandwidth）用于调整[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)(简称EIP)带宽，包括后付费EIP, 预付费EIP和带宽包EIP"
  },
  "CreateNatGatewayDestinationIpPortTranslationNatRule": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "NAT网关的ID，形如：`nat-df45454`。"
      },
      {
        "name": "DestinationIpPortTranslationNatRules",
        "desc": "NAT网关的端口转换规则。"
      }
    ],
    "desc": "本接口(CreateNatGatewayDestinationIpPortTranslationNatRule)用于创建NAT网关端口转发规则。"
  },
  "CreateSubnet": {
    "params": [
      {
        "name": "VpcId",
        "desc": "待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "SubnetName",
        "desc": "子网名称，最大长度不能超过60个字节。"
      },
      {
        "name": "CidrBlock",
        "desc": "子网网段，子网网段必须在VPC网段内，相同VPC内子网网段不能重叠。"
      },
      {
        "name": "Zone",
        "desc": "子网所在的可用区ID，不同子网选择不同可用区可以做跨可用区灾备。"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "本接口(CreateSubnet)用于创建子网。\n* 创建子网前必须创建好 VPC。\n* 子网创建成功后，子网网段不能修改。子网网段必须在VPC网段内，可以和VPC网段相同（VPC有且只有一个子网时），建议子网网段在VPC网段内，预留网段给其他子网使用。\n* 您可以创建的最小网段子网掩码为28（有16个IP地址），最大网段子网掩码为16（65,536个IP地址）。\n* 同一个VPC内，多个子网的网段不能重叠。\n* 子网创建后会自动关联到默认路由表。\n* 创建子网同时可以绑定标签, 应答里的标签列表代表添加成功的标签。"
  },
  "AllocateIp6AddressesBandwidth": {
    "params": [
      {
        "name": "Ip6Addresses",
        "desc": "需要开通公网访问能力的IPV6地址"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "带宽，单位Mbps。默认是1Mbps"
      },
      {
        "name": "InternetChargeType",
        "desc": "网络计费模式。IPV6当前对带宽上移账户支持\"TRAFFIC_POSTPAID_BY_HOUR\"，对带宽非上移支持\"BANDWIDTH_PACKAGE\"。默认网络计费模式是\"TRAFFIC_POSTPAID_BY_HOUR\"。"
      }
    ],
    "desc": "该接口用于给IPv6地址初次分配公网带宽"
  },
  "DeleteDhcpIp": {
    "params": [
      {
        "name": "DhcpIpId",
        "desc": "`DhcpIp`的`ID`，是`DhcpIp`的唯一标识。"
      }
    ],
    "desc": "本接口（DeleteDhcpIp）用于删除DhcpIp"
  },
  "ModifyAddressTemplateAttribute": {
    "params": [
      {
        "name": "AddressTemplateId",
        "desc": "IP地址模板实例ID，例如：ipm-mdunqeb6。"
      },
      {
        "name": "AddressTemplateName",
        "desc": "IP地址模板名称。"
      },
      {
        "name": "Addresses",
        "desc": "地址信息，支持 IP、CIDR、IP 范围。"
      }
    ],
    "desc": "本接口（ModifyAddressTemplateAttribute）用于修改IP地址模板"
  },
  "AcceptAttachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。"
      },
      {
        "name": "Instances",
        "desc": "接受关联实例列表。"
      }
    ],
    "desc": "本接口（AcceptAttachCcnInstances）用于跨账号关联实例时，云联网所有者接受并同意关联操作。"
  },
  "DeleteServiceTemplateGroup": {
    "params": [
      {
        "name": "ServiceTemplateGroupId",
        "desc": "协议端口模板集合实例ID，例如：ppmg-n17uxvve。"
      }
    ],
    "desc": "本接口（DeleteServiceTemplateGroup）用于删除协议端口模板集合"
  },
  "DescribeGatewayFlowQos": {
    "params": [
      {
        "name": "GatewayId",
        "desc": "网关实例ID，目前我们支持的网关实例类型有，\n专线网关实例ID，形如，`dcg-ltjahce6`；\nNat网关实例ID，形如，`nat-ltjahce6`；\nVPN网关实例ID，形如，`vpn-ltjahce6`。"
      },
      {
        "name": "IpAddresses",
        "desc": "限流的云服务器内网IP。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeGatewayFlowQos）用于查询网关来访IP流控带宽。"
  },
  "DescribeIp6Translators": {
    "params": [
      {
        "name": "Ip6TranslatorIds",
        "desc": "IPV6转换实例唯一ID数组，形如ip6-xxxxxxxx"
      },
      {
        "name": "Filters",
        "desc": "每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`Ip6TranslatorIds`和`Filters`。详细的过滤条件如下：\n<li> ip6-translator-id - String - 是否必填：否 - （过滤条件）按照IPV6转换实例的唯一ID过滤,形如ip6-xxxxxxx。</li>\n<li> ip6-translator-vip6 - String - 是否必填：否 - （过滤条件）按照IPV6地址过滤。不支持模糊过滤。</li>\n<li> ip6-translator-name - String - 是否必填：否 - （过滤条件）按照IPV6转换实例名称过滤。不支持模糊过滤。</li>\n<li> ip6-translator-status - String - 是否必填：否 - （过滤条件）按照IPV6转换实例的状态过滤。状态取值范围为\"CREATING\",\"RUNNING\",\"DELETING\",\"MODIFYING\""
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。"
      }
    ],
    "desc": "1. 该接口用于查询账户下的IPV6转换实例及其绑定的转换规则信息\n2. 支持过滤查询"
  },
  "ModifyServiceTemplateGroupAttribute": {
    "params": [
      {
        "name": "ServiceTemplateGroupId",
        "desc": "协议端口模板集合实例ID，例如：ppmg-ei8hfd9a。"
      },
      {
        "name": "ServiceTemplateGroupName",
        "desc": "协议端口模板集合名称。"
      },
      {
        "name": "ServiceTemplateIds",
        "desc": "协议端口模板实例ID，例如：ppm-4dw6agho。"
      }
    ],
    "desc": "本接口（ModifyServiceTemplateGroupAttribute）用于修改协议端口模板集合。"
  },
  "CreateVpc": {
    "params": [
      {
        "name": "VpcName",
        "desc": "vpc名称，最大长度不能超过60个字节。"
      },
      {
        "name": "CidrBlock",
        "desc": "vpc的cidr，只能为10.0.0.0/16，172.16.0.0/16，192.168.0.0/16这三个内网网段内。"
      },
      {
        "name": "EnableMulticast",
        "desc": "是否开启组播。true: 开启, false: 不开启。"
      },
      {
        "name": "DnsServers",
        "desc": "DNS地址，最多支持4个"
      },
      {
        "name": "DomainName",
        "desc": "域名"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "本接口(CreateVpc)用于创建私有网络(VPC)。\n* 用户可以创建的最小网段子网掩码为28（有16个IP地址），最大网段子网掩码为16（65,536个IP地址）,如果规划VPC网段请参见VPC网段规划说明。\n* 同一个地域能创建的VPC资源个数也是有限制的，详见 <a href=\"https://cloud.tencent.com/doc/product/215/537\" title=\"VPC使用限制\">VPC使用限制</a>,如果需要扩充请联系在线客服。\n* 创建VPC同时可以绑定标签, 应答里的标签列表代表添加成功的标签。"
  },
  "ModifyIp6Rule": {
    "params": [
      {
        "name": "Ip6TranslatorId",
        "desc": "IPV6转换实例唯一ID，形如ip6-xxxxxxxx"
      },
      {
        "name": "Ip6RuleId",
        "desc": "IPV6转换规则唯一ID，形如rule6-xxxxxxxx"
      },
      {
        "name": "Ip6RuleName",
        "desc": "IPV6转换规则修改后的名称"
      },
      {
        "name": "Vip",
        "desc": "IPV6转换规则修改后的IPV4地址"
      },
      {
        "name": "Vport",
        "desc": "IPV6转换规则修改后的IPV4端口号"
      }
    ],
    "desc": "该接口用于修改IPV6转换规则，当前仅支持修改转换规则名称，IPV4地址和IPV4端口号"
  },
  "AddBandwidthPackageResources": {
    "params": [
      {
        "name": "ResourceIds",
        "desc": "资源唯一ID，当前支持EIP资源和LB资源，形如'eip-xxxx', 'lb-xxxx'"
      },
      {
        "name": "BandwidthPackageId",
        "desc": "带宽包唯一标识ID，形如'bwp-xxxx'"
      },
      {
        "name": "NetworkType",
        "desc": "带宽包类型，当前支持'BGP'类型，表示内部资源是BGP IP。"
      },
      {
        "name": "ResourceType",
        "desc": "资源类型，包括'Address', 'LoadBalance'"
      },
      {
        "name": "Protocol",
        "desc": "带宽包协议类型。当前支持'ipv4'和'ipv6'协议类型。"
      }
    ],
    "desc": "接口用于添加带宽包资源，包括[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)和[负载均衡](https://cloud.tencent.com/document/product/214/517)等"
  },
  "AssignIpv6SubnetCidrBlock": {
    "params": [
      {
        "name": "VpcId",
        "desc": "子网所在私有网络`ID`。形如：`vpc-f49l6u0z`。"
      },
      {
        "name": "Ipv6SubnetCidrBlocks",
        "desc": "分配 `IPv6` 子网段列表。"
      }
    ],
    "desc": "本接口（AssignIpv6SubnetCidrBlock）用于分配IPv6子网段。\n* 给子网分配 `IPv6` 网段，要求子网所属 `VPC` 已获得 `IPv6` 网段。如果尚未分配，请先通过接口 `AssignIpv6CidrBlock` 给子网所属 `VPC` 分配一个 `IPv6` 网段。否则无法分配 `IPv6` 子网段。\n* 每个子网只能分配一个IPv6网段。"
  },
  "DescribeVpnGatewayCcnRoutes": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      }
    ],
    "desc": "本接口（DescribeVpnGatewayCcnRoutes）用于查询VPN网关云联网路由"
  },
  "AllocateAddresses": {
    "params": [
      {
        "name": "AddressCount",
        "desc": "EIP数量。默认值：1。"
      },
      {
        "name": "InternetServiceProvider",
        "desc": "EIP线路类型。默认值：BGP。\n<ul style=\"margin:0\"><li>已开通静态单线IP白名单的用户，可选值：<ul><li>CMCC：中国移动</li>\n<li>CTCC：中国电信</li>\n<li>CUCC：中国联通</li></ul>注意：仅部分地域支持静态单线IP。</li></ul>"
      },
      {
        "name": "InternetChargeType",
        "desc": "EIP计费方式。\n<ul style=\"margin:0\"><li>已开通带宽上移白名单的用户，可选值：<ul><li>BANDWIDTH_PACKAGE：[共享带宽包](https://cloud.tencent.com/document/product/684/15255)付费（需额外开通共享带宽包白名单）</li>\n<li>BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费</li>\n<li>TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费</li></ul>默认值：TRAFFIC_POSTPAID_BY_HOUR。</li>\n<li>未开通带宽上移白名单的用户，EIP计费方式与其绑定的实例的计费方式一致，无需传递此参数。</li></ul>"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "EIP出带宽上限，单位：Mbps。\n<ul style=\"margin:0\"><li>已开通带宽上移白名单的用户，可选值范围取决于EIP计费方式：<ul><li>BANDWIDTH_PACKAGE：1 Mbps 至 1000 Mbps</li>\n<li>BANDWIDTH_POSTPAID_BY_HOUR：1 Mbps 至 100 Mbps</li>\n<li>TRAFFIC_POSTPAID_BY_HOUR：1 Mbps 至 100 Mbps</li></ul>默认值：1 Mbps。</li>\n<li>未开通带宽上移白名单的用户，EIP出带宽上限取决于与其绑定的实例的公网出带宽上限，无需传递此参数。</li></ul>"
      },
      {
        "name": "AddressType",
        "desc": "EIP类型。默认值：EIP。\n<ul style=\"margin:0\"><li>已开通Anycast公网加速白名单的用户，可选值：<ul><li>AnycastEIP：加速IP，可参见 [Anycast 公网加速](https://cloud.tencent.com/document/product/644)</li></ul>注意：仅部分地域支持加速IP。</li></ul>"
      },
      {
        "name": "AnycastZone",
        "desc": "Anycast发布域。\n<ul style=\"margin:0\"><li>已开通Anycast公网加速白名单的用户，可选值：<ul><li>ANYCAST_ZONE_GLOBAL：全球发布域（需要额外开通Anycast全球加速白名单）</li><li>ANYCAST_ZONE_OVERSEAS：境外发布域</li><li><b>[已废弃]</b> ANYCAST_ZONE_A：发布域A（已更新为全球发布域）</li><li><b>[已废弃]</b> ANYCAST_ZONE_B：发布域B（已更新为全球发布域）</li></ul>默认值：ANYCAST_ZONE_OVERSEAS。</li></ul>"
      },
      {
        "name": "ApplicableForCLB",
        "desc": "<b>[已废弃]</b> AnycastEIP不再区分是否负载均衡。原参数说明如下：\nAnycastEIP是否用于绑定负载均衡。\n<ul style=\"margin:0\"><li>已开通Anycast公网加速白名单的用户，可选值：<ul><li>TRUE：AnycastEIP可绑定对象为负载均衡</li>\n<li>FALSE：AnycastEIP可绑定对象为云服务器、NAT网关、高可用虚拟IP等</li></ul>默认值：FALSE。</li></ul>"
      },
      {
        "name": "Tags",
        "desc": "需要关联的标签列表。"
      },
      {
        "name": "BandwidthPackageId",
        "desc": "BGP带宽包唯一ID参数。设定该参数且InternetChargeType为BANDWIDTH_PACKAGE，则表示创建的EIP加入该BGP带宽包并采用带宽包计费"
      }
    ],
    "desc": "本接口 (AllocateAddresses) 用于申请一个或多个[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。\n* EIP 是专为动态云计算设计的静态 IP 地址。借助 EIP，您可以快速将 EIP 重新映射到您的另一个实例上，从而屏蔽实例故障。\n* 您的 EIP 与腾讯云账户相关联，而不是与某个实例相关联。在您选择显式释放该地址，或欠费超过24小时之前，它会一直与您的腾讯云账户保持关联。\n* 一个腾讯云账户在每个地域能申请的 EIP 最大配额有所限制，可参见 [EIP 产品简介](https://cloud.tencent.com/document/product/213/5733)，上述配额可通过 DescribeAddressQuota 接口获取。"
  },
  "CheckAssistantCidr": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC`实例`ID`。形如：`vpc-6v2ht8q5`"
      },
      {
        "name": "NewCidrBlocks",
        "desc": "待添加的负载CIDR。CIDR数组，格式如[\"10.0.0.0/16\", \"172.16.0.0/16\"]。入参NewCidrBlocks和OldCidrBlocks至少需要其一。"
      },
      {
        "name": "OldCidrBlocks",
        "desc": "待删除的负载CIDR。CIDR数组，格式如[\"10.0.0.0/16\", \"172.16.0.0/16\"]。入参NewCidrBlocks和OldCidrBlocks至少需要其一。"
      }
    ],
    "desc": "本接口(CheckAssistantCidr)用于检查辅助CIDR是否与存量路由、对等连接（对端VPC的CIDR）等资源存在冲突。如果存在重叠，则返回重叠的资源。（接口灰度中，如需使用请提工单。）\n* 检测辅助CIDR是否与当前VPC的主CIDR和辅助CIDR存在重叠。\n* 检测辅助CIDR是否与当前VPC的路由的目的端存在重叠。\n* 检测辅助CIDR是否与当前VPC的对等连接，对端VPC下的主CIDR或辅助CIDR存在重叠。"
  },
  "DescribeVpcIpv6Addresses": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC`实例`ID`，形如：`vpc-f49l6u0z`。"
      },
      {
        "name": "Ipv6Addresses",
        "desc": "`IP`地址列表，批量查询单次请求最多支持`10`个。"
      },
      {
        "name": "Offset",
        "desc": "偏移量。"
      },
      {
        "name": "Limit",
        "desc": "返回数量。"
      }
    ],
    "desc": "本接口（DescribeVpcIpv6Addresses）用于查询 `VPC` `IPv6` 信息。\n只能查询已使用的`IPv6`信息，当查询未使用的IP时，本接口不会报错，但不会出现在返回结果里。"
  },
  "DescribeIp6Addresses": {
    "params": [
      {
        "name": "Ip6AddressIds",
        "desc": "标识 IPV6 的唯一 ID 列表。IPV6 唯一 ID 形如：`eip-11112222`。参数不支持同时指定`Ip6AddressIds`和`Filters`。"
      },
      {
        "name": "Filters",
        "desc": "每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AddressIds`和`Filters`。详细的过滤条件如下：\n<li> address-ip - String - 是否必填：否 - （过滤条件）按照 EIP 的 IP 地址过滤。</li>\n<li> network-interface-id - String - 是否必填：否 - （过滤条件）按照弹性网卡的唯一ID过滤。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。"
      }
    ],
    "desc": "该接口用于查询IPV6地址信息"
  },
  "DescribeAccountAttributes": {
    "params": [],
    "desc": "本接口（DescribeAccountAttributes）用于查询用户账号私有属性。"
  },
  "DescribeDhcpIps": {
    "params": [
      {
        "name": "DhcpIpIds",
        "desc": "DhcpIp实例ID。形如：dhcpip-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定DhcpIpIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定DhcpIpIds和Filters。\n<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>\n<li>subnet-id - String - （过滤条件）所属子网实例ID，形如：subnet-f49l6u0z。</li>\n<li>dhcpip-id - String - （过滤条件）DhcpIp实例ID，形如：dhcpip-pxir56ns。</li>\n<li>dhcpip-name - String - （过滤条件）DhcpIp实例名称。</li>\n<li>address-ip - String - （过滤条件）DhcpIp实例的IP，根据IP精确查找。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeDhcpIps）用于查询DhcpIp列表"
  },
  "AttachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。"
      },
      {
        "name": "Instances",
        "desc": "关联网络实例列表"
      },
      {
        "name": "CcnUin",
        "desc": "CCN所属UIN（根账号），默认当前账号所属UIN"
      }
    ],
    "desc": "本接口（AttachCcnInstances）用于将网络实例加载到云联网实例中，网络实例包括VPC和专线网关。<br />\n每个云联网能够关联的网络实例个数是有限的，详请参考产品文档。如果需要扩充请联系在线客服。"
  },
  "AssociateAddress": {
    "params": [
      {
        "name": "AddressId",
        "desc": "标识 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。"
      },
      {
        "name": "InstanceId",
        "desc": "要绑定的实例 ID。实例 ID 形如：`ins-11112222`。可通过登录[控制台](https://console.cloud.tencent.com/cvm)查询，也可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。"
      },
      {
        "name": "NetworkInterfaceId",
        "desc": "要绑定的弹性网卡 ID。 弹性网卡 ID 形如：`eni-11112222`。`NetworkInterfaceId` 与 `InstanceId` 不可同时指定。弹性网卡 ID 可通过登录[控制台](https://console.cloud.tencent.com/vpc/eni)查询，也可通过[DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/15817)接口返回值中的`networkInterfaceId`获取。"
      },
      {
        "name": "PrivateIpAddress",
        "desc": "要绑定的内网 IP。如果指定了 `NetworkInterfaceId` 则也必须指定 `PrivateIpAddress` ，表示将 EIP 绑定到指定弹性网卡的指定内网 IP 上。同时要确保指定的 `PrivateIpAddress` 是指定的 `NetworkInterfaceId` 上的一个内网 IP。指定弹性网卡的内网 IP 可通过登录[控制台](https://console.cloud.tencent.com/vpc/eni)查询，也可通过[DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/15817)接口返回值中的`privateIpAddress`获取。"
      }
    ],
    "desc": "本接口 (AssociateAddress) 用于将[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）绑定到实例或弹性网卡的指定内网 IP 上。\n* 将 EIP 绑定到实例（CVM）上，其本质是将 EIP 绑定到实例上主网卡的主内网 IP 上。\n* 将 EIP 绑定到主网卡的主内网IP上，绑定过程会把其上绑定的普通公网 IP 自动解绑并释放。\n* 将 EIP 绑定到指定网卡的内网 IP上（非主网卡的主内网IP），则必须先解绑该 EIP，才能再绑定新的。\n* 将 EIP 绑定到NAT网关，请使用接口[EipBindNatGateway](https://cloud.tencent.com/document/product/215/4093)\n* EIP 如果欠费或被封堵，则不能被绑定。\n* 只有状态为 UNBIND 的 EIP 才能够被绑定。"
  },
  "DeleteCustomerGateway": {
    "params": [
      {
        "name": "CustomerGatewayId",
        "desc": "对端网关ID，例如：cgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。"
      }
    ],
    "desc": "本接口（DeleteCustomerGateway）用于删除对端网关。"
  },
  "DeleteSubnet": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "子网实例ID。可通过DescribeSubnets接口返回值中的SubnetId获取。"
      }
    ],
    "desc": "本接口（DeleteSubnet）用于用于删除子网(Subnet)。\n* 删除子网前，请清理该子网下所有资源，包括云服务器、负载均衡、云数据、noSql、弹性网卡等资源。"
  },
  "AttachClassicLinkVpc": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID"
      },
      {
        "name": "InstanceIds",
        "desc": "CVM实例ID"
      }
    ],
    "desc": "本接口(AttachClassicLinkVpc)用于创建私有网络和基础网络设备互通。\n* 私有网络和基础网络设备必须在同一个地域。\n* 私有网络和基础网络的区别详见vpc产品文档-<a href=\"https://cloud.tencent.com/document/product/215/30720\">私有网络与基础网络</a>。"
  },
  "DisassociateNatGatewayAddress": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "NAT网关的ID，形如：`nat-df45454`。"
      },
      {
        "name": "PublicIpAddresses",
        "desc": "绑定NAT网关的弹性IP数组。"
      }
    ],
    "desc": "本接口（DisassociateNatGatewayAddress）用于NAT网关解绑弹性IP。"
  },
  "DescribeFlowLogs": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私用网络ID或者统一ID，建议使用统一ID"
      },
      {
        "name": "FlowLogId",
        "desc": "流日志唯一ID"
      },
      {
        "name": "FlowLogName",
        "desc": "流日志实例名字"
      },
      {
        "name": "ResourceType",
        "desc": "流日志所属资源类型，VPC|SUBNET|NETWORKINTERFACE"
      },
      {
        "name": "ResourceId",
        "desc": "资源唯一ID"
      },
      {
        "name": "TrafficType",
        "desc": "流日志采集类型，ACCEPT|REJECT|ALL"
      },
      {
        "name": "CloudLogId",
        "desc": "流日志存储ID"
      },
      {
        "name": "CloudLogState",
        "desc": "流日志存储ID状态"
      },
      {
        "name": "OrderField",
        "desc": "按某个字段排序,支持字段：flowLogName,createTime，默认按createTime"
      },
      {
        "name": "OrderDirection",
        "desc": "升序（asc）还是降序（desc）,默认：desc"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "每页行数，默认为10"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定FlowLogIds和Filters。\n<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。</li>\n<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。</li>"
      }
    ],
    "desc": "本接口（DescribeFlowLogs）用于查询获取流日志集合"
  },
  "DeleteDirectConnectGateway": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "专线网关唯一`ID`，形如：`dcg-9o233uri`。"
      }
    ],
    "desc": "本接口（DeleteDirectConnectGateway）用于删除专线网关。\n<li>如果是 NAT 网关，删除专线网关后，NAT 规则以及 ACL 策略都被清理了。</li>\n<li>删除专线网关后，系统会删除路由表中跟该专线网关相关的路由策略。</li>\n本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口"
  },
  "DescribeDirectConnectGatewayCcnRoutes": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "专线网关ID，形如：`dcg-prpqlmg1`。"
      },
      {
        "name": "CcnRouteType",
        "desc": "云联网路由学习类型，可选值：\n<li>`BGP` - 自动学习。</li>\n<li>`STATIC` - 静态，即用户配置，默认值。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量。"
      },
      {
        "name": "Limit",
        "desc": "返回数量。"
      }
    ],
    "desc": "本接口（DescribeDirectConnectGatewayCcnRoutes）用于查询专线网关的云联网路由（IDC网段）"
  },
  "CreateNetworkInterface": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "NetworkInterfaceName",
        "desc": "弹性网卡名称，最大长度不能超过60个字节。"
      },
      {
        "name": "SubnetId",
        "desc": "弹性网卡所在的子网实例ID，例如：subnet-0ap8nwca。"
      },
      {
        "name": "NetworkInterfaceDescription",
        "desc": "弹性网卡描述，可任意命名，但不得超过60个字符。"
      },
      {
        "name": "SecondaryPrivateIpAddressCount",
        "desc": "新申请的内网IP地址个数，内网IP地址个数总和不能超过配数。"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "指定绑定的安全组，例如：['sg-1dd51d']。"
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "指定的内网IP信息，单次最多指定10个。"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "本接口（CreateNetworkInterface）用于创建弹性网卡。\n* 创建弹性网卡时可以指定内网IP，并且可以指定一个主IP，指定的内网IP必须在弹性网卡所在子网内，而且不能被占用。\n* 创建弹性网卡时可以指定需要申请的内网IP数量，系统会随机生成内网IP地址。\n* 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href=\"/document/product/576/18527\">弹性网卡使用限制</a>。\n* 创建弹性网卡同时可以绑定已有安全组。\n* 创建弹性网卡同时可以绑定标签, 应答里的标签列表代表添加成功的标签。"
  },
  "DeleteBandwidthPackage": {
    "params": [
      {
        "name": "BandwidthPackageId",
        "desc": "待删除带宽包唯一ID"
      }
    ],
    "desc": "接口支持删除共享带宽包，包括[设备带宽包](https://cloud.tencent.com/document/product/684/15246#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85)和[IP带宽包](https://cloud.tencent.com/document/product/684/15246#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85)"
  },
  "DescribeNetDetectStates": {
    "params": [
      {
        "name": "NetDetectIds",
        "desc": "网络探测实例`ID`数组。形如：[`netd-12345678`]"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定NetDetectIds和Filters。\n<li>net-detect-id - String - （过滤条件）网络探测实例ID，形如：netd-12345678</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口(DescribeNetDetectStates)用于查询网络探测验证结果列表。"
  },
  "DescribeCcns": {
    "params": [
      {
        "name": "CcnIds",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定CcnIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定CcnIds和Filters。\n<li>ccn-id - String - （过滤条件）CCN唯一ID，形如：vpc-f49l6u0z。</li>\n<li>ccn-name - String - （过滤条件）CCN名称。</li>\n<li>ccn-description - String - （过滤条件）CCN描述。</li>\n<li>state - String - （过滤条件）实例状态， 'ISOLATED': 隔离中（欠费停服），'AVAILABLE'：运行中。</li>\n<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。</li>\n<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例：查询绑定了标签的CCN列表。</li>"
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
        "desc": "排序字段。支持：`CcnId` `CcnName` `CreateTime` `State` `QosLevel`"
      },
      {
        "name": "OrderDirection",
        "desc": "排序方法。顺序：`ASC`，倒序：`DESC`。"
      }
    ],
    "desc": "本接口（DescribeCcns）用于查询云联网（CCN）列表。"
  },
  "DeleteIp6Translators": {
    "params": [
      {
        "name": "Ip6TranslatorIds",
        "desc": "待释放的IPV6转换实例的唯一ID，形如‘ip6-xxxxxxxx’"
      }
    ],
    "desc": "1. 该接口用于释放IPV6转换实例，支持批量。\n2.  如果IPV6转换实例建立有转换规则，会一并删除。"
  },
  "DisassociateDirectConnectGatewayNatGateway": {
    "params": [
      {
        "name": "VpcId",
        "desc": "专线网关ID。"
      },
      {
        "name": "NatGatewayId",
        "desc": "NAT网关ID。"
      },
      {
        "name": "DirectConnectGatewayId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      }
    ],
    "desc": "将专线网关与NAT网关解绑，解绑之后，专线网关将不能通过NAT网关访问公网"
  },
  "ModifyNetworkAclEntries": {
    "params": [
      {
        "name": "NetworkAclId",
        "desc": "网络ACL实例ID。例如：acl-12345678。"
      },
      {
        "name": "NetworkAclEntrySet",
        "desc": "网络ACL规则集。"
      }
    ],
    "desc": "本接口（ModifyNetworkAclEntries）用于修改（包括添加和删除）网络ACL的入站规则和出站规则。在NetworkAclEntrySet参数中：\n* 若同时传入入站规则和出站规则，则重置原有的入站规则和出站规则，并分别导入传入的规则。\n* 若仅传入入站规则，则仅重置原有的入站规则，并导入传入的规则，不影响原有的出站规则（若仅传入出站规则，处理方式类似入站方向）。"
  },
  "HaVipDisassociateAddressIp": {
    "params": [
      {
        "name": "HaVipId",
        "desc": "`HAVIP`唯一`ID`，形如：`havip-9o233uri`。必须是已绑定`EIP`的`HAVIP`。"
      }
    ],
    "desc": "本接口（HaVipDisassociateAddressIp）用于将高可用虚拟IP（HAVIP）已绑定的弹性公网IP（EIP）解除绑定<br />\n本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口"
  },
  "ModifyVpnGatewayCcnRoutes": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID"
      },
      {
        "name": "Routes",
        "desc": "云联网路由（IDC网段）列表"
      }
    ],
    "desc": "本接口（ModifyVpnGatewayCcnRoutes）用于修改VPN网关云联网路由"
  },
  "DetachNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-m6dyj72l。"
      },
      {
        "name": "InstanceId",
        "desc": "CVM实例ID。形如：ins-r8hr2upy。"
      }
    ],
    "desc": "本接口（DetachNetworkInterface）用于弹性网卡解绑云主机。"
  },
  "DeleteAssistantCidr": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC`实例`ID`。形如：`vpc-6v2ht8q5`"
      },
      {
        "name": "CidrBlocks",
        "desc": "CIDR数组，格式如[\"10.0.0.0/16\", \"172.16.0.0/16\"]"
      }
    ],
    "desc": "本接口(DeleteAssistantCidr)用于删除辅助CIDR。（接口灰度中，如需使用请提工单。）"
  },
  "ModifyDhcpIpAttribute": {
    "params": [
      {
        "name": "DhcpIpId",
        "desc": "`DhcpIp`唯一`ID`，形如：`dhcpip-9o233uri`。"
      },
      {
        "name": "DhcpIpName",
        "desc": "`DhcpIp`名称，可任意命名，但不得超过60个字符。"
      }
    ],
    "desc": "本接口（ModifyDhcpIpAttribute）用于修改DhcpIp属性"
  },
  "DeleteNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-m6dyj72l。"
      }
    ],
    "desc": "本接口（DeleteNetworkInterface）用于删除弹性网卡。\n* 弹性网卡上绑定了云服务器时，不能被删除。\n* 删除指定弹性网卡，弹性网卡必须先和子机解绑才能删除。删除之后弹性网卡上所有内网IP都将被退还。"
  },
  "DescribeVpnConnections": {
    "params": [
      {
        "name": "VpnConnectionIds",
        "desc": "VPN通道实例ID。形如：vpnx-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpnConnectionIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定VpnConnectionIds和Filters。\n<li>vpc-id - String - VPC实例ID，形如：`vpc-0a36uwkr`。</li>\n<li>vpn-gateway-id - String - VPN网关实例ID，形如：`vpngw-p4lmqawn`。</li>\n<li>customer-gateway-id - String - 对端网关实例ID，形如：`cgw-l4rblw63`。</li>\n<li>vpn-connection-name - String - 通道名称，形如：`test-vpn`。</li>\n<li>vpn-connection-id - String - 通道实例ID，形如：`vpnx-5p7vkch8\"`。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": " 本接口（DescribeVpnConnections）查询VPN通道列表。"
  },
  "DescribeSecurityGroupReferences": {
    "params": [
      {
        "name": "SecurityGroupIds",
        "desc": "安全组实例ID数组。格式如：['sg-12345678']"
      }
    ],
    "desc": "本接口（DescribeSecurityGroupReferences）用于查询安全组被引用信息。"
  },
  "DescribeFlowLog": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私用网络ID或者统一ID，建议使用统一ID"
      },
      {
        "name": "FlowLogId",
        "desc": "流日志唯一ID"
      }
    ],
    "desc": "本接口（DescribeFlowLog）用于查询流日志实例信息"
  },
  "ModifyGatewayFlowQos": {
    "params": [
      {
        "name": "GatewayId",
        "desc": "网关实例ID，目前我们支持的网关实例类型有，\n专线网关实例ID，形如，`dcg-ltjahce6`；\nNat网关实例ID，形如，`nat-ltjahce6`；\nVPN网关实例ID，形如，`vpn-ltjahce6`。"
      },
      {
        "name": "Bandwidth",
        "desc": "流控带宽值。取值大于0，表示限流到指定的Mbps；取值等于0，表示完全限流；取值为-1，不限流。"
      },
      {
        "name": "IpAddresses",
        "desc": "限流的云服务器内网IP。"
      }
    ],
    "desc": "本接口（ModifyGatewayFlowQos）用于调整网关流控带宽。"
  },
  "DeleteNatGateway": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "NAT网关的ID，形如：`nat-df45454`。"
      }
    ],
    "desc": "本接口（DeleteNatGateway）用于删除NAT网关。\n删除 NAT 网关后，系统会自动删除路由表中包含此 NAT 网关的路由项，同时也会解绑弹性公网IP（EIP）。"
  },
  "DescribeRouteConflicts": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表实例ID，例如：rtb-azd4dt1c。"
      },
      {
        "name": "DestinationCidrBlocks",
        "desc": "要检查的与之冲突的目的端列表"
      }
    ],
    "desc": "本接口（DescribeRouteConflicts）用于查询自定义路由策略与云联网路由策略冲突列表"
  },
  "DisableRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表唯一ID。"
      },
      {
        "name": "RouteIds",
        "desc": "路由策略ID。不能和RouteItemIds同时使用。"
      },
      {
        "name": "RouteItemIds",
        "desc": "路由策略唯一ID。不能和RouteIds同时使用。"
      }
    ],
    "desc": "本接口（DisableRoutes）用于禁用已启用的子网路由"
  },
  "DescribeCcnRegionBandwidthLimits": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。"
      }
    ],
    "desc": "本接口（DescribeCcnRegionBandwidthLimits）用于查询云联网各地域出带宽上限，该接口只返回已关联网络实例包含的地域"
  },
  "AddIp6Rules": {
    "params": [
      {
        "name": "Ip6TranslatorId",
        "desc": "IPV6转换实例唯一ID，形如ip6-xxxxxxxx"
      },
      {
        "name": "Ip6RuleInfos",
        "desc": "IPV6转换规则信息"
      },
      {
        "name": "Ip6RuleName",
        "desc": "IPV6转换规则名称"
      }
    ],
    "desc": "1. 该接口用于在转换实例下添加IPV6转换规则。\n2. 支持在同一个转换实例下批量添加转换规则，一个账户在一个地域最多50个。\n3. 一个完整的转换规则包括vip6:vport6:protocol:vip:vport，其中vip6:vport6:protocol必须是唯一。"
  },
  "AssociateDhcpIpWithAddressIp": {
    "params": [
      {
        "name": "DhcpIpId",
        "desc": "`DhcpIp`唯一`ID`，形如：`dhcpip-9o233uri`。必须是没有绑定`EIP`的`DhcpIp`"
      },
      {
        "name": "AddressIp",
        "desc": "弹性公网`IP`。必须是没有绑定`DhcpIp`的`EIP`"
      }
    ],
    "desc": "本接口（AssociateDhcpIpWithAddressIp）用于DhcpIp绑定弹性公网IP（EIP）。<br />"
  },
  "DeleteCcn": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。"
      }
    ],
    "desc": "本接口（DeleteCcn）用于删除云联网。\n* 删除后，云联网关联的所有实例间路由将被删除，网络将会中断，请务必确认\n* 删除云联网是不可逆的操作，请谨慎处理。\n"
  },
  "UnassignPrivateIpAddresses": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-m6dyj72l。"
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "指定的内网IP信息，单次最多指定10个。"
      }
    ],
    "desc": "本接口（UnassignPrivateIpAddresses）用于弹性网卡退还内网 IP。\n* 退还弹性网卡上的辅助内网IP，接口自动解关联弹性公网 IP。不能退还弹性网卡的主内网IP。"
  },
  "ModifyAddressTemplateGroupAttribute": {
    "params": [
      {
        "name": "AddressTemplateGroupId",
        "desc": "IP地址模板集合实例ID，例如：ipmg-2uw6ujo6。"
      },
      {
        "name": "AddressTemplateGroupName",
        "desc": "IP地址模板集合名称。"
      },
      {
        "name": "AddressTemplateIds",
        "desc": "IP地址模板实例ID， 例如：ipm-mdunqeb6。"
      }
    ],
    "desc": "本接口（ModifyAddressTemplateGroupAttribute）用于修改IP地址模板集合"
  },
  "DescribeCcnRoutes": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID，形如：ccn-gree226l。"
      },
      {
        "name": "RouteIds",
        "desc": "CCN路由策略唯一ID。形如：ccnr-f49l6u0z。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定RouteIds和Filters。\n<li>route-id - String -（过滤条件）路由策略ID。</li>\n<li>cidr-block - String -（过滤条件）目的端。</li>\n<li>instance-type - String -（过滤条件）下一跳类型。</li>\n<li>instance-region - String -（过滤条件）下一跳所属地域。</li>\n<li>instance-id - String -（过滤条件）下一跳实例ID。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      }
    ],
    "desc": "本接口（DescribeCcnRoutes）用于查询已加入云联网（CCN）的路由"
  },
  "CreateNetDetect": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC`实例`ID`。形如：`vpc-12345678`"
      },
      {
        "name": "SubnetId",
        "desc": "子网实例ID。形如：subnet-12345678。"
      },
      {
        "name": "NetDetectName",
        "desc": "网络探测名称，最大长度不能超过60个字节。"
      },
      {
        "name": "DetectDestinationIp",
        "desc": "探测目的IPv4地址数组。最多两个。"
      },
      {
        "name": "NextHopType",
        "desc": "下一跳类型，目前我们支持的类型有：\nVPN：VPN网关；\nDIRECTCONNECT：专线网关；\nPEERCONNECTION：对等连接；\nNAT：NAT网关；\nNORMAL_CVM：普通云服务器；"
      },
      {
        "name": "NextHopDestination",
        "desc": "下一跳目的网关，取值与“下一跳类型”相关：\n下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；\n下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；\n下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；\n下一跳类型为NAT，取值Nat网关，形如：nat-12345678；\n下一跳类型为NORMAL_CVM，取值云服务器IPv4地址，形如：10.0.0.12；"
      },
      {
        "name": "NetDetectDescription",
        "desc": "网络探测描述。"
      }
    ],
    "desc": "本接口(CreateNetDetect)用于创建网络探测。"
  },
  "CreateIp6Translators": {
    "params": [
      {
        "name": "Ip6TranslatorName",
        "desc": "转换实例名称"
      },
      {
        "name": "Ip6TranslatorCount",
        "desc": "创建转换实例数量，默认是1个"
      },
      {
        "name": "Ip6InternetServiceProvider",
        "desc": "转换实例运营商属性，可取\"CMCC\",\"CTCC\",\"CUCC\",\"BGP\""
      }
    ],
    "desc": "1. 该接口用于创建IPV6转换IPV4实例，支持批量\n2. 同一个账户在一个地域最多允许创建10个转换实例"
  },
  "CreateAssistantCidr": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC`实例`ID`。形如：`vpc-6v2ht8q5`"
      },
      {
        "name": "CidrBlocks",
        "desc": "CIDR数组，格式如[\"10.0.0.0/16\", \"172.16.0.0/16\"]"
      }
    ],
    "desc": "本接口(CreateAssistantCidr)用于批量创建辅助CIDR。（接口灰度中，如需使用请提工单。）"
  },
  "CreateDefaultVpc": {
    "params": [
      {
        "name": "Zone",
        "desc": "子网所在的可用区ID，不指定将随机选择可用区"
      },
      {
        "name": "Force",
        "desc": "是否强制返回默认VPC"
      }
    ],
    "desc": "本接口（CreateDefaultVpc）用于创建默认私有网络(VPC）。\n\n默认VPC适用于快速入门和启动公共实例，您可以像使用任何其他VPC一样使用默认VPC。如果您想创建标准VPC，即指定VPC名称、VPC网段、子网网段、子网可用区，请使用常规创建VPC接口（CreateVpc）\n\n正常情况，本接口并不一定生产默认VPC，而是根据用户账号的网络属性（DescribeAccountAttributes）来决定的\n* 支持基础网络、VPC，返回VpcId为0\n* 只支持VPC，返回默认VPC信息\n\n您也可以通过 Force 参数，强制返回默认VPC"
  },
  "AttachNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-m6dyj72l。"
      },
      {
        "name": "InstanceId",
        "desc": "CVM实例ID。形如：ins-r8hr2upy。"
      }
    ],
    "desc": "本接口（AttachNetworkInterface）用于弹性网卡绑定云主机。\n* 一个云主机可以绑定多个弹性网卡，但只能绑定一个主网卡。更多限制信息详见<a href=\"https://cloud.tencent.com/document/product/576/18527\">弹性网卡使用限制</a>。\n* 一个弹性网卡只能同时绑定一个云主机。\n* 只有运行中或者已关机状态的云主机才能绑定弹性网卡，查看云主机状态详见<a href=\"https://cloud.tencent.com/document/api/213/9452#InstanceStatus\">腾讯云主机信息</a>。\n* 弹性网卡绑定的云主机必须是私有网络的，而且云主机所在可用区必须和弹性网卡子网的可用区相同。"
  },
  "ReplaceDirectConnectGatewayCcnRoutes": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "专线网关ID，形如：dcg-prpqlmg1"
      },
      {
        "name": "Routes",
        "desc": "需要连通的IDC网段列表"
      }
    ],
    "desc": "本接口（ReplaceDirectConnectGatewayCcnRoutes）根据路由ID（RouteId）修改指定的路由（Route），支持批量修改。"
  },
  "GetCcnRegionBandwidthLimits": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>sregion - String - （过滤条件）源地域，形如：ap-guangzhou。</li>\n<li>dregion - String - （过滤条件）目的地域，形如：ap-shanghai-bm</li>"
      },
      {
        "name": "SortedBy",
        "desc": "排序条件，目前支持带宽（BandwidthLimit）和过期时间（ExpireTime）"
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
        "name": "OrderBy",
        "desc": "排序方式，'ASC':升序,'DESC':降序。"
      }
    ],
    "desc": "本接口（GetCcnRegionBandwidthLimits）用于查询云联网相关地域带宽信息，其中预付费模式的云联网仅支持地域间限速，后付费模式的云联网支持地域间限速和地域出口限速。"
  },
  "DeleteSecurityGroupPolicies": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。"
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "安全组规则集合。一个请求中只能删除单个方向的一条或多条规则。支持指定索引（PolicyIndex） 匹配删除和安全组规则匹配删除两种方式，一个请求中只能使用一种匹配方式。"
      }
    ],
    "desc": "本接口（DeleteSecurityGroupPolicies）用于用于删除安全组规则（SecurityGroupPolicy）。\n* SecurityGroupPolicySet.Version 用于指定要操作的安全组的版本。传入 Version 版本号若不等于当前安全组的最新版本，将返回失败；若不传 Version 则直接删除指定PolicyIndex的规则。"
  },
  "DeleteNetDetect": {
    "params": [
      {
        "name": "NetDetectId",
        "desc": "网络探测实例`ID`。形如：`netd-12345678`"
      }
    ],
    "desc": "本接口(DeleteNetDetect)用于删除网络探测实例。"
  },
  "ModifySecurityGroupAttribute": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。"
      },
      {
        "name": "GroupName",
        "desc": "安全组名称，可任意命名，但不得超过60个字符。"
      },
      {
        "name": "GroupDescription",
        "desc": "安全组备注，最多100个字符。"
      }
    ],
    "desc": "本接口（ModifySecurityGroupAttribute）用于修改安全组（SecurityGroupPolicy）属性。"
  },
  "DeleteAddressTemplate": {
    "params": [
      {
        "name": "AddressTemplateId",
        "desc": "IP地址模板实例ID，例如：ipm-09o5m8kc。"
      }
    ],
    "desc": "本接口（DeleteAddressTemplate）用于删除IP地址模板"
  },
  "ModifyAssistantCidr": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC`实例`ID`。形如：`vpc-6v2ht8q5`"
      },
      {
        "name": "NewCidrBlocks",
        "desc": "待添加的负载CIDR。CIDR数组，格式如[\"10.0.0.0/16\", \"172.16.0.0/16\"]"
      },
      {
        "name": "OldCidrBlocks",
        "desc": "待删除的负载CIDR。CIDR数组，格式如[\"10.0.0.0/16\", \"172.16.0.0/16\"]"
      }
    ],
    "desc": "本接口(ModifyAssistantCidr)用于批量修改辅助CIDR，支持新增和删除。（接口灰度中，如需使用请提工单。）"
  },
  "DeleteVpnGateway": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID。"
      }
    ],
    "desc": "本接口（DeleteVpnGateway）用于删除VPN网关。目前只支持删除运行中的按量计费的IPSEC网关实例。"
  },
  "CreateServiceTemplate": {
    "params": [
      {
        "name": "ServiceTemplateName",
        "desc": "协议端口模板名称"
      },
      {
        "name": "Services",
        "desc": "支持单个端口、多个端口、连续端口及所有端口，协议支持：TCP、UDP、ICMP、GRE 协议。"
      }
    ],
    "desc": "本接口（CreateServiceTemplate）用于创建协议端口模板"
  },
  "DeleteRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表实例ID。"
      },
      {
        "name": "Routes",
        "desc": "路由策略对象。"
      }
    ],
    "desc": "本接口(DeleteRoutes)用于对某个路由表批量删除路由策略（Route）。"
  },
  "ModifySecurityGroupPolicies": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。"
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "安全组规则集合。 SecurityGroupPolicySet对象必须同时指定新的出（Egress）入（Ingress）站规则。 SecurityGroupPolicy对象不支持自定义索引（PolicyIndex）。"
      },
      {
        "name": "SortPolicys",
        "desc": "排序安全组标识。值为True时，支持安全组排序；SortPolicys不存在或SortPolicys为False时，为修改安全组规则。"
      }
    ],
    "desc": "本接口（ModifySecurityGroupPolicies）用于重置安全组出站和入站规则（SecurityGroupPolicy）。\n\n<ul>\n<li>接口是先删除当前所有的出入站规则，然后再添加 Egress 和 Ingress 规则，不支持自定义索引 PolicyIndex。</li>\n<li>在 SecurityGroupPolicySet 参数中：<ul>\n\t<li> 如果指定 SecurityGroupPolicySet.Version 为0, 表示清空所有规则，并忽略 Egress 和 Ingress。</li>\n\t<li> 如果指定 SecurityGroupPolicySet.Version 不为0, 在添加出站和入站规则（Egress 和 Ingress）时：<ul>\n\t\t<li>Protocol 字段支持输入 TCP, UDP, ICMP, ICMPV6, GRE, ALL。</li>\n\t\t<li>CidrBlock 字段允许输入符合 cidr 格式标准的任意字符串。(展开)在基础网络中，如果 CidrBlock 包含您的账户内的云服务器之外的设备在腾讯云的内网 IP，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。</li>\n\t\t<li>Ipv6CidrBlock 字段允许输入符合 IPv6 cidr 格式标准的任意字符串。(展开)在基础网络中，如果Ipv6CidrBlock 包含您的账户内的云服务器之外的设备在腾讯云的内网 IPv6，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。</li>\n\t\t<li>SecurityGroupId 字段允许输入与待修改的安全组位于相同项目中的安全组 ID，包括这个安全组 ID 本身，代表安全组下所有云服务器的内网 IP。使用这个字段时，这条规则用来匹配网络报文的过程中会随着被使用的这个ID所关联的云服务器变化而变化，不需要重新修改。</li>\n\t\t<li>Port 字段允许输入一个单独端口号，或者用减号分隔的两个端口号代表端口范围，例如80或8000-8010。只有当 Protocol 字段是 TCP 或 UDP 时，Port 字段才被接受。</li>\n\t\t<li>Action 字段只允许输入 ACCEPT 或 DROP。</li>\n\t\t<li>CidrBlock, Ipv6CidrBlock, SecurityGroupId, AddressTemplate 四者是排他关系，不允许同时输入，Protocol + Port 和 ServiceTemplate 二者是排他关系，不允许同时输入。</li>\n</ul></li></ul></li>\n</ul>"
  },
  "ModifySubnetAttribute": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "子网实例ID。形如：subnet-pxir56ns。"
      },
      {
        "name": "SubnetName",
        "desc": "子网名称，最大长度不能超过60个字节。"
      },
      {
        "name": "EnableBroadcast",
        "desc": "子网是否开启广播。"
      }
    ],
    "desc": "本接口（ModifySubnetAttribute）用于修改子网属性。"
  },
  "DescribeNetworkInterfaces": {
    "params": [
      {
        "name": "NetworkInterfaceIds",
        "desc": "弹性网卡实例ID查询。形如：eni-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定NetworkInterfaceIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定NetworkInterfaceIds和Filters。\n<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>\n<li>subnet-id - String - （过滤条件）所属子网实例ID，形如：subnet-f49l6u0z。</li>\n<li>network-interface-id - String - （过滤条件）弹性网卡实例ID，形如：eni-5k56k7k7。</li>\n<li>attachment.instance-id - String - （过滤条件）绑定的云服务器实例ID，形如：ins-3nqpdn3i。</li>\n<li>groups.security-group-id - String - （过滤条件）绑定的安全组实例ID，例如：sg-f9ekbxeq。</li>\n<li>network-interface-name - String - （过滤条件）网卡实例名称。</li>\n<li>network-interface-description - String - （过滤条件）网卡实例描述。</li>\n<li>address-ip - String - （过滤条件）内网IPv4地址，单IP后缀模糊匹配，多IP精确匹配。可以与`ip-exact-match`配合做单IP的精确匹配查询。</li>\n<li>ip-exact-match - Boolean - （过滤条件）内网IPv4精确匹配查询，存在多值情况，只取第一个。</li>\n<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。使用请参考示例2</li>\n<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例3。</li>\n<li>is-primary - Boolean - 是否必填：否 - （过滤条件）按照是否主网卡进行过滤。值为true时，仅过滤主网卡；值为false时，仅过滤辅助网卡；此过滤参数未提供时，同时过滤主网卡和辅助网卡。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeNetworkInterfaces）用于查询弹性网卡列表。"
  },
  "AssociateNetworkAclSubnets": {
    "params": [
      {
        "name": "NetworkAclId",
        "desc": "网络ACL实例ID。例如：acl-12345678。"
      },
      {
        "name": "SubnetIds",
        "desc": "子网实例ID数组。例如：[subnet-12345678]"
      }
    ],
    "desc": "本接口（AssociateNetworkAclSubnets）用于网络ACL关联vpc下的子网。"
  },
  "DisableCcnRoutes": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。"
      },
      {
        "name": "RouteIds",
        "desc": "CCN路由策略唯一ID。形如：ccnr-f49l6u0z。"
      }
    ],
    "desc": "本接口（DisableCcnRoutes）用于禁用已经启用的云联网（CCN）路由"
  },
  "InquiryPriceCreateVpnGateway": {
    "params": [
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "公网带宽设置。可选带宽规格：5, 10, 20, 50, 100；单位：Mbps。"
      },
      {
        "name": "InstanceChargeType",
        "desc": "VPN网关计费模式，PREPAID：表示预付费，即包年包月，POSTPAID_BY_HOUR：表示后付费，即按量计费。默认：POSTPAID_BY_HOUR，如果指定预付费模式，参数InstanceChargePrepaid必填。"
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。"
      }
    ],
    "desc": "本接口（InquiryPriceCreateVpnGateway）用于创建VPN网关询价。"
  },
  "ResetVpnConnection": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID。"
      },
      {
        "name": "VpnConnectionId",
        "desc": "VPN通道实例ID。形如：vpnx-f49l6u0z。"
      }
    ],
    "desc": "本接口(ResetVpnConnection)用于重置VPN通道。"
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
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "本接口（CreateCustomerGateway）用于创建对端网关。"
  },
  "ModifyDirectConnectGatewayAttribute": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "专线网关唯一`ID`，形如：`dcg-9o233uri`。"
      },
      {
        "name": "DirectConnectGatewayName",
        "desc": "专线网关名称，可任意命名，但不得超过60个字符。"
      },
      {
        "name": "CcnRouteType",
        "desc": "云联网路由学习类型，可选值：`BGP`（自动学习）、`STATIC`（静态，即用户配置）。只有云联网类型专线网关且开启了BGP功能才支持修改`CcnRouteType`。"
      }
    ],
    "desc": "本接口（ModifyDirectConnectGatewayAttribute）用于修改专线网关属性\n"
  },
  "CreateSecurityGroup": {
    "params": [
      {
        "name": "GroupName",
        "desc": "安全组名称，可任意命名，但不得超过60个字符。"
      },
      {
        "name": "GroupDescription",
        "desc": "安全组备注，最多100个字符。"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，默认0。可在qcloud控制台项目管理页面查询到。"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "本接口（CreateSecurityGroup）用于创建新的安全组（SecurityGroup）。\n* 每个账户下每个地域的每个项目的<a href=\"https://cloud.tencent.com/document/product/213/12453\">安全组数量限制</a>。\n* 新建的安全组的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用CreateSecurityGroupPolicies将安全组的规则设置为需要的规则。\n* 创建安全组同时可以绑定标签, 应答里的标签列表代表添加成功的标签。"
  },
  "ModifyNetworkInterfaceAttribute": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-pxir56ns。"
      },
      {
        "name": "NetworkInterfaceName",
        "desc": "弹性网卡名称，最大长度不能超过60个字节。"
      },
      {
        "name": "NetworkInterfaceDescription",
        "desc": "弹性网卡描述，可任意命名，但不得超过60个字符。"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "指定绑定的安全组，例如:['sg-1dd51d']。"
      }
    ],
    "desc": "本接口（ModifyNetworkInterfaceAttribute）用于修改弹性网卡属性。"
  },
  "DescribeVpnGateways": {
    "params": [
      {
        "name": "VpnGatewayIds",
        "desc": "VPN网关实例ID。形如：vpngw-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpnGatewayIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定VpnGatewayIds和Filters。\n<li>vpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。</li>\n<li>vpn-gateway-id - String - （过滤条件）VPN实例ID形如：vpngw-5aluhh9t。</li>\n<li>vpn-gateway-name - String - （过滤条件）VPN实例名称。</li>\n<li>type - String - （过滤条件）VPN网关类型：'IPSEC', 'SSL'。</li>\n<li>public-ip-address- String - （过滤条件）公网IP。</li>\n<li>renew-flag - String - （过滤条件）网关续费类型，手动续费：'NOTIFY_AND_MANUAL_RENEW'、自动续费：'NOTIFY_AND_AUTO_RENEW'。</li>\n<li>zone - String - （过滤条件）VPN所在可用区，形如：ap-guangzhou-2。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "请求对象个数"
      }
    ],
    "desc": "本接口（DescribeVpnGateways）用于查询VPN网关列表。"
  },
  "DownloadCustomerGatewayConfiguration": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID。"
      },
      {
        "name": "VpnConnectionId",
        "desc": "VPN通道实例ID。形如：vpnx-f49l6u0z。"
      },
      {
        "name": "CustomerGatewayVendor",
        "desc": "对端网关厂商信息对象，可通过DescribeCustomerGatewayVendors获取。"
      },
      {
        "name": "InterfaceName",
        "desc": "通道接入设备物理接口名称。"
      }
    ],
    "desc": "本接口(DownloadCustomerGatewayConfiguration)用于下载VPN通道配置。"
  },
  "DescribeVpcInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定RouteTableIds和Filters。\n<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>\n<li>instance-id - String - （过滤条件）云主机实例ID。</li>\n<li>instance-name - String - （过滤条件）云主机名称。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量。"
      },
      {
        "name": "Limit",
        "desc": "请求对象个数。"
      }
    ],
    "desc": " 本接口（DescribeVpcInstances）用于查询VPC下的云主机实例列表。"
  },
  "CreateDirectConnectGatewayCcnRoutes": {
    "params": [
      {
        "name": "DirectConnectGatewayId",
        "desc": "专线网关ID，形如：dcg-prpqlmg1"
      },
      {
        "name": "Routes",
        "desc": "需要连通的IDC网段列表"
      }
    ],
    "desc": "本接口（CreateDirectConnectGatewayCcnRoutes）用于创建专线网关的云联网路由（IDC网段）"
  },
  "DescribeSecurityGroupLimits": {
    "params": [],
    "desc": "本接口(DescribeSecurityGroupLimits)用于查询用户安全组配额。"
  },
  "DisassociateAddress": {
    "params": [
      {
        "name": "AddressId",
        "desc": "标识 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。"
      },
      {
        "name": "ReallocateNormalPublicIp",
        "desc": "表示解绑 EIP 之后是否分配普通公网 IP。取值范围：<br><li>TRUE：表示解绑 EIP 之后分配普通公网 IP。<br><li>FALSE：表示解绑 EIP 之后不分配普通公网 IP。<br>默认取值：FALSE。<br><br>只有满足以下条件时才能指定该参数：<br><li> 只有在解绑主网卡的主内网 IP 上的 EIP 时才能指定该参数。<br><li>解绑 EIP 后重新分配普通公网 IP 操作一个账号每天最多操作 10 次；详情可通过 [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378) 接口获取。"
      }
    ],
    "desc": "本接口 (DisassociateAddress) 用于解绑[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。\n* 支持CVM实例，弹性网卡上的EIP解绑\n* 不支持NAT上的EIP解绑。NAT上的EIP解绑请参考[EipUnBindNatGateway](https://cloud.tencent.com/document/product/215/4092)\n* 只有状态为 BIND 和 BIND_ENI 的 EIP 才能进行解绑定操作。\n* EIP 如果被封堵，则不能进行解绑定操作。"
  },
  "DescribeVpcPrivateIpAddresses": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC`实例`ID`，形如：`vpc-f49l6u0z`。"
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "内网`IP`地址列表，批量查询单次请求最多支持`10`个。"
      }
    ],
    "desc": "本接口（DescribeVpcPrivateIpAddresses）用于查询VPC内网IP信息。<br />\n只能查询已使用的IP信息，当查询未使用的IP时，本接口不会报错，但不会出现在返回结果里。"
  },
  "ModifyIpv6AddressesAttribute": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例`ID`，形如：`eni-m6dyj72l`。"
      },
      {
        "name": "Ipv6Addresses",
        "desc": "指定的内网IPv6`地址信息。"
      }
    ],
    "desc": "本接口（ModifyIpv6AddressesAttribute）用于修改弹性网卡内网IPv6地址属性。"
  },
  "DescribeDirectConnectGateways": {
    "params": [
      {
        "name": "DirectConnectGatewayIds",
        "desc": "专线网关唯一`ID`，形如：`dcg-9o233uri`。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定`DirectConnectGatewayIds`和`Filters`。\n<li>direct-connect-gateway-id - String - 专线网关唯一`ID`，形如：`dcg-9o233uri`。</li>\n<li>direct-connect-gateway-name - String - 专线网关名称，默认模糊查询。</li>\n<li>direct-connect-gateway-ip - String - 专线网关`IP`。</li>\n<li>gateway-type - String - 网关类型，可选值：`NORMAL`（普通型）、`NAT`（NAT型）。</li>\n<li>network-type- String - 网络类型，可选值：`VPC`（私有网络类型）、`CCN`（云联网类型）。</li>\n<li>ccn-id - String - 专线网关所在云联网`ID`。</li>\n<li>vpc-id - String - 专线网关所在私有网络`ID`。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量。"
      },
      {
        "name": "Limit",
        "desc": "返回数量。"
      }
    ],
    "desc": "本接口（DescribeDirectConnectGateways）用于查询专线网关。"
  },
  "DescribeSecurityGroupAssociationStatistics": {
    "params": [
      {
        "name": "SecurityGroupIds",
        "desc": "安全实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。"
      }
    ],
    "desc": "本接口（DescribeSecurityGroupAssociationStatistics）用于查询安全组关联的实例统计。"
  },
  "RenewVpnGateway": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID。"
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "预付费计费模式。"
      }
    ],
    "desc": "本接口（RenewVpnGateway）用于预付费（包年包月）VPN网关续费。目前只支持IPSEC网关。"
  },
  "AssignIpv6Addresses": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例`ID`，形如：`eni-m6dyj72l`。"
      },
      {
        "name": "Ipv6Addresses",
        "desc": "指定的`IPv6`地址列表，单次最多指定10个。与入参`Ipv6AddressCount`合并计算配额。与Ipv6AddressCount必填一个。"
      },
      {
        "name": "Ipv6AddressCount",
        "desc": "自动分配`IPv6`地址个数，内网IP地址个数总和不能超过配数。与入参`Ipv6Addresses`合并计算配额。与Ipv6Addresses必填一个。"
      }
    ],
    "desc": "本接口（AssignIpv6Addresses）用于弹性网卡申请`IPv6`地址。<br />\n本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口。\n* 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href=\"/document/product/576/18527\">弹性网卡使用限制</a>。\n* 可以指定`IPv6`地址申请，地址类型不能为主`IP`，`IPv6`地址暂时只支持作为辅助`IP`。\n* 地址必须要在弹性网卡所在子网内，而且不能被占用。\n* 在弹性网卡上申请一个到多个辅助`IPv6`地址，接口会在弹性网卡所在子网段内返回指定数量的辅助`IPv6`地址。"
  },
  "MigratePrivateIpAddress": {
    "params": [
      {
        "name": "SourceNetworkInterfaceId",
        "desc": "当内网IP绑定的弹性网卡实例ID，例如：eni-m6dyj72l。"
      },
      {
        "name": "DestinationNetworkInterfaceId",
        "desc": "待迁移的目的弹性网卡实例ID。"
      },
      {
        "name": "PrivateIpAddress",
        "desc": "迁移的内网IP地址，例如：10.0.0.6。"
      }
    ],
    "desc": " 本接口（MigratePrivateIpAddress）用于弹性网卡内网IP迁移。\n\n* 该接口用于将一个内网IP从一个弹性网卡上迁移到另外一个弹性网卡，主IP地址不支持迁移。\n* 迁移前后的弹性网卡必须在同一个子网内。"
  },
  "DescribeServiceTemplates": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>service-template-name - String - （过滤条件）协议端口模板名称。</li>\n<li>service-template-id - String - （过滤条件）协议端口模板实例ID，例如：ppm-e6dy460g。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeServiceTemplates）用于查询协议端口模板"
  },
  "UnassignIpv6CidrBlock": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`VPC`实例`ID`，形如：`vpc-f49l6u0z`。"
      },
      {
        "name": "Ipv6CidrBlock",
        "desc": "`IPv6`网段。形如：`3402:4e00:20:1000::/56`"
      }
    ],
    "desc": "本接口（UnassignIpv6CidrBlock）用于释放IPv6网段。<br />\n网段如果还有IP占用且未回收，则网段无法释放。"
  },
  "ModifyNatGatewayDestinationIpPortTranslationNatRule": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "NAT网关的ID，形如：`nat-df45454`。"
      },
      {
        "name": "SourceNatRule",
        "desc": "源NAT网关的端口转换规则。"
      },
      {
        "name": "DestinationNatRule",
        "desc": "目的NAT网关的端口转换规则。"
      }
    ],
    "desc": "本接口（ModifyNatGatewayDestinationIpPortTranslationNatRule）用于修改NAT网关端口转发规则。"
  },
  "DescribeVpcLimits": {
    "params": [
      {
        "name": "LimitTypes",
        "desc": "配额名称。每次最大查询100个配额类型。"
      }
    ],
    "desc": "获取私有网络配额，部分私有网络的配额有地域属性。\nLimitTypes取值范围：\n* appid-max-vpcs （每个开发商每个地域可创建的VPC数）\n* vpc-max-subnets（每个VPC可创建的子网数）\n* vpc-max-route-tables（每个VPC可创建的路由表数）\n* route-table-max-policies（每个路由表可添加的策略数）\n* vpc-max-vpn-gateways（每个VPC可创建的VPN网关数）\n* appid-max-custom-gateways（每个开发商可创建的对端网关数）\n* appid-max-vpn-connections（每个开发商可创建的VPN通道数）\n* custom-gateway-max-vpn-connections（每个对端网关可创建的VPN通道数）\n* vpn-gateway-max-custom-gateways（每个VPNGW可以创建的通道数）\n* vpc-max-network-acls（每个VPC可创建的网络ACL数）\n* network-acl-max-inbound-policies（每个网络ACL可添加的入站规则数）\n* network-acl-max-outbound-policies（每个网络ACL可添加的出站规则数）\n* vpc-max-vpcpeers（每个VPC可创建的对等连接数）\n* vpc-max-available-vpcpeers（每个VPC可创建的有效对等连接数）\n* vpc-max-basic-network-interconnections（每个VPC可创建的基础网络云主机与VPC互通数）\n* direct-connection-max-snats（每个专线网关可创建的SNAT数）\n* direct-connection-max-dnats（每个专线网关可创建的DNAT数）\n* direct-connection-max-snapts（每个专线网关可创建的SNAPT数）\n* direct-connection-max-dnapts（每个专线网关可创建的DNAPT数）\n* vpc-max-nat-gateways（每个VPC可创建的NAT网关数）\n* nat-gateway-max-eips（每个NAT可以购买的外网IP数量）\n* vpc-max-enis（每个VPC可创建弹性网卡数）\n* vpc-max-havips（每个VPC可创建HAVIP数）\n* eni-max-private-ips（每个ENI可以绑定的内网IP数（ENI未绑定子机））\n* nat-gateway-max-dnapts（每个NAT网关可创建的DNAPT数）\n* vpc-max-ipv6s（每个VPC可分配的IPv6地址数）\n* eni-max-ipv6s（每个ENI可分配的IPv6地址数）\n* vpc-max-assistant_cidrs（每个VPC可分配的辅助CIDR数）"
  },
  "HaVipAssociateAddressIp": {
    "params": [
      {
        "name": "HaVipId",
        "desc": "`HAVIP`唯一`ID`，形如：`havip-9o233uri`。必须是没有绑定`EIP`的`HAVIP`"
      },
      {
        "name": "AddressIp",
        "desc": "弹性公网`IP`。必须是没有绑定`HAVIP`的`EIP`"
      }
    ],
    "desc": "本接口（HaVipAssociateAddressIp）用于高可用虚拟IP（HAVIP）绑定弹性公网IP（EIP）<br />\n本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口"
  },
  "RemoveIp6Rules": {
    "params": [
      {
        "name": "Ip6TranslatorId",
        "desc": "IPV6转换规则所属的转换实例唯一ID，形如ip6-xxxxxxxx"
      },
      {
        "name": "Ip6RuleIds",
        "desc": "待删除IPV6转换规则，形如rule6-xxxxxxxx"
      }
    ],
    "desc": "1. 该接口用于删除IPV6转换规则\n2. 支持批量删除同一个转换实例下的多个转换规则"
  },
  "CheckDefaultSubnet": {
    "params": [
      {
        "name": "Zone",
        "desc": "子网所在的可用区ID，不同子网选择不同可用区可以做跨可用区灾备。"
      }
    ],
    "desc": "本接口（CheckDefaultSubnet）用于预判是否可建默认子网。"
  },
  "DescribeHaVips": {
    "params": [
      {
        "name": "HaVipIds",
        "desc": "`HAVIP`唯一`ID`，形如：`havip-9o233uri`。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定`HaVipIds`和`Filters`。\n<li>havip-id - String - `HAVIP`唯一`ID`，形如：`havip-9o233uri`。</li>\n<li>havip-name - String - `HAVIP`名称。</li>\n<li>vpc-id - String - `HAVIP`所在私有网络`ID`。</li>\n<li>subnet-id - String - `HAVIP`所在子网`ID`。</li>\n<li>vip - String - `HAVIP`的地址`VIP`。</li>\n<li>address-ip - String - `HAVIP`绑定的弹性公网`IP`。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      }
    ],
    "desc": "本接口（DescribeHaVips）用于查询高可用虚拟IP（HAVIP）列表。"
  },
  "AssociateNetworkInterfaceSecurityGroups": {
    "params": [
      {
        "name": "NetworkInterfaceIds",
        "desc": "弹性网卡实例ID。形如：eni-pxir56ns。每次请求的实例的上限为100。"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "安全组实例ID，例如：sg-33ocnj9n，可通过DescribeSecurityGroups获取。每次请求的实例的上限为100。"
      }
    ],
    "desc": "本接口（AssociateNetworkInterfaceSecurityGroups）用于弹性网卡绑定安全组（SecurityGroup）。"
  },
  "DeleteHaVip": {
    "params": [
      {
        "name": "HaVipId",
        "desc": "`HAVIP`唯一`ID`，形如：`havip-9o233uri`。"
      }
    ],
    "desc": "本接口（DeleteHaVip）用于删除高可用虚拟IP（HAVIP）<br />\n本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口"
  },
  "ModifyBandwidthPackageAttribute": {
    "params": [
      {
        "name": "BandwidthPackageId",
        "desc": "带宽包唯一标识ID"
      },
      {
        "name": "BandwidthPackageName",
        "desc": "带宽包名称"
      },
      {
        "name": "ChargeType",
        "desc": "带宽包计费模式"
      }
    ],
    "desc": "接口用于修改带宽包属性，包括带宽包名字等"
  },
  "DescribeAddressQuota": {
    "params": [],
    "desc": "本接口 (DescribeAddressQuota) 用于查询您账户的[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）在当前地域的配额信息。配额详情可参见 [EIP 产品简介](https://cloud.tencent.com/document/product/213/5733)。"
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
      },
      {
        "name": "InstanceChargeType",
        "desc": "VPN网关计费模式，目前只支持预付费（即包年包月）到后付费（即按量计费）的转换。即参数只支持：POSTPAID_BY_HOUR。"
      }
    ],
    "desc": "本接口（ModifyVpnGatewayAttribute）用于修改VPN网关属性。"
  },
  "ResetVpnGatewayInternetMaxBandwidth": {
    "params": [
      {
        "name": "VpnGatewayId",
        "desc": "VPN网关实例ID。"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "公网带宽设置。可选带宽规格：5, 10, 20, 50, 100；单位：Mbps。"
      }
    ],
    "desc": "本接口（ResetVpnGatewayInternetMaxBandwidth）调整VPN网关带宽上限。目前支持升级配置，如果是包年包月VPN网关需要在有效期内。"
  },
  "DeleteVpc": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      }
    ],
    "desc": "本接口（DeleteVpc）用于删除私有网络。\n* 删除前请确保 VPC 内已经没有相关资源，例如云服务器、云数据库、NoSQL、VPN网关、专线网关、负载均衡、对等连接、与之互通的基础网络设备等。\n* 删除私有网络是不可逆的操作，请谨慎处理。"
  },
  "DescribeSubnets": {
    "params": [
      {
        "name": "SubnetIds",
        "desc": "子网实例ID查询。形如：subnet-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定SubnetIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定SubnetIds和Filters。\n<li>subnet-id - String - （过滤条件）Subnet实例名称。</li>\n<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>\n<li>cidr-block - String - （过滤条件）子网网段，形如: 192.168.1.0 。</li>\n<li>is-default - Boolean - （过滤条件）是否是默认子网。</li>\n<li>is-remote-vpc-snat - Boolean - （过滤条件）是否为VPC SNAT地址池子网。</li>\n<li>subnet-name - String - （过滤条件）子网名称。</li>\n<li>zone - String - （过滤条件）可用区。</li>\n<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。</li>\n<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例2。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeSubnets）用于查询子网列表。"
  },
  "CreateCcn": {
    "params": [
      {
        "name": "CcnName",
        "desc": "CCN名称，最大长度不能超过60个字节。"
      },
      {
        "name": "CcnDescription",
        "desc": "CCN描述信息，最大长度不能超过100个字节。"
      },
      {
        "name": "QosLevel",
        "desc": "CCN服务质量，'PT'：白金，'AU'：金，'AG'：银，默认为‘AU’。"
      },
      {
        "name": "InstanceChargeType",
        "desc": "计费模式，PREPAID：表示预付费，即包年包月，POSTPAID：表示后付费，即按量计费。默认：POSTPAID。"
      },
      {
        "name": "BandwidthLimitType",
        "desc": "限速类型，OUTER_REGION_LIMIT表示地域出口限速，INTER_REGION_LIMIT为地域间限速，默认为OUTER_REGION_LIMIT"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "本接口（CreateCcn）用于创建云联网（CCN）。<br />\n* 创建云联网同时可以绑定标签, 应答里的标签列表代表添加成功的标签。\n每个账号能创建的云联网实例个数是有限的，详请参考产品文档。如果需要扩充请联系在线客服。"
  },
  "ModifyCustomerGatewayAttribute": {
    "params": [
      {
        "name": "CustomerGatewayId",
        "desc": "对端网关ID，例如：cgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。"
      },
      {
        "name": "CustomerGatewayName",
        "desc": "对端网关名称，可任意命名，但不得超过60个字符。"
      }
    ],
    "desc": "本接口（ModifyCustomerGatewayAttribute）用于修改对端网关信息。"
  },
  "DescribeNetworkAcls": {
    "params": [
      {
        "name": "NetworkAclIds",
        "desc": "网络ACL实例ID数组。形如：[acl-12345678]。每次请求的实例的上限为100。参数不支持同时指定NetworkAclIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定NetworkAclIds和Filters。\n<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-12345678。</li>\n<li>network-acl-id - String - （过滤条件）网络ACL实例ID，形如：acl-12345678。</li>\n<li>network-acl-name - String - （过滤条件）网络ACL实例名称。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最小值为1，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeNetworkAcls）用于查询网络ACL列表。"
  },
  "ModifyVpnConnectionAttribute": {
    "params": [
      {
        "name": "VpnConnectionId",
        "desc": "VPN通道实例ID。形如：vpnx-f49l6u0z。"
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
  "DescribeSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupIds",
        "desc": "安全组实例ID，例如：sg-33ocnj9n，可通过DescribeSecurityGroups获取。每次请求的实例的上限为100。参数不支持同时指定SecurityGroupIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定SecurityGroupIds和Filters。\n<li>security-group-id - String - （过滤条件）安全组ID。</li>\n<li>project-id - Integer - （过滤条件）项目ID。</li>\n<li>security-group-name - String - （过滤条件）安全组名称。</li>\n<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。使用请参考示例2。</li>\n<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例3。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeSecurityGroups）用于查询安全组。"
  },
  "CreateVpnGateway": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "VpnGatewayName",
        "desc": "VPN网关名称，最大长度不能超过60个字节。"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "公网带宽设置。可选带宽规格：5, 10, 20, 50, 100；单位：Mbps"
      },
      {
        "name": "InstanceChargeType",
        "desc": "VPN网关计费模式，PREPAID：表示预付费，即包年包月，POSTPAID_BY_HOUR：表示后付费，即按量计费。默认：POSTPAID_BY_HOUR，如果指定预付费模式，参数InstanceChargePrepaid必填。"
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。"
      },
      {
        "name": "Zone",
        "desc": "可用区，如：ap-guangzhou-2。"
      },
      {
        "name": "Type",
        "desc": "VPN网关类型。值“CCN”云联网类型VPN网关"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "本接口（CreateVpnGateway）用于创建VPN网关。"
  },
  "ModifyPrivateIpAddressesAttribute": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-m6dyj72l。"
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "指定的内网IP信息。"
      }
    ],
    "desc": "本接口（ModifyPrivateIpAddressesAttribute）用于修改弹性网卡内网IP属性。"
  },
  "DescribeAssistantCidr": {
    "params": [
      {
        "name": "VpcIds",
        "desc": "`VPC`实例`ID`数组。形如：[`vpc-6v2ht8q5`]"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定NetworkInterfaceIds和Filters。\n<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeAssistantCidr）用于查询辅助CIDR列表。（接口灰度中，如需使用请提工单。）"
  },
  "CreateDirectConnectGateway": {
    "params": [
      {
        "name": "DirectConnectGatewayName",
        "desc": "专线网关名称"
      },
      {
        "name": "NetworkType",
        "desc": "关联网络类型，可选值：\n<li>VPC - 私有网络</li>\n<li>CCN - 云联网</li>"
      },
      {
        "name": "NetworkInstanceId",
        "desc": "<li>NetworkType 为 VPC 时，这里传值为私有网络实例ID</li>\n<li>NetworkType 为 CCN 时，这里传值为云联网实例ID</li>"
      },
      {
        "name": "GatewayType",
        "desc": "网关类型，可选值：\n<li>NORMAL - （默认）标准型，注：云联网只支持标准型</li>\n<li>NAT - NAT型</li>NAT类型支持网络地址转换配置，类型确定后不能修改；一个私有网络可以创建一个NAT类型的专线网关和一个非NAT类型的专线网关"
      }
    ],
    "desc": "本接口（CreateDirectConnectGateway）用于创建专线网关。"
  },
  "DetachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。"
      },
      {
        "name": "Instances",
        "desc": "要解关联网络实例列表"
      }
    ],
    "desc": "本接口（DetachCcnInstances）用于从云联网实例中解关联指定的网络实例。<br />\n解关联网络实例后，相应的路由策略会一并删除。"
  },
  "DetachClassicLinkVpc": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "InstanceIds",
        "desc": "CVM实例ID查询。形如：ins-r8hr2upy。"
      }
    ],
    "desc": "本接口(DetachClassicLinkVpc)用于删除私有网络和基础网络设备互通。"
  },
  "EnableRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表唯一ID。"
      },
      {
        "name": "RouteIds",
        "desc": "路由策略ID。不能和RouteItemIds同时使用。"
      },
      {
        "name": "RouteItemIds",
        "desc": "路由策略唯一ID。不能和RouteIds同时使用。"
      }
    ],
    "desc": "本接口（EnableRoutes）用于启用已禁用的子网路由。<br />\n本接口会校验启用后，是否与已有路由冲突，如果冲突，则无法启用，失败处理。路由冲突时，需要先禁用与之冲突的路由，才能启用该路由。"
  },
  "SetCcnRegionBandwidthLimits": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。"
      },
      {
        "name": "CcnRegionBandwidthLimits",
        "desc": "云联网（CCN）各地域出带宽上限。"
      }
    ],
    "desc": "本接口（SetCcnRegionBandwidthLimits）用于设置云联网（CCN）各地域出带宽上限，或者地域间带宽上限。"
  },
  "CreateHaVip": {
    "params": [
      {
        "name": "VpcId",
        "desc": "`HAVIP`所在私有网络`ID`。"
      },
      {
        "name": "SubnetId",
        "desc": "`HAVIP`所在子网`ID`。"
      },
      {
        "name": "HaVipName",
        "desc": "`HAVIP`名称。"
      },
      {
        "name": "Vip",
        "desc": "指定虚拟IP地址，必须在`VPC`网段内且未被占用。不指定则自动分配。"
      }
    ],
    "desc": "本接口（CreateHaVip）用于创建高可用虚拟IP（HAVIP）"
  },
  "MigrateNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-m6dyj72l。"
      },
      {
        "name": "SourceInstanceId",
        "desc": "弹性网卡当前绑定的CVM实例ID。形如：ins-r8hr2upy。"
      },
      {
        "name": "DestinationInstanceId",
        "desc": "待迁移的目的CVM实例ID。"
      }
    ],
    "desc": "本接口（MigrateNetworkInterface）用于弹性网卡迁移。"
  },
  "ReleaseAddresses": {
    "params": [
      {
        "name": "AddressIds",
        "desc": "标识 EIP 的唯一 ID 列表。EIP 唯一 ID 形如：`eip-11112222`。"
      }
    ],
    "desc": "本接口 (ReleaseAddresses) 用于释放一个或多个[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。\n* 该操作不可逆，释放后 EIP 关联的 IP 地址将不再属于您的名下。\n* 只有状态为 UNBIND 的 EIP 才能进行释放操作。"
  },
  "DisassociateNetworkAclSubnets": {
    "params": [
      {
        "name": "NetworkAclId",
        "desc": "网络ACL实例ID。例如：acl-12345678。"
      },
      {
        "name": "SubnetIds",
        "desc": "子网实例ID数组。例如：[subnet-12345678]"
      }
    ],
    "desc": "本接口（DisassociateNetworkAclSubnets）用于网络ACL解关联vpc下的子网。"
  },
  "EnableCcnRoutes": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。"
      },
      {
        "name": "RouteIds",
        "desc": "CCN路由策略唯一ID。形如：ccnr-f49l6u0z。"
      }
    ],
    "desc": "本接口（EnableCcnRoutes）用于启用已经加入云联网（CCN）的路由。<br />\n本接口会校验启用后，是否与已有路由冲突，如果冲突，则无法启用，失败处理。路由冲突时，需要先禁用与之冲突的路由，才能启用该路由。"
  },
  "ModifyRouteTableAttribute": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表实例ID，例如：rtb-azd4dt1c。"
      },
      {
        "name": "RouteTableName",
        "desc": "路由表名称。"
      }
    ],
    "desc": "本接口（ModifyRouteTableAttribute）用于修改路由表（RouteTable）属性。"
  },
  "CreateNatGateway": {
    "params": [
      {
        "name": "NatGatewayName",
        "desc": "NAT网关名称"
      },
      {
        "name": "VpcId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "NAT网关最大外网出带宽(单位:Mbps)，支持的参数值：`20, 50, 100, 200, 500, 1000, 2000, 5000`，默认: `100Mbps`。"
      },
      {
        "name": "MaxConcurrentConnection",
        "desc": "NAT网关并发连接上限，支持参数值：`1000000、3000000、10000000`，默认值为`100000`。"
      },
      {
        "name": "AddressCount",
        "desc": "需要申请的弹性IP个数，系统会按您的要求生产N个弹性IP，其中AddressCount和PublicAddresses至少传递一个。"
      },
      {
        "name": "PublicIpAddresses",
        "desc": "绑定NAT网关的弹性IP数组，其中AddressCount和PublicAddresses至少传递一个。"
      },
      {
        "name": "Zone",
        "desc": "可用区，形如：`ap-guangzhou-1`。"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      },
      {
        "name": "SubnetId",
        "desc": "NAT网关所属子网"
      }
    ],
    "desc": "本接口(CreateNatGateway)用于创建NAT网关。"
  },
  "ModifyNetDetect": {
    "params": [
      {
        "name": "NetDetectId",
        "desc": "网络探测实例`ID`。形如：`netd-12345678`"
      },
      {
        "name": "NetDetectName",
        "desc": "网络探测名称，最大长度不能超过60个字节。"
      },
      {
        "name": "DetectDestinationIp",
        "desc": "探测目的IPv4地址数组，最多两个。"
      },
      {
        "name": "NextHopType",
        "desc": "下一跳类型，目前我们支持的类型有：\nVPN：VPN网关；\nDIRECTCONNECT：专线网关；\nPEERCONNECTION：对等连接；\nNAT：NAT网关；\nNORMAL_CVM：普通云服务器；"
      },
      {
        "name": "NextHopDestination",
        "desc": "下一跳目的网关，取值与“下一跳类型”相关：\n下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；\n下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；\n下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；\n下一跳类型为NAT，取值Nat网关，形如：nat-12345678；\n下一跳类型为NORMAL_CVM，取值云服务器IPv4地址，形如：10.0.0.12；"
      },
      {
        "name": "NetDetectDescription",
        "desc": "网络探测描述。"
      }
    ],
    "desc": "本接口(ModifyNetDetect)用于修改网络探测参数。"
  },
  "DisableGatewayFlowMonitor": {
    "params": [
      {
        "name": "GatewayId",
        "desc": "网关实例ID，目前我们支持的网关实例类型有，\n专线网关实例ID，形如，`dcg-ltjahce6`；\nNat网关实例ID，形如，`nat-ltjahce6`；\nVPN网关实例ID，形如，`vpn-ltjahce6`。"
      }
    ],
    "desc": "本接口（DisableGatewayFlowMonitor）用于关闭网关流量监控。"
  },
  "DeleteNatGatewayDestinationIpPortTranslationNatRule": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "NAT网关的ID，形如：`nat-df45454`。"
      },
      {
        "name": "DestinationIpPortTranslationNatRules",
        "desc": "NAT网关的端口转换规则。"
      }
    ],
    "desc": "本接口（DeleteNatGatewayDestinationIpPortTranslationNatRule）用于删除NAT网关端口转发规则。"
  },
  "CreateRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表实例ID。"
      },
      {
        "name": "Routes",
        "desc": "路由策略对象。"
      }
    ],
    "desc": "本接口(CreateRoutes)用于创建路由策略。\n* 向指定路由表批量新增路由策略。"
  },
  "DescribeBandwidthPackageQuota": {
    "params": [],
    "desc": "接口用于查询账户在当前地域的带宽包上限数量以及使用数量"
  },
  "ModifyHaVipAttribute": {
    "params": [
      {
        "name": "HaVipId",
        "desc": "`HAVIP`唯一`ID`，形如：`havip-9o233uri`。"
      },
      {
        "name": "HaVipName",
        "desc": "`HAVIP`名称，可任意命名，但不得超过60个字符。"
      }
    ],
    "desc": "本接口（ModifyHaVipAttribute）用于修改高可用虚拟IP（HAVIP）属性"
  },
  "ResetAttachCcnInstances": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。"
      },
      {
        "name": "CcnUin",
        "desc": "CCN所属UIN（根账号）。"
      },
      {
        "name": "Instances",
        "desc": "重新申请关联网络实例列表。"
      }
    ],
    "desc": "本接口（ResetAttachCcnInstances）用于跨账号关联实例申请过期时，重新申请关联操作。"
  },
  "DescribeBandwidthPackages": {
    "params": [
      {
        "name": "BandwidthPackageIds",
        "desc": "带宽包唯一ID列表"
      },
      {
        "name": "Filters",
        "desc": "每次请求的`Filters`的上限为10。参数不支持同时指定`BandwidthPackageIds`和`Filters`。详细的过滤条件如下：\n<li> bandwidth-package_id - String - 是否必填：否 - （过滤条件）按照带宽包的唯一标识ID过滤。</li>\n<li> bandwidth-package-name - String - 是否必填：否 - （过滤条件）按照 带宽包名称过滤。不支持模糊过滤。</li>\n<li> network-type - String - 是否必填：否 - （过滤条件）按照带宽包的类型过滤。类型包括'BGP','SINGLEISP'和'ANYCAST'。</li>\n<li> charge-type - String - 是否必填：否 - （过滤条件）按照带宽包的计费类型过滤。计费类型包括'TOP5_POSTPAID_BY_MONTH'和'PERCENT95_POSTPAID_BY_MONTH'</li>\n<li> resource.resource-type - String - 是否必填：否 - （过滤条件）按照带宽包资源类型过滤。资源类型包括'Address'和'LoadBalance'</li>\n<li> resource.resource-id - String - 是否必填：否 - （过滤条件）按照带宽包资源Id过滤。资源Id形如'eip-xxxx','lb-xxxx'</li>\n<li> resource.address-ip - String - 是否必填：否 - （过滤条件）按照带宽包资源Ip过滤。</li>"
      },
      {
        "name": "Offset",
        "desc": "查询带宽包偏移量"
      },
      {
        "name": "Limit",
        "desc": "查询带宽包数量限制"
      }
    ],
    "desc": "接口用于查询带宽包详细信息，包括带宽包唯一标识ID，类型，计费模式，名称，资源信息等"
  },
  "CreateServiceTemplateGroup": {
    "params": [
      {
        "name": "ServiceTemplateGroupName",
        "desc": "协议端口模板集合名称"
      },
      {
        "name": "ServiceTemplateIds",
        "desc": "协议端口模板实例ID，例如：ppm-4dw6agho。"
      }
    ],
    "desc": "本接口（CreateServiceTemplateGroup）用于创建协议端口模板集合"
  },
  "ReleaseIp6AddressesBandwidth": {
    "params": [
      {
        "name": "Ip6Addresses",
        "desc": "IPV6地址。Ip6Addresses和Ip6AddressIds必须且只能传一个"
      },
      {
        "name": "Ip6AddressIds",
        "desc": "IPV6地址对应的唯一ID，形如eip-xxxxxxxx。Ip6Addresses和Ip6AddressIds必须且只能传一个。"
      }
    ],
    "desc": "该接口用于给弹性公网IPv6地址释放带宽。"
  },
  "CreateDhcpIp": {
    "params": [
      {
        "name": "VpcId",
        "desc": "私有网络`ID`。"
      },
      {
        "name": "SubnetId",
        "desc": "子网`ID`。"
      },
      {
        "name": "DhcpIpName",
        "desc": "`DhcpIp`名称。"
      },
      {
        "name": "SecondaryPrivateIpAddressCount",
        "desc": "新申请的内网IP地址个数。总数不能超过64个。"
      }
    ],
    "desc": "本接口（CreateDhcpIp）用于创建DhcpIp"
  },
  "ReplaceRoutes": {
    "params": [
      {
        "name": "RouteTableId",
        "desc": "路由表实例ID，例如：rtb-azd4dt1c。"
      },
      {
        "name": "Routes",
        "desc": "路由策略对象。需要指定路由策略ID（RouteId）。"
      }
    ],
    "desc": "本接口（ReplaceRoutes）根据路由策略ID（RouteId）修改指定的路由策略（Route），支持批量修改。"
  },
  "ModifyCcnAttribute": {
    "params": [
      {
        "name": "CcnId",
        "desc": "CCN实例ID。形如：ccn-f49l6u0z。"
      },
      {
        "name": "CcnName",
        "desc": "CCN名称，最大长度不能超过60个字节。"
      },
      {
        "name": "CcnDescription",
        "desc": "CCN描述信息，最大长度不能超过100个字节。"
      }
    ],
    "desc": "本接口（ModifyCcnAttribute）用于修改云联网（CCN）的相关属性。"
  },
  "CreateAddressTemplateGroup": {
    "params": [
      {
        "name": "AddressTemplateGroupName",
        "desc": "IP地址模版集合名称。"
      },
      {
        "name": "AddressTemplateIds",
        "desc": "IP地址模版实例ID，例如：ipm-mdunqeb6。"
      }
    ],
    "desc": "本接口（CreateAddressTemplateGroup）用于创建IP地址模版集合"
  },
  "ModifyIp6Translator": {
    "params": [
      {
        "name": "Ip6TranslatorId",
        "desc": "IPV6转换实例唯一ID，形如ip6-xxxxxxxxx"
      },
      {
        "name": "Ip6TranslatorName",
        "desc": "IPV6转换实例修改名称"
      }
    ],
    "desc": "该接口用于修改IP6转换实例属性，当前仅支持修改实例名称。"
  },
  "UnassignIpv6SubnetCidrBlock": {
    "params": [
      {
        "name": "VpcId",
        "desc": "子网所在私有网络`ID`。形如：`vpc-f49l6u0z`。"
      },
      {
        "name": "Ipv6SubnetCidrBlocks",
        "desc": "`IPv6` 子网段列表。"
      }
    ],
    "desc": "本接口（UnassignIpv6SubnetCidrBlock）用于释放IPv6子网段。<br />\n子网段如果还有IP占用且未回收，则子网段无法释放。"
  },
  "ModifyIp6AddressesBandwidth": {
    "params": [
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "修改的目标带宽，单位Mbps"
      },
      {
        "name": "Ip6Addresses",
        "desc": "IPV6地址。Ip6Addresses和Ip6AddressId必须且只能传一个"
      },
      {
        "name": "Ip6AddressIds",
        "desc": "IPV6地址对应的唯一ID，形如eip-xxxxxxxx。Ip6Addresses和Ip6AddressId必须且只能传一个"
      }
    ],
    "desc": "该接口用于修改IPV6地址访问internet的带宽"
  },
  "DescribeAddressTemplates": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>address-template-name - String - （过滤条件）IP地址模板名称。</li>\n<li>address-template-id - String - （过滤条件）IP地址模板实例ID，例如：ipm-mdunqeb6。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeAddressTemplates）用于查询IP地址模板"
  },
  "CreateAddressTemplate": {
    "params": [
      {
        "name": "AddressTemplateName",
        "desc": "IP地址模版名称"
      },
      {
        "name": "Addresses",
        "desc": "地址信息，支持 IP、CIDR、IP 范围。"
      }
    ],
    "desc": "本接口（CreateAddressTemplate）用于创建IP地址模版"
  },
  "ModifyAddressAttribute": {
    "params": [
      {
        "name": "AddressId",
        "desc": "标识 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。"
      },
      {
        "name": "AddressName",
        "desc": "修改后的 EIP 名称。长度上限为20个字符。"
      },
      {
        "name": "EipDirectConnection",
        "desc": "设定EIP是否直通，\"TRUE\"表示直通，\"FALSE\"表示非直通。注意该参数仅对EIP直通功能可见的用户可以设定。"
      }
    ],
    "desc": "本接口 (ModifyAddressAttribute) 用于修改[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）的名称。"
  },
  "DescribeAddressTemplateGroups": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>address-template-group-name - String - （过滤条件）IP地址模板集合名称。</li>\n<li>address-template-group-id - String - （过滤条件）IP地址模板实集合例ID，例如：ipmg-mdunqeb6。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口（DescribeAddressTemplateGroups）用于查询IP地址模板集合"
  },
  "TransformAddress": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待操作有普通公网 IP 的实例 ID。实例 ID 形如：`ins-11112222`。可通过登录[控制台](https://console.cloud.tencent.com/cvm)查询，也可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/9389) 接口返回值中的`InstanceId`获取。"
      }
    ],
    "desc": "本接口 (TransformAddress) 用于将实例的普通公网 IP 转换为[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。\n* 平台对用户每地域每日解绑 EIP 重新分配普通公网 IP 次数有所限制（可参见 [EIP 产品简介](/document/product/213/1941)）。上述配额可通过 [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378) 接口获取。"
  },
  "CreateSecurityGroupWithPolicies": {
    "params": [
      {
        "name": "GroupName",
        "desc": "安全组名称，可任意命名，但不得超过60个字符。"
      },
      {
        "name": "GroupDescription",
        "desc": "安全组备注，最多100个字符。"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，默认0。可在qcloud控制台项目管理页面查询到。"
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "安全组规则集合。"
      }
    ],
    "desc": "本接口（CreateSecurityGroupWithPolicies）用于创建新的安全组（SecurityGroup），并且可以同时添加安全组规则（SecurityGroupPolicy）。\n* 每个账户下每个地域的每个项目的<a href=\"https://cloud.tencent.com/document/product/213/12453\">安全组数量限制</a>。\n* 新建的安全组的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用CreateSecurityGroupPolicies将安全组的规则设置为需要的规则。\n\n安全组规则说明：\n* Version安全组规则版本号，用户每次更新安全规则版本会自动加1，防止您更新的路由规则已过期，不填不考虑冲突。\n* Protocol字段支持输入TCP, UDP, ICMP, ICMPV6, GRE, ALL。\n* CidrBlock字段允许输入符合cidr格式标准的任意字符串。(展开)在基础网络中，如果CidrBlock包含您的账户内的云服务器之外的设备在腾讯云的内网IP，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。\n* Ipv6CidrBlock字段允许输入符合IPv6 cidr格式标准的任意字符串。(展开)在基础网络中，如果Ipv6CidrBlock包含您的账户内的云服务器之外的设备在腾讯云的内网IPv6，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。\n* SecurityGroupId字段允许输入与待修改的安全组位于相同项目中的安全组ID，包括这个安全组ID本身，代表安全组下所有云服务器的内网IP。使用这个字段时，这条规则用来匹配网络报文的过程中会随着被使用的这个ID所关联的云服务器变化而变化，不需要重新修改。\n* Port字段允许输入一个单独端口号，或者用减号分隔的两个端口号代表端口范围，例如80或8000-8010。只有当Protocol字段是TCP或UDP时，Port字段才被接受，即Protocol字段不是TCP或UDP时，Protocol和Port排他关系，不允许同时输入，否则会接口报错。\n* Action字段只允许输入ACCEPT或DROP。\n* CidrBlock, Ipv6CidrBlock, SecurityGroupId, AddressTemplate四者是排他关系，不允许同时输入，Protocol + Port和ServiceTemplate二者是排他关系，不允许同时输入。\n* 一次请求中只能创建单个方向的规则, 如果需要指定索引（PolicyIndex）参数, 多条规则的索引必须一致。"
  },
  "CreateSecurityGroupPolicies": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。"
      },
      {
        "name": "SecurityGroupPolicySet",
        "desc": "安全组规则集合。"
      }
    ],
    "desc": "本接口（CreateSecurityGroupPolicies）用于创建安全组规则（SecurityGroupPolicy）。\n\n在 SecurityGroupPolicySet 参数中：\n<ul>\n<li>Version 安全组规则版本号，用户每次更新安全规则版本会自动加1，防止您更新的路由规则已过期，不填不考虑冲突。</li>\n<li>在创建出站和入站规则（Egress 和 Ingress）时：<ul>\n<li>Protocol 字段支持输入TCP, UDP, ICMP, ICMPV6, GRE, ALL。</li>\n<li>CidrBlock 字段允许输入符合cidr格式标准的任意字符串。(展开)在基础网络中，如果 CidrBlock 包含您的账户内的云服务器之外的设备在腾讯云的内网 IP，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。</li>\n<li>Ipv6CidrBlock 字段允许输入符合IPv6 cidr格式标准的任意字符串。(展开)在基础网络中，如果Ipv6CidrBlock 包含您的账户内的云服务器之外的设备在腾讯云的内网 IPv6，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。</li>\n<li>SecurityGroupId 字段允许输入与待修改的安全组位于相同项目中的安全组 ID，包括这个安全组 ID 本身，代表安全组下所有云服务器的内网 IP。使用这个字段时，这条规则用来匹配网络报文的过程中会随着被使用的这个 ID 所关联的云服务器变化而变化，不需要重新修改。</li>\n<li>Port 字段允许输入一个单独端口号，或者用减号分隔的两个端口号代表端口范围，例如80或8000-8010。只有当 Protocol 字段是 TCP 或 UDP 时，Port 字段才被接受，即 Protocol 字段不是 TCP 或 UDP 时，Protocol 和 Port 排他关系，不允许同时输入，否则会接口报错。</li>\n<li>Action 字段只允许输入 ACCEPT 或 DROP。</li>\n<li>CidrBlock, Ipv6CidrBlock, SecurityGroupId, AddressTemplate 四者是排他关系，不允许同时输入，Protocol + Port 和 ServiceTemplate 二者是排他关系，不允许同时输入。</li>\n<li>一次请求中只能创建单个方向的规则, 如果需要指定索引（PolicyIndex）参数, 多条规则的索引必须一致。</li>\n</ul></li></ul>"
  },
  "ModifyNetworkAclAttribute": {
    "params": [
      {
        "name": "NetworkAclId",
        "desc": "网络ACL实例ID。例如：acl-12345678。"
      },
      {
        "name": "NetworkAclName",
        "desc": "网络ACL名称，最大长度不能超过60个字节。"
      }
    ],
    "desc": "本接口（ModifyNetworkAclAttribute）用于修改网络ACL属性。"
  },
  "ResetNatGatewayConnection": {
    "params": [
      {
        "name": "NatGatewayId",
        "desc": "NAT网关ID。"
      },
      {
        "name": "MaxConcurrentConnection",
        "desc": "NAT网关并发连接上限，形如：1000000、3000000、10000000。"
      }
    ],
    "desc": "本接口（ResetNatGatewayConnection）用来NAT网关并发连接上限。"
  },
  "ModifyVpcAttribute": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。"
      },
      {
        "name": "VpcName",
        "desc": "私有网络名称，可任意命名，但不得超过60个字符。"
      },
      {
        "name": "EnableMulticast",
        "desc": "是否开启组播。true: 开启, false: 关闭。"
      },
      {
        "name": "DnsServers",
        "desc": "DNS地址，最多支持4个，第1个默认为主，其余为备"
      },
      {
        "name": "DomainName",
        "desc": "域名"
      }
    ],
    "desc": "本接口（ModifyVpcAttribute）用于修改私有网络（VPC）的相关属性。"
  },
  "DescribeIp6TranslatorQuota": {
    "params": [
      {
        "name": "Ip6TranslatorIds",
        "desc": "待查询IPV6转换实例的唯一ID列表，形如ip6-xxxxxxxx"
      }
    ],
    "desc": "查询账户在指定地域IPV6转换实例和规则的配额"
  }
}