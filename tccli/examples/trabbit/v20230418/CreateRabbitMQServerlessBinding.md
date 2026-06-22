**Example 1: Header 类型 Exchange 绑定队列**



Input: 

```
tccli trabbit CreateRabbitMQServerlessBinding --cli-unfold-argument  \
    --InstanceId amqp-slranxpibb \
    --VirtualHost / \
    --Source ledou-test \
    --DestinationType queue \
    --Destination ledou-test \
    --Arguments.0.Key x-match \
    --Arguments.0.Value all
```

Output: 
```
{
    "Response": {
        "BindingId": 0,
        "InstanceId": "amqp-slranxpibb",
        "VirtualHost": "/",
        "RequestId": "0964a348-9573-41d1-89e0-9f1b42cacdc4"
    }
}
```

