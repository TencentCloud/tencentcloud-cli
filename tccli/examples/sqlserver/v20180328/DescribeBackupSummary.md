**Example 1: 查询数据库备份概览信息**



Input: 

```
tccli sqlserver DescribeBackupSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ActualUsedSpace": 1193345364,
        "AutoBackupCount": 1615,
        "AutoBackupSpace": 953883130,
        "BackupFilesTotal": 16637,
        "BillingSpace": 605473752,
        "CrossAutoBackupCount": 288,
        "CrossAutoBackupSpace": 146231712,
        "CrossBackupFilesTotal": 3303,
        "CrossBillingSpace": 147469692,
        "CrossEstimatedAmount": 0.114,
        "CrossLogBackupCount": 3015,
        "CrossLogBackupSpace": 1237980,
        "DataBackupCount": 2046,
        "DataBackupSpace": 1183658714,
        "EstimatedAmount": 0.4616,
        "FreeSpace": 440401920,
        "LocalBackupFilesTotal": 13334,
        "LocalLogBackupCount": 11576,
        "LocalLogBackupSpace": 8448670,
        "LogBackupCount": 14591,
        "LogBackupSpace": 9686650,
        "ManualBackupCount": 143,
        "ManualBackupSpace": 83543872,
        "RequestId": "8b5d62cb-40f4-45ba-8a26-a2083d4f9eee"
    }
}
```

