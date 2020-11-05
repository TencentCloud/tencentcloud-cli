**Example 1: Querying the configuration information of TencentDB instance backup**



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
            "Friday": "10:00-14:00",
            "Monday": "10:00-14:00",
            "Saturday": "10:00-14:00",
            "Sunday": "10:00-14:00",
            "Thursday": "10:00-14:00",
            "Tuesday": "10:00-14:00",
            "Wednesday": "10:00-14:00"
        },
        "RequestId": "9d73ec37-89b8-4d36-9f40-123123123"
    }
}
```

