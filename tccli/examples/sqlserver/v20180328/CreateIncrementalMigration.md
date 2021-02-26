**Example 1: 创建增量迁移任务**



Input: 

```
tccli sqlserver CreateIncrementalMigration --cli-unfold-argument  \
    --InstanceId mssql-rdc0gajn \
    --BackupMigrationId mssql-backup-migration-cg0ffgqt \
    --IsRecovery NO \
    --BackupFiles db_cvm_1_20200927204209_2log2_2noreconvery2.bak
```

Output: 
```
{
    "Response": {
        "IncrementalMigrationId": "mssql-incremental-migration-kp7bgv8p",
        "RequestId": "1e3d890b-1ff7-44ba-808d-633f11c873d8"
    }
}
```

