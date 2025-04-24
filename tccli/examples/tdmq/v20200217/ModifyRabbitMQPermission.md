**Example 1: 修改RabbitMQ权限**



Input: 

```
tccli tdmq ModifyRabbitMQPermission --cli-unfold-argument  \
    --InstanceId amqp-2ppxx4rq \
    --User admin \
    --VirtualHost testVhost \
    --ConfigRegexp .* \
    --WriteRegexp .* \
    --ReadRegexp .*
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0"
    }
}
```

