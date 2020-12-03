**Example 1: 获取点位列表**



Input: 

```
tccli ump DescribeZones --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Zones": [
            {
                "ZoneId": 1,
                "ZoneName": "zone_name",
                "ZoneType": 1,
                "BindNum": 0,
                "DebugNum": 0,
                "BunkCodes": "bunk_codes",
                "FloorId": 0,
                "FloorName": "floor_name",
                "State": 0
            }
        ]
    }
}
```

