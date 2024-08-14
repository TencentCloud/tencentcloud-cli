**Example 1: 查询用户同步异步任务的状态**

查询用户同步异步任务的状态

Input: 

```
tccli organization GetProvisioningTaskStatus --cli-unfold-argument  \
    --ZoneId z-djw98wnd*** \
    --TaskId t-d8wjd8j3****
```

Output: 
```
{
    "Response": {
        "TaskStatus": {
            "Status": "Success",
            "TaskId": "z-dnsudniw****",
            "TaskType": "StartProvisioning",
            "FailureReason": ""
        },
        "RequestId": "e297543a-80de-4039-83c8-9d35d4545"
    }
}
```

