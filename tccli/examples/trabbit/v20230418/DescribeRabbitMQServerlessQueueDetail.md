**Example 1: 查询RabbitMQ队列详情**

查询RabbitMQ队列详情

Input: 

```
tccli trabbit DescribeRabbitMQServerlessQueueDetail --cli-unfold-argument  \
    --InstanceId amqp-slmejnrgtz \
    --VirtualHost vhost1 \
    --QueueName queue1
```

Output: 
```
{
    "Response": {
        "RequestId": "e44774dc-597a-45d0-8a41-e5a13bae3878",
        "InstanceId": "amqp-slygmxjifs",
        "VirtualHost": "test-vhost",
        "QueueName": "queue-test",
        "QueueType": "classic",
        "Consumers": 0,
        "Durable": true,
        "AutoDelete": false,
        "Remark": "",
        "MessageTTL": 100000,
        "AutoExpire": 1,
        "MaxLength": 100,
        "MaxLengthBytes": 1204,
        "DeliveryLimit": 100,
        "OverflowBehaviour": "",
        "DeadLetterExchange": "",
        "DeadLetterRoutingKey": "",
        "SingleActiveConsumer": false,
        "MaximumPriority": 100,
        "LazyMode": false,
        "MasterLocator": "",
        "MaxInMemoryLength": 1024,
        "MaxInMemoryBytes": 1024,
        "CreateTime": 1739935376,
        "Node": "",
        "DeadLetterStrategy": "",
        "QueueLeaderLocator": "",
        "QuorumInitialGroupSize": 100,
        "Exclusive": false,
        "Policy": "",
        "Arguments": "{\"x-ordered\": false}"
    }
}
```

