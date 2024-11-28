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
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "VirtualHostList": [
            {
                "VirtualHostName": "tdmq_data",
                "Description": "The virtual host is for test"
            }
        ]
    }
}
```

