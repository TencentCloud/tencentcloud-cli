**Example 1: BatchStartIntegrationTasks**

批量运行任务

Input: 

```
tccli wedata BatchStartIntegrationTasks --cli-unfold-argument  \
    --TaskIds abc \
    --TaskType 0 \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "SuccessCount": 0,
        "FailedCount": 0,
        "TotalCount": 0,
        "TaskNames": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

