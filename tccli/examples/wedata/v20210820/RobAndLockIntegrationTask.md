**Example 1: 抢占锁定集成任务**

抢占锁定集成任务

Input: 

```
tccli wedata RobAndLockIntegrationTask --cli-unfold-argument  \
    --ProjectId xx \
    --TaskId xx \
    --TaskType 201
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "RobLockState": {
            "Locker": "xx",
            "IsRob": true
        }
    }
}
```

