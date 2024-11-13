**Example 1: 查询专属可用区白名单信息**

查询专属可用区白名单信息



Input: 

```
tccli cdz DescribeCloudDedicatedZoneWhiteList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ZoneSet": [
            {
                "AppId": "1318574890",
                "CdzId": "cdz-el3pwfik",
                "RegionId": "1",
                "Uin": "100031808324",
                "WhiteList": [
                    "800000918292"
                ],
                "WhiteListKey": "CDZ_WHITELIST",
                "ZoneId": "100002",
                "ZoneName": "Some Zone"
            }
        ],
        "RequestId": "753f3845-637f-4023-b141-3440f20b16d8"
    }
}
```

