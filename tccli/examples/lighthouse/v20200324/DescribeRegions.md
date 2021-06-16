**Example 1: 查询地域列表**



Input: 

```
tccli lighthouse DescribeRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "RegionSet": [
            {
                "Region": "ap-beijing",
                "RegionName": "北京",
                "RegionState": "AVAILABLE",
                "IsChinaMainland": true
            },
            {
                "Region": "ap-guangzhou",
                "RegionName": "广州",
                "RegionState": "AVAILABLE",
                "IsChinaMainland": true
            },
            {
                "Region": "ap-shanghai",
                "RegionName": "上海",
                "RegionState": "AVAILABLE",
                "IsChinaMainland": true
            },
            {
                "Region": "ap-hongkong",
                "RegionName": "中国香港",
                "RegionState": "AVAILABLE",
                "IsChinaMainland": false
            }
        ],
        "RequestId": "52c5ec46-30ca-47b9-8b72-f696c6cb65ea"
    }
}
```

