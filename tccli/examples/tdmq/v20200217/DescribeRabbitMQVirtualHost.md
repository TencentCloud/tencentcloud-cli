**Example 1: 查询RabbitMQ vhost列表**

-

Input: 

```
tccli tdmq DescribeRabbitMQVirtualHost --cli-unfold-argument  \
    --InstanceId amqp-test
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "VirtualHostList": [
            {
                "InstanceId": "amqp-test",
                "VirtualHost": "vhost",
                "Description": "",
                "Tags": [],
                "CreateTime": "2023-07-18 12:55:00.778",
                "ModifyTime": "2023-07-18 12:55:00.778",
                "VirtualHostStatistics": {
                    "CurrentQueues": 1,
                    "CurrentExchanges": 6,
                    "CurrentConnections": 1,
                    "CurrentChannels": 1,
                    "CurrentUsers": 1
                },
                "TraceFlag": true,
                "MessageHeapCount": 0,
                "MessageRateIn": 0,
                "MessageRateOut": 0
            },
            {
                "InstanceId": "amqp-test",
                "VirtualHost": "test2",
                "Description": "",
                "Tags": [],
                "CreateTime": "2023-07-18 12:55:16.230",
                "ModifyTime": "2023-07-18 12:55:19.856",
                "VirtualHostStatistics": {
                    "CurrentQueues": 0,
                    "CurrentExchanges": 0,
                    "CurrentConnections": 0,
                    "CurrentChannels": 0,
                    "CurrentUsers": 0
                },
                "TraceFlag": true,
                "MessageHeapCount": 0,
                "MessageRateIn": 0,
                "MessageRateOut": 0
            }
        ],
        "TotalCount": 2
    }
}
```

