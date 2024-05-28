**Example 1: 批量停止任务**

任务运维-批量停止任务

Input: 

```
tccli wedata BatchStopOpsTasks --cli-unfold-argument  \
    --TaskIdList 111 \
    --ProjectId 1485413914375667
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
        "RequestId": "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    }
}
```

