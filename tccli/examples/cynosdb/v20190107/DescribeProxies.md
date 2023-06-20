**Example 1: 查询数据库代理列表**

查询数据库代理

Input: 

```
tccli cynosdb DescribeProxies --cli-unfold-argument  \
    --OrderBy createTime \
    --ClusterId cynosdbmysql-xx \
    --Limit 0 \
    --Filters.0.Values proxyGroupId \
    --Filters.0.Names cynosdbmysql-proxy-xx \
    --Filters.0.ExactMatch True \
    --Offset 0 \
    --OrderByType desc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ProxyGroupInfos": [
            {
                "ProxyGroup": {
                    "ProxyGroupId": "abc",
                    "ProxyNodeCount": 0,
                    "Status": "abc",
                    "Region": "abc",
                    "Zone": "abc",
                    "CurrentProxyVersion": "abc",
                    "ClusterId": "abc",
                    "AppId": 0,
                    "OpenRw": "abc"
                },
                "ProxyGroupRwInfo": {
                    "ConsistencyType": "abc",
                    "ConsistencyTimeOut": 0,
                    "WeightMode": "abc",
                    "FailOver": "abc",
                    "AutoAddRo": "abc",
                    "InstanceWeights": [
                        {
                            "InstanceId": "abc",
                            "Weight": 0
                        }
                    ],
                    "OpenRw": "abc"
                },
                "ProxyNodes": [
                    {
                        "ProxyNodeId": "abc",
                        "ProxyNodeConnections": 0,
                        "Cpu": 0,
                        "Mem": 0,
                        "Status": "abc",
                        "ProxyGroupId": "abc",
                        "ClusterId": "abc",
                        "AppId": 0,
                        "Region": "abc",
                        "Zone": "abc"
                    }
                ],
                "ConnectionPool": {
                    "OpenConnectionPool": "abc",
                    "ConnectionPoolType": "abc",
                    "ConnectionPoolTimeOut": 0
                },
                "NetAddrInfos": [
                    {
                        "Vip": "abc",
                        "Vport": 0,
                        "WanDomain": "abc",
                        "WanPort": 0,
                        "NetType": "abc",
                        "UniqSubnetId": "abc",
                        "UniqVpcId": "abc",
                        "Description": "abc",
                        "WanIP": "abc",
                        "WanStatus": "abc"
                    }
                ],
                "Tasks": [
                    {
                        "TaskId": 0,
                        "TaskType": "abc",
                        "TaskStatus": "abc",
                        "ObjectId": "abc",
                        "ObjectType": "abc"
                    }
                ]
            }
        ],
        "ProxyNodeInfos": [
            {
                "ProxyNodeId": "abc",
                "ProxyNodeConnections": 0,
                "Cpu": 0,
                "Mem": 0,
                "Status": "abc",
                "ProxyGroupId": "abc",
                "ClusterId": "abc",
                "AppId": 0,
                "Region": "abc",
                "Zone": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

