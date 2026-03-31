**Example 1: 修改实例备份策略**

修改实例备份策略

Input: 

```
tccli tdmysql ModifyDBSBackupPolicy --cli-unfold-argument  \
    --BackupPolicy.BackupEndTime 04:00 \
    --BackupPolicy.BackupMethod physical \
    --BackupPolicy.BackupStartTime 00:00 \
    --BackupPolicy.EnableFull 1 \
    --BackupPolicy.EnableLog 1 \
    --BackupPolicy.FullRetentionPeriod 7 \
    --BackupPolicy.InstanceId tdsql3-3f17e49d \
    --BackupPolicy.PeriodTime 0,1,2,3,4,5,6 \
    --BackupPolicy.StorageType COS \
    --InstanceId tdsql3-3f17e49d
```

Output: 
```
{
    "Response": {
        "IsSuccess": true,
        "Msg": "Modify backup policy successfully",
        "RequestId": "823cf9b7-d0b0-4a77-a16c-058634190809"
    }
}
```

