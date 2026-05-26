**Example 1: 指标趋势**



Input: 

```
tccli trp DescribeFlavorKingCycleBrandScanMetrics --cli-unfold-argument  \
    --CorpId 10046 \
    --QueryDate 2026-05-01
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Duration": "20260425",
                "Ratio": 0.74
            }
        ],
        "RequestId": "7e82bdd9-5d65-45e6-b18b-6d589dd175da"
    }
}
```

