**Example 1: 获取代金券相关信息**

获取代金券相关信息

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
        "RequestId": "9988deda-d6b4-4c74-9bbf-b3f0cd4f5dba",
        "TotalBalance": 42000000000,
        "TotalCount": 2,
        "VoucherInfos": [
            {
                "ApplicableProducts": {
                    "GoodsName": "全产品通用",
                    "PayMode": "*"
                },
                "Balance": 12000000000,
                "BeginTime": "2023-01-10 14:42:17",
                "EndTime": "2023-04-10 14:42:17",
                "ExcludedProducts": [
                    {
                        "GoodsName": "域名注册",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "云市场",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "云市场镜像",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "培训服务training",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "节省计划",
                        "PayMode": "*"
                    }
                ],
                "NominalValue": 30000000000,
                "OwnerUin": "100026601318",
                "PayMode": "*",
                "PayScene": "settle account",
                "Status": "unUsed",
                "VoucherId": "OZRCGNAV5AB9H9ECMP1VVP"
            },
            {
                "ApplicableProducts": {
                    "GoodsName": "全产品通用",
                    "PayMode": "*"
                },
                "Balance": 30000000000,
                "BeginTime": "2023-02-07 16:40:45",
                "EndTime": "2023-05-08 16:40:45",
                "ExcludedProducts": [
                    {
                        "GoodsName": "域名注册",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "云市场",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "云市场镜像",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "培训服务training",
                        "PayMode": "*"
                    },
                    {
                        "GoodsName": "节省计划",
                        "PayMode": "*"
                    }
                ],
                "NominalValue": 30000000000,
                "OwnerUin": "100026601318",
                "PayMode": "*",
                "PayScene": "settle account",
                "Status": "unUsed",
                "VoucherId": "OZRCGNAV8D9BMI9KMG1FIQ"
            }
        ]
    }
}
```

