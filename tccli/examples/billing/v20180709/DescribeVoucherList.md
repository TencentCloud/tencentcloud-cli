**Example 1: 获取代金券列表**



Input: 

```
tccli billing DescribeVoucherList --cli-unfold-argument  \
    --Limit 100 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "TotalBalance": 0,
        "VoucherInfos": [
            {
                "Status": 0,
                "BatchCreateTime": "xx",
                "CouponType": "xx",
                "PolicyId": "xx",
                "ActivityName": "xx",
                "Creator": "xx",
                "ProductDefine": "xx",
                "OwnerUin": "xx",
                "VoucherName": "xx",
                "ActivityId": "xx",
                "CreateTime": "xx",
                "PayMode": "xx",
                "Amount": 0,
                "PayScene": "xx",
                "VoucherId": "xx",
                "CodeId": "xx",
                "UsedAmount": 0,
                "EndTime": "xx",
                "LeftAmount": 0,
                "BeginTime": "xx"
            }
        ]
    }
}
```

