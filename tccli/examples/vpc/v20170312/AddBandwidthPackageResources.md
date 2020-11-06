**Example 1: Adding resource to a bandwidth package**



Input: 

```
tccli vpc AddBandwidthPackageResources --cli-unfold-argument  \
    --BandwidthPackageId bwp-e40edw8y \
    --ResourceType Address \
    --ResourceIds eip-pez0oibs
```

Output: 
```
{
    "Response": {
        "RequestId": "2ece8f4a-c0f5-4b83-8054-a9b808a5c465"
    }
}
```

