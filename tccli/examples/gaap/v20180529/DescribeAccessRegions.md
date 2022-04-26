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
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

