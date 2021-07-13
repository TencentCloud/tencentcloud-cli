**Example 1: 查询增量备份导入任务**



Input: 

```
tccli sqlserver DescribeIncrementalMigration --cli-unfold-argument  \
    --BackupMigrationId mssql-backup-migration-cg0ffgqt \
    --BackupFileName cvm \
    --Limit 100 \
    --Offset 0 \
    --OrderBy createTime \
    --OrderByType desc \
    --IncrementalMigrationId mssql-incremental-migration-kp7bgv8p \
    --StatusSet 2 \
    --InstanceId mssql-rdc0gajn
```

Output: 
```
{
    "Response": {
        "IncrementalMigrationSet": [
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
                    "db_cvm_1_20200927204209_2log2_2noreconvery2.bak"
                ],
                "CreateTime": "2020-09-27 20:44:59",
                "Detail": {
                    "Progress": 0,
                    "StepAll": 0,
                    "StepInfo": [],
                    "StepNow": 0
                },
                "EndTime": "0000-00-00 00:00:00",
                "InstanceId": "mssql-rdc0gajn",
                "IsRecovery": "NO",
                "Message": "",
                "MigrationId": "mssql-incremental-migration-kp7bgv8p",
                "MigrationName": "",
                "RecoveryType": "FULL_LOG",
                "Region": "ap-guangzhou",
                "StartTime": "0000-00-00 00:00:00",
                "Status": 2,
                "UploadType": "COS_UPLOAD"
            }
        ],
        "RequestId": "6dc136cb-e2e8-42b7-babc-2fc3b6f50d3d",
        "TotalCount": 1
    }
}
```

