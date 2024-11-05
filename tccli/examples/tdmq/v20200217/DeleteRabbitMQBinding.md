**Example 1: 解绑RabbitMQ路由关系**



Input: 

```
tccli tdmq DeleteRabbitMQBinding --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --VirtualHost test \
    --BindingId 127441
```

Output: 
```
{
    "Response": {
        "RequestId": "cxvxcvcxfsdfds",
        "InstanceId": "amqp-44w9928j",
        "VirtualHost": "test",
        "BindingId": 127441
    }
}
```

