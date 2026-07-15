**Example 1: 查询全部资源**



Input: 

```
tccli cvm DescribeInstanceStatistics --cli-unfold-argument  \
    --Filters.0.Name None \
    --Filters.0.Values None
```

Output: 
```
{
    "Response": {
        "InstanceStatisticsSet": [
            {
                "ExpiredInstanceCount": 0,
                "NewInstanceCount": 0,
                "Region": "ap-guangzhou",
                "TotalCount": 0
            }
        ],
        "RequestId": "d5356626-4fbf-4bc0-8e24-b804b8878134"
    }
}
```

