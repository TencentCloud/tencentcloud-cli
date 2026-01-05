**Example 1: 删除工作流调度任务**

删除工作流调度任务

Input: 

```
tccli wedata DeleteTriggerTask --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20251121160447036 \
    --OperateInform True \
    --DeleteMode False
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "f900a031-5ff0-4f33-97e9-aadb7f534542"
    }
}
```

