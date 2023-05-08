**Example 1: 批量停止任务**



Input: 

```
tccli wedata BatchStopTasksNew --cli-unfold-argument  \
    --TaskIdList 1111 22222 \
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

