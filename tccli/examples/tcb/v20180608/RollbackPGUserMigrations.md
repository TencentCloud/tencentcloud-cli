**Example 1: RollbackPGUserMigrations**

回滚最近2条migration

Input: 

```
tccli tcb RollbackPGUserMigrations --cli-unfold-argument  \
    --EnvId pg-ethan06-d9gzgavrt1f14772b \
    --LastN 2 \
    --LockTimeoutMs 5000 \
    --StatementTimeoutMs 300000 \
    --Source cli
```

Output: 
```
{
    "Response": {
        "TaskId": "task-d9fd1d51",
        "RequestId": "ac6ed9c4-1560-4896-8706-52f715d73fed"
    }
}
```

