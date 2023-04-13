**Example 1: 删除备份记录**

删除备份记录

Input: 

```
tccli tcaplusdb DeleteBackupRecords --cli-unfold-argument  \
    --ClusterId xx \
    --BackupRecords.0.BackupBatchTime xx \
    --BackupRecords.0.AppId 1 \
    --BackupRecords.0.TableName xx \
    --BackupRecords.0.ZoneId 1 \
    --BackupRecords.0.BackupType xx \
    --BackupRecords.0.FileTag xx \
    --BackupRecords.0.ShardCount 1 \
    --BackupRecords.0.BackupExpireTime xx \
    --BackupRecords.0.BackupSuccRate xx \
    --BackupRecords.0.BackupFileSize 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TaskId": "xx"
    }
}
```

