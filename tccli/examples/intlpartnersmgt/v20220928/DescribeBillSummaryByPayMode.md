**Example 1: 通过API获取子客账单付费模式汇总值**

通过API获取子客账单付费模式汇总值

Input: 

```
tccli intlpartnersmgt DescribeBillSummaryByPayMode --cli-unfold-argument  \
    --BillMonth 2022-11 \
    --CustomerUin 123456
```

Output: 
```
{
    "Response": {
        "SummaryOverview": [
            {
                "PayMode": "postPay",
                "PayModeName": "Pay-As-You-Go resources",
                "OriginalCost": "100.00000000",
                "Detail": [
                    {
                        "ActionType": "postpay_deduct_h",
                        "ActionTypeName": "Hourly settlement",
                        "OriginalCost": "100.00000000",
                        "VoucherPayAmount": "100.00000000",
                        "TotalCost": "100.00000000"
                    }
                ],
                "VoucherPayAmount": "100.00000000",
                "TotalCost": "100.00000000"
            }
        ],
        "RequestId": "asdfgh"
    }
}
```

