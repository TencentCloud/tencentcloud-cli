**Example 1: 创建RabbitMQ用户**



Input: 

```
tccli tdmq CreateRabbitMQUser --cli-unfold-argument  \
    --InstanceId amqp-7jwe5pr5 \
    --User grace \
    --Password abcABC123 \
    --EnableCamAuth True
```

Output: 
```
{
    "Response": {
        "User": "grace",
        "RequestId": "83a4c4d3-43d9-456a-bf80-c8a5aa27c26a"
    }
}
```

