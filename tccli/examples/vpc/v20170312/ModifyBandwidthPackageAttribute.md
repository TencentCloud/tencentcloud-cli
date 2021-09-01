**Example 1: 修改带宽包名称**



Input: 

```
tccli vpc ModifyBandwidthPackageAttribute --cli-unfold-argument  \
    --BandwidthPackageId bwp-e40edw8y \
    --BandwidthPackageName test
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
    --BandwidthPackageId bwp-e40edw8y \
    --BandwidthPackageName test \
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

