**Example 1: 批量创建任务**

批量创建任务

Input: 

```
tccli dlc CreateTasks --cli-unfold-argument  \
    --Tasks.SQL xx \
    --Tasks.TaskType xx \
    --Tasks.Config.0.Value xx \
    --Tasks.Config.0.Key xx \
    --Tasks.FailureTolerance xx \
    --DatabaseName xx \
    --DatasourceConnectionName xx
```

Output: 
```
{
    "Response": {
        "BatchId": "xx",
        "TaskIdSet": [
            "xx"
        ],
        "RequestId": "xx"
    }
}
```

