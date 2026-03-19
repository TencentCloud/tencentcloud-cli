**Example 1: 修改实例备份策略**

修改实例备份策略

Input: 

```
tccli tdmysql ModifyDBSBackupPolicy --cli-unfold-argument  \
    --InstanceId tdsql3-31l2r0yn912rg \
    --BackupPolicy.FullRetentionPeriod 7 \
    --BackupPolicy.LogRetentionPeriod 8 \
    --BackupPolicy.PeriodTime 0,1,2,3,4,5,6 \
    --BackupPolicy.BackupMethod physical \
    --BackupPolicy.BackupStartTime 00:00 \
    --BackupPolicy.BackupEndTime 04:00 \
    --BackupPolicy.StorageType COS
```

Output: 
```
{
    "Response": {
        "IsSuccess": true,
        "Msg": "Modify backup policy successfully",
        "RequestId": "5cf77a8a-94e8-4fae-8abf-a48284f75606"
    }
}
```

