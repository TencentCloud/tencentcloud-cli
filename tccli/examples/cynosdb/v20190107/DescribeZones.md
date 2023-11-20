**Example 1: 查询可售卖地域可用区信息**

仅查看用户有权限的可用区

Input: 

```
tccli cynosdb DescribeZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionSet": [
            {
                "DbType": "MYSQL",
                "Region": "ap-guangzhou",
                "RegionId": 100001,
                "Modules": [
                    {
                        "ModuleName": "is.disable.wan",
                        "IsDisable": "yes"
                    }
                ],
                "RegionZh": "广州",
                "ZoneSet": [
                    {
                        "PhysicalZone": "ap-guangzhou-2",
                        "Zone": "ap-guangzhou-2",
                        "IsSupportServerless": 0,
                        "ZoneId": 100003,
                        "IsSupportNormal": 0,
                        "ZoneZh": "广州二区",
                        "HasPermission": true,
                        "IsWholeRdmaZone": "abc"
                    },
                    {
                        "PhysicalZone": "ao-guangzhou-5",
                        "Zone": "ap-guangzhou-5",
                        "IsSupportServerless": 0,
                        "ZoneId": 100004,
                        "IsSupportNormal": 0,
                        "ZoneZh": "广州五区",
                        "HasPermission": true,
                        "IsWholeRdmaZone": "abc"
                    }
                ]
            },
            {
                "DbType": "MYSQL",
                "Region": "ap-beijing",
                "RegionId": 8,
                "Modules": [
                    {
                        "ModuleName": "is.disable.wan",
                        "IsDisable": "no"
                    }
                ],
                "RegionZh": "北京",
                "ZoneSet": [
                    {
                        "PhysicalZone": "ap-beijing-5",
                        "Zone": "ap-beijing-5",
                        "IsSupportServerless": 0,
                        "ZoneId": 800001,
                        "IsSupportNormal": 0,
                        "ZoneZh": "北京五区",
                        "HasPermission": true,
                        "IsWholeRdmaZone": "abc"
                    }
                ]
            }
        ],
        "RequestId": "1qwert-123-asbc"
    }
}
```

