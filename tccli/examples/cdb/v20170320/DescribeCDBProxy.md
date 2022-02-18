**Example 1: 查询数据库代理**



Input: 

```
tccli cdb DescribeCDBProxy --cli-unfold-argument  \
    --InstanceId xx \
    --ProxyGroupId xx
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "RWInstInfo": {
            "MaxDelay": 1,
            "AutoAddRo": true,
            "IsKickOut": true,
            "FailOver": true,
            "RWInstInfo": {},
            "MinCount": 1,
            "WeightMode": "xx",
            "InstCount": 1
        },
        "ProxyNode": {
            "ProxyNodeId": "xx",
            "ProxyNodeMem": 1,
            "ProxyNodeConnections": 1,
            "ProxyNodeCpu": 1,
            "ProxyStatus": "xx"
        },
        "ConnectionPoolInfo": {
            "ConnectionPoolType": "xx",
            "PoolConnectionTimeOut": 0,
            "ConnectionPool": true
        },
        "RequestId": "xx",
        "Address": {
            "UniqVpcId": "xx",
            "VPort": 1,
            "Vip": "xx",
            "UniqSubnet": "xx",
            "Desc": "xx"
        },
        "ProxyGroup": [
            {
                "ConnectionPoolInfo": {
                    "ConnectionPoolType": "xx",
                    "PoolConnectionTimeOut": 0,
                    "ConnectionPool": false
                },
                "RWInstInfo": {
                    "MaxDelay": 1,
                    "AutoAddRo": true,
                    "IsKickOut": true,
                    "FailOver": true,
                    "RWInstInfo": {},
                    "MinCount": 1,
                    "WeightMode": "xx",
                    "InstCount": 1
                },
                "BaseGroup": {
                    "Status": "xx",
                    "CurrentProxyVersion": "xx",
                    "ProxyGroupId": "xx",
                    "Zone": "xx",
                    "Region": "xx",
                    "NodeCount": 1,
                    "SupportUpgradeProxyVersion": "xx",
                    "OpenRW": true
                },
                "ProxyNode": {
                    "ProxyNodeId": "xx",
                    "ProxyNodeMem": 1,
                    "ProxyNodeConnections": 1,
                    "ProxyNodeCpu": 1,
                    "ProxyStatus": "xx"
                },
                "Address": {
                    "UniqVpcId": "xx",
                    "VPort": 1,
                    "Vip": "xx",
                    "UniqSubnet": "xx",
                    "Desc": "xx"
                }
            }
        ],
        "BaseGroup": {
            "Status": "xx",
            "CurrentProxyVersion": "xx",
            "ProxyGroupId": "xx",
            "Zone": "xx",
            "Region": "xx",
            "NodeCount": 1,
            "SupportUpgradeProxyVersion": "xx",
            "OpenRW": true
        }
    }
}
```

