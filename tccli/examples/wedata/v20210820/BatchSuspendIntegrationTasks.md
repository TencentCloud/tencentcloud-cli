**Example 1: BatchSuspendIntegrationTasks**



Input: 

```
tccli wedata BatchSuspendIntegrationTasks --cli-unfold-argument  \
    --ProjectId 123 \
    --TaskIds 123 124 \
    --TaskType 201 \
    --Event SUSPEND_WITHOUT_SP
```

Output: 
```
{
    "Response": {
        "SuccessCount": 1,
        "FailedCount": 1,
        "TotalCount": 2,
        "RequestId": "123"
    }
}
```

