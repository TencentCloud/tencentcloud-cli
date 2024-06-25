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
                "Alias": "gz",
                "RegionId": 1,
                "RegionName": "ap-guangzhou",
                "Status": "alluser",
                "Remark": "alluser",
                "CreatedAt": "2020-09-22T00:00:00+00:00",
                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                "Id": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

