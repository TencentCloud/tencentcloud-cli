**Example 1: BatchKillIntegrationTaskInstances**



Input: 

```
tccli wedata BatchKillIntegrationTaskInstances --cli-unfold-argument  \
    --ProjectId xx \
    --Instances.0.TaskId 123 \
    --Instances.0.CurRunDate 2022-04-12 17:00:15 \
    --Instances.1.TaskId 1234 \
    --Instances.1.CurRunDate 2022-04-12 18:00:15
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

