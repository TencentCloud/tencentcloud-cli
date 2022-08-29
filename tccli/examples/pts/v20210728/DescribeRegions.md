**Example 1: 查询地域列表**



Input: 

```
tccli pts DescribeRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionSet": [
            {
                "CreatedAt": "2021-08-20T16:33:00+08:00",
                "UpdatedAt": "2021-08-20T16:33:00+08:00",
                "RegionId": 1,
                "Region": "ap-guangzhou",
                "RegionShortName": "gz",
                "RegionState": 1,
                "RegionName": "广州",
                "Area": "华南地区"
            },
            {
                "CreatedAt": "2021-08-20T16:33:00+08:00",
                "UpdatedAt": "2021-08-20T16:33:00+08:00",
                "RegionId": 37,
                "Region": "ap-shenzhen",
                "RegionShortName": "szx",
                "RegionState": 1,
                "RegionName": "深圳",
                "Area": "华南地区"
            }
        ],
        "RequestId": "xx"
    }
}
```

