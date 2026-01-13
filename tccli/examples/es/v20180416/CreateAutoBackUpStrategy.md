**Example 1: demo**



Input: 

```
tccli es CreateAutoBackUpStrategy --cli-unfold-argument  \
    --InstanceId es-m6d4maox \
    --CosBackup.IsAutoBackup True \
    --CosBackup.BackupTime 01:00 \
    --CosBackup.SnapshotName test2 \
    --CosBackup.EsRepositoryType 0 \
    --CosBackup.StorageDuration 3 \
    --CosBackup.AutoBackupInterval 1 \
    --CosBackup.CosRetention 0 \
    --CosBackup.RemoteCos 0 \
    --CosBackup.StrategyName mypolicy2
```

Output: 
```
{
    "Response": {
        "Status": true,
        "RequestId": "99593835-47fd-401d-b59f-9f84e641737c"
    }
}
```

