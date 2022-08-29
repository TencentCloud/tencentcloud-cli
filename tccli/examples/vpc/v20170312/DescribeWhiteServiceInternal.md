**Example 1: 用于获取WhiteService**



Input: 

```
tccli vpc DescribeWhiteServiceInternal --cli-unfold-argument  \
    --Protocol tcp \
    --Name name \
    --VirtualPort 80 \
    --BypassFlag 1 \
    --Offset 0 \
    --Vip 10.1.1.1 \
    --Limit 100 \
    --WhiteServiceId 1 \
    --OwnerLevel 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "WhiteServiceSet": [
            {
                "UniqueRouteGroupId": "",
                "Name": "leohli测试白名单服务",
                "Protocol": "tcp",
                "BypassFlag": 0,
                "ResetFlag": 0,
                "RouteGroupId": 0,
                "Vip": "183.60.83.19",
                "RouteGroupFlag": 0,
                "WhiteServiceId": 4,
                "OwnerLevel": -1,
                "VirtualPort": 53,
                "CreateTime": "2017-07-12 10:56:24"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

