**Example 1: 创建备份文件导入任务**



Input: 

```
tccli sqlserver CreateBackupMigration --cli-unfold-argument  \
    --InstanceId mssql-rdc0gajn \
    --RecoveryType FULL \
    --UploadType COS_UPLOAD \
    --MigrationName 字符串 \
    --BackupFiles db1.bak
```

Output: 
```
{
    "Response": {
        "BackupMigrationId": "mssql-backup-migration-cg0ffgqt",
        "RequestId": "4e2f2093-9cde-44ec-b64b-edfcc2f911d4"
    }
}
```

