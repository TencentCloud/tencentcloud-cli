**Example 1: 查询增量备份集列表**



Input: 

```
tccli dbs DescribeIncrementBackupSets --cli-unfold-argument  \
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
                "EndTime": "2022-05-25 12:33:33",
                "ExpireTime": "2022-06-24 12:33:33",
                "FileCount": 1,
                "ResourceDetail": {
                    "StayTime": 0,
                    "TieredType": "standard"
                },
                "RetentionType": "standard",
                "SourceInfo": "cdb-hj0xshpk",
                "StartTime": "2022-05-25 11:33:33",
                "Status": "finished",
                "StorageType": "DBSStorage"
            }
        ],
        "RequestId": "56af4d60-dbdc-11ec-9a80-47aee7851065",
        "TotalCount": 1
    }
}
```

