**Example 1: 购买RocketMQ专享实例**

购买RocketMQ专享实例

Input: 

```
tccli tdmq CreateRocketMQVipInstance --cli-unfold-argument  \
    --Name test_instance \
    --Spec rocket-vip-basic-1 \
    --NodeCount 2 \
    --StorageSize 200 \
    --ZoneIds 100001 100002 \
    --VpcInfo.VpcId vpc-9dlrd5h1 \
    --VpcInfo.SubnetId subnet-jadmas \
    --TimeSpan 1
```

Output: 
```
{
    "Response": {
        "ClusterId": "rocketmq-7drjznvjqzee",
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

