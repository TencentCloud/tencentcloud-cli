**Example 1: 修改RabbitMQ的vhost**

-

Input: 

```
tccli tdmq ModifyRabbitMQVirtualHost --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --VirtualHost testVhost \
    --Description hello
```

Output: 
```
{
    "Response": {
        "RequestId": "dsfsdfs"
    }
}
```

