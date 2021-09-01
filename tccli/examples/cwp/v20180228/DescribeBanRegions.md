**Example 1: 获取阻断地域**



Input: 

```
tccli cwp DescribeBanRegions --cli-unfold-argument  \
    --Mode STANDARD_MODE
```

Output: 
```
{
    "Response": {
        "RegionSet": [
            {
                "ZoneSet": [
                    {
                        "ZoneName": "xx"
                    }
                ],
                "RegionName": "xx"
            },
            {
                "ZoneSet": [
                    {
                        "ZoneName": "xx"
                    }
                ],
                "RegionName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

