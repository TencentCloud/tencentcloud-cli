**Example 1: 购买RocketMQ专享实例**

购买RocketMQ专享实例

Input: 

```
tccli tdmq CreateRocketMQVipInstance --cli-unfold-argument  \
    --Name abc \
    --Spec rocket-vip-basic-1 \
    --NodeCount 1 \
    --StorageSize 0 \
    --ZoneIds 100001 \
    --VpcInfo.VpcId abc \
    --VpcInfo.SubnetId abc \
    --TimeSpan 1
```

Output: 
```
{
    "Response": {
        "ClusterId": "rocketmq-xxxx",
        "RequestId": "abc"
    }
}
```

