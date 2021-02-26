**Example 1: 启动增量导入任务**



Input: 

```
tccli sqlserver StartIncrementalMigration --cli-unfold-argument  \
    --InstanceId mssql-rdc0gajn \
    --BackupMigrationId mssql-backup-migration-cg0ffgqt \
    --IncrementalMigrationId mssql-incremental-migration-kp7bgv8p
```

Output: 
```
{
    "Response": {
        "FlowId": 1001403,
        "RequestId": "6f2b5d2b-a3c1-426d-8e1c-325a69ccb694"
    }
}
```

