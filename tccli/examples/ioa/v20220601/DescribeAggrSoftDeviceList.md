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

**Example 2: 测试查询**



Input: 

```
tccli ioa DescribeAggrSoftDeviceList --cli-unfold-argument  \
    --Condition.PageSize 1 \
    --Condition.PageNum 1 \
    --Name group.is.workflow \
    --OsType 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "AggrSoftDeviceList": [
                {
                    "DeviceId": 288744,
                    "DeviceName": "spike0528的虚拟机",
                    "DeviceUserName": "spike0528",
                    "FullSoftName": "group.is.workflow",
                    "IP": "119.147.10.159",
                    "Id": 2147484652,
                    "InstallTime": "2025/05/28",
                    "LastLoginAccount": "spike",
                    "MAC": "FA:45:FD:8C:B0:5F",
                    "NewVersion": "",
                    "OsType": 2,
                    "PiracyReason": "",
                    "PiracyRisk": 0,
                    "RemarkName": "",
                    "SoftwareId": 222,
                    "UpgradeSoftId": 0,
                    "UseTime": 0,
                    "UserGroup": "全网终端.未分组终端",
                    "UserPath": "全网账户.lucal-",
                    "Version": ""
                }
            ],
            "Page": {
                "PageCount": 16,
                "PageNum": 1,
                "PageSize": 1,
                "Total": 16
            },
            "Total": 16
        },
        "RequestId": "ae6a0f42-a5d5-4669-ad5e-7091072bf4c2"
    }
}
```

