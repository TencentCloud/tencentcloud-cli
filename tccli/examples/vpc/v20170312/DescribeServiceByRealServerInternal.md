**Example 1: 用于获取根据rs查询规则**



Input: 

```
tccli vpc DescribeServiceByRealServerInternal --cli-unfold-argument  \
    --VpcId 1 \
    --UniqueVpcId vpc-xxx \
    --Vip 1.1.1.1 \
    --VirtualPort 4432 \
    --PrivateIp 1.1.1.1 \
    --PrivatePort 3232
```

Output: 
```
{
    "Response": {
        "ServiceSet": [
            {
                "VpcId": 2598864,
                "UniqueVpcId": "vpc-rpufyveg",
                "ToaHostIpFlag": 0,
                "VpcGatewayIp": "9.105.119.10",
                "NoSnatFlag": 0,
                "LbType": 0,
                "Vip": "169.254.0.30",
                "StickyMaxCount": 0,
                "VirtualPort": 443,
                "StickyFlag": 0,
                "VipVpcGatewayId": "vpcgw-7hk70tq8",
                "Protocol": "tcp",
                "BypassFlag": 0,
                "ResetFlag": 0,
                "HealthFlag": 1,
                "Type": 1,
                "SubnetRouteAlgorithm": 0,
                "StickyTimeout": 0,
                "VipSetId": 0,
                "Business": "",
                "GroupId": [
                    0
                ],
                "RouteSet": [
                    {
                        "Weight": 16,
                        "PrivatePort": 443,
                        "ZoneId": 0,
                        "UdpOption": 0,
                        "HostIp": "0.0.0.0",
                        "PrivateIp": "10.112.65.50"
                    }
                ],
                "RemoteVpcId": 0,
                "UniqueVpcGatewayId": "vpcgw-7hk70tq8",
                "UniqueClassicVpcGatewayId": "vpcgw-7hk70tq8",
                "SetId": 0
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

