**Example 1: 示例**

获取超期备份策略

Input: 

```
tccli dcdb DescribeBackupConfigs --cli-unfold-argument  \
    --InstanceId tdsqlshard-6cmpk1rd
```

Output: 
```
{
    "Response": {
        "Days": 30,
        "StartBackupTime": "03:00",
        "EndBackupTime": "05:00",
        "WeekDays": [
            "Monday",
            "Sunday"
        ],
        "ArchiveDays": 91,
        "BackupConfigSet": [
            {
                "BackupCount": 1,
                "BeginDate": "2023-06-08",
                "EnableBackupPolicy": true,
                "Frequency": "monthly",
                "MaxRetentionDays": 365,
                "WeekDays": []
            }
        ],
        "InstanceId": "tdsqlshard-6cmpk1rd",
        "RequestId": "827d5b16-d464-4f43-af92-06c63d25375e"
    }
}
```

**Example 2: 示例1**

示例1

Input: 

```
tccli dcdb DescribeBackupConfigs --cli-unfold-argument  \
    --InstanceId tdsqlshard-2500dqmh
```

Output: 
```
{
    "Response": {
        "Days": 30,
        "StartBackupTime": "03:00",
        "EndBackupTime": "05:00",
        "WeekDays": [
            "Monday",
            "Sunday"
        ],
        "ArchiveDays": 91,
        "BackupConfigSet": [
            {
                "BackupCount": 0,
                "BeginDate": "2023-07-20",
                "EnableBackupPolicy": true,
                "Frequency": "weekly",
                "MaxRetentionDays": 100,
                "WeekDays": [
                    "Monday",
                    "Tuesday"
                ]
            }
        ],
        "InstanceId": "tdsqlshard-2500dqmh",
        "RequestId": "c4712e5d-78f3-4899-b8f4-0b6af5a17b77"
    }
}
```

