**Example 1: 查询地域列表**

查询地域列表

Input: 

```
tccli hai DescribeRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionSet": [
            {
                "Region": "ap-guangzhou",
                "RegionName": "广州",
                "RegionState": "AVAILABLE",
                "ScholarRocketSupportState": "ALREADY_SUPPORT"
            },
            {
                "Region": "ap-chongqing",
                "RegionName": "重庆",
                "RegionState": "UNAVAILABLE",
                "ScholarRocketSupportState": "NOT_SUPPORT_YET"
            }
        ],
        "RequestId": "e34431dd-763e-4523-92da-ec68016a3d6a"
    }
}
```

