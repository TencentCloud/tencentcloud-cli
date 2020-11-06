**Example 1: 查询BGP路由的专用通道**



Input: 

```
tccli dc DescribeDirectConnectTunnels --cli-unfold-argument  \
    --Filters.0.Name direct-connect-tunnel-id \
    --Filters.0.Values dcx-r3sml04o \
    --Limit 20 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "DirectConnectTunnelSet": [
            {
                "DirectConnectOwnerAccount": "2407912486",
                "DirectConnectGatewayId": "dcg-r70hz833",
                "BgpPeer": {
                    "AuthKey": "tencent",
                    "Asn": 65139
                },
                "OwnerAccount": "2407912486",
                "DirectConnectId": "dc-9s5kpgyp",
                "State": "PENDING",
                "TencentAddress": "169.254.64.1/30",
                "CreatedTime": "2018-06-01 14:59:16",
                "DirectConnectTunnelId": "dcx-r3sml04o",
                "NetworkRegion": "ap-guangzhou",
                "VpcId": "vpc-aipqhdez",
                "CustomerAddress": "169.254.64.2/30",
                "Vlan": 1321,
                "RouteFilterPrefixes": [],
                "NetworkType": "VPC",
                "DirectConnectTunnelName": "测试专用通道",
                "RouteType": "BGP"
            }
        ]
    }
}
```

**Example 2: 查询STATIC路由的专用通道**



Input: 

```
tccli dc DescribeDirectConnectTunnels --cli-unfold-argument  \
    --Filters.0.Name direct-connect-tunnel-id \
    --Filters.0.Values dcx-r3sml04o \
    --Limit 20 \
    --Offset 2
```

Output: 
```
{
    "Response": {
        "DirectConnectTunnelSet": [
            {
                "DirectConnectOwnerAccount": "2407912486",
                "DirectConnectGatewayId": "dcg-r70hz833",
                "BgpPeer": {
                    "AuthKey": "",
                    "Asn": -1
                },
                "OwnerAccount": "2407912486",
                "DirectConnectId": "dc-9s5kpgyp",
                "State": "PENDING",
                "TencentAddress": "169.254.64.1/30",
                "CreatedTime": "2018-06-01 14:59:16",
                "DirectConnectTunnelId": "dcx-r3sml04o",
                "NetworkRegion": "ap-guangzhou",
                "VpcId": "vpc-aipqhdez",
                "CustomerAddress": "169.254.64.2/30",
                "Vlan": 1321,
                "RouteFilterPrefixes": [
                    {
                        "Cidr": "172.18.27.6/32"
                    },
                    {
                        "Cidr": "172.18.27.0/24"
                    }
                ],
                "NetworkType": "VPC",
                "DirectConnectTunnelName": "测试专用通道",
                "RouteType": "STATIC"
            }
        ]
    }
}
```

