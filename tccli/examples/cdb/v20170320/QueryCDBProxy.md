**Example 1: 查询代理详情**



Input: 

```
tccli cdb QueryCDBProxy --cli-unfold-argument  \
    --InstanceId cdb-test \
    --ProxyGroupId proxy-test
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "ProxyGroup": [
            {
                "Address": [
                    {
                        "Desc": "",
                        "UniqSubnet": "subnet-test",
                        "UniqVpcId": "vpc-test",
                        "VPort": 3306,
                        "Vip": "172.16.48.49"
                    }
                ],
                "BaseGroup": {
                    "CurrentProxyVersion": "1.0.1",
                    "NodeCount": 2,
                    "OpenRW": false,
                    "ProxyGroupId": "proxy-test",
                    "Region": "ap-guangzhou",
                    "Status": "online",
                    "SupportUpgradeProxyVersion": "1.0.1",
                    "Zone": "ap-guangzhou-6"
                },
                "ConnectionPoolInfo": {
                    "ConnectionPool": false,
                    "ConnectionPoolType": "",
                    "PoolConnectionTimeOut": 0
                },
                "ProxyNode": [
                    {
                        "ProxyNodeConnections": 2,
                        "ProxyNodeId": "proxynode-test",
                        "ProxyStatus": "online"
                    },
                    {
                        "ProxyNodeConnections": 2,
                        "ProxyNodeId": "proxynode-test",
                        "ProxyStatus": "online"
                    }
                ],
                "RWInstInfo": {
                    "AutoAddRo": false,
                    "FailOver": false,
                    "InstCount": 0,
                    "IsKickOut": false,
                    "MaxDelay": 0,
                    "MinCount": 0,
                    "RWInstInfo": [],
                    "WeightMode": ""
                }
            }
        ],
        "RequestId": "733f71d8-6c3a-419e-830f-4471c5bc2791"
    }
}
```

