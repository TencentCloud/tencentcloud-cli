**Example 1: 查询分布式数据库可售卖地域和可用区信息**



Input: 

```
tccli dcdb DescribeDCDBSaleInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "c70bafb9-914e-4160-a92c-a3d4582fcbbc",
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

