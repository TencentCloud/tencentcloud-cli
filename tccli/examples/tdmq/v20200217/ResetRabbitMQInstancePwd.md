**Example 1: 重置ssm托管密码**



Input: 

```
tccli tdmq ResetRabbitMQInstancePwd --cli-unfold-argument  \
    --UserResourceId amqp-wdxk9k2q \
    --ResourceAccount test03187 \
    --ResourceRegionType rabbitmq \
    --Password wrqwet21412 \
    --AccountHost %
```

Output: 
```
{
    "Response": {
        "ResetTimestamp": 1776246143727,
        "TimeCost": 501,
        "RequestId": "baa90926-62f3-4010-af2b-7c5670c85fc3"
    }
}
```

