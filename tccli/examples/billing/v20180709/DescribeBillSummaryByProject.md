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
                "RealTotalCost": "1596.49",
                "CashPayAmount": "1420.49",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "176.00",
                "RealTotalCostRatio": "100.00",
                "BillMonth": "2018-11",
                "ProjectName": "默认项目"
            }
        ],
        "RequestId": "bac68152-46e8-4538-8bdb-040c40567095"
    }
}
```

