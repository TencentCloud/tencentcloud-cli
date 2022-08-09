**Example 1: 批量修改任务责任人**



Input: 

```
tccli wedata BatchModifyOwnersNew --cli-unfold-argument  \
    --TaskIdList 1111 22222 \
    --Owners wangling;xue; \
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

