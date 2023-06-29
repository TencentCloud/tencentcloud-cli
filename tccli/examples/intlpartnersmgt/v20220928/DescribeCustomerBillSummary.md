**Example 1: DescribeCustomerBillSummary**

通过API获取子客账单汇总值

Input: 

```
tccli intlpartnersmgt DescribeCustomerBillSummary --cli-unfold-argument  \
    --CustomerUin 1 \
    --Month 2023-02 \
    --PayMode postPay \
    --ActionType postpay_deduct_h \
    --IsConfirmed 0
```

Output: 
```
{
    "Response": {
        "TotalCost": 0,
        "RequestId": "123456"
    }
}
```

