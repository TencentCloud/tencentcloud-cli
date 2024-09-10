**Example 1: 示例1**

每年保留2个超期备份

Input: 

```
tccli mariadb ModifyBackupConfigs --cli-unfold-argument  \
    --InstanceId tdsql-5a6zl9ez \
    --BackupConfigSet.0.EnableBackupPolicy True \
    --BackupConfigSet.0.BeginDate 2023-07-01 \
    --BackupConfigSet.0.MaxRetentionDays 101 \
    --BackupConfigSet.0.Frequency annually \
    --BackupConfigSet.0.BackupCount 2
```

Output: 
```
{
    "Response": {
        "RequestId": "58c161ee-c463-463a-bb5a-b34c81132063"
    }
}
```

