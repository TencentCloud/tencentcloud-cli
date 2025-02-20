**Example 1: 添加绑定关系**

添加绑定关系

Input: 

```
tccli trabbit CreateRabbitMQServerlessBinding --cli-unfold-argument  \
    --InstanceId amqp-slnatbyves \
    --VirtualHost vhost \
    --Source fanout-exchange-1061997075421934168 \
    --DestinationType queue \
    --Destination queue-623992266636621729
```

Output: 
```
{
    "Response": {
        "BindingId": 0,
        "InstanceId": "amqp-slnatbyves",
        "RequestId": "1dd2c068-0d69-4ec4-a9e5-adce8cffa43b",
        "VirtualHost": "vhost"
    }
}
```

