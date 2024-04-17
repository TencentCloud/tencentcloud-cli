**Example 1: 查看任务锁状态信息**

查看任务锁状态信息

Input: 

```
tccli wedata DescribeTaskLockStatus --cli-unfold-argument  \
    --TaskId 20220506145218687 \
    --ProjectId 20220506145218687 \
    --TaskType 201
```

Output: 
```
{
    "Response": {
        "TaskLockStatus": {
            "TaskId": "20220506145218687",
            "Locker": "Locker",
            "IsLocker": 0,
            "IsRob": 0
        },
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

