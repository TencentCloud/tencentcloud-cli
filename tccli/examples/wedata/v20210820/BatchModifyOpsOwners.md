**Example 1: 批量修改任务责任人**

任务运维-批量修改任务责任人

Input: 

```
tccli wedata BatchModifyOpsOwners --cli-unfold-argument  \
    --TaskIdList abc \
    --Owners abc \
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

