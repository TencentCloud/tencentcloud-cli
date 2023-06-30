**Example 1: 示例**



Input: 

```
tccli tcb DescribeBillingInfo --cli-unfold-argument  \
    --EnvId tnt-j715s5gda
```

Output: 
```
{
    "Response": {
        "EnvBillingInfoList": [
            {
                "EnvId": "tnt-j715s5gda",
                "PackageId": "professional",
                "IsAutoRenew": true,
                "Status": "NORMAL",
                "PayMode": "PREPAYMENT",
                "IsolatedTime": "2011-5-16 12:15:01",
                "ExpireTime": "2019-5-25 12:15:01",
                "CreateTime": "2016-5-25 12:15:01",
                "UpdateTime": "2019-4-25 12:15:01"
            }
        ],
        "RequestId": "ec5dde6a-6c21-4777-bf4a-99e1f910247e"
    }
}
```

