**Example 1: 备份组回滚**



Input: 

```
tccli bdrc ApplyBackupGroup --cli-unfold-argument  \
    --BackupGroupId cbackup-n3thksnh \
    --ApplyDisks.0.BackupId backup-4odzwf0l \
    --ApplyDisks.0.DiskId disk-22u8462w \
    --AutoStopInstance True \
    --AutoStartInstance True
```

Output: 
```
{
    "Response": {
        "RequestId": "8b2d33b5-68a0-41f8-b9df-6f29912f5176"
    }
}
```

