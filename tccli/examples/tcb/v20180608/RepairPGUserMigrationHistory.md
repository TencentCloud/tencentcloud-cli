**Example 1: RepairPGUserMigrationHistory**

修复migration历史

Input: 

```
tccli tcb RepairPGUserMigrationHistory --cli-unfold-argument  \
    --EnvId pg-ethan06-d9gzgavrt1f14772b \
    --MigrationVersion 20260526000000 \
    --Name test_init \
    --Status applied \
    --Reason 手动执行 \
    --Query CREATE TABLE IF NOT EXISTS public.test ( version BIGINT PRIMARY KEY, name TEXT NOT NULL);
```

Output: 
```
{
    "Response": {
        "RequestId": "4730dcbe-09ce-40cc-9cd5-b0757449430b"
    }
}
```

