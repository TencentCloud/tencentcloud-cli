**Example 1: 查询RabbitMQ队列详情**



Input: 

```
tccli tdmq DescribeRabbitMQQueueDetail --cli-unfold-argument  \
    --InstanceId amqp-jero744g \
    --VirtualHost tdmq_data \
    --QueueName prod.queue
```

Output: 
```
{
    "Response": {
        "Arguments": "{\"x-ordered\": false}",
        "AutoDelete": false,
        "AutoExpire": 1000,
        "Consumers": 1,
        "CreateTime": 1728982735,
        "DeadLetterExchange": "dl-exchange",
        "DeadLetterRoutingKey": "test-dl",
        "DeadLetterStrategy": "at-most-once",
        "DeliveryLimit": null,
        "Durable": true,
        "Exclusive": false,
        "InstanceId": "amqp-jero744g",
        "LazyMode": false,
        "MasterLocator": "client-local",
        "MaxInMemoryBytes": null,
        "MaxInMemoryLength": null,
        "MaxLength": 10000,
        "MaxLengthBytes": 1000,
        "MaximumPriority": 0,
        "MessageTTL": 1000,
        "Node": "rabbit@rabbitmq-broker-0.rabbitmq-broker-internal.amqp-test.svc.cluster.local",
        "OverflowBehaviour": "drop-head",
        "Policy": "test-policy",
        "QueueLeaderLocator": null,
        "QueueName": "prod.queue",
        "QueueType": "classic",
        "QuorumInitialGroupSize": null,
        "Remark": "[系统自动批量同步]",
        "RequestId": "bf6ea82d-213b-4d44-be1f-74cd31f9a22b",
        "SingleActiveConsumer": false,
        "VirtualHost": "tdmq_data"
    }
}
```

