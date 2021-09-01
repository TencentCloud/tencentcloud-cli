**Example 1: 删除全量备份导入任务**



Input: 

```
tccli sqlserver DeleteBackupMigration --cli-unfold-argument  \
    --InstanceId mssql-rdc0gajn \
    --BackupMigrationId mssql-backup-migration-cg0ffgqt
```

Output: 
```
{
    "Response": {
        "RequestId": "f0c186aa-b171-4a96-b176-b8e8ff23994d"
    }
}
```

