**Example 1: BatchDeleteIntegrationTasks**



Input: 

```
tccli wedata BatchDeleteIntegrationTasks --cli-unfold-argument  \
    --ProjectId 11022568003970304 \
    --TaskIds 20220506145218687 20230506145218687 \
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

