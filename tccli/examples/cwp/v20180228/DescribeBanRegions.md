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
                "RegionName": "华南地区（广州）",
                "ZoneSet": [
                    {
                        "ZoneName": "广州二区"
                    },
                    {
                        "ZoneName": "广州三区"
                    },
                    {
                        "ZoneName": "广州四区"
                    },
                    {
                        "ZoneName": "广州六区"
                    },
                    {
                        "ZoneName": "广州七区"
                    }
                ]
            }
        ],
        "RequestId": "dd2d8482-b462-4260-a9df-2f9e92abd72b"
    }
}
```

