**Example 1: 查询云数据库可售卖地域和可用区信息**



Input: 

```
tccli mariadb DescribeSaleInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "e44995d7-4889-4f73-a42a-36c21120e126",
        "RegionList": [
            {
                "AvailableChoice": [
                    {
                        "SlaveZones": [
                            {
                                "ZoneName": "成都一区",
                                "Zone": "ap-chengdu-1",
                                "ZoneId": 160001
                            }
                        ],
                        "MasterZone": {
                            "ZoneName": "成都一区",
                            "Zone": "ap-chengdu-1",
                            "ZoneId": 160001
                        }
                    }
                ],
                "Region": "ap-chengdu",
                "RegionId": 16,
                "ZoneList": [
                    {
                        "ZoneName": "成都二区",
                        "Zone": "ap-chengdu-2",
                        "ZoneId": 160002
                    },
                    {
                        "ZoneName": "成都一区",
                        "Zone": "ap-chengdu-1",
                        "ZoneId": 160001
                    }
                ],
                "RegionName": "成都"
            }
        ]
    }
}
```

