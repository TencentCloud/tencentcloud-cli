**Example 1: 抢占锁定集成任务**

抢占锁定集成任务

Input: 

```
tccli wedata RobAndLockIntegrationTask --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId abc \
    --TaskType 1
```

Output: 
```
{
    "Response": {
        "RobLockState": {
            "IsRob": true,
            "Locker": "abc"
        },
        "RequestId": "abc"
    }
}
```

