**Example 1: 获取地域列表**

获取地域列表

Input: 

```
tccli tke DescribeRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RegionInstanceSet": [
            {
                "RegionName": "ap-guangzhou",
                "RegionId": 1,
                "Status": "",
                "FeatureGates": "",
                "Alias": "gz",
                "Remark": ""
            }
        ],
        "RequestId": "d367ff5c-3871-4f1b-b8f1-4d51ea689e29"
    }
}
```

