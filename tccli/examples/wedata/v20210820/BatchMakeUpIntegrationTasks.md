**Example 1: BatchMakeUpIntegrationTasks**



Input: 

```
tccli wedata BatchMakeUpIntegrationTasks --cli-unfold-argument  \
    --ProjectId xx \
    --TaskIds 123 1234 \
    --StartTime 2022-04-18 12:00:00 \
    --EndTime 2022-04-18 13:00:00 \
    --TaskType 202
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

