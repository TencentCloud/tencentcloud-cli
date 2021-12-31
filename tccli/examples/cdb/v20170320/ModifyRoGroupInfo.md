**Example 1: 设置RO组的延迟剔除策略**



Input: 

```
tccli cdb ModifyRoGroupInfo --cli-unfold-argument  \
    --RoGroupId cdbrg-iup41a4t \
    --RoGroupInfo.RoOfflineDelay 1 \
    --RoGroupInfo.RoMaxDelayTime 10 \
    --RoGroupInfo.MinRoInGroup 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "AsyncRequestId": "xx"
    }
}
```

**Example 2: 重新均衡RO组内实例的权重**



Input: 

```
tccli cdb ModifyRoGroupInfo --cli-unfold-argument  \
    --RoGroupId cdbrg-iup41a4t \
    --RoGroupInfo.WeightMode custom \
    --RoWeightValues.0.InstanceId cdbr0-iup41a4t \
    --RoWeightValues.0.Weight 30 \
    --RoWeightValues.1.InstanceId cdbr0-test1234 \
    --RoWeightValues.1.Weight 70 \
    --IsBalanceRoLoad 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "AsyncRequestId": "xx"
    }
}
```

