**Example 1: 返回售卖地域**



Input: 

```
tccli tdmysql DescribeSaleInfo --cli-unfold-argument  \
    --InstanceType serverless
```

Output: 
```
{
    "Response": {
        "RegionList": [
            {
                "AvailableZoneNum": 3,
                "Enable": 1,
                "IsSupportServerless": true,
                "IsSupportedLogReplica": true,
                "Region": "ap-guangzhou",
                "RegionName": "å¹¿å·ž",
                "ZoneGroup": [
                    {
                        "AvailableDiskTypes": [],
                        "IsSupportServerless": true,
                        "SupportTypes": [
                            "0"
                        ],
                        "ZoneNum": 1,
                        "Zones": [
                            "ap-guangzhou-7"
                        ]
                    }
                ],
                "ZoneList": [
                    {
                        "AvailableDiskTypes": [],
                        "Enable": 1,
                        "IsDefaultMaster": 0,
                        "IsSupportServerless": true,
                        "SupportTypes": [
                            "0"
                        ],
                        "Zone": "ap-guangzhou-7",
                        "ZoneName": "å¹¿å·žä¸ƒåŒº"
                    }
                ]
            }
        ],
        "RequestId": "cc7f4880-5ed6-4daa-a45f-df2a5780d573"
    }
}
```

