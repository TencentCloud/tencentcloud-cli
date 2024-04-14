**Example 1: 抢占锁定集成任务**

抢占锁定集成任务

Input: 

```
tccli wedata RobAndLockIntegrationTask --cli-unfold-argument  \
    --TaskId a9471037vb432fa8f88io37a217 \
    --ProjectId 110225083773970304 \
    --TaskType 202
```

Output: 
```
{
    "Response": {
        "RobLockState": {
            "IsRob": true,
            "Locker": "username"
        },
        "RequestId": "m8d94710-374fe432f-a8f88ba4-d437a210"
    }
}
```

