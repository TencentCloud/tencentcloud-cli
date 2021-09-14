**Example 1: 获取按标签汇总费用分布**



Input: 

```
tccli billing DescribeBillSummaryByTag --cli-unfold-argument  \
    --BeginTime 2019-09 \
    --EndTime 2019-09 \
    --TagKey province
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "SummaryOverview": [
            {
                "TagValue": "",
                "RealTotalCost": "13001.95",
                "RealTotalCostRatio": "100.00"
            }
        ],
        "SummaryTotal": {
            "RealTotalCost": "13001.95"
        },
        "RequestId": "7119a6ed-5023-4682-9ea3-33102af1b19e"
    }
}
```

