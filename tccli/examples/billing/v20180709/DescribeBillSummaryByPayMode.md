**Example 1: 获取按付费模式汇总费用分布**



Input: 

```
tccli billing DescribeBillSummaryByPayMode --cli-unfold-argument  \
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
                "PayMode": "prePay",
                "PayModeName": "包年包月",
                "RealTotalCost": "0.00",
                "TotalCost": "-",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "Detail": [
                    {
                        "ActionType": "prepay_purchase",
                        "ActionTypeName": "包年包月新购",
                        "RealTotalCost": "0.00",
                        "TotalCost": "-",
                        "CashPayAmount": "0.00",
                        "IncentivePayAmount": "0.00",
                        "VoucherPayAmount": "0.00",
                        "RealTotalCostRatio": "100.00",
                        "BillMonth": "2021-01"
                    }
                ]
            },
            {
                "PayMode": "postPay",
                "PayModeName": "按量计费",
                "RealTotalCost": "224.81",
                "TotalCost": "-",
                "CashPayAmount": "206.12",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "18.69",
                "RealTotalCostRatio": "100.00",
                "Detail": [
                    {
                        "ActionType": "recon_deduct",
                        "ActionTypeName": "调账扣费",
                        "RealTotalCost": "206.45",
                        "TotalCost": "-",
                        "CashPayAmount": "206.45",
                        "IncentivePayAmount": "0.00",
                        "VoucherPayAmount": "0.00",
                        "RealTotalCostRatio": "87.39",
                        "BillMonth": "2021-01"
                    },
                    {
                        "ActionType": "postpay_deduct_s",
                        "ActionTypeName": "竞价实例小时结",
                        "RealTotalCost": "26.78",
                        "TotalCost": "-",
                        "CashPayAmount": "6.30",
                        "IncentivePayAmount": "0.00",
                        "VoucherPayAmount": "20.48",
                        "RealTotalCostRatio": "11.34",
                        "BillMonth": "2021-01"
                    },
                    {
                        "ActionType": "billVirtualId",
                        "ActionTypeName": "月度计费精度差异",
                        "RealTotalCost": "2.98",
                        "TotalCost": "-",
                        "CashPayAmount": "0.70",
                        "IncentivePayAmount": "0.00",
                        "VoucherPayAmount": "2.28",
                        "RealTotalCostRatio": "1.26",
                        "BillMonth": "2021-01"
                    },
                    {
                        "ActionType": "postpay_deduct_m",
                        "ActionTypeName": "按量计费月结",
                        "RealTotalCost": "0.02",
                        "TotalCost": "-",
                        "CashPayAmount": "0.00",
                        "IncentivePayAmount": "0.00",
                        "VoucherPayAmount": "0.02",
                        "RealTotalCostRatio": "0.01",
                        "BillMonth": "2021-01"
                    },
                    {
                        "ActionType": "postpay_deduct_d",
                        "ActionTypeName": "按量计费日结",
                        "RealTotalCost": "0.00",
                        "TotalCost": "-",
                        "CashPayAmount": "0.00",
                        "IncentivePayAmount": "0.00",
                        "VoucherPayAmount": "0.00",
                        "RealTotalCostRatio": "0.00",
                        "BillMonth": "2021-01"
                    },
                    {
                        "ActionType": "recon_increase",
                        "ActionTypeName": "调账补偿",
                        "RealTotalCost": "-2.00",
                        "TotalCost": "-",
                        "CashPayAmount": "-2.00",
                        "IncentivePayAmount": "0.00",
                        "VoucherPayAmount": "0.00",
                        "RealTotalCostRatio": "0.00",
                        "BillMonth": "2021-01"
                    },
                    {
                        "ActionType": "recon_increase_d",
                        "ActionTypeName": "优惠补偿",
                        "RealTotalCost": "-9.42",
                        "TotalCost": "-",
                        "CashPayAmount": "-5.33",
                        "IncentivePayAmount": "0.00",
                        "VoucherPayAmount": "-4.09",
                        "RealTotalCostRatio": "0.00",
                        "BillMonth": "2021-01"
                    }
                ]
            }
        ],
        "RequestId": "cbe90413-4027-4c7d-a6de-82bc57db396c"
    }
}
```

