**Example 1: 查询RabbitMQ vhost列表**



Input: 

```
tccli trabbit DescribeRabbitMQServerlessVirtualHost --cli-unfold-argument  \
    --InstanceId amqp-44w9928j
```

Output: 
```
{
    "Response": {
        "RequestId": "dc0de4d7-31c0-47ca-8142-d803d704a44b",
        "TotalCount": 2,
        "VirtualHostList": [
            {
                "InstanceId": "ramqp-cpssyrct",
                "VirtualHost": "testVhost",
                "Description": "default vhost",
                "Tags": [],
                "CreateTime": "2024-10-14 20:06:40:000",
                "ModifyTime": "2024-10-14 20:06:40:000",
                "VirtualHostStatistics": {
                    "CurrentQueues": 0,
                    "CurrentExchanges": 0,
                    "CurrentConnections": 0,
                    "CurrentChannels": 0,
                    "CurrentUsers": 0
                },
                "Status": "running",
                "MessageHeapCount": 0,
                "MessageRateIn": 0,
                "MessageRateOut": 0,
                "MirrorQueuePolicyFlag": false
            },
            {
                "InstanceId": "ramqp-cpssyrct",
                "VirtualHost": "ledou-test",
                "Description": "",
                "Tags": [],
                "CreateTime": "2024-10-16 14:38:58:000",
                "ModifyTime": "2024-10-16 14:38:58:000",
                "VirtualHostStatistics": {
                    "CurrentQueues": 0,
                    "CurrentExchanges": 0,
                    "CurrentConnections": 0,
                    "CurrentChannels": 0,
                    "CurrentUsers": 0
                },
                "Status": "running",
                "MessageHeapCount": 0,
                "MessageRateIn": 0,
                "MessageRateOut": 0,
                "MirrorQueuePolicyFlag": false
            }
        ]
    }
}
```

