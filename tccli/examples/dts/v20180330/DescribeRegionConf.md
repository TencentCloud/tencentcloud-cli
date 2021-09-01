**Example 1: 查询可售卖订阅的地域**



Input: 

```
tccli dts DescribeRegionConf --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "RegionName": "广州",
                "Region": "ap-guangzhou",
                "Area": "华南地区",
                "IsDefaultRegion": 1,
                "Status": 1
            }
        ]
    }
}
```

