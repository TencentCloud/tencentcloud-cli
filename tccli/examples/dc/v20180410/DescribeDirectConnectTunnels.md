**Example 1: 查询BGP路由的专用通道**

查询BGP路由的专用通道。

Input: 

```
tccli dc DescribeDirectConnectTunnels --cli-unfold-argument  \
    --Filters.0.Name direct-connect-tunnel-id \
    --Filters.0.Values dcx-047zz5e6 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "DirectConnectTunnelSet": [
            {
                "OwnerAccount": "100001332514",
                "DirectConnectOwnerAccount": "100001332514",
                "DirectConnectId": "dc-n6c9vvv3",
                "SignLaw": true,
                "DirectConnectTunnelId": "dcx-047zz5e6",
                "DirectConnectTunnelName": "DCXCCNVxlanBgpEcmpTestautotestdcxtwo",
                "State": "AVAILABLE",
                "VpcId": "",
                "NetworkRegion": "ap-chongqing",
                "VpcRegion": "cq",
                "DirectConnectGatewayId": "dcg-meljxc9n",
                "Bandwidth": 100,
                "Vlan": 2432,
                "TencentAddress": "192.168.0.3/29",
                "CustomerAddress": "192.168.0.1/29",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "NetDetectId": "",
                "EnableBGPCommunity": false,
                "NatType": 0,
                "BfdEnable": 0,
                "AccessPointType": "VXLAN",
                "DirectConnectGatewayName": "",
                "VpcName": "",
                "ShareOrNot": 0,
                "TencentBackupAddress": "192.168.0.2/29",
                "NetworkType": "CCN",
                "CloudAttachId": null,
                "RouteType": "BGP",
                "BgpPeer": {
                    "Asn": 65120,
                    "AuthKey": "tencent"
                },
                "RouteFilterPrefixes": [],
                "TagSet": []
            }
        ],
        "RequestId": "8ae32da8-db96-400f-908e-0de2c89e96ea",
        "TotalCount": 1
    }
}
```

**Example 2: 查询STATIC路由的专用通道**

查询STATIC路由的专用通道。

Input: 

```
tccli dc DescribeDirectConnectTunnels --cli-unfold-argument  \
    --Filters.0.Name direct-connect-tunnel-id \
    --Filters.0.Values dcx-ltcfypom \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "DirectConnectTunnelSet": [
            {
                "OwnerAccount": "100001332514",
                "DirectConnectOwnerAccount": "100001332514",
                "DirectConnectId": "dc-n6c9vvv3",
                "SignLaw": true,
                "DirectConnectTunnelId": "dcx-ltcfypom",
                "DirectConnectTunnelName": "DCXVPCVxlanStaticEcmpTestautotestdcxone",
                "State": "AVAILABLE",
                "VpcId": "vpc-q1cy5hgx",
                "NetworkRegion": "ap-chongqing",
                "VpcRegion": "cq",
                "DirectConnectGatewayId": "dcg-f5ucfdg3",
                "Bandwidth": 100,
                "Vlan": 2414,
                "TencentAddress": "192.168.0.3/29",
                "CustomerAddress": "192.168.0.1/29",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "NetDetectId": "",
                "EnableBGPCommunity": false,
                "NatType": 0,
                "BfdEnable": 0,
                "AccessPointType": "VXLAN",
                "DirectConnectGatewayName": "",
                "VpcName": "",
                "ShareOrNot": 0,
                "TencentBackupAddress": "",
                "NetworkType": "VPC",
                "CloudAttachId": null,
                "RouteType": "STATIC",
                "RouteFilterPrefixes": [
                    {
                        "Cidr": "19.244.99.224/32"
                    }
                ],
                "BgpPeer": {
                    "Asn": -1,
                    "AuthKey": ""
                },
                "TagSet": []
            }
        ],
        "RequestId": "8ae32da8-db96-400f-908e-0de2c89e96ea",
        "TotalCount": 1
    }
}
```

