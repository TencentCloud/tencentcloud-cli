**Example 1: 批量暂停任务**

任务运维-批量冻结任务

Input: 

```
tccli wedata FreezeOpsTasks --cli-unfold-argument  \
    --Tasks.0.TaskId 10001 \
    --Tasks.0.TaskName ew \
    --OperateIsInform True
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "09d8a38d-a051-42f6-8bba-239fa13d19c9"
    }
}
```

