**Example 1: 创建RabbitMQ路由关系**



Input: 

```
tccli tdmq CreateRabbitMQBinding --cli-unfold-argument  \
    --InstanceId amqp-jero744g \
    --VirtualHost tdmq_data \
    --Source amq.direct \
    --DestinationType queue \
    --Destination prod.queue \
    --RoutingKey permission.created
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "InstanceId": "amqp-jero744g",
        "VirtualHost": "tdmq_data",
        "BindingId": 127441
    }
}
```

