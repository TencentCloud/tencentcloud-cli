**Example 1: 查询云数据库实例的客户端连接情况**

查询云数据库实例的客户端连接情况

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
                "IP": "192.168.1.1",
                "InternalService": true
            }
        ],
        "RequestId": "1df930fb-eb7e-4e3f-bcab-15a1aa5fede0"
    }
}
```

