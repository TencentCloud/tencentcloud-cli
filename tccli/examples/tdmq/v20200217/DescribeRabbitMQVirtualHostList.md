**Example 1: 获取云服务器列表**



Input: 

```
tccli tdmq DescribeRabbitMQVirtualHostList --cli-unfold-argument  \
    --InstanceId amqp-testtesttest \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "abc",
        "VirtualHostList": [
            {
                "VirtualHostName": "abc",
                "Description": "abc"
            }
        ]
    }
}
```

