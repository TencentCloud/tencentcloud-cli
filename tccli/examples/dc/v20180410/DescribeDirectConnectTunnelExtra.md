**Example 1: 查询专用通道扩展信息**



Input: 

```
tccli dc DescribeDirectConnectTunnelExtra --cli-unfold-argument  \
    --DirectConnectTunnelId dcx-r3sml04o
```

Output: 
```
{
    "Response": {
        "RequestId": "8ae32da8-db96-400f-908e-0de2c89e96ea",
        "DirectConnectTunnelExtra": {
            "DirectConnectOwnerAccount": "2581192000",
            "BfdEnable": 0,
            "BgpPeer": {
                "AuthKey": "tencentnew",
                "Asn": 65719
            },
            "OwnerAccount": "2581192000",
            "DirectConnectId": "dc-c3hbbsw9",
            "NetDetectId": "",
            "State": "AVAILABLE",
            "TencentBackupAddress": "42.34.32.4/27",
            "CreatedTime": "2020-08-20 15:10:03",
            "DirectConnectTunnelId": "dcx-hp42dd1q",
            "SignLaw": false,
            "VpcId": "vpc-a1qkzv63",
            "EnableBGPCommunity": false,
            "NqaEnable": 0,
            "Vlan": 89,
            "RouteFilterPrefixes": [],
            "VpcName": "new-vpc",
            "DirectConnectTunnelName": "vxlan-vpc-",
            "DirectConnectGatewayId": "dcg-0l80ynoj",
            "TencentAddress": "42.34.32.3/27",
            "NetworkRegion": "ap-guangzhou",
            "CustomerAddress": "42.34.32.1/27",
            "NatType": 0,
            "AccessPointType": "VXLAN",
            "BgpStatus": {
                "TencentAddressBgpState": "CONNECT"
            },
            "Bandwidth": 2000,
            "VpcRegion": "gz",
            "RouteType": "BGP",
            "NetworkType": "VPC",
            "DirectConnectGatewayName": "8-2-"
        }
    }
}
```

