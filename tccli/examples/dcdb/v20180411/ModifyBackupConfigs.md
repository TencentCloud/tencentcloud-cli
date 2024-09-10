**Example 1: 示例**

近一年每个月保留一个备份

Input: 

```
tccli dcdb ModifyBackupConfigs --cli-unfold-argument  \
    --InstanceId tdsqlshard-6cmpk1rd \
    --BackupConfigSet.0.EnableBackupPolicy True \
    --BackupConfigSet.0.BeginDate 2023-06-08 \
    --BackupConfigSet.0.MaxRetentionDays 365 \
    --BackupConfigSet.0.Frequency monthly \
    --BackupConfigSet.0.BackupCount 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a0495e38-cd59-420c-8f09-893207d28955"
    }
}
```

**Example 2: 示例1**

按周保留备份

Input: 

```
tccli dcdb ModifyBackupConfigs --cli-unfold-argument  \
    --InstanceId tdsqlshard-2500dqmh \
    --BackupConfigSet.0.EnableBackupPolicy True \
    --BackupConfigSet.0.BeginDate 2023-07-20 \
    --BackupConfigSet.0.MaxRetentionDays 100 \
    --BackupConfigSet.0.Frequency weekly \
    --BackupConfigSet.0.WeekDays Monday Tuesday
```

Output: 
```
{
    "Response": {
        "RequestId": "45b034f3-1ace-45c7-b49e-1fca45f89d9e"
    }
}
```

