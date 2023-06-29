**Example 1: 查询全量备份集列表**



Input: 

```
tccli dbs DescribeFullBackupSets --cli-unfold-argument  \
    --BackupPlanId dbs-qcloudtest \
    --BackupSetId backupset-test \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "BackupMethod": "logical",
                "BackupPool": "DefaultPool",
                "BackupSetId": "backupset-test",
                "BackupSize": 722,
                "EndTime": "2022-05-19 14:58:19",
                "ExpireTime": "2022-05-26 14:58:19",
                "SourceInfo": "cdb-m4l1qwh3",
                "StartTime": "2022-05-19 14:57:09",
                "Status": "finished",
                "StorageType": "DBSStorage"
            },
            {
                "BackupMethod": "logical",
                "BackupPool": "DefaultPool",
                "BackupSetId": "backupset-gt1yxgic",
                "BackupSize": 0,
                "EndTime": "2022-05-19 14:58:49",
                "ExpireTime": "2022-05-26 14:58:49",
                "SourceInfo": "cdb-m4l1qwh3",
                "StartTime": "2022-05-19 14:57:03",
                "Status": "failed",
                "StorageType": "DBSStorage"
            }
        ],
        "RequestId": "6a7be250-dc9e-11ec-b8b3-d985aa28bfec",
        "TotalCount": 2
    }
}
```

