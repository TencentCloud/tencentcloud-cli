**Example 1: 正常调用**



Input: 

```
tccli billing DescribeVoucherInfo --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalBalance": 265645002000000,
        "TotalCount": 1828,
        "RequestId": "47f4df05-5c77-467b-8c83-6b9304e20321",
        "VoucherInfos": [
            {
                "Status": "",
                "PolicyRemark": "",
                "EndTime": "0002-11-30",
                "NominalValue": 1200000000,
                "CreateTime": "2016-03-12 14:51:52",
                "BeginTime": "0002-11-30",
                "PayMode": "prePay",
                "PayScene": "purchase,renew",
                "VoucherId": "PPVIA653S3T7L07A4P",
                "ExcludedProducts": [
                    {
                        "PayMode": "*",
                        "GoodsName": "轻量应用服务器"
                    },
                    {
                        "PayMode": "*",
                        "GoodsName": "腾讯企点客服"
                    },
                    {
                        "PayMode": "*",
                        "GoodsName": "腾讯企点营销云Tencent QiDian Marketing Cloud"
                    }
                ],
                "OwnerUin": "909619400",
                "Balance": 1200000000,
                "ApplicableProducts": {
                    "PayMode": "prePay",
                    "GoodsName": "云服务器CVM"
                }
            }
        ],
        "Unit": "micro"
    }
}
```

