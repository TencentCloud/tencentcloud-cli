**Example 1: demo**



Input: 

```
tccli es DescribeAutoBackUpStrategy --cli-unfold-argument  \
    --InstanceId es-m6d4maox
```

Output: 
```
{
    "Response": {
        "CosBackupList": [
            {
                "AutoBackupInterval": 12,
                "BackupTime": "01:00",
                "CosRetention": 0,
                "CreateTime": "2025-11-12 18:02:39",
                "EsRepositoryType": 0,
                "Indices": "",
                "IsAutoBackup": true,
                "PaasEsRepository": "ES_AUTO_BACKUP_ap-beijing",
                "RemoteCos": 1,
                "RemoteCosRegion": "ap-beijing",
                "RetainUntilDate": "",
                "RetentionGraceTime": 0,
                "SnapshotName": "zzxtest",
                "StorageDuration": 3,
                "StrategyName": "mypolicy",
                "UserEsRepository": ""
            }
        ],
        "RequestId": "2206ef18-73f2-4e8f-a237-621664885fcc"
    }
}
```

