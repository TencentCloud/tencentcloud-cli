**Example 1: 请求示例**

请求示例

Input: 

```
tccli sms SmsPackagesStatistics --cli-unfold-argument  \
    --SmsSdkAppId 1400006874 \
    --EndTime 2021043023 \
    --Limit 2 \
    --BeginTime 2021040113 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "SmsPackagesStatisticsSet": [
            {
                "PackageCreateTime": 1617292800,
                "PackageExpiredTime": 1617292800,
                "PackageEffectiveTime": 1619884800,
                "PackageType": 1,
                "CurrentUsage": 1000,
                "PackageId": 1000791745,
                "PackageAmount": 1000
            },
            {
                "PackageCreateTime": 1617379200,
                "PackageExpiredTime": 1617379200,
                "PackageEffectiveTime": 1619971200,
                "PackageType": 1,
                "CurrentUsage": 100,
                "PackageId": 1000876572,
                "PackageAmount": 1000
            }
        ],
        "RequestId": "3314836f-0b10-45cb-b7be-593e84c1c197"
    }
}
```

