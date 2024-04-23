**Example 1: 查询RabbitMQ队列详情**



Input: 

```
tccli tdmq DescribeRabbitMQQueueDetail --cli-unfold-argument  \
    --InstanceId abc \
    --VirtualHost abc \
    --QueueName abc
```

Output: 
```
{
    "Response": {
        "InstanceId": "abc",
        "VirtualHost": "abc",
        "QueueName": "abc",
        "QueueType": "abc",
        "Consumers": 0,
        "Durable": true,
        "AutoDelete": true,
        "Remark": "abc",
        "MessageTTL": 0,
        "AutoExpire": 0,
        "MaxLength": 0,
        "MaxLengthBytes": 0,
        "DeliveryLimit": 0,
        "OverflowBehaviour": "abc",
        "DeadLetterExchange": "abc",
        "DeadLetterRoutingKey": "abc",
        "SingleActiveConsumer": true,
        "MaximumPriority": 0,
        "LazyMode": true,
        "MasterLocator": "abc",
        "MaxInMemoryLength": 0,
        "MaxInMemoryBytes": 0,
        "CreateTime": 0,
        "Node": "abc",
        "DeadLetterStrategy": "abc",
        "QueueLeaderLocator": "abc",
        "QuorumInitialGroupSize": 0,
        "RequestId": "abc"
    }
}
```

