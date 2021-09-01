**Example 1: 删除增量导入任务**



Input: 

```
tccli sqlserver DeleteIncrementalMigration --cli-unfold-argument  \
    --InstanceId mssql-rdc0gajn \
    --BackupMigrationId mssql-backup-migration-cg0ffgqt \
    --IncrementalMigrationId mssql-incremental-migration-67q4wy87
```

Output: 
```
{
    "Response": {
        "RequestId": "6ed62412-c476-4714-8042-241f50b2aedf"
    }
}
```

