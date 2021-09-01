**Example 1: 修改全量备份导入任务**



Input: 

```
tccli sqlserver ModifyBackupMigration --cli-unfold-argument  \
    --InstanceId mssql-rdc0gajn \
    --BackupMigrationId mssql-backup-migration-kpl74n9l \
    --MigrationName 字符串 \
    --RecoveryType FULL \
    --UploadType COS_UPLOAD \
    --BackupFiles db1.bak
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

