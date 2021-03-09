**Example 1: 查询用户增值包详情**



Input: 

```
tccli tcb DescribeExtraPkgBillingInfo --cli-unfold-argument  \
    --EnvId cdnheader-v2a
```

Output: 
```
{
    "Response": {
        "EnvInfoList": [
            {
                "EnvId": "cdnheader-v2",
                "PackageId": "tcb_pkg_hosting_add_2",
                "Status": "normal",
                "PayMode": "prepayment",
                "IsolatedTime": "0000-00-00 00:00:00",
                "ExpireTime": "2020-05-16 23:59:59",
                "CreateTime": "2020-04-16 18:50:10",
                "UpdateTime": "2020-05-14 16:00:42",
                "IsAutoRenew": "true",
                "PaymentChannel": "qcloud"
            }
        ],
        "RequestId": "e2450786-2fec-47de-9d8d-ee1bb7805d38",
        "Total": 1
    }
}
```

