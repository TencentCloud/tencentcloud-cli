**Example 1: 请求示例**



Input: 

```
tccli sms SmsPackagesStatistics --cli-unfold-argument  \
    --SmsSdkAppid 1400006879 \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "SmsPackagesStatisticsSet": [
            {
                "PackageCreateTime": "2019-05-01 00:00:00",
                "PackageEffectiveTime": "2019-05-01 00:00:00",
                "PackageExpiredTime": "2019-05-31 23:59:59",
                "PackageCreateUnixTime": 1556640000,
                "PackageExpiredUnixTime": 1556640000,
                "PackageEffectiveUnixTime": 1559318399,
                "AmountOfPackage": 1000,
                "TypeOfPackage": 0,
                "PackageId": 1000876572,
                "CurrentUsage": 100
            },
            {
                "PackageCreateTime": "2019-04-01 00:00:00",
                "PackageEffectiveTime": "2019-04-01 00:00:00",
                "PackageExpiredTime": "2019-04-30 23:59:59",
                "PackageCreateUnixTime": 1554048000,
                "PackageExpiredUnixTime": 1554048000,
                "PackageEffectiveUnixTime": 1556639999,
                "AmountOfPackage": 1000,
                "TypeOfPackage": 0,
                "PackageId": 1000791745,
                "CurrentUsage": 100
            }
        ],
        "RequestId": "90242d16-de50-4c9a-80fc-7709b566e93e"
    }
}
```

