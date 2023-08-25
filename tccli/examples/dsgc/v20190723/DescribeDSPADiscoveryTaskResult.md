**Example 1: 获取分类分级任务结果**



Input: 

```
tccli dsgc DescribeDSPADiscoveryTaskResult --cli-unfold-argument  \
    --DataSourceType cdb \
    --DspaId dspa-001 \
    --Limit 1 \
    --TaskId 1 \
    --Offset 0 \
    --TaskName test
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "TotalCount": 1,
        "Items": [
            {
                "DbResultId": 3,
                "TaskId": 28,
                "TaskName": "898111",
                "DbName": "testdb",
                "TotalTables": 2
            }
        ]
    }
}
```

