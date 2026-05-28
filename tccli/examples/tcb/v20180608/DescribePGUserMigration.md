**Example 1: DescribePGUserMigration**

查询指定migration详情

Input: 

```
tccli tcb DescribePGUserMigration --cli-unfold-argument  \
    --EnvId pg-ethan06-d9gzgavrt1f14772b \
    --MigrationVersion 20260526000000
```

Output: 
```
{
    "Response": {
        "AppliedAt": "2026-05-26T11:34:19+08:00",
        "Checksum": "eeaf0dd9391ba7829bd12b47482fab4a0e031a040f00cfb6eafc5c23b9fcf791",
        "CreatedAt": "2026-05-26T11:34:19+08:00",
        "CreatedBy": "100019231666",
        "DurationMs": 0,
        "Name": "test_init",
        "Query": "CREATE TABLE IF NOT EXISTS public.test ( version BIGINT PRIMARY KEY, name TEXT NOT NULL);",
        "Rollback": "",
        "Source": "repair",
        "Version": "20260526000000",
        "RequestId": "f68be1af-9118-45de-a062-88c6bbc671e3"
    }
}
```

