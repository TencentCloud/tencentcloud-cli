**Example 1: 获取保险版的计费信息**



Input: 

```
tccli antiddos DescribeInsuranceBillingInfo --cli-unfold-argument  \
    --InstanceIds lh-xxxxxx
```

Output: 
```
{
    "Response": {
        "InsuranceBillingInfos": [
            {
                "CreateTime": "2023-01-01 00:00:00",
                "ExpireTime": "2023-01-01 00:00:00",
                "InstanceId": "lh-xxxxxxx",
                "InsuranceId": "newinsurance-xxxxxxx",
                "AutoRenewFlag": 1,
                "Status": 6
            }
        ],
        "RequestId": "abc"
    }
}
```

