**Example 1: 无**



Input: 

```
tccli mariadb DescribeBackupFiles --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Files": [
            {
                "BackupType": "Data",
                "EndTime": "2022-05-20 00:02:19",
                "FileName": "cos_xtrabackup+1652976129+20220520+000209+3085636221+xbstream.lz4",
                "FilePath": "cos_backup/tdsql/set_1652843814_8559529/xtrabackup/2022-05-20/cos_xtrabackup+1652976129+20220520+000209+3085636221+xbstream.lz4",
                "FileSize": 48721218,
                "InstanceId": "tdsql-lyzax5rb",
                "InstanceName": "test-name",
                "InstanceStatus": 2,
                "ManualBackup": 0,
                "ShardId": "",
                "StartTime": "2022-05-20 00:02:09"
            },
            {
                "BackupType": "Data",
                "EndTime": "2022-05-19 00:23:03",
                "FileName": "cos_xtrabackup+1652890972+20220519+002252+3085636221+xbstream.lz4",
                "FilePath": "cos_backup/tdsql/set_1652843814_8559529/xtrabackup/2022-05-19/cos_xtrabackup+1652890972+20220519+002252+3085636221+xbstream.lz4",
                "FileSize": 47738611,
                "InstanceId": "tdsql-lyzax5rb",
                "InstanceName": "test-name",
                "InstanceStatus": 2,
                "ManualBackup": 0,
                "ShardId": "",
                "StartTime": "2022-05-19 00:22:52"
            },
            {
                "BackupType": "Data",
                "EndTime": "2022-05-18 11:44:52",
                "FileName": "cos_xtrabackup+1652845485+20220518+114445+3085636221+xbstream.lz4",
                "FilePath": "cos_backup/tdsql/set_1652843814_8559529/xtrabackup/2022-05-18/cos_xtrabackup+1652845485+20220518+114445+3085636221+xbstream.lz4",
                "FileSize": 10281128,
                "InstanceId": "tdsql-lyzax5rb",
                "InstanceName": "test-name",
                "InstanceStatus": 2,
                "ManualBackup": 0,
                "ShardId": "",
                "StartTime": "2022-05-18 11:44:45"
            },
            {
                "BackupType": "Binlog",
                "EndTime": "2022-05-20 17:13:31",
                "FileName": "binlog+1652843821+20220518+111701+3085636221+binlog.000002.lz4",
                "FilePath": "cos_backup/tdsql/set_1652843814_8559529/binlog/2022-05-18/binlog+1652843821+20220518+111701+3085636221+binlog.000002.lz4",
                "FileSize": 51119079,
                "InstanceId": "tdsql-lyzax5rb",
                "InstanceName": "test-name",
                "InstanceStatus": 2,
                "ManualBackup": 0,
                "ShardId": "",
                "StartTime": "2022-05-18 11:17:01"
            }
        ],
        "RequestId": "dce77e5f-57b9-4df5-9889-1a4b9f318659",
        "TotalCount": 4
    }
}
```

