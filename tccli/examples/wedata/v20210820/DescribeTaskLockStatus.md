**Example 1: 查看任务锁状态信息**

查看任务锁状态信息

Input: 

```
tccli wedata DescribeTaskLockStatus --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId abc \
    --TaskType 1
```

Output: 
```
{
    "Response": {
        "TaskLockStatus": {
            "TaskId": "abc",
            "Locker": "abc",
            "IsLocker": 0,
            "IsRob": 0
        },
        "RequestId": "abc"
    }
}
```

