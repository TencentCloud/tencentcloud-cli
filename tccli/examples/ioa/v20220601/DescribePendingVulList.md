**Example 1: DescribePendingVulList接口示例**



Input: 

```
tccli ioa DescribePendingVulList --cli-unfold-argument  \
    --OnlineStatus 5 \
    --Cond.Sort.Field 字符串 \
    --Cond.Sort.Order 字符串 \
    --Cond.FilterGroups.0.Filters.0.Operator 字符串 \
    --Cond.FilterGroups.0.Filters.0.Field 字符串 \
    --Cond.FilterGroups.0.Filters.0.Values 字符串 \
    --Cond.PageNum 1 \
    --Cond.Filters.0.Operator 字符串 \
    --Cond.Filters.0.Field 字符串 \
    --Cond.Filters.0.Values 字符串 \
    --Cond.PageSize 10 \
    --GroupId 1 \
    --DeviceRange 字符串
```

Output: 
```
{
    "Response": {
        "Data": {
            "Item": [
                {
                    "UserName": "abc",
                    "VulScanTime": "abc",
                    "GroupNamePath": "abc",
                    "Mid": "abc",
                    "VulInstallCount": 0,
                    "VulIgnoreCount": 0,
                    "CriticalVulListCount": 0,
                    "StrVersion": "abc",
                    "MacAddr": "abc",
                    "Name": "abc",
                    "GroupName": "abc",
                    "GroupId": 0,
                    "Os": "abc",
                    "Itime": "abc",
                    "Ip": "abc",
                    "OnlineStatus": 0,
                    "VulVersion": "abc",
                    "IoaUserName": "abc",
                    "VulCriticalList": [
                        "abc"
                    ],
                    "LocalIpList": "abc",
                    "ConnActiveTime": "abc",
                    "Id": 0
                }
            ],
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            }
        },
        "RequestId": "abc"
    }
}
```

**Example 2: DescribePendingVulList**

DescribePendingVulList

Input: 

```
tccli ioa DescribePendingVulList --cli-unfold-argument  \
    --OnlineStatus 1 \
    --Cond.PageSize 1 \
    --Cond.PageNum 1 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "60aa48f5-71d9-489c-9b86-72ed126ef39c"
    }
}
```

