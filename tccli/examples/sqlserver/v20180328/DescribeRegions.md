**Example 1: 查询所有地域**



Input: 

```
tccli sqlserver DescribeRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "9b0beca5-f3ea-44d3-97de-ec8f02effaea",
        "TotalCount": 9,
        "RegionSet": [
            {
                "Region": "ap-hongkong",
                "RegionName": "中国香港",
                "RegionId": 5,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shanghai-fsi",
                "RegionName": "上海金融",
                "RegionId": 7,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shantou",
                "RegionName": "汕头",
                "RegionId": 2,
                "RegionState": "UNAVAILABLE"
            },
            {
                "Region": "ap-tianjin",
                "RegionName": "天津",
                "RegionId": 3,
                "RegionState": "UNAVAILABLE"
            },
            {
                "Region": "na-toronto",
                "RegionName": "北美",
                "RegionId": 6,
                "RegionState": "UNAVAILABLE"
            },
            {
                "Region": "ap-beijing",
                "RegionName": "北京",
                "RegionId": 8,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shenzhen-fsi",
                "RegionName": "深圳金融",
                "RegionId": 11,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-guangzhou",
                "RegionName": "广州",
                "RegionId": 1,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shanghai",
                "RegionName": "上海",
                "RegionId": 4,
                "RegionState": "AVAILABLE"
            }
        ]
    }
}
```

