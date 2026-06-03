**Example 1: PreviewPGUserMigrations**

预览 migration执行计划

Input: 

```
tccli tcb PreviewPGUserMigrations --cli-unfold-argument  \
    --EnvId pg-ethan06-d9gzgavrt1f14772b \
    --Migrations.0.Version 20260526000000 \
    --Migrations.0.Name test_init \
    --Migrations.0.Query CREATE TABLE IF NOT EXISTS public.test ( version BIGINT PRIMARY KEY, name TEXT NOT NULL); \
    --Migrations.0.Rollback DROP TABLE IF EXISTS public.test; \
    --Source cli
```

Output: 
```
{
    "Response": {
        "Applied": [
            {
                "Checksum": "eeaf0dd9391ba7829bd12b47482fab4a0e031a040f00cfb6eafc5c23b9fcf791",
                "Name": "test_init",
                "Reason": "checksum_matched",
                "Source": "cli",
                "Status": "applied",
                "Version": "20260526000000"
            }
        ],
        "Conflicts": null,
        "Executable": true,
        "Pending": null,
        "RequestId": "b2792e8a-da94-422e-9ef5-b4e60a46ec0f"
    }
}
```

