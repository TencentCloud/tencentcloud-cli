**Example 1: 批量补录任务**



Input: 

```
tccli wedata MakeUpTasksNew --cli-unfold-argument  \
    --TaskIdList 1111 22222 \
    --CheckParent True \
    --StartTime yyyy-MM-dd HH:mm:ss \
    --EndTime yyyy-MM-dd HH:mm:ss \
    --MakeUpType 1 \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "SuccessCount": 0,
            "FailedCount": 0,
            "TotalCount": 0
        },
        "RequestId": "xx"
    }
}
```

