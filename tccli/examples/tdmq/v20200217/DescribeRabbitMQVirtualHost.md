**Example 1: 查询RabbitMQ vhost列表**

-

Input: 

```
tccli tdmq DescribeRabbitMQVirtualHost --cli-unfold-argument  \
    --InstanceId amqp-44w9928j
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "VirtualHostList": [
            {
                "InstanceId": "amqp-xxxxxxxx",
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
                "MessageHeapCount": 0,
                "MessageRateIn": 0,
                "MessageRateOut": 0
            },
            {
                "InstanceId": "amqp-xxxxxxxx",
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
                "MessageHeapCount": 0,
                "MessageRateIn": 0,
                "MessageRateOut": 0
            }
        ],
        "TotalCount": 2
    }
}
```

