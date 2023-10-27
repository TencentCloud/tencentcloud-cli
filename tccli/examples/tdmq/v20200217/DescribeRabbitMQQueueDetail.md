**Example 1: 查询RabbitMQ队列详情**



Input: 

```
tccli tdmq DescribeRabbitMQQueueDetail --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --VirtualHost test \
    --QueueName xx
```

Output: 
```
{
    "Response": {
        "Consumers": 0,
        "Durable": true,
        "LazyMode": true,
        "QueueName": "xx",
        "QueueType": "xx",
        "VirtualHost": "xx",
        "InstanceId": "xx",
        "AutoExpire": 0,
        "MaxInMemoryLength": 0,
        "MaxLengthBytes": 0,
        "MessageTTL": 0,
        "SingleActiveConsumer": true,
        "Remark": "xx",
        "AutoDelete": true,
        "DeadLetterExchange": "xx",
        "DeliveryLimit": 0,
        "RequestId": "xx",
        "OverflowBehaviour": "xx",
        "MasterLocator": "xx",
        "MaxInMemoryBytes": 0,
        "MaximumPriority": 0,
        "DeadLetterRoutingKey": "xx",
        "MaxLength": 0,
        "Node": "xx",
        "CreateTime": 1669174535
    }
}
```

