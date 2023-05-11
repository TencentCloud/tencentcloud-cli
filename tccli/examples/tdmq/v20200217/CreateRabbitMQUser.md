**Example 1: 创建RabbitMQ用户**

-

Input: 

```
tccli tdmq CreateRabbitMQUser --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --User test_user \
    --Password abc123
```

Output: 
```
{
    "Response": {
        "RequestId": "dsfsdfs",
        "User": "test_user"
    }
}
```

