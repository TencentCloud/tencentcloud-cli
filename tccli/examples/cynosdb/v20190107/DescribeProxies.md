**Example 1: 查询数据库代理列表**

查询数据库代理

Input: 

```
tccli cynosdb DescribeProxies --cli-unfold-argument  \
    --OrderBy createTime \
    --ClusterId cynosdbmysql-xx \
    --Limit 0 \
    --Filters.0.Values proxyGroupId \
    --Filters.0.Names cynosdbmysql-proxy-tshj6btw \
    --Filters.0.ExactMatch True \
    --Offset 0 \
    --OrderByType desc
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "ProxyGroupInfos": [
            {
                "ConnectionPool": {
                    "ConnectionPoolTimeOut": 30,
                    "ConnectionPoolType": "SessionConnectionPool",
                    "OpenConnectionPool": "yes"
                },
                "NetAddrInfos": [
                    {
                        "Description": "external-ro new",
                        "InstanceGroupId": "cynosdbmysql-grp-nsiuj4aj",
                        "NetType": "",
                        "UniqSubnetId": "subnet-pmqqss72",
                        "UniqVpcId": "vpc-gvelzo5j",
                        "Vip": "11.2.1.43",
                        "Vport": 3306,
                        "WanDomain": "test.wan.domain",
                        "WanIP": "11.2.3.43",
                        "WanPort": 3306,
                        "WanStatus": "open"
                    }
                ],
                "ProxyGroup": {
                    "AppId": 1772344699,
                    "ClusterId": "cynosdbmysql-i2weamox",
                    "CurrentProxyVersion": "1.3.11",
                    "OpenRw": "yes",
                    "ProxyGroupId": "cynosdbmysql-proxy-mdhg55su",
                    "ProxyNodeCount": 4,
                    "Region": "ap-guangzhou",
                    "Status": "running",
                    "Zone": "ap-guangzhou-6"
                },
                "ProxyGroupRwInfo": {
                    "AccessMode": "balance",
                    "AutoAddRo": "no",
                    "ConsistencyTimeOut": 0,
                    "ConsistencyType": "eventual",
                    "FailOver": "no",
                    "InstanceWeights": [
                        {
                            "InstanceId": "cynosdbmysql-ins-ka2i3m48",
                            "Weight": 1
                        }
                    ],
                    "OpenRw": "yes",
                    "RwType": "READONLY",
                    "TransSplit": false,
                    "WeightMode": "system"
                },
                "ProxyNodes": [
                    {
                        "AppId": 1772344699,
                        "ClusterId": "cynosdbmysql-i2weamox",
                        "Cpu": 2,
                        "Mem": 4000,
                        "OssProxyNodeName": "cynosdbmysql-proxyNode-q52v1wp4",
                        "ProxyGroupId": "cynosdbmysql-proxy-mdhg57su",
                        "ProxyNodeConnections": 157,
                        "ProxyNodeId": "cynosdbmysql-proxyNode-pv4hg4na",
                        "Region": "ap-guangzhou",
                        "Status": "running",
                        "Zone": "ap-guangzhou-6"
                    }
                ],
                "Tasks": [
                    {
                        "TaskId": 123124,
                        "TaskType": "taskModifyProxyRwSplit",
                        "TaskStatus": "processing",
                        "ObjectId": "cynosdbmysql-proxy-mdhg57su",
                        "ObjectType": "taskObjTypeCluster"
                    }
                ]
            }
        ],
        "ProxyNodeInfos": [
            {
                "ProxyNodeId": "cynosdbmysql-proxyNode-pv4hg4na",
                "ProxyNodeConnections": 157,
                "Cpu": 2,
                "Mem": 4000,
                "Status": "running",
                "ProxyGroupId": "cynosdbmysql-proxy-mdhg57su",
                "ClusterId": "cynosdbmysql-i2weamox",
                "AppId": 1772344699,
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-6",
                "OssProxyNodeName": "cynosdbmysql-proxyNode-q52v1wp4"
            }
        ],
        "RequestId": "ed0bd4ca-b5c0-4230-a8b5-6d2dc5ec1eb0"
    }
}
```

