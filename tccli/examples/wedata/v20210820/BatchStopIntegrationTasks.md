**Example 1: BatchStopIntegrationTasks**



Input: 

```
tccli wedata BatchStopIntegrationTasks --cli-unfold-argument  \
    --ProjectId xx \
    --TaskIds 123 1234 \
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

