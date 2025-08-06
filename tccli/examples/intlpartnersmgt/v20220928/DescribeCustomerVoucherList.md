**Example 1: 查询成功**

查询成功

Input: 

```
tccli intlpartnersmgt DescribeCustomerVoucherList --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10 \
    --VoucherId 12342356
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ApplyReason": "接口测试使用，请勿审核，子客券",
                "CustomerUin": 800000183985,
                "EffectiveTime": "2025-07-21 06:10:24",
                "ExpireTime": "2025-10-19 23:59:59",
                "PaymentMode": "AllPayment",
                "ProductScope": "AllProducts",
                "RemainingAmount": 0.797104,
                "TotalAmount": 1,
                "Usage": "CustomerOffer",
                "VoucherId": 12342356,
                "VoucherStatus": "Canceled"
            }
        ],
        "RequestId": "0849df12-3c82-4edb-a4be-18df464ce468",
        "TotalCount": 1
    }
}
```

