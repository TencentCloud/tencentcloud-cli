**Example 1: 备份用量总览**

Describe Backup Overview

Input: 

```
tccli cynosdb DescribeBackupOverview --cli-unfold-argument  \
    --ClusterId cynosdbmysql-gfo7ejhl
```

Output: 
```
{
    "Response": {
        "BackupLogicVolume": 0.009,
        "BackupSnapshotVolume": 0.212,
        "BackupTotalVolume": 0.222,
        "BackupVolumeInfos": [
            {
                "BackupMethod": "auto",
                "BackupType": "snapshot",
                "BackupVolume": 0.002
            },
            {
                "BackupMethod": "manual",
                "BackupType": "snapshot",
                "BackupVolume": 0.21
            },
            {
                "BackupMethod": "auto",
                "BackupType": "logic",
                "BackupVolume": 0
            },
            {
                "BackupMethod": "manual",
                "BackupType": "logic",
                "BackupVolume": 0.009
            }
        ],
        "CrossRegionBackupVolume": 0,
        "CrossRegionBackupVolumeInfos": [
            {
                "BackupMethod": "auto",
                "BackupType": "snapshot",
                "BackupVolume": 0
            },
            {
                "BackupMethod": "manual",
                "BackupType": "snapshot",
                "BackupVolume": 0
            },
            {
                "BackupMethod": "auto",
                "BackupType": "logic",
                "BackupVolume": 0
            },
            {
                "BackupMethod": "manual",
                "BackupType": "logic",
                "BackupVolume": 0
            }
        ],
        "CrossRegionLogVolume": 0,
        "CrossRegions": [],
        "CrossTotalVolume": 0,
        "LogBinlogVolume": 5.834,
        "LogRedoLogVolume": 7.466,
        "LogTotalVolume": 13.3,
        "RequestId": "ccb664a6-5093-40fb-938d-b2d7318c078d"
    }
}
```

