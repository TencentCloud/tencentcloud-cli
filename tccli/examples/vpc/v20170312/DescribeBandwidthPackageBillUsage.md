**Example 1: 查询共享带宽包的当前计费用量**



Input: 

```
tccli vpc DescribeBandwidthPackageBillUsage --cli-unfold-argument  \
    --BandwidthPackageId bwp-pply3nak
```

Output: 
```
{
    "Response": {
        "BandwidthPackageBillBandwidthSet": [
            {
                "BandwidthUsage": 1
            }
        ],
        "RequestId": "f30a042c-0234-4474-99e5-2f16be243be5"
    }
}
```

