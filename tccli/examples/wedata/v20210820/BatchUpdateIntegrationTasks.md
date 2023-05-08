**Example 1: BatchUpdateIntegrationTasks**



Input: 

```
tccli wedata BatchUpdateIntegrationTasks --cli-unfold-argument  \
    --ProjectId xx \
    --TaskIds 123 1234 \
    --Incharge 352;345 \
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

