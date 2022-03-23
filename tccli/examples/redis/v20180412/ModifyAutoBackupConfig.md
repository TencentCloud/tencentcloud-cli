**Example 1: 请求示例**



Input: 

```
tccli redis ModifyAutoBackupConfig --cli-unfold-argument  \
    --InstanceId crs-5a4py64p \
    --TimePeriod 00%3A00-01%3A00 \
    --AutoBackupType 1 \
    --WeekDays Wednesday
```

Output: 
```
{
    "Response": {
        "BackupStorageDays": 0,
        "AutoBackupType": 1,
        "WeekDays": [
            "Wednesday"
        ],
        "RequestId": "xx",
        "TimePeriod": "xx"
    }
}
```

