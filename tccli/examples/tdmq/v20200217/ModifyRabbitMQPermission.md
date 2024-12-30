**Example 1: 修改RabbitMQ权限**

-

Input: 

```
tccli tdmq ModifyRabbitMQPermission --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --User admin \
    --VirtualHost tdmq_data \
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

