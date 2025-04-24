**Example 1: 解绑RabbitMQ路由关系**



Input: 

```
tccli tdmq DeleteRabbitMQBinding --cli-unfold-argument  \
    --InstanceId amqp-jero744g \
    --VirtualHost testVhost \
    --BindingId 127441
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "InstanceId": "amqp-jero744g",
        "VirtualHost": "testVhost",
        "BindingId": 127441
    }
}
```

