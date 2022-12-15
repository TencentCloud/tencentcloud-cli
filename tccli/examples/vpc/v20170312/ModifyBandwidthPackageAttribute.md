**Example 1: 修改带宽包名称**



Input: 

```
tccli vpc ModifyBandwidthPackageAttribute --cli-unfold-argument  \
    --BandwidthPackageName test \
    --BandwidthPackageId bwp-e40edw8y
```

Output: 
```
{
    "Response": {
        "RequestId": "2ece8f4a-c0f5-4b83-8054-a9b808a5c465"
    }
}
```

**Example 2: 修改带宽包计费模式**



Input: 

```
tccli vpc ModifyBandwidthPackageAttribute --cli-unfold-argument  \
    --BandwidthPackageName test \
    --BandwidthPackageId bwp-e40edw8y \
    --ChargeType TOP5
```

Output: 
```
{
    "Response": {
        "RequestId": "2ece8f4a-c0f5-4b83-8054-a9b808a5c465"
    }
}
```

