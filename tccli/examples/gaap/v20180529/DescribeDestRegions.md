**Example 1: 查询源站 区域**



Input: 

```
tccli gaap DescribeDestRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DestRegionSet": [
            {
                "RegionId": "NorthChina",
                "RegionAreaName": "中国大陆-华北",
                "IDCType": "dc",
                "FeatureBitmap": 1,
                "RegionArea": "NorthChina",
                "RegionName": "中国大陆-华北",
                "SupportFeature": {
                    "NetworkType": [
                        "normal",
                        "cn2"
                    ]
                }
            }
        ],
        "RequestId": "dad2a717-3c7d-444d-8f98-0cca9c897ff3"
    }
}
```

