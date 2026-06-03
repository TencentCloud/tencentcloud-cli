**Example 1: 查询备份集列表**

查询备份集列表

Input: 

```
tccli tdmysql DescribeDBSBackupSets --cli-unfold-argument  \
    --InstanceId tdsql3-3f17e49d \
    --EndTime 2026-03-27 10:00:00 \
    --FilterBy.BackupMethod physical,snapshot \
    --FilterBy.BackupStatus running,success \
    --FilterBy.BackupType full \
    --FilterBy.ManualBackup 0,1 \
    --Limit 1 \
    --Offset 0 \
    --OrderType DESC \
    --StartTime 2026-03-23 10:00:00
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "BackupDuration": 75,
                "BackupMethod": "physical",
                "BackupName": "tdsql3-3f17e49d_20260327000013",
                "BackupProgress": 100,
                "BackupSetId": 73180813688075,
                "BackupStatus": "success",
                "BackupType": "full",
                "DBVersion": "21.6.1",
                "EndTime": "2026-03-27 00:01:28",
                "EndTrxTime": "2026-03-27 00:00:49",
                "ErrorMessage": "",
                "ExpiredTime": "2026-04-03 00:01:28",
                "FileName": "tdstore-data",
                "FileSize": 9437184,
                "InstanceId": "tdsql3-3f17e49d",
                "ManualBackup": 0,
                "StartTime": "2026-03-27 00:00:13"
            }
        ],
        "TotalCount": 5,
        "RequestId": "66a71db2-18c5-445e-a28b-39ab02c1774e"
    }
}
```

