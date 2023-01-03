**Example 1: 示例一**



Input: 

```
tccli region DescribeRegionsAndZones --cli-unfold-argument  \
    --Product xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "ProductType": "xx",
        "ResourceRegionSet": [
            {
                "ProductWhiteList": "xx",
                "RegionNameJp": "xx",
                "Weight": 1,
                "OnlineState": "xx",
                "RegionState": "xx",
                "Region": "xx",
                "RegionId": "xx",
                "RegionNameEn": "xx",
                "LocationJp": "xx",
                "RegionType": "xx",
                "RegionShortName": "xx",
                "LocationKo": "xx",
                "InnerDomainName": "xx",
                "OuterDomainName": "xx",
                "Location": "xx",
                "LocationEn": "xx",
                "ResourceZoneSet": [
                    {
                        "ProductWhiteList": "xx",
                        "ZoneNameEn": "xx",
                        "Weight": 1,
                        "Zone": "xx",
                        "OnlineState": "xx",
                        "SaleType": "xx",
                        "WhiteList": "xx",
                        "ZoneId": "xx",
                        "ZoneState": "xx",
                        "MachineRoomType": "xx",
                        "ZoneNameJp": "xx",
                        "LifeState": "xx",
                        "ZoneNameKo": "xx",
                        "ZoneName": "xx"
                    }
                ],
                "RegionNameKo": "xx",
                "RegionName": "xx"
            }
        ]
    }
}
```

