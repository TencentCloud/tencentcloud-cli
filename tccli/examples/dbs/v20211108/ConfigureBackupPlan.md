**Example 1: ConfigureBackupPlan**



Input: 

```
tccli dbs ConfigureBackupPlan --cli-unfold-argument  \
    --BackupPlanId dbs-xxxxxx \
    --SourceEndPoint.Region ap-guangzhou \
    --SourceEndPoint.DatabaseType mysql \
    --SourceEndPoint.AccessType cdb \
    --SourceEndPoint.InstanceId cdb-xxxxxxxx \
    --SourceEndPoint.Supplier others \
    --SourceEndPoint.UserName root \
    --SourceEndPoint.Password xxxxxxxx \
    --BackupObject.ObjectMode all \
    --BackupStrategy.BackupPeriod.PeriodType Weekly \
    --BackupStrategy.BackupPeriod.Day Monday \
    --BackupStrategy.BackupMethod logical \
    --BackupStrategy.StrategyType period \
    --BackupStrategy.BackupStartTime 02:00 \
    --BackupStrategy.EnableIncrement True \
    --BackupStrategy.StorageStrategy.BackupRetentionPeriod 30 \
    --BackupStrategy.StorageStrategy.StorageType system \
    --BackupPlanName backupPlan
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

