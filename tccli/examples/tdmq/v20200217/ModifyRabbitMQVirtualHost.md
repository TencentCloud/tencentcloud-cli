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
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0"
    }
}
```

