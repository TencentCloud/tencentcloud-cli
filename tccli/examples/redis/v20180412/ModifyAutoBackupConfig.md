**Example 1: 请求示例**

自动备份配置

Input: 

```
tccli redis ModifyAutoBackupConfig --cli-unfold-argument  \
    --InstanceId crs-5a4py64p \
    --AutoBackupType 1 \
    --TimePeriod 00%3A00-01%3A00 \
    --WeekDays Wednesday
```

Output: 
```
{
    "Response": {
        "BackupStorageDays": 7,
        "AutoBackupType": 1,
        "WeekDays": [
            "Wednesday"
        ],
        "RequestId": "65e950b9-78e8-49b1-9200-0e62a1925554",
        "TimePeriod": "00:00-01:00"
    }
}
```

