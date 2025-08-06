**Example 1: 查询成功**

查询成功

Input: 

```
tccli intlpartnersmgt DescribeCustomerOwnVoucherList --cli-unfold-argument  \
    --Page 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CustomerUin": 800000234475,
                "EffectiveTime": "2025-07-29 10:59:39",
                "ExpireTime": "2025-08-28 23:59:59",
                "PaymentMode": "Prepaid",
                "ProductScope": "SpecifyProductsBlacklist",
                "RemainingAmount": 2,
                "TotalAmount": 2,
                "VoucherId": 12348270,
                "VoucherStatus": "Invalidated"
            }
        ],
        "RequestId": "e106fce6-7c1c-4d06-936b-e581ed07926b",
        "TotalCount": 11221
    }
}
```

