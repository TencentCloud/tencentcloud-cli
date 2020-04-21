# -*- coding: utf-8 -*-
DESC = "dc-2018-04-10"
INFO = {
  "ModifyDirectConnectAttribute": {
    "params": [
      {
        "name": "DirectConnectId",
        "desc": "物理专线的ID。"
      },
      {
        "name": "DirectConnectName",
        "desc": "物理专线名称。"
      },
      {
        "name": "CircuitCode",
        "desc": "运营商或者服务商为物理专线提供的电路编码。"
      },
      {
        "name": "Vlan",
        "desc": "物理专线调试VLAN。"
      },
      {
        "name": "TencentAddress",
        "desc": "物理专线调试腾讯侧互联 IP。"
      },
      {
        "name": "CustomerAddress",
        "desc": "物理专线调试用户侧互联 IP。"
      },
      {
        "name": "CustomerName",
        "desc": "物理专线申请者姓名。默认从账户体系获取。"
      },
      {
        "name": "CustomerContactMail",
        "desc": "物理专线申请者联系邮箱。默认从账户体系获取。"
      },
      {
        "name": "CustomerContactNumber",
        "desc": "物理专线申请者联系号码。默认从账户体系获取。"
      },
      {
        "name": "FaultReportContactPerson",
        "desc": "报障联系人。"
      },
      {
        "name": "FaultReportContactNumber",
        "desc": "报障联系电话。"
      }
    ],
    "desc": "修改物理专线的属性。"
  },
  "CreateDirectConnectTunnel": {
    "params": [
      {
        "name": "DirectConnectId",
        "desc": "专线 ID，例如：dc-kd7d06of"
      },
      {
        "name": "DirectConnectTunnelName",
        "desc": "专用通道名称"
      },
      {
        "name": "DirectConnectOwnerAccount",
        "desc": "物理专线 owner，缺省为当前客户（物理专线 owner）\n共享专线时这里需要填写共享专线的开发商账号 ID"
      },
      {
        "name": "NetworkType",
        "desc": "网络类型，分别为VPC、BMVPC，CCN，默认是VPC\nVPC：私有网络\nBMVPC：黑石网络\nCCN：云联网"
      },
      {
        "name": "NetworkRegion",
        "desc": "网络地域"
      },
      {
        "name": "VpcId",
        "desc": "私有网络统一 ID 或者黑石网络统一 ID"
      },
      {
        "name": "DirectConnectGatewayId",
        "desc": "专线网关 ID，例如 dcg-d545ddf"
      },
      {
        "name": "Bandwidth",
        "desc": "专线带宽，单位：Mbps\n默认是物理专线带宽值"
      },
      {
        "name": "RouteType",
        "desc": "BGP ：BGP路由\nSTATIC：静态\n默认为 BGP 路由"
      },
      {
        "name": "BgpPeer",
        "desc": "BgpPeer，用户侧bgp信息，包括Asn和AuthKey"
      },
      {
        "name": "RouteFilterPrefixes",
        "desc": "静态路由，用户IDC的网段地址"
      },
      {
        "name": "Vlan",
        "desc": "vlan，范围：0 ~ 3000\n0：不开启子接口\n默认值是非0"
      },
      {
        "name": "TencentAddress",
        "desc": "TencentAddress，腾讯侧互联 IP"
      },
      {
        "name": "CustomerAddress",
        "desc": "CustomerAddress，用户侧互联 IP"
      },
      {
        "name": "TencentBackupAddress",
        "desc": "TencentBackupAddress，腾讯侧备用互联 IP"
      }
    ],
    "desc": "用于创建专用通道的接口"
  },
  "DeleteDirectConnect": {
    "params": [
      {
        "name": "DirectConnectId",
        "desc": "物理专线的ID。"
      }
    ],
    "desc": "删除物理专线。\n只能删除处于已连接状态的物理专线。"
  },
  "AcceptDirectConnectTunnel": {
    "params": [
      {
        "name": "DirectConnectTunnelId",
        "desc": "物理专线拥有者接受共享专用通道申请"
      }
    ],
    "desc": "接受专用通道申请"
  },
  "DeleteDirectConnectTunnel": {
    "params": [
      {
        "name": "DirectConnectTunnelId",
        "desc": "专用通道ID"
      }
    ],
    "desc": "删除专用通道"
  },
  "CreateDirectConnect": {
    "params": [
      {
        "name": "DirectConnectName",
        "desc": "物理专线的名称。"
      },
      {
        "name": "AccessPointId",
        "desc": "物理专线所在的接入点。\n您可以通过调用 DescribeAccessPoints接口获取地域ID。所选择的接入点必须存在且处于可接入的状态。"
      },
      {
        "name": "LineOperator",
        "desc": "提供接入物理专线的运营商。ChinaTelecom：中国电信， ChinaMobile：中国移动，ChinaUnicom：中国联通， In-houseWiring：楼内线，ChinaOther：中国其他， InternationalOperator：境外其他。"
      },
      {
        "name": "Location",
        "desc": "本地数据中心的地理位置。"
      },
      {
        "name": "PortType",
        "desc": "物理专线接入端口类型,取值：100Base-T：百兆电口,1000Base-T（默认值）：千兆电口,1000Base-LX：千兆单模光口（10千米）,10GBase-T：万兆电口10GBase-LR：万兆单模光口（10千米），默认值，千兆单模光口（10千米）。"
      },
      {
        "name": "CircuitCode",
        "desc": "运营商或者服务商为物理专线提供的电路编码。"
      },
      {
        "name": "Bandwidth",
        "desc": "物理专线接入接口带宽，单位为Mbps，默认值为1000，取值范围为 [2, 10240]。"
      },
      {
        "name": "RedundantDirectConnectId",
        "desc": "冗余物理专线的ID。"
      },
      {
        "name": "Vlan",
        "desc": "物理专线调试VLAN。默认开启VLAN，自动分配VLAN。"
      },
      {
        "name": "TencentAddress",
        "desc": "物理专线调试腾讯侧互联 IP。默认自动分配。"
      },
      {
        "name": "CustomerAddress",
        "desc": "物理专线调试用户侧互联 IP。默认自动分配。"
      },
      {
        "name": "CustomerName",
        "desc": "物理专线申请者姓名。默认从账户体系获取。"
      },
      {
        "name": "CustomerContactMail",
        "desc": "物理专线申请者联系邮箱。默认从账户体系获取。"
      },
      {
        "name": "CustomerContactNumber",
        "desc": "物理专线申请者联系号码。默认从账户体系获取。"
      },
      {
        "name": "FaultReportContactPerson",
        "desc": "报障联系人。"
      },
      {
        "name": "FaultReportContactNumber",
        "desc": "报障联系电话。"
      }
    ],
    "desc": "申请物理专线接入。\n调用该接口时，请注意：\n账号要进行实名认证，否则不允许申请物理专线；\n若账户下存在欠费状态的物理专线，则不能申请更多的物理专线。"
  },
  "DescribeDirectConnectTunnels": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件:\n参数不支持同时指定DirectConnectTunnelIds和Filters。\n<li> direct-connect-tunnel-name, 专用通道名称。</li>\n<li> direct-connect-tunnel-id, 专用通道实例ID，如dcx-abcdefgh。</li>\n<li>direct-connect-id, 物理专线实例ID，如，dc-abcdefgh。</li>"
      },
      {
        "name": "DirectConnectTunnelIds",
        "desc": "专用通道 ID数组"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100"
      }
    ],
    "desc": "用于查询专用通道列表。"
  },
  "DescribeAccessPoints": {
    "params": [
      {
        "name": "RegionId",
        "desc": "接入点所在的地域。使用DescribeRegions查询\n\n您可以通过调用 DescribeRegions接口获取地域ID。"
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
    "desc": "查询物理专线接入点\n"
  },
  "RejectDirectConnectTunnel": {
    "params": [
      {
        "name": "DirectConnectTunnelId",
        "desc": "无"
      }
    ],
    "desc": "拒绝专用通道申请"
  },
  "DescribeDirectConnects": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件:"
      },
      {
        "name": "DirectConnectIds",
        "desc": "物理专线 ID数组"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100"
      }
    ],
    "desc": "查询物理专线列表。"
  },
  "ModifyDirectConnectTunnelAttribute": {
    "params": [
      {
        "name": "DirectConnectTunnelId",
        "desc": "专用通道ID"
      },
      {
        "name": "DirectConnectTunnelName",
        "desc": "专用通道名称"
      },
      {
        "name": "BgpPeer",
        "desc": "用户侧BGP，包括Asn，AuthKey"
      },
      {
        "name": "RouteFilterPrefixes",
        "desc": "用户侧网段地址"
      },
      {
        "name": "TencentAddress",
        "desc": "腾讯侧互联IP"
      },
      {
        "name": "CustomerAddress",
        "desc": "用户侧互联IP"
      },
      {
        "name": "Bandwidth",
        "desc": "专用通道带宽值，单位为M。"
      },
      {
        "name": "TencentBackupAddress",
        "desc": "腾讯侧备用互联IP"
      }
    ],
    "desc": "修改专用通道属性"
  }
}