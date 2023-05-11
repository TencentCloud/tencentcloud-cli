**Example 1: 创建RabbitMQ的vhost**

-

Input: 

```
tccli tdmq CreateRabbitMQVirtualHost --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --VirtualHost testVhost \
    --Description hello
```

Output: 
```
{
    "Response": {
        "RequestId": "dsfsdfs",
        "VirtualHost": "testVhost"
    }
}
```

