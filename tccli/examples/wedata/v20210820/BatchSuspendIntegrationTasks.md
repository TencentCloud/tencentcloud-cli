**Example 1: BatchSuspendIntegrationTasks**



Input: 

```
tccli wedata BatchSuspendIntegrationTasks --cli-unfold-argument  \
    --ProjectId 11022568003970304 \
    --TaskIds 20220506145218687 20230506145218687 \
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
        "RequestId": "9f2cdb12-cbc8-431a-94e8-c658ae3ca3ac"
    }
}
```

