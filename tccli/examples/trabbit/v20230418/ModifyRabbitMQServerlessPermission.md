**Example 1: 成功**



Input: 

```
tccli trabbit ModifyRabbitMQServerlessPermission --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --User test_user \
    --VirtualHost testVhost \
    --ConfigRegexp .* \
    --WriteRegexp .* \
    --ReadRegexp .*
```

Output: 
```
{
    "Response": {
        "RequestId": "dsfsdfs"
    }
}
```

