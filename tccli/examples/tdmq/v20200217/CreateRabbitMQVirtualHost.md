**Example 1: 创建RabbitMQ的vhost**

-

Input: 

```
tccli tdmq CreateRabbitMQVirtualHost --cli-unfold-argument  \
    --InstanceId amqp-test \
    --VirtualHost testVhost \
    --Description hello
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "VirtualHost": "testVhost"
    }
}
```

