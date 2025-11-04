**Example 1: 查询RabbitMQ队列消费者列表**



Input: 

```
tccli trabbit DescribeRabbitMQServerlessConsumers --cli-unfold-argument  \
    --InstanceId amqp-jero744g \
    --VirtualHost testVhost \
    --QueueName testQueue \
    --Limit 0 \
    --Offset 0 \
    --SearchWord testSearchWord
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "ConsumerInfoList": [
            {
                "ClientIp": "119.147.10.198",
                "ConsumerTag": "ctag1.6473a72d0293494197684c6c3261318b"
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 2: 正常获取消费者列表**



Input: 

```
tccli trabbit DescribeRabbitMQServerlessConsumers --cli-unfold-argument  \
    --InstanceId amqp-slbswcjhay \
    --VirtualHost / \
    --QueueName normal-queue \
    --SearchWord amq.ctag-0b29cd9c
```

Output: 
```
{
    "Response": {
        "ConsumerInfoList": [
            {
                "AckRequired": true,
                "Active": "up",
                "ClientIp": "11.151.193.8",
                "ConsumerTag": "amq.ctag-0b29cd9c",
                "PrefetchCount": 500,
                "QueueName": "normal-queue"
            }
        ],
        "RequestId": "271eecb0-9c34-43d0-b06d-4a539abda5f8",
        "TotalCount": 1
    }
}
```

