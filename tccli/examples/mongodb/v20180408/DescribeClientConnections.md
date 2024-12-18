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
                "IP": "abc",
                "Count": 1
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

