**Example 1: 删除RabbitMQ的vhost**

-

Input: 

```
tccli tdmq DeleteRabbitMQVirtualHost --cli-unfold-argument  \
    --InstanceId amqp-test \
    --VirtualHost testVhost
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0"
    }
}
```

