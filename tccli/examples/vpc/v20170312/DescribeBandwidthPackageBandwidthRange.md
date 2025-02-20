**Example 1: 查询指定带宽包的带宽上下限范围**



Input: 

```
tccli vpc DescribeBandwidthPackageBandwidthRange --cli-unfold-argument  \
    --BandwidthPackageIds bwp-enjefhij bwp-l5jt4oz1
```

Output: 
```
{
    "Response": {
        "BandwidthRangeSet": [
            {
                "BandwidthLowerLimit": 300,
                "BandwidthUpperLimit": 5000,
                "ResourceId": "bwp-enjefhij"
            },
            {
                "BandwidthLowerLimit": 100,
                "BandwidthUpperLimit": 5000,
                "ResourceId": "bwp-l5jt4oz1"
            }
        ],
        "RequestId": "d3c929a2-5b2e-4c90-b826-b4807dd96052"
    }
}
```

