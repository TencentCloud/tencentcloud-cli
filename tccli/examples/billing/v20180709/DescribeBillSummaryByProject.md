**Example 1: DescribeBillSummaryByProject**



Input: 

```
tccli billing DescribeBillSummaryByProject --cli-unfold-argument  \
    --BeginTime 2018-11 \
    --EndTime 2018-11
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "SummaryOverview": [
            {
                "ProjectId": "0",
                "RealTotalCost": "224.81",
                "TotalCost": "-",
                "CashPayAmount": "206.12",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "18.69",
                "RealTotalCostRatio": "100.00",
                "BillMonth": "2021-01",
                "ProjectName": "默认项目"
            }
        ],
        "RequestId": "ba1319fb-8875-4289-a717-4125ce26802c"
    }
}
```

