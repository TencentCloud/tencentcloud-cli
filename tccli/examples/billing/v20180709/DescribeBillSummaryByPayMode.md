**Example 1: 获取按付费模式汇总费用分布**

获取按付费模式汇总费用分布

Input: 

```
tccli billing DescribeBillSummaryByPayMode --cli-unfold-argument  \
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
                "PayMode": "prePay",
                "PayModeName": "包年包月",
                "RealTotalCost": "3228.80000000",
                "TotalCost": "5064.00000000",
                "CashPayAmount": "0.00000000",
                "IncentivePayAmount": "3228.80000000",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "RealTotalCostRatio": "99.49",
                "Detail": [
                    {
                        "ActionType": "prepay_renew",
                        "ActionTypeName": "包年包月续费",
                        "RealTotalCost": "3228.80000000",
                        "TotalCost": "5064.00000000",
                        "CashPayAmount": "0.00000000",
                        "IncentivePayAmount": "3228.80000000",
                        "VoucherPayAmount": "0.00000000",
                        "TransferPayAmount": "0.00000000",
                        "RealTotalCostRatio": "100.00",
                        "BillMonth": "2021-12"
                    }
                ]
            },
            {
                "PayMode": "postPay",
                "PayModeName": "按量计费",
                "RealTotalCost": "16.44000000",
                "TotalCost": "27.64446128",
                "CashPayAmount": "0.00000000",
                "IncentivePayAmount": "16.44000000",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "RealTotalCostRatio": "0.51",
                "Detail": [
                    {
                        "ActionType": "postpay_deduct_h",
                        "ActionTypeName": "按量计费小时结",
                        "RealTotalCost": "19.32711686",
                        "TotalCost": "29.73402790",
                        "CashPayAmount": "3.83470332",
                        "IncentivePayAmount": "15.49241354",
                        "VoucherPayAmount": "0.00000000",
                        "TransferPayAmount": "0.00000000",
                        "RealTotalCostRatio": "96.00",
                        "BillMonth": "2021-12"
                    },
                    {
                        "ActionType": "postpay_deduct_d",
                        "ActionTypeName": "按量计费日结",
                        "RealTotalCost": "0.80604458",
                        "TotalCost": "1.24113445",
                        "CashPayAmount": "0.00000000",
                        "IncentivePayAmount": "0.80604458",
                        "VoucherPayAmount": "0.00000000",
                        "TransferPayAmount": "0.00000000",
                        "RealTotalCostRatio": "4.00",
                        "BillMonth": "2021-12"
                    },
                    {
                        "ActionType": "postpay_deduct_m",
                        "ActionTypeName": "按量计费月结",
                        "RealTotalCost": "0.00000000",
                        "TotalCost": "0.36246037",
                        "CashPayAmount": "0.00000000",
                        "IncentivePayAmount": "0.00000000",
                        "VoucherPayAmount": "0.00000000",
                        "TransferPayAmount": "0.00000000",
                        "RealTotalCostRatio": "0.00",
                        "BillMonth": "2021-12"
                    },
                    {
                        "ActionType": "billVirtualId",
                        "ActionTypeName": "月度计费精度差异",
                        "RealTotalCost": "-3.69316144",
                        "TotalCost": "-3.69316144",
                        "CashPayAmount": "-3.83470332",
                        "IncentivePayAmount": "0.14154188",
                        "VoucherPayAmount": "0.00000000",
                        "TransferPayAmount": "0.00000000",
                        "RealTotalCostRatio": "0.00",
                        "BillMonth": "2021-12"
                    }
                ]
            }
        ],
        "RequestId": "5d83209a-3223-497f-a36b-32330d88e454"
    }
}
```

