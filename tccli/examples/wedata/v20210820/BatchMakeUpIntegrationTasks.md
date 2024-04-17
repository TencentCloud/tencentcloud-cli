**Example 1: BatchMakeUpIntegrationTasks**



Input: 

```
tccli wedata BatchMakeUpIntegrationTasks --cli-unfold-argument  \
    --ProjectId 11022568003970304 \
    --TaskIds 20220506145218687 20230506145218687 \
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
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

