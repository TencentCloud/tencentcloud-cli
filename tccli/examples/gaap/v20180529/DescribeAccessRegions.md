**Example 1: 查询加速区域**



Input: 

```
tccli gaap DescribeAccessRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AccessRegionSet": [
            {
                "RegionId": "NorthChina",
                "RegionName": "中国大陆-华北",
                "RegionArea": "NorthChina",
                "RegionAreaName": "中国大陆-华北",
                "IDCType": "dc",
                "FeatureBitmap": 1,
                "SupportFeature": {
                    "NetworkType": [
                        "normal"
                    ]
                }
            }
        ],
        "RequestId": "209e95b9-488d-4a58-bc86-810859577af3"
    }
}
```

