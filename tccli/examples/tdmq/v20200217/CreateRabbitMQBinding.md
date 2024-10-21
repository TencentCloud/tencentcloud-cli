**Example 1: 创建RabbitMQ路由关系**



Input: 

```
tccli tdmq CreateRabbitMQBinding --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
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
        "RequestId": "dsfadsa",
        "InstanceId": "amqp-44w9928j",
        "VirtualHost": "test",
        "BindingId": 127441
    }
}
```

