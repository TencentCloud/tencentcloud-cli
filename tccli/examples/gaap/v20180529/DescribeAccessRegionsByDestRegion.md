**Example 1: 根据源站区域查询可用加速区域**



Input: 

```
tccli gaap DescribeAccessRegionsByDestRegion --cli-unfold-argument  \
    --DestRegion Hongkong
```

Output: 
```
{
    "Response": {
        "AccessRegionSet": [
            {
                "RegionId": "Chongqing",
                "RegionName": "重庆",
                "ConcurrentList": [
                    2,
                    5,
                    10,
                    20,
                    30
                ],
                "BandwidthList": [
                    10,
                    20,
                    50,
                    100,
                    200,
                    500,
                    1000
                ],
                "RegionArea": "SouthwestChina",
                "RegionAreaName": "重庆",
                "IDCType": "dc",
                "FeatureBitmap": 71
            }
        ],
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd",
        "TotalCount": 1
    }
}
```

