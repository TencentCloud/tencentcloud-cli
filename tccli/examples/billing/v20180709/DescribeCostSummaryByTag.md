**Example 1: 获取按标签汇总消耗详情**



Input: 

```
tccli billing DescribeCostSummaryByTag --cli-unfold-argument  \
    --BeginTime 2025-03-01 00:00:00 \
    --EndTime 2025-03-31 23:59:59 \
    --TagKey olinatest
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "RequestId": "89e54575-dc13-4506-8aaf-7bab9c7e6242",
        "SummaryOverview": [
            {
                "CashPayAmount": "0.03649794",
                "IncentivePayAmount": "1.42589172",
                "RealTotalCost": "1.46238966",
                "RealTotalCostRatio": "0.01",
                "TagValue": "选项4",
                "TotalCost": "2.13082235",
                "TransferPayAmount": "0.00000000",
                "VoucherPayAmount": "0.00000000"
            },
            {
                "CashPayAmount": "349.11233834",
                "IncentivePayAmount": "26791.85486446",
                "RealTotalCost": "27202.36063812",
                "RealTotalCostRatio": "99.99",
                "TagValue": "",
                "TotalCost": "47452.01346118",
                "TransferPayAmount": "0.00000000",
                "VoucherPayAmount": "61.39343531"
            }
        ],
        "SummaryTotal": {
            "RealTotalCost": "27203.82302778",
            "TotalCost": "47454.14428353"
        }
    }
}
```

