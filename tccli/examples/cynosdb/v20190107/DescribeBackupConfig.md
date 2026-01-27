**Example 1: 查看备份配置**

Describe Backup Config

Input: 

```
tccli cynosdb DescribeBackupConfig --cli-unfold-argument  \
    --ClusterId cynosdbmysql-aws1kpv6
```

Output: 
```
{
    "Response": {
        "BackupFreq": [
            "full",
            "full",
            "full",
            "full",
            "full",
            "full",
            "full"
        ],
        "BackupTimeBeg": 7200,
        "BackupTimeEnd": 21600,
        "BackupType": "snapshot",
        "LogicBackupConfig": {
            "LogicBackupEnable": "OFF",
            "LogicBackupTimeBeg": 0,
            "LogicBackupTimeEnd": 0,
            "LogicCrossRegions": null,
            "LogicCrossRegionsEnable": "",
            "LogicReserveDuration": 0
        },
        "LogicCrossRegionsConfigUpdateTime": "",
        "RequestId": "e0127059-bb40-4308-a67d-c3bcddba372e",
        "ReserveDuration": 604800,
        "SnapshotSecondaryBackupConfig": {
            "BackupCustomAutoTime": false,
            "BackupIntervalTime": 0,
            "BackupTimeBeg": 0,
            "BackupTimeEnd": 0,
            "BackupTriggerStrategy": "",
            "BackupWeekDays": null,
            "CrossRegions": null,
            "CrossRegionsEnable": "",
            "ReserveDuration": 0
        }
    }
}
```

