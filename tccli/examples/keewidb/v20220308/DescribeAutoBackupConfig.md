**Example 1: 示例1**



Input: 

```
tccli keewidb DescribeAutoBackupConfig --cli-unfold-argument  \
    --InstanceId kee-9vrt****
```

Output: 
```
{
    "Response": {
        "BackupStorageDays": 7,
        "BinlogStorageDays": 3,
        "RequestId": "5d5449dc-e36f-47d8-ae50-5988f69991ad",
        "TimePeriod": "03:00-04:00",
        "WeekDays": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    }
}
```

