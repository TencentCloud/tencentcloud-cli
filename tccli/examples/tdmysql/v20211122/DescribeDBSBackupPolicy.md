**Example 1: 查询实例备份策略信息**

查询实例备份策略信息

Input: 

```
tccli tdmysql DescribeDBSBackupPolicy --cli-unfold-argument  \
    --InstanceId tdsql3-3f17e49d
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "BackupEndTime": "04:00",
                "BackupMethod": "physical",
                "BackupStartTime": "00:00",
                "DBType": "tdstore",
                "DBVersion": "21.6.1",
                "EnableFull": 1,
                "EnableLog": 1,
                "ExpectedNextBackupPeriod": "2026-03-27 00:00:00 ~ 2026-03-27 04:00:00",
                "FullRetentionPeriod": 7,
                "ID": 3260,
                "InstanceId": "tdsql3-3f17e49d",
                "LogRetentionPeriod": 7,
                "PeriodTime": "0,1,2,3,4,5,6",
                "PeriodType": 0,
                "Region": "ap-chengdu"
            }
        ],
        "TotalCount": 1,
        "RequestId": "ae01ddd4-36fd-44af-a71c-7f786f01e6c7"
    }
}
```

