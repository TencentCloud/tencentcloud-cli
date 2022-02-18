**Example 1: 根据源站区域查询可用加速区域**



Input: 

```
tccli gaap DescribeAccessRegionsByDestRegion --cli-unfold-argument  \
    --DestRegion SouthChina
```

Output: 
```
{
    "Response": {
        "AccessRegionSet": [
            {
                "RegionId": "eu-moscow",
                "RegionName": "Russia",
                "ConcurrentList": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "BandwidthList": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "RegionArea": "NorthChina",
                "RegionAreaName": "中国大陆-华北",
                "IDCType": "dc",
                "FeatureBitmap": 3
            }
        ],
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd",
        "TotalCount": 1
    }
}
```

