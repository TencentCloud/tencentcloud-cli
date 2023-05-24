**Example 1: 获取产品汇总费用分布**

获取产品汇总费用分布

Input: 

```
tccli billing DescribeBillSummaryByProduct --cli-unfold-argument  \
    --EndTime 2018-11 \
    --BeginTime 2018-11
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "SummaryTotal": {
            "RealTotalCost": "1458.00000000",
            "TotalCost": "1458.00000000",
            "VoucherPayAmount": "0.00000000",
            "IncentivePayAmount": "0.00000000",
            "CashPayAmount": "1458.00000000",
            "TransferPayAmount": "0.00000000"
        },
        "SummaryOverview": [
            {
                "BusinessCode": "p_ssl",
                "RealTotalCost": "1458.00000000",
                "TotalCost": "1458.00000000",
                "CashPayAmount": "1458.00000000",
                "IncentivePayAmount": "0.00000000",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "RealTotalCostRatio": "100.00",
                "BillMonth": "2022-07",
                "BusinessCodeName": "SSL证书"
            }
        ],
        "RequestId": "67cd3369-b022-4a6a-818e-7ba5a05cb5d7"
    }
}
```

