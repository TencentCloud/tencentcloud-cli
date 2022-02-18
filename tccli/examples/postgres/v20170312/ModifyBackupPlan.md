**Example 1: 修改实例备份计划**

将实例postgres-xxxxxxxx的备份计划修改为每周一、周二的01:00:00~02:00:00，且备份保留3天

Input: 

```
tccli postgres ModifyBackupPlan --cli-unfold-argument  \
    --DBInstanceId postgres-xxxxxxxx \
    --BackupPeriod monday tuesday \
    --BaseBackupRetentionPeriod 3 \
    --MinBackupStartTime 01:00:00 \
    --MaxBackupStartTime 02:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "8a61e500-aa33-454c-9ec2-da2a368c39ab"
    }
}
```

