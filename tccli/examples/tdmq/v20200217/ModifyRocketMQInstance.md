**Example 1: 修改RocketMQ专享实例**

修改RocketMQ专享实例

Input: 

```
tccli tdmq ModifyRocketMQInstance --cli-unfold-argument  \
    --InstanceId abc \
    --Name abc \
    --Remark abc \
    --MessageRetention 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

