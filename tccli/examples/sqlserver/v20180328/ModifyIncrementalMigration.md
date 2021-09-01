**Example 1: 修改增量迁移任务**



Input: 

```
tccli sqlserver ModifyIncrementalMigration --cli-unfold-argument  \
    --InstanceId mssql-rdc0gajn \
    --BackupMigrationId mssql-backup-migration-cg0ffgqt \
    --IncrementalMigrationId mssql-incremental-migration-kp7bgv8p \
    --IsRecovery YES \
    --BackupFiles db_cvm_1_20200927204209_2log2_2reconvery2.bak
```

Output: 
```
{
    "Response": {
        "IncrementalMigrationId": "mssql-incremental-migration-kp7bgv8p",
        "RequestId": "dab70669-594b-4610-981b-5bfeef7182bb"
    }
}
```

