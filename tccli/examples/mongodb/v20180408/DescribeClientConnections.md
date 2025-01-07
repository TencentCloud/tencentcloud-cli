**Example 1: 查询云数据库实例的客户端连接情况**



Input: 

```
tccli mongodb DescribeClientConnections --cli-unfold-argument  \
    --InstanceId cmgo-eqmoaxxx
```

Output: 
```
{
    "Response": {
        "Clients": [
            {
                "IP": "10.0.0.1",
                "Count": 1
            }
        ],
        "TotalCount": 0,
        "RequestId": "59b477da-6473-4ea8-85b3-7f4473744981"
    }
}
```

