**Example 1: 列出集群中所有的客户端节点**



Input: 

```
tccli goosefs DescribeClientNodes --cli-unfold-argument  \
    --FileSystemId x_c60_r3c4fa1f
```

Output: 
```
{
    "Response": {
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6",
        "ClientNodes": [
            {
                "Status": "active",
                "ClientNodeIp": "10.0.1.2"
            },
            {
                "Status": "active",
                "ClientNodeIp": "10.0.1.3"
            },
            {
                "Status": "down",
                "ClientNodeIp": "10.0.1.4"
            }
        ]
    }
}
```

