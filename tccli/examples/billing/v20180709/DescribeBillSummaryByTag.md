**Example 1: 获取按标签汇总费用分布**

获取按标签汇总费用分布

Input: 

```
tccli billing DescribeBillSummaryByTag --cli-unfold-argument  \
    --TagKey province \
    --EndTime 2019-09 \
    --BeginTime 2019-09
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "SummaryOverview": [
            {
                "TagValue": "",
                "RealTotalCost": "3081.26707105",
                "TotalCost": "5026.37707609",
                "RealTotalCostRatio": "99.88",
                "CashPayAmount": "3081.26707105",
                "IncentivePayAmount": "0.00000000",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000"
            },
            {
                "TagValue": "kCH0vYyI",
                "RealTotalCost": "3.77264000",
                "TotalCost": "4.71580000",
                "RealTotalCostRatio": "0.12",
                "CashPayAmount": "3.77264000",
                "IncentivePayAmount": "0.00000000",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000"
            }
        ],
        "SummaryTotal": {
            "RealTotalCost": "3085.03971105",
            "TotalCost": "5031.09287609"
        },
        "RequestId": "0cdd9b57-4597-4e78-a60b-0e72f7637a3a"
    }
}
```

