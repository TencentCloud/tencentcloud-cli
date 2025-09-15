**Example 1: ~**

~

Input: 

```
tccli ioa DescribeAggrSoftDeviceList --cli-unfold-argument  \
    --Condition.Filters.0.Field 1 \
    --Condition.Filters.0.Operator 1 \
    --Condition.Filters.0.Values 1 \
    --Condition.FilterGroups.0.Filters.0.Field 1 \
    --Condition.FilterGroups.0.Filters.0.Operator 1 \
    --Condition.FilterGroups.0.Filters.0.Values 1 \
    --Condition.Sort.Field 1 \
    --Condition.Sort.Order 1 \
    --Condition.PageSize 1 \
    --Condition.PageNum 10 \
    --Name 1 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            },
            "Total": 0,
            "AggrSoftDeviceList": [
                {
                    "DeviceName": "1",
                    "LastLoginAccount": "1",
                    "DeviceUserName": "1",
                    "Version": "1",
                    "PiracyRisk": 0,
                    "PiracyReason": "1",
                    "InstallTime": "1",
                    "UserPath": "1",
                    "UserGroup": "1",
                    "IP": "1",
                    "MAC": "1",
                    "UseTime": 0,
                    "DeviceId": 0,
                    "FullSoftName": "1"
                }
            ]
        },
        "RequestId": "1"
    }
}
```

