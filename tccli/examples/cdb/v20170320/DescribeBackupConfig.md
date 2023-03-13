**Example 1: 查询云数据库备份配置信息**

查询云数据库备份配置信息

Input: 

```
tccli cdb DescribeBackupConfig --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv
```

Output: 
```
{
    "Response": {
        "BackupMethod": "physical",
        "BinlogExpireDays": 7,
        "BackupExpireDays": 7,
        "StartTimeMin": 10,
        "StartTimeMax": 14,
        "BackupTimeWindow": {
            "BackupPeriodStrategy": "weekly",
            "BackupPeriodTime": "00:00-12:00",
            "Days": [],
            "Friday": "10:00-14:00",
            "Monday": "10:00-14:00",
            "Saturday": "10:00-14:00",
            "Sunday": "10:00-14:00",
            "Thursday": "10:00-14:00",
            "Tuesday": "10:00-14:00",
            "Wednesday": "10:00-14:00"
        },
        "EnableBackupPeriodSave": "off",
        "BackupPeriodSaveDays": 1080,
        "BackupPeriodSaveInterval": "monthly",
        "BackupPeriodSaveCount": 1,
        "StartBackupPeriodSaveDate": "2021-12-12 00:00:00",
        "EnableBackupArchive": "on",
        "BackupArchiveDays": 180,
        "EnableBinlogArchive": "on",
        "BinlogArchiveDays": 180,
        "EnableBackupStandby": "on",
        "BackupStandbyDays": 30,
        "EnableBinlogStandby": "on",
        "BinlogStandbyDays": 30,
        "RequestId": "9d73ec37-89b8-4d36-9f40-123123123"
    }
}
```

