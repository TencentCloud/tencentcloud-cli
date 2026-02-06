**Example 1: 删除备份记录**

删除备份记录

Input: 

```
tccli tcaplusdb DeleteBackupRecords --cli-unfold-argument  \
    --ClusterId 12345 \
    --BackupRecords.0.BackupBatchTime 1731661134 \
    --BackupRecords.0.AppId 1 \
    --BackupRecords.0.TableName test \
    --BackupRecords.0.ZoneId 1 \
    --BackupRecords.0.BackupType 1 \
    --BackupRecords.0.FileTag 1 \
    --BackupRecords.0.ShardCount 1 \
    --BackupRecords.0.BackupExpireTime 1731661134 \
    --BackupRecords.0.BackupSuccRate 1 \
    --BackupRecords.0.BackupFileSize 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1232222",
        "TaskId": "12321"
    }
}
```

