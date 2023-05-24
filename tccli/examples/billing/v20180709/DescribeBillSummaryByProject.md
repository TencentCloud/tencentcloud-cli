**Example 1: DescribeBillSummaryByProject**

DescribeBillSummaryByProject

Input: 

```
tccli billing DescribeBillSummaryByProject --cli-unfold-argument  \
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
                "ProjectId": "0",
                "RealTotalCost": "693.59753331",
                "TotalCost": "1117.51686802",
                "CashPayAmount": "-1.24511821",
                "IncentivePayAmount": "694.84265152",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "RealTotalCostRatio": "36.01",
                "BillMonth": "2022-04",
                "ProjectName": "默认项目"
            },
            {
                "ProjectId": "1161824",
                "RealTotalCost": "692.84272353",
                "TotalCost": "1067.95034395",
                "CashPayAmount": "0.35221517",
                "IncentivePayAmount": "692.49050836",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "RealTotalCostRatio": "35.97",
                "BillMonth": "2022-04",
                "ProjectName": "安玛"
            },
            {
                "ProjectId": "1178116",
                "RealTotalCost": "363.78903384",
                "TotalCost": "582.90620577",
                "CashPayAmount": "0.46518134",
                "IncentivePayAmount": "363.32385250",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "RealTotalCostRatio": "18.89",
                "BillMonth": "2022-04",
                "ProjectName": "开放平台"
            },
            {
                "ProjectId": "1229753",
                "RealTotalCost": "175.91070932",
                "TotalCost": "293.01647591",
                "CashPayAmount": "0.42772170",
                "IncentivePayAmount": "175.48298762",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "RealTotalCostRatio": "9.13",
                "BillMonth": "2022-04",
                "ProjectName": "有云"
            }
        ],
        "RequestId": "7651899f-01c5-4988-b203-59eae7e55272"
    }
}
```

