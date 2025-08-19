**Example 1: 查询用户可使用的专属可用区列表**



Input: 

```
tccli cdz DescribeUserAvailableCloudDedicatedZones --cli-unfold-argument  \
    --CheckUin 700000775535 \
    --RegionId 1
```

Output: 
```
{
    "Response": {
        "ZoneIdSet": [
            "2000800002"
        ],
        "ZoneSet": [
            {
                "Zone": "ap-beijing-cdz-dedicatedzone-1",
                "ZoneId": "2000800002",
                "ZoneName": "北京客户专属可用一区",
                "IsLiteMode": false,
                "Region": "ap-beijing"
            }
        ],
        "RequestId": "4f165d08-e21e-4057-ba2c-c2b193930541"
    }
}
```

**Example 2: 按过滤条件查询用户可使用的专属可用区列表**



Input: 

```
tccli cdz DescribeUserAvailableCloudDedicatedZones --cli-unfold-argument  \
    --CheckUin 700000775535 \
    --Filters.0.Name region \
    --Filters.0.Values ap-beijing \
    --Filters.1.Name zone \
    --Filters.1.Values ap-beijing-cdz-haerbin-1
```

Output: 
```
{
    "Response": {
        "ZoneIdSet": [
            "2000800002"
        ],
        "ZoneSet": [
            {
                "Zone": "ap-beijing-cdz-dedicatedzone-1",
                "ZoneId": "2000800002",
                "ZoneName": "北京客户专属可用一区",
                "IsLiteMode": false,
                "Region": "ap-beijing"
            }
        ],
        "RequestId": "4f165d08-e21e-4057-ba2c-c2b193930541"
    }
}
```

