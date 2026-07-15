**Example 1: demo**



Input: 

```
tccli es DescribeCosBackupStrategyViews --cli-unfold-argument  \
    --InstanceId es-ldmd4rpp
```

Output: 
```
{
    "Response": {
        "CosBackupList": [
            {
                "AutoBackupInterval": 48,
                "BackupTime": "00:00",
                "CosBasePath": "/es_backup/es-ldmd4rpp/cosbackup4294967515",
                "CosRetention": 0,
                "CreateTime": "2026-04-20 09:39:43",
                "EsRepositoryType": 0,
                "Indices": "",
                "InstanceId": "es-ldmd4rpp",
                "IsAutoBackup": true,
                "MaxRestorePerSec": "",
                "MaxSnapshotPerSec": "",
                "MultiAz": 0,
                "PaasEsRepository": "ES_AUTO_BACKUP_cosbackup4294967515",
                "RemoteCos": 0,
                "RemoteCosRegion": "ap-guangzhou",
                "RetainUntilDate": "",
                "RetentionGraceTime": 0,
                "SnapshotName": "test2-snapshot",
                "StorageDuration": 7,
                "StrategyName": "test2",
                "UserEsRepository": ""
            }
        ],
        "RequestId": "42d79686-f550-4789-8455-bfd3544712ec"
    }
}
```

