**Example 1: 查询地域列表**



Input: 

```
tccli tat DescribeRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "RegionSet": [
            {
                "Region": "ap-guangzhou",
                "RegionName": "广州",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shanghai",
                "RegionName": "上海",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-hongkong",
                "RegionName": "中国香港",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-beijing",
                "RegionName": "北京",
                "RegionState": "AVAILABLE"
            }
        ],
        "RequestId": "3863868a-ab4b-4185-9e48-e6f4ec11d296"
    }
}
```

