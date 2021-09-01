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
                "Count": 15,
                "IP": "10.xx.xx.xx"
            },
            {
                "Count": 15,
                "IP": "10.xx.xx.xx"
            }
        ],
        "RequestId": "c61fd6e2-c505-4fb9-9f30-edd8e897b236"
    }
}
```

