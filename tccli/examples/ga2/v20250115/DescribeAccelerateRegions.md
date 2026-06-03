**Example 1: 查看可加速地域**



Input: 

```
tccli ga2 DescribeAccelerateRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AcceleratorRegionSet": [
            {
                "IsAvailable": 1,
                "Name": "北京",
                "Region": "ap-beijing",
                "IsChinaMainland": 1,
                "AreaName": "中国大陆",
                "SupportIspType": [
                    "CMCC"
                ]
            }
        ],
        "RequestId": "616ddd83-2e8f-4419-938d-c08250e5c319"
    }
}
```

