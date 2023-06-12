**Example 1: 获取虚拟机列表**



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
        "RequestId": "xx",
        "VirtualHostList": [
            {
                "VirtualHostName": "xx",
                "Description": "xx"
            }
        ]
    }
}
```

