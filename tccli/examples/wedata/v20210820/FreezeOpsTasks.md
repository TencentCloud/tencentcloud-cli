**Example 1: 批量冻结任务**

任务运维-批量冻结任务

Input: 

```
tccli wedata FreezeOpsTasks --cli-unfold-argument  \
    --Tasks.0.TaskId 123 \
    --Tasks.0.TaskName ew \
    --OperateIsInform True
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "12345"
    }
}
```

