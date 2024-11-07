**Example 1: 创建RabbitMQ路由关系**



Input: 

```
tccli tdmq CreateRabbitMQBinding --cli-unfold-argument  \
    --InstanceId amqp-test \
    --VirtualHost test \
    --Source amq.direct \
    --DestinationType queue \
    --Destination test \
    --RoutingKey hehe1
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "InstanceId": "amqp-test",
        "VirtualHost": "test",
        "BindingId": 127441
    }
}
```

