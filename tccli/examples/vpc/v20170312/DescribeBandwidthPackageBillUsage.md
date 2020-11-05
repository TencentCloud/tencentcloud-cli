**Example 1: Querying the current billable usage of a bandwidth package**



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
                "BandwidthUsage": 1.0
            }
        ],
        "RequestId": "f30a042c-0234-4474-99e5-2f16be243be5"
    }
}
```

