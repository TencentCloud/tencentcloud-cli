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
                "CdzId": "xx",
                "ZoneId": "xx",
                "Uin": "xx",
                "AppId": "xx",
                "WhiteListKey": "xx",
                "RegionId": "xx",
                "ZoneName": "xx",
                "WhiteList": [
                    "xx"
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

