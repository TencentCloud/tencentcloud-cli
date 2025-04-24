**Example 1: 创建RabbitMQ用户**



Input: 

```
tccli tdmq CreateRabbitMQUser --cli-unfold-argument  \
    --InstanceId amqp-2ppxx4rq \
    --User test_user \
    --Password abc123._
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "User": "test_user"
    }
}
```

