**Example 1: 查询接口**



Input: 

```
tccli vpc DescribeServiceInternal --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --Filters.0.Name vpc-id \
    --Filters.0.Values vpc-e3t30r8t
```

Output: 
```
{
    "Response": {
        "ServiceSet": [
            {
                "IpType": 1,
                "VpcGatewayIp": "10.0.0.1",
                "VpcGatewayId": "vpcgw-12efr432",
                "RsZoneVpcGatewayId": 1,
                "VpcGatewayAttrFlag": 1,
                "SetId": 1,
                "Type": 1,
                "SubnetRouteAlgorithm": 1,
                "VpcId": "xx",
                "VipSetId": 1,
                "Business": "xx",
                "ToaHostIpFlag": 1,
                "ClassicVpcGatewayId": "vpcgw-12efr432",
                "LbType": 1,
                "SnatFlag": 1,
                "StickyFlag": 1,
                "VpcGatewayZoneId": 1,
                "BypassFlag": 1,
                "ResetFlag": 1,
                "RemoteVpcId": 1,
                "HealthFlag": 1,
                "StickyTimeout": 1,
                "RouteSet": [
                    {
                        "Weight": 1,
                        "PrivateIP": "123.0.0.0",
                        "HostIp": "196.0.0.1",
                        "ProtocolPort": 1,
                        "ForwardingMode": 1,
                        "ZoneId": 1
                    }
                ],
                "Protocol": "tcp",
                "VipVpcGatewayId": "vpcgw-3rft532",
                "Vip": "10.0.0.1",
                "VirtualPort": 1,
                "StickyMaxCount": 1,
                "GroupId": [
                    1
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

