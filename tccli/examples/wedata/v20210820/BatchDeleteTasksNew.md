**Example 1: 批量删除任务**



Input: 

```
tccli wedata BatchDeleteTasksNew --cli-unfold-argument  \
    --TaskIdList 1111 22222 \
    --EnableNotify True \
    --DeleteMode True \
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

