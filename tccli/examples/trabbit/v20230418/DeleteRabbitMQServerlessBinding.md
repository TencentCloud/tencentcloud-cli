**Example 1: 解绑RabbitMQ路由关系**



Input: 

```
tccli trabbit DeleteRabbitMQServerlessBinding --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --VirtualHost testVhost \
    --BindingId 127441
```

Output: 
```
{
    "Response": {
        "RequestId": "cxvxcvcxfsdfds",
        "InstanceId": "amqp-44w9928j",
        "VirtualHost": "testVhost",
        "BindingId": 127441
    }
}
```

