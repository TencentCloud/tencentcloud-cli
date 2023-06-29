**Example 1: 示例1**



Input: 

```
tccli keewidb ModifyAutoBackupConfig --cli-unfold-argument  \
    --InstanceId kee-9vrt**** \
    --TimePeriod 13:00-14:00 \
    --WeekDays Monday Tuesday Wednesday
```

Output: 
```
{
    "Response": {
        "BackupStorageDays": 7,
        "BinlogStorageDays": 3,
        "RequestId": "f0ad3a24-4a40-44a4-a4a5-f7a6239095ec",
        "TimePeriod": "13:00-14:00",
        "WeekDays": [
            "Monday",
            "Tuesday",
            "Wednesday"
        ]
    }
}
```

