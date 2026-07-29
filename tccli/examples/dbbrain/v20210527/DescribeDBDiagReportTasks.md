**Example 1: 查询健康报告任务列表**



Input: 

```
tccli dbbrain DescribeDBDiagReportTasks --cli-unfold-argument  \
    --Offset 0 \
    --Limit 50 \
    --Product mysql \
    --TagFilters.0.TagPairs.0.TagKey cdb_has_ro_01 \
    --TagFilters.0.TagPairs.0.TagValue 1
```

Output: 
```
{
    "Response": {
        "Tasks": [],
        "TotalCount": 0,
        "RequestId": "5945e2ce-05df-432e-9ef0-9213c3589088"
    }
}
```

