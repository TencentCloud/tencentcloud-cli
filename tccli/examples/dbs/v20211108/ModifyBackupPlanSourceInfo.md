**Example 1: ModifyBackupPlanSourceInfo**



Input: 

```
tccli dbs ModifyBackupPlanSourceInfo --cli-unfold-argument  \
    --BackupPlanId dbs-xxxxxx \
    --SourceEndPoint.Region ap-guangzhou \
    --SourceEndPoint.DatabaseType mysql \
    --SourceEndPoint.AccessType cdb \
    --SourceEndPoint.InstanceId cdb-xxxxxxxx \
    --SourceEndPoint.Supplier others \
    --SourceEndPoint.UserName root \
    --SourceEndPoint.Password xxxxxxxx \
    --BackupObject.ObjectMode all \
    --BackupPlanName mysql-daily-backup
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

