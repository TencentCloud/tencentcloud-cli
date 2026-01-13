**Example 1: demo**



Input: 

```
tccli es ModifyAutoBackUpStrategy --cli-unfold-argument  \
    --InstanceId es-m6d4maox \
    --StrategyName mypolicy2 \
    --CosBackup.IsAutoBackup True \
    --CosBackup.BackupTime 01:00 \
    --CosBackup.SnapshotName test2 \
    --CosBackup.EsRepositoryType 0 \
    --CosBackup.StorageDuration 4 \
    --CosBackup.AutoBackupInterval 12 \
    --CosBackup.CosRetention 0 \
    --CosBackup.RemoteCos 0 \
    --CosBackup.StrategyName mypolicy2
```

Output: 
```
{
    "Response": {
        "Status": true,
        "RequestId": "794affac-7f0b-4ff1-8737-8c5aff2401c1"
    }
}
```

