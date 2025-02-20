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

