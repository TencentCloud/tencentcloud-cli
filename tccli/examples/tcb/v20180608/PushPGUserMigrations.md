**Example 1: PushPGUserMigrations**

应用migration

Input: 

```
tccli tcb PushPGUserMigrations --cli-unfold-argument  \
    --EnvId pg-ethan06-d9gzgavrt1f14772b \
    --Migrations.0.Version 20260526000000 \
    --Migrations.0.Name test_init \
    --Migrations.0.Query CREATE TABLE IF NOT EXISTS public.test ( version BIGINT PRIMARY KEY, name TEXT NOT NULL); \
    --Migrations.0.Rollback DROP TABLE IF EXISTS public.test; \
    --LockTimeoutMs 5000 \
    --StatementTimeoutMs 300000 \
    --Source cloudapi
```

Output: 
```
{
    "Response": {
        "TaskId": "task-1ef06db7",
        "RequestId": "9e40cb4d-ce83-442d-97f2-abdf65c0c58f"
    }
}
```

