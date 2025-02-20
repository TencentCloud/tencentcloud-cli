**Example 1: 查询RabbitMQ队列列表**



Input: 

```
tccli trabbit DescribeRabbitMQServerlessQueues --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --VirtualHost testVhost
```

Output: 
```
{
    "Response": {
        "RequestId": "8b5d9dd2-b80f-40da-8c8c-fd180a78be38",
        "TotalCount": 1,
        "QueueInfoList": [
            {
                "QueueName": "ledou-test",
                "Remark": "",
                "ConsumerDetail": {
                    "ConsumersNumber": 0
                },
                "QueueType": "normal",
                "MessageHeapCount": 0,
                "MessageRateIn": 0,
                "MessageRateOut": 0,
                "CreateTime": "2024-10-16 14:39:58:000",
                "ModifyTime": "2024-10-16 14:39:58:000",
                "Durable": true,
                "AutoDelete": false,
                "InstanceId": "ramqp-cpssyrct",
                "VirtualHost": "testVhost",
                "Node": "",
                "Policy": "",
                "Arguments": "{\"x-message-ttl\":100000.0}",
                "Exclusive": false
            }
        ]
    }
}
```

