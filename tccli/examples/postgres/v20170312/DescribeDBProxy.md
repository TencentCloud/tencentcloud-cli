**Example 1: 查询数据库代理**

查询指定 PG 实例下的全部 Proxy 信息

Input: 

```
tccli postgres DescribeDBProxy --cli-unfold-argument  \
    --DBInstanceId postgres-oul13k0b
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "ProxyInfos": [
            {
                "ConnectionPoolLimit": 0,
                "CreateTime": "2026-06-17 16:46:12",
                "Description": "",
                "ProxyAddressSet": [
                    {
                        "AddressId": "proxyaddr-80ab0kho",
                        "ConnectionPool": true,
                        "ConnectionPoolLimit": 300,
                        "Description": "",
                        "Routes": [
                            {
                                "NodeId": "postgres-oul13k0b",
                                "Role": "master",
                                "Status": "online",
                                "Weight": 100
                            }
                        ],
                        "SubnetId": "6888276",
                        "Vip": "10.0.0.91",
                        "VpcId": "12115942",
                        "Vport": 5432
                    }
                ],
                "ProxyGroupId": "proxy-i36xgkkt",
                "ProxyNodeSet": [
                    {
                        "Connection": 0,
                        "Cpu": 2,
                        "Mem": 4000,
                        "ProxyNodeId": "proxynode-d1d9to0k",
                        "Status": "online",
                        "Zone": "ap-guangzhou-3"
                    }
                ],
                "ProxyVersion": "1.4.9",
                "Status": "online",
                "TaskStatus": ""
            }
        ],
        "RequestId": "81a642d4-3ec9-43b3-b74e-be7b22dc391e"
    }
}
```

