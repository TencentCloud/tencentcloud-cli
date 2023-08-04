**Example 1: BatchDeleteIntegrationTasks**



Input: 

```
tccli wedata BatchDeleteIntegrationTasks --cli-unfold-argument  \
    --ProjectId 2385923 \
    --TaskIds 123 124 \
    --TaskType 201 \
    --DeleteKFFlag 1
```

Output: 
```
{
    "Response": {
        "SuccessCount": 1,
        "FailedCount": 1,
        "TotalCount": 2,
        "RequestId": "feo-afe-x2o"
    }
}
```

