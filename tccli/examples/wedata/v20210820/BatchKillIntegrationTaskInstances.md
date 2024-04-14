**Example 1: BatchKillIntegrationTaskInstances**



Input: 

```
tccli wedata BatchKillIntegrationTaskInstances --cli-unfold-argument  \
    --ProjectId 11022568003970304 \
    --Instances.0.TaskId 20220506145218687 \
    --Instances.0.CurRunDate 2022-04-12 17:00:15 \
    --Instances.1.TaskId 20220413104752613 \
    --Instances.1.CurRunDate 2022-04-12 18:00:15
```

Output: 
```
{
    "Response": {
        "SuccessCount": 1,
        "FailedCount": 1,
        "TotalCount": 2,
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

