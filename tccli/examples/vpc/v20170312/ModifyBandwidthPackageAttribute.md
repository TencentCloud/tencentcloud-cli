**Example 1: Modifying the name of a bandwidth package**



Input: 

```
tccli vpc ModifyBandwidthPackageAttribute --cli-unfold-argument  \
    --BandwidthPackageId bwp-e40edw8y\
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

**Example 2: Modifying the billing mode of a bandwidth package**



Input: 

```
tccli vpc ModifyBandwidthPackageAttribute --cli-unfold-argument  \
    --BandwidthPackageId bwp-e40edw8y\
    --BandwidthPackageName test\
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

