**Example 1: 实例小版本升级**



Input: 

```
tccli redis UpgradeSmallVersion --cli-unfold-argument  \
    --InstanceId crs-2btr9ryn \
    --CurrentRedisVersion 2.3.0 \
    --UpgradeRedisVersion 2.4.0 \
    --InstanceTypeUpgradeNow 1
```

Output: 
```
{
    "Response": {
        "FlowId": 329,
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522"
    }
}
```

