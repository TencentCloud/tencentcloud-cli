**Example 1: Getting cost distribution over different tags**



Input: 

```
tccli billing DescribeBillSummaryByTag --cli-unfold-argument  \
    --PayerUin 100000007615\
    --BeginTime '9/1/2019 00:00:00'\
    --EndTime '9/30/2019 23:59:59'\
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
                “RealTotalCost": "0.30",
                "RealTotalCostRatio": "17.08"
            },
            {
                "TagValue": "shanghai",
                “RealTotalCost": "0.26",
                "RealTotalCostRatio": "15.21"
            },
            {
                "TagValue": "beijing",
                “RealTotalCost": "0.26",
                "RealTotalCostRatio": "15.21"
            },
            {
                "TagValue": "guangdong",
                “RealTotalCost": "0.26",
                "RealTotalCostRatio": "15.21"
            },
            {
                "TagValue": "xiamen",
                “RealTotalCost": "0.22",
                "RealTotalCostRatio": "12.43"
            },
            {
                "TagValue": "tianjin",
                “RealTotalCost": "0.22",
                "RealTotalCostRatio": "12.43"
            },
            {
                "TagValue": "sichuan",
                “RealTotalCost": "0.22",
                "RealTotalCostRatio": "12.43"
            }
        ],
        "SummaryTotal": {
            "RealTotalCost": "1.74"
        },
        "RequestId": "b7649c63-59e5-49d3-bbde-64292cc4174d"
    }
}
```

