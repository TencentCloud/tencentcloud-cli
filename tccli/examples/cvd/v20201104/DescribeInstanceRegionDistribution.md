**Example 1: DescribeInstanceRegionDistribution**



Input: 

```
tccli cvd DescribeInstanceRegionDistribution --cli-unfold-argument  \
    --Regions ap-guangzhou \
    --Types S1
```

Output: 
```
{
    "Response": {
        "RequestId": "2bcfe8b7-8ea8-4488-9d17-f1aeb106eecd",
        "DistributionInfo": [
            {
                "Count": 1,
                "Region": "ap-guangzhou"
            }
        ]
    }
}
```

