**Example 1: 查询保险箱下数据备份列表**



Input: 

```
tccli cynosdb DescribeBackupListByVault --cli-unfold-argument  \
    --VaultId vault-a6ed23f2-f03e-4410-b946-624d1e7d9b5a
```

Output: 
```
{
    "Response": {
        "BackupList": [
            {
                "BackupFileInfo": {
                    "BackupId": 631,
                    "BackupMethod": "manual",
                    "BackupName": "",
                    "BackupStatus": "success",
                    "BackupType": "snapshot",
                    "CopyStatus": "done",
                    "FileName": "backupT_202602021412_20260202150536",
                    "FileSize": 4183356,
                    "FinishTime": "2026-02-02 15:05:41",
                    "SnapShotType": "full",
                    "SnapshotId": 631,
                    "SnapshotTime": "2026-02-02 14:47:38",
                    "StartTime": "2026-02-02 15:05:36"
                },
                "ClusterId": "cynosdbmysql-h30xf5d7",
                "ClusterName": "backupT_202602021412"
            }
        ],
        "TotalCount": 1,
        "RequestId": "805500d0-0399-4f8c-acaf-3d6de1d607d5"
    }
}
```

