**Example 1: 示例1**

示例1

Input: 

```
tccli mariadb DescribeBackupConfigs --cli-unfold-argument  \
    --InstanceId tdsql-5a6zl9ez
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
                "BackupCount": 2,
                "BeginDate": "2023-07-01",
                "EnableBackupPolicy": true,
                "Frequency": "annually",
                "MaxRetentionDays": 101,
                "WeekDays": [
                    "Monday"
                ]
            }
        ],
        "InstanceId": "tdsql-5a6zl9ez",
        "RequestId": "3a2996d9-e46b-4b2c-98d2-d654f3f7db3e"
    }
}
```

