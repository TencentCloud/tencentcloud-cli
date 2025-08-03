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
                        "PhysicalZone": "ap-guangzhou-3",
                        "Zone": "ap-guangzhou-3",
                        "IsSupportServerless": 0,
                        "ZoneId": 100003,
                        "IsSupportNormal": 0,
                        "ZoneZh": "广州三区",
                        "HasPermission": true,
                        "IsWholeRdmaZone": "tcp",
                        "IsSupportCreateCluster": 1
                    },
                    {
                        "PhysicalZone": "ao-guangzhou-5",
                        "Zone": "ap-guangzhou-5",
                        "IsSupportServerless": 0,
                        "ZoneId": 100004,
                        "IsSupportNormal": 0,
                        "ZoneZh": "广州五区",
                        "HasPermission": true,
                        "IsWholeRdmaZone": "whole_rdma",
                        "IsSupportCreateCluster": 0
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
                        "IsWholeRdmaZone": "whole_rdma",
                        "IsSupportCreateCluster": 1
                    }
                ]
            }
        ],
        "RequestId": "8fa5cf5-77db-4e32-90ef-22c71ed95f51"
    }
}
```

