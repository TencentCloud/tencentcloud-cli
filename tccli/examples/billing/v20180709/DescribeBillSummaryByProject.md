**Example 1: DescribeBillSummaryByProject**



Input: 

```
tccli billing DescribeBillSummaryByProject --cli-unfold-argument  \
    --PayerUin 909619400 \
    --BeginTime '2018-11-01 00:00:00' \
    --EndTime '2018-11-01 23:59:59'
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "SummaryOverview": [
            {
                "ProjectId": "0",
                “RealTotalCost": "1596.49",
                "CashPayAmount": "1420.49",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "176.00",
                "RealTotalCostRatio": "100.00",
                "BillMonth": "2018-11",
                "ProjectName": "Default project"
            }
        ],
        "RequestId": "bac68152-46e8-4538-8bdb-040c40567095"
    }
}
```

