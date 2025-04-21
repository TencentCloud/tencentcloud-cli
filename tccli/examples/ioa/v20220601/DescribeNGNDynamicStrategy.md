**Example 1: 示例**

获取动态访问策略详情

Input: 

```
tccli ioa DescribeNGNDynamicStrategy --cli-unfold-argument  \
    --Id 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "abc",
            "UpdateTime": "abc",
            "Id": 0,
            "Name": "abc",
            "Description": "abc",
            "Status": 0,
            "Level": 0,
            "ActionResult": "abc",
            "Hint": "abc",
            "UserScope": {
                "Users": [
                    {
                        "Id": 0,
                        "Name": "abc",
                        "ParentId": 0,
                        "NamePath": "abc",
                        "IdPath": "abc",
                        "UserId": "abc"
                    }
                ],
                "Groups": [
                    {
                        "Id": 0,
                        "Name": "abc",
                        "ParentId": 0,
                        "NamePath": "abc",
                        "IdPath": "abc"
                    }
                ],
                "VirtualGroups": [
                    {
                        "Id": 0,
                        "Name": "abc"
                    }
                ]
            },
            "ResourceScope": {
                "Resources": [
                    {
                        "Id": 0,
                        "Name": "abc"
                    }
                ],
                "ResourceGroups": [
                    {
                        "Id": 0,
                        "Name": "abc"
                    }
                ]
            },
            "TimeCondition": {
                "Type": "abc",
                "TimeScope": [
                    "abc"
                ],
                "DateScope": [
                    "abc"
                ],
                "WeekDays": [
                    0
                ],
                "Months": [
                    0
                ]
            },
            "LocationCondition": {
                "Type": "abc",
                "IPAreaList": [
                    {
                        "Id": 0,
                        "Name": "abc",
                        "Code": "abc",
                        "TotalCount": 0
                    }
                ],
                "Locations": [
                    {
                        "Code": "abc",
                        "Name": "abc",
                        "Id": 0
                    }
                ]
            },
            "PlatformCondition": {
                "Type": "abc",
                "Platforms": [
                    "abc"
                ]
            },
            "AppProcessCondition": {
                "Type": "abc",
                "Apps": [
                    {
                        "Id": 0,
                        "Name": "abc",
                        "OsType": "abc"
                    }
                ],
                "AppCategoryList": [
                    {
                        "Id": 0,
                        "Name": "abc",
                        "OsType": "abc",
                        "TotalCount": 0
                    }
                ]
            },
            "ComplianceCondition": {
                "Type": "abc",
                "LevelScope": [
                    "abc"
                ]
            },
            "UserRiskCondition": {
                "Type": "abc",
                "LevelScope": [
                    "abc"
                ]
            },
            "DeviceCondition": {
                "Type": "abc",
                "Devices": [
                    {
                        "Id": 0,
                        "Name": "abc",
                        "OsType": 0,
                        "OsTypeString": "abc"
                    }
                ],
                "DeviceVirtualGroups": [
                    {
                        "Id": 0,
                        "Name": "abc",
                        "OsType": 0,
                        "OsTypeString": "abc",
                        "TotalCount": 0
                    }
                ]
            }
        },
        "RequestId": "abc"
    }
}
```

