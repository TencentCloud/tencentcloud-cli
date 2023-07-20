**Example 1: 批量停止任务**

任务运维-批量停止任务

Input: 

```
tccli wedata BatchStopOpsTasks --cli-unfold-argument  \
    --TaskIdList abc \
    --ProjectId abc
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
        "RequestId": "abc"
    }
}
```

