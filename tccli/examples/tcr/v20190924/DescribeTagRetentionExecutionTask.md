**Example 1: 查询版本保留执行任务**



Input: 

```
tccli tcr DescribeTagRetentionExecutionTask --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --RetentionId 1 \
    --ExecutionId 1 \
    --Limit 20 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RetentionTaskList": [
            {
                "Status": "success",
                "Total": 0,
                "Retained": 0,
                "TaskId": 0,
                "Repository": "repo",
                "ExecutionId": 0,
                "StartTime": "2024-06-01",
                "EndTime": "2024-06-01"
            }
        ],
        "RequestId": "1234-666"
    }
}
```

