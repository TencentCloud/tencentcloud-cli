**Example 1: 批量删除任务**

1

Input: 

```
tccli wedata BatchDeleteOpsTasks --cli-unfold-argument  \
    --TaskIdList 20210223145698 \
    --DeleteMode True \
    --EnableNotify True \
    --ProjectId 11127277799887
```

Output: 
```
{
    "Response": {
        "Data": {
            "SuccessCount": 1,
            "FailedCount": 0,
            "TotalCount": 0
        },
        "RequestId": "1d287884-1214-4b75-b4e8-383ee8e57918"
    }
}
```

