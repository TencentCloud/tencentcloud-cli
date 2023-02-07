**Example 1: 获取spark应用列表**

本接口用于获取spark应用列表。

Input: 

```
tccli dlc DescribeSparkAppJobs --cli-unfold-argument  \
    --Sorting desc \
    --SortBy create-time \
    --StartTime 2022-01-01 00:00:00 \
    --EndTime 2022-01-01 00:00:00 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "2ae4707a-9f72-44aa-9fd4-65cb739d6301",
        "SparkAppJobs": [],
        "TotalCount": 0
    }
}
```

