**Example 1: 删除RabbitMQ权限**

-

Input: 

```
tccli tdmq DeleteRabbitMQPermission --cli-unfold-argument  \
    --InstanceId amqp-jero744g \
    --User admin \
    --VirtualHost tdmq_data
```

Output: 
```
{
    "Response": {
        "RequestId": "b7bd149f-06e1-40ad-82cb-9f0500b5194c"
    }
}
```

