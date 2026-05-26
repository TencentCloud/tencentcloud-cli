**Example 1: 查询备份集统计详情**

查询备份集统计详情

Input: 

```
tccli tdmysql DescribeDBSBackupStatisticsDetail --cli-unfold-argument  \
    --InstanceId tdsql3-3f17e49d \
    --EndTime 2026-03-23 22:00:00 \
    --StartTime 2026-03-23 00:00:00
```

Output: 
```
{
    "Response": {
        "BackupMethodStatistics": {
            "AutoBackupSize": [
                9437184
            ],
            "ManualBackupSize": [
                0
            ]
        },
        "BackupTime": [
            "2026-03-23"
        ],
        "BackupTypeStatistics": {
            "DataBackupSize": [
                9437184
            ],
            "LogBackupSize": [
                2332672
            ]
        },
        "RequestId": "712340ca-ab30-4acb-a784-38473a2c57f0"
    }
}
```

