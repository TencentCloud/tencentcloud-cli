**Example 1: 查询增量备份集文件列表**



Input: 

```
tccli dbs DescribeIncrementBackupSetFiles --cli-unfold-argument  \
    --BackupSetId dbsset-xxxxxxxx \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BackupFiles": [
            {
                "FileName": "mysql-bin.000001",
                "BackupSetId": "dbsset-xxxxxxxx",
                "Status": "finished",
                "SourceInfo": "127.0.0.1:3306",
                "StartTime": "2022-05-23 11:12:13",
                "EndTime": "2022-05-23 11:20:13",
                "ExpireTime": "2022-06-23 11:20:13",
                "BackupSize": 1024,
                "BackupMethod": "logical",
                "StorageType": "system",
                "RetentionType": "standard",
                "ResourceDetail": {
                    "TieredType": "standard",
                    "StayTime": 0
                },
                "BackupPool": "DefaultPool",
                "AllowedActions": [
                    "download"
                ],
                "AllActions": [
                    "download"
                ],
                "LastModified": "2022-05-23 11:20:13"
            }
        ],
        "RequestId": "ce31a435-eb3d-4508-b6e9-1b96cf86c8c7"
    }
}
```

