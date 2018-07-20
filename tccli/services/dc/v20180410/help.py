# -*- coding: utf-8 -*-
DESC = "dc-2018-04-10"
INFO = {
  "CreateDirectConnectTunnel": {
    "params": [
      {
        "name": "DirectConnectId",
        "desc": "专线 ID，例如：dc-kd7d06of"
      },
      {
        "name": "DirectConnectTunnelName",
        "desc": "专线通道名称"
      },
      {
        "name": "DirectConnectOwnerAccount",
        "desc": "物理专线 owner，缺省为当前客户（物理专线 owner）\n共享专线时这里需要填写共享专线的开发商账号 ID"
      },
      {
        "name": "NetworkType",
        "desc": "网络类型，分别为VPC、BMVPC\nVPC：私有网络\nBMVPC：黑石网络"
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
        "desc": "BgpPeer，用户侧bgp信息，包括asn和AuthKey"
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
      }
    ],
    "desc": "用于创建专线通道的接口"
  },
  "DescribeDirectConnectTunnels": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件:\n参数不支持同时指定DirectConnectTunnelIds和Filters。\n<li> direct-connect-tunnel-name, 专线通道名称。</li>\n<li> direct-connect-tunnel-id, 专线通道实例ID，如dcx-abcdefgh。</li>\n<li>direct-connect-id, 物理专线实例ID，如，dc-abcdefgh。</li>"
      },
      {
        "name": "DirectConnectTunnelIds",
        "desc": "专线通道 ID数组"
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
    "desc": "用于查询专线通道列表。"
  },
  "AcceptDirectConnectTunnel": {
    "params": [
      {
        "name": "DirectConnectTunnelId",
        "desc": "物理专线拥有者接受共享专线通道申请"
      }
    ],
    "desc": "接受专线通道申请"
  },
  "DeleteDirectConnectTunnel": {
    "params": [
      {
        "name": "DirectConnectTunnelId",
        "desc": "专线通道ID"
      }
    ],
    "desc": "删除专线通道"
  },
  "RejectDirectConnectTunnel": {
    "params": [
      {
        "name": "DirectConnectTunnelId",
        "desc": "无"
      }
    ],
    "desc": "拒绝专线通道申请"
  },
  "ModifyDirectConnectTunnelAttribute": {
    "params": [
      {
        "name": "DirectConnectTunnelId",
        "desc": "专线通道ID"
      },
      {
        "name": "DirectConnectTunnelName",
        "desc": "专线通道名称"
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
        "desc": "专线通道带宽值，单位为M。"
      }
    ],
    "desc": "修改专线通道属性"
  }
}