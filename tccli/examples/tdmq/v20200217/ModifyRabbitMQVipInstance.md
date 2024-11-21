**Example 1: 修改RabbitMQ专享版实例**

修改RabbitMQ专享版实例

Input: 

```
tccli tdmq ModifyRabbitMQVipInstance --cli-unfold-argument  \
    --InstanceId amqp-jero744g \
    --Remark 生产使用集群
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "InstanceId": "amqp-jero744g"
    }
}
```

