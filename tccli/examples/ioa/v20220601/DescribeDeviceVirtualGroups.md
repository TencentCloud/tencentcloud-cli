**Example 1: 示例1**

查询终端自定义分组列表

Input: 

```
tccli ioa DescribeDeviceVirtualGroups --cli-unfold-argument  \
    --OsType 0 \
    --Condition.PageNum 0 \
    --Condition.PageSize 10 \
    --Condition.Filters.0.Field Name \
    --Condition.Filters.0.Operator like \
    --Condition.Filters.0.Values auottest1666336897100 \
    --Condition.Sort.Field Itime \
    --Condition.Sort.Order desc
```

Output: 
```
{
    "Response": {
        "RequestId": "0bd4d6b9-be26-4435-9f3e-79dbdb0c57c9",
        "Data": {
            "Page": {
                "PageNum": 1,
                "Total": 0,
                "PageCount": 0,
                "PageSize": 1000
            },
            "Items": [
                {
                    "Utime": "2022-10-21 15:21:37",
                    "DeviceVirtualGroupName": "auottest1666336897100",
                    "DeviceCount": 0,
                    "Itime": "2022-10-21 15:21:37",
                    "OsType": 0,
                    "Id": 356
                }
            ]
        }
    }
}
```

**Example 2: 示例2**

展示自定义分组列表

Input: 

```
tccli ioa DescribeDeviceVirtualGroups --cli-unfold-argument  \
    --Condition.FilterGroups.0.Filters.0.Field DeviceVirtualGroupName \
    --Condition.FilterGroups.0.Filters.0.Operator eq \
    --Condition.FilterGroups.0.Filters.0.Values auto00 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "DeviceCount": 0,
                    "DeviceVirtualGroupName": "auto00",
                    "Id": 7,
                    "Itime": "2023-03-28T15:07:52.581053+08:00",
                    "OsType": 0,
                    "Utime": "2023-03-28T15:24:46.281814+08:00"
                }
            ],
            "Page": {
                "PageCount": 1,
                "PageNum": 1,
                "PageSize": 1000,
                "Total": 1
            }
        },
        "RequestId": "5d27c416-73d6-4081-809b-c5ac5943f33c"
    }
}
```

**Example 3: 查询设备自定义分组列表**

查询设备自定义分组列表

Input: 

```
tccli ioa DescribeDeviceVirtualGroups --cli-unfold-argument  \
    --DomainInstanceId 1 \
    --Condition.PageSize 10 \
    --Condition.PageNum 1 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "Page": {
                "PageCount": 0,
                "PageNum": 1,
                "PageSize": 10,
                "Total": 0
            }
        },
        "RequestId": "a4408eff-66b2-4705-ac4e-80c9a1371088"
    }
}
```

