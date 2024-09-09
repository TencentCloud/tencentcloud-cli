**Example 1: 查询专用通道扩展信息**

查询专用通道扩展信息

Input: 

```
tccli dc DescribeDirectConnectTunnelExtra --cli-unfold-argument  \
    --DirectConnectTunnelId dcx-047zz5e6
```

Output: 
```
{
    "Response": {
        "DirectConnectTunnelExtra": {
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
            "NqaEnable": 0,
            "BfdInfo": {
                "ProbeFailedTimes": -1,
                "Interval": -1
            },
            "NqaInfo": {
                "ProbeFailedTimes": -1,
                "Interval": -1,
                "DestinationIp": "0.0.0.0"
            },
            "IPv6Enable": 0,
            "PublicAddresses": [],
            "JumboEnable": 0,
            "HighPrecisionBFDEnable": 0,
            "TencentBackupAddress": "192.168.0.2/29",
            "NetworkType": "CCN",
            "RouteType": "BGP",
            "BgpPeer": {
                "Asn": 65120,
                "AuthKey": "tencent"
            },
            "RouteFilterPrefixes": [],
            "BgpStatus": {
                "TencentAddressBgpState": "Established",
                "TencentBackupAddressBgpState": "Connect"
            },
            "TencentIPv6Address": "",
            "TencentBackupIPv6Address": "",
            "CustomerIPv6Address": "",
            "BgpIPv6Status": {
                "TencentAddressBgpState": "",
                "TencentBackupAddressBgpState": ""
            }
        },
        "RequestId": "8ae32da8-db96-400f-908e-0de2c89e96ea"
    }
}
```

