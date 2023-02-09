**Example 1: 查询全量备份导入任务**



Input: 

```
tccli sqlserver DescribeBackupMigration --cli-unfold-argument  \
    --BackupMigrationId mssql-backup-migration-kpl74n9l \
    --OrderBy createTime \
    --MigrationName 字符串 \
    --UploadType COS_UPLOAD \
    --Offset 0 \
    --StatusSet 2 \
    --InstanceId mssql-rdc0gajn \
    --Limit 100 \
    --OrderByType desc \
    --BackupFileName db1 \
    --RecoveryType FULL
```

Output: 
```
{
    "Response": {
        "BackupMigrationSet": [
            {
                "Action": {
                    "AllAction": [
                        "start",
                        "delete",
                        "incremental",
                        "modify",
                        "view",
                        "upload"
                    ],
                    "AllowedAction": [
                        "view",
                        "modify",
                        "delete",
                        "upload",
                        "start"
                    ]
                },
                "AppId": 251006279,
                "BackupFiles": [
                    "db1.bak"
                ],
                "CreateTime": "2020-09-27 16:23:47",
                "Detail": {
                    "Progress": 0,
                    "StepAll": 0,
                    "StepInfo": [],
                    "StepNow": 0
                },
                "EndTime": "0000-00-00 00:00:00",
                "InstanceId": "mssql-rdc0gajn",
                "IsRecovery": "",
                "Message": "",
                "MigrationId": "mssql-backup-migration-kpl74n9l",
                "MigrationName": "字符串",
                "RecoveryType": "FULL",
                "Region": "ap-guangzhou",
                "StartTime": "0000-00-00 00:00:00",
                "Status": 2,
                "DBRename": [
                    {
                        "NewName": "newdb",
                        "OldName": "olddb"
                    }
                ],
                "UploadType": "COS_UPLOAD"
            }
        ],
        "RequestId": "cf4b1509-8029-4daf-b7b1-e504ff82cbba",
        "TotalCount": 1
    }
}
```

