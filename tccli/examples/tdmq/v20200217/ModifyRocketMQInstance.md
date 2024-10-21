**Example 1: 修改RocketMQ专享实例**

修改RocketMQ专享实例

Input: 

```
tccli tdmq ModifyRocketMQInstance --cli-unfold-argument  \
    --InstanceId rocketmq-4k4orqgq \
    --Name order-service-instance \
    --Remark info-mark \
    --MessageRetention 24
```

Output: 
```
{
    "Response": {
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

