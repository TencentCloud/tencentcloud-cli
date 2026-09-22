**Example 1: DescribeTaskResult**



Input: 

```
tccli tcb DescribeTaskResult --cli-unfold-argument  \
    --EnvId pg-***********zgavrt1f14772b \
    --TaskId task-e6ee5110
```

Output: 
```
{
    "Response": {
        "CreatedAt": "2026-05-26T11:26:13+08:00",
        "Phase": "RunMigrations",
        "Reason": "",
        "Status": "Succeed",
        "TaskId": "task-e6ee5110",
        "TaskType": "PGUserMigration",
        "UpdatedAt": "2026-05-26T11:26:14+08:00",
        "RequestId": "2763d06c-6ee4-4290-b261-479e3ffc670b"
    }
}
```

