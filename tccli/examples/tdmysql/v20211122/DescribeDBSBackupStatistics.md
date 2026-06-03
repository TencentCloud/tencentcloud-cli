**Example 1: 备份概览统计**

备份概览统计

Input: 

```
tccli tdmysql DescribeDBSBackupStatistics --cli-unfold-argument  \
    --InstanceId tdsql3-3f17e49d \
    --EndTime 2026-03-26 20:10:00 \
    --StartTime 2026-03-20 10:10:00
```

Output: 
```
{
    "Response": {
        "BackupMethodStatistics": {
            "AutoBackupSize": 37748736,
            "AverageSizePerDay": 18874368,
            "ManualBackupSize": 0,
            "TotalSize": 37748736
        },
        "BackupStatistics": {
            "AverageSizePerDay": 50508288,
            "DataBackupSize": 37748736,
            "LogBackupSize": 63267840,
            "TotalCount": 8,
            "TotalSize": 101016576
        },
        "DataBackupStatistics": {
            "AutoBackupCount": 0,
            "AutoBackupSize": 0,
            "AverageSizePerBackup": 9437184,
            "AverageSizePerDay": 18874368,
            "ManualBackupCount": 0,
            "ManualBackupSize": 0,
            "TotalCount": 4,
            "TotalSize": 37748736
        },
        "LogBackupStatistics": {
            "AverageSizePerBackup": 15816960,
            "AverageSizePerDay": 31633920,
            "TotalCount": 4,
            "TotalSize": 63267840
        },
        "RequestId": "35fc7900-6809-4168-916e-e42be89c02cb"
    }
}
```

