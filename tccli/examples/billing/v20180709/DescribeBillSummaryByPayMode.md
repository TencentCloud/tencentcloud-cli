**Example 1: 获取按付费模式汇总费用分布**



Input: 

```
tccli billing DescribeBillSummaryByPayMode --cli-unfold-argument  \
    --PayerUin 909619400\
    --BeginTime '2018-11-01 00:00:00'\
    --EndTime '2018-11-01 23:59:59'
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "SummaryOverview": [
            {
                "PayMode": "prePay",
                "PayModeName": "包年包月",
                "RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "Detail": []
            },
            {
                "PayMode": "postPay",
                "PayModeName": "按量计费",
                "RealTotalCost": "1596.49",
                "CashPayAmount": "1420.49",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "176.00",
                "RealTotalCostRatio": "100.00",
                "Detail": [
                    {
                        "ActionType": "postpay_deduct",
                        "ActionTypeName": "按量计费扣费",
                        "RealTotalCost": "1598.44",
                        "CashPayAmount": "1422.45",
                        "IncentivePayAmount": "0.00",
                        "VoucherPayAmount": "175.99",
                        "RealTotalCostRatio": "100.00",
                        "BillMonth": "2018-11"
                    },
                    {
                        "ActionType": "billVirtualId",
                        "ActionTypeName": "月度计费精度差异",
                        "RealTotalCost": "-1.95",
                        "CashPayAmount": "-1.96",
                        "IncentivePayAmount": "0.00",
                        "VoucherPayAmount": "0.01",
                        "RealTotalCostRatio": "0.00",
                        "BillMonth": "2018-11"
                    }
                ]
            }
        ],
        "RequestId": "f40a84b9-d74b-4cf5-89ea-56558baf1c96"
    }
}
```

