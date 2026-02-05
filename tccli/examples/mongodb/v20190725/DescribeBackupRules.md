**Example 1: 获取实例备份规则**



Input: 

```
tccli mongodb DescribeBackupRules --cli-unfold-argument  \
    --InstanceId cmgo-xxxxx
```

Output: 
```
{
    "Response": {
        "ActiveWeekdays": "0,1,2,3,4,5,6",
        "AlertThreshold": 0,
        "BackupFrequency": 12,
        "BackupMethod": 0,
        "BackupSaveTime": 7,
        "BackupTime": 0,
        "BackupTotalSize": {
            "FreeQuota": 10737418240,
            "OplogSize": 602372,
            "SnapshotSize": 28916
        },
        "BackupVersion": 1,
        "LongTermActiveDays": "",
        "LongTermExpiredDays": 0,
        "LongTermInterval": "",
        "OplogExpiredDays": 0,
        "RequestId": "b544304c-e8eb-4819-8715-05a005c010ca"
    }
}
```

