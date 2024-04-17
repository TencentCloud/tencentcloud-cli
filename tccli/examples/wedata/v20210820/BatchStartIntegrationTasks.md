**Example 1: BatchStartIntegrationTasks**

批量运行任务

Input: 

```
tccli wedata BatchStartIntegrationTasks --cli-unfold-argument  \
    --TaskIds 20220506145218687 \
    --TaskType 201 \
    --ProjectId 11022568003970304
```

Output: 
```
{
    "Response": {
        "SuccessCount": 0,
        "FailedCount": 0,
        "TotalCount": 0,
        "TaskNames": [
            "20220506145218687"
        ],
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

