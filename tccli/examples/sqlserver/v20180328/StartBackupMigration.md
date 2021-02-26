**Example 1: 启动全量迁移任务**



Input: 

```
tccli sqlserver StartBackupMigration --cli-unfold-argument  \
    --InstanceId mssql-rdc0gajn \
    --BackupMigrationId mssql-backup-migration-kpl74n9l
```

Output: 
```
{
    "Response": {
        "FlowId": 1001399,
        "RequestId": "551b4694-5f0b-43e7-a62d-94afb2af4d3d"
    }
}
```

