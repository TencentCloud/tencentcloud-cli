**Example 1: 查询容器实例支持的地域**



Input: 

```
tccli tke DescribeEKSContainerInstanceRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "10d9ea5a-6e9e-4384-88da-84229e133555",
        "Regions": [
            {
                "Alias": "cq",
                "RegionName": "ap-chongqing",
                "RegionId": 19
            },
            {
                "Alias": "gz",
                "RegionName": "ap-guangzhou",
                "RegionId": 1
            }
        ],
        "TotalCount": 2
    }
}
```

