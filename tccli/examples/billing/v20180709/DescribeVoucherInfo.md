**Example 1: 获取代金券相关信息**



Input: 

```
tccli billing DescribeVoucherInfo --cli-unfold-argument  \
    --Limit 10 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "TotalBalance": 0,
        "VoucherInfos": [
            {
                "Status": "overdue",
                "OwnerUin": "xx",
                "PayMode": "*postPay*",
                "NominalValue": 0,
                "PayScene": "all",
                "VoucherId": "xx",
                "EndTime": "xx",
                "Balance": 0,
                "BeginTime": "xx",
                "ApplicableProducts": {
                    "GoodsName": "全产品通用",
                    "PayMode": "*"
                },
                "ExcludedProducts": [
                    {
                        "GoodsName": "xxx",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "xxx",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "xxx",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "xxx",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "xxx",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "xxx",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "xxx",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "xxx",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "xxx",
                        "PayMode": "*"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

