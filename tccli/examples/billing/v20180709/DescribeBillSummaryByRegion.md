**Example 1: 获取按地域汇总费用分布**

获取按地域汇总费用分布

Input: 

```
tccli billing DescribeBillSummaryByRegion --cli-unfold-argument  \
    --EndTime 2018-11 \
    --BeginTime 2018-11
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "SummaryOverview": [
            {
                "RegionId": "1",
                "RealTotalCost": "100631.85486247",
                "TotalCost": "101708.25486247",
                "CashPayAmount": "2922.91140386",
                "IncentivePayAmount": "97708.94345861",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "RealTotalCostRatio": "55.61",
                "BillMonth": "2021-11",
                "RegionName": "华南地区（广州）"
            },
            {
                "RegionId": "8",
                "RealTotalCost": "52596.91309090",
                "TotalCost": "52596.91309090",
                "CashPayAmount": "64.99381195",
                "IncentivePayAmount": "52531.91927895",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "RealTotalCostRatio": "29.07",
                "BillMonth": "2021-11",
                "RegionName": "华北地区（北京）"
            },
            {
                "RegionId": "4",
                "RealTotalCost": "27731.41174702",
                "TotalCost": "27731.41174702",
                "CashPayAmount": "71.09880801",
                "IncentivePayAmount": "27660.31293901",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "RealTotalCostRatio": "15.32",
                "BillMonth": "2021-11",
                "RegionName": "华东地区（上海）"
            },
            {
                "RegionId": "0",
                "RealTotalCost": "-5.24970039",
                "TotalCost": "-5.24970039",
                "CashPayAmount": "-3059.00402382",
                "IncentivePayAmount": "3053.75432343",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2021-11",
                "RegionName": "其他"
            }
        ],
        "RequestId": "0053df4c-c08d-4f43-bcaf-e181fc501167"
    }
}
```

