**Example 1: 查看任务锁状态信息**

查看任务锁状态信息

Input: 

```
tccli wedata DescribeTaskLockStatus --cli-unfold-argument  \
    --ProjectId xx \
    --TaskId xx \
    --TaskType 1
```

Output: 
```
{
    "Response": {
        "TaskLockStatus": {
            "IsRob": 1,
            "Locker": "xx",
            "IsLocker": 1,
            "TaskId": "xx"
        },
        "RequestId": "xx"
    }
}
```

