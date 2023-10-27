**Example 1: 获取保险版的计费信息**



Input: 

```
tccli antiddos DescribeInsuranceBillingInfo --cli-unfold-argument  \
    --InstanceId lh-xxxxxx
```

Output: 
```
{
    "Response": {
        "CreateTime": "2023-01-01 00:00:00",
        "ExpireTime": "2023-01-01 00:00:00",
        "AutoRenewFlag": 1,
        "RequestId": "abc"
    }
}
```

