**Example 1: 范例**



Input: 

```
tccli wedata FreezeTasks --cli-unfold-argument  \
    --Tasks.0.TaskName 1234ff \
    --Tasks.0.TaskId 20220711143109589 \
    --OperateIsInform false
```

Output: 
```
{
    "Response": {
        "RequestId": "f1ead836-05aa-4a25-98da-7fb77c0a84ea",
        "Data": {
            "Result": false,
            "ErrorId": "null(20220711143109589)",
            "ErrorDesc": "任务1234ff(20220711143109589)冻结失败, 只有已发布运行的任务能够冻结"
        }
    }
}
```

