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
                "DbType": "xx",
                "Region": "xx",
                "RegionId": 1,
                "Modules": [
                    {
                        "ModuleName": "xx",
                        "IsDisable": "xx"
                    }
                ],
                "RegionZh": "xx",
                "ZoneSet": [
                    {
                        "PhysicalZone": "xx",
                        "Zone": "xx",
                        "IsSupportServerless": 0,
                        "ZoneId": 100003,
                        "IsSupportNormal": 0,
                        "ZoneZh": "xx"
                    },
                    {
                        "PhysicalZone": "xx",
                        "Zone": "xx",
                        "IsSupportServerless": 0,
                        "ZoneId": 100003,
                        "IsSupportNormal": 0,
                        "ZoneZh": "xx"
                    },
                    {
                        "PhysicalZone": "xx",
                        "Zone": "xx",
                        "IsSupportServerless": 0,
                        "ZoneId": 100004,
                        "IsSupportNormal": 0,
                        "ZoneZh": "xx"
                    }
                ]
            },
            {
                "DbType": "xx",
                "Region": "xx",
                "RegionId": 8,
                "Modules": [
                    {
                        "ModuleName": "xx",
                        "IsDisable": "xx"
                    }
                ],
                "RegionZh": "xx",
                "ZoneSet": [
                    {
                        "PhysicalZone": "xx",
                        "Zone": "xx",
                        "IsSupportServerless": 0,
                        "ZoneId": 800001,
                        "IsSupportNormal": 0,
                        "ZoneZh": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

