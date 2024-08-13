**Example 1: 查询异步任务的状态**

查询异步任务的状态

Input: 

```
tccli organization GetTaskStatus --cli-unfold-argument  \
    --ZoneId z-dsiwnw*** \
    --TaskId t-duxj***
```

Output: 
```
{
    "Response": {
        "TaskStatus": {
            "Status": "Success",
            "TaskId": "z-dksodm***",
            "TaskType": "ProvisionRoleConfiguration",
            "FailureReason": "fielded"
        },
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

