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
                "Status": "xx",
                "Total": 0,
                "Retained": 0,
                "TaskId": 0,
                "Repository": "xx",
                "ExecutionId": 0,
                "StartTime": "xx",
                "EndTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

