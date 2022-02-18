**Example 1: 查询数据库代理连接池配置**



Input: 

```
tccli cdb DescribeProxyConnectionPoolConf --cli-unfold-argument  \
    --InstanceId cdb-test \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "PoolConf": [
            {
                "ConnectionPoolType": "SessionConnectionPool",
                "MaxPoolConnectionTimeOut": 600,
                "MinPoolConnectionTimeOut": 1
            }
        ],
        "RequestId": "a1ae22d5-2633-4f09-ba59-8fe103ac64b6"
    }
}
```

