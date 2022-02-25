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
        "TotalCount": 1,
        "Clients": [
            {
                "Count": 1,
                "IP": "xx",
                "InternalService": true
            },
            {
                "Count": 1,
                "IP": "xx",
                "InternalService": true
            }
        ],
        "RequestId": "xx"
    }
}
```

