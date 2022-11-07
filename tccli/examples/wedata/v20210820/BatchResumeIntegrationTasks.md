**Example 1: BatchResumeIntegrationTasks**



Input: 

```
tccli wedata BatchResumeIntegrationTasks --cli-unfold-argument  \
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

