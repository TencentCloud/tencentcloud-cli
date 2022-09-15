**Example 1: 查询ServiceIPv6**



Input: 

```
tccli vpc DescribeServiceIpv6Internal --cli-unfold-argument  \
    --VpcId 1 \
    --Protocol tcp \
    --RstFlag 1 \
    --Vip 10.6.2.3 \
    --VirtualPort 80 \
    --StickyMaxCount 100 \
    --UniqueVpcId vpc-asdasd \
    --StickyFlag 1 \
    --StickyTimeout 30
```

Output: 
```
{
    "Response": {
        "GetServiceIpv6Result": [
            {
                "VpcId": 77471,
                "UniqueVpcId": "vpc-hagn831r",
                "Protocol": "tcp",
                "RouteSet": [
                    {
                        "PrivateIp": "2402:4e00:2190:e100::1e",
                        "ZoneId": 1,
                        "ProtocolPort": 3306,
                        "Weight": 19,
                        "RemoteVpcId": 0
                    }
                ],
                "ResetFlag": 0,
                "Vip": "2402:4e00:1000:600:0:906c:917e:4aab",
                "StickyMaxCount": 3000,
                "VirtualPort": 3306,
                "StickyFlag": 1,
                "StickyTimeout": 300
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

