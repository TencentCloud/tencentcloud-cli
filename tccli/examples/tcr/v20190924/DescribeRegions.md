**Example 1: 列出TCR可用区域**



Input: 

```
tccli tcr DescribeRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Regions": [
            {
                "RegionId": "1",
                "RegionName": "ap-guangzhou",
                "Status": "alluser",
                "Remark": "aaa",
                "Alias": "gz",
                "CreatedAt": "2019-08-09",
                "UpdatedAt": "2019-08-09"
            }
        ],
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

