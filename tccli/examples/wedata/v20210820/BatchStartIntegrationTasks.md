**Example 1: BatchStartIntegrationTasks**

批量运行任务

Input: 

```
tccli wedata BatchStartIntegrationTasks --cli-unfold-argument  \
    --ProjectId xx \
    --TaskIds 123 124 \
    --TaskType 201
```

Output: 
```
{
    "Response": {
        "SuccessCount": 1,
        "FailedCount": 1,
        "TotalCount": 2,
        "RequestId": "xx"
    }
}
```

