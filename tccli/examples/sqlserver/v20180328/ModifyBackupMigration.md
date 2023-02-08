**Example 1: 修改全量备份导入任务**



Input: 

```
tccli sqlserver ModifyBackupMigration --cli-unfold-argument  \
    --BackupMigrationId mssql-backup-migration-kpl74n9l \
    --InstanceId mssql-rdc0gajn \
    --UploadType COS_UPLOAD \
    --BackupFiles db1.bak \
    --MigrationName 字符串 \
    --RecoveryType FULL
```

Output: 
```
{
    "Response": {
        "BackupMigrationId": "mssql-backup-migration-kpl74n9l",
        "RequestId": "836a10d3-cd1f-4ac1-96a9-f2e642333f0b"
    }
}
```

