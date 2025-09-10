**Example 1: ~**

~

Input: 

```
tccli ioa DescribeAggrSoftDeviceList --cli-unfold-argument  \
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

