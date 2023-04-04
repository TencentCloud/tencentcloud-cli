**Example 1: 无**



Input: 

```
tccli dcdb DescribeBackupFiles --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Files": [
            {
                "BackupType": "Binlog",
                "EndTime": "2022-05-23 09:16:18",
                "FileName": "binlog+1653031073+20220520+151753+3085689978+binlog.000003.lz4",
                "FilePath": "cos_backup/tdsql/group_1652793502_8559507/set_1652793624_1/binlog/2022-05-20/binlog+1653031073+20220520+151753+3085689978+binlog.000003.lz4",
                "FileSize": 30537563,
                "InstanceId": "dcdbt-21dfpcv1",
                "InstanceName": "test-name",
                "InstanceStatus": 2,
                "ManualBackup": 0,
                "ShardId": "shard-ngbrea6b",
                "StartTime": "2022-05-20 15:17:53"
            },
            {
                "BackupType": "Binlog",
                "EndTime": "2022-05-22 21:33:53",
                "FileName": "binlog+1653010199+20220520+092959+3085680764+binlog.000003.lz4",
                "FilePath": "cos_backup/tdsql/group_1652793502_8559507/set_1652793754_3/binlog/2022-05-20/binlog+1653010199+20220520+092959+3085680764+binlog.000003.lz4",
                "FileSize": 31018905,
                "InstanceId": "dcdbt-21dfpcv1",
                "InstanceName": "test-name",
                "InstanceStatus": 2,
                "ManualBackup": 0,
                "ShardId": "shard-5zf65smf",
                "StartTime": "2022-05-20 09:29:59"
            },
            {
                "BackupType": "Data",
                "EndTime": "2022-05-20 00:20:06",
                "FileName": "cos_xtrabackup+1652977196+20220520+001956+3085689978+xbstream.lz4",
                "FilePath": "cos_backup/tdsql/group_1652793502_8559507/set_1652793624_1/xtrabackup/2022-05-20/cos_xtrabackup+1652977196+20220520+001956+3085689978+xbstream.lz4",
                "FileSize": 165413701,
                "InstanceId": "dcdbt-21dfpcv1",
                "InstanceName": "test-name",
                "InstanceStatus": 2,
                "ManualBackup": 0,
                "ShardId": "shard-ngbrea6b",
                "StartTime": "2022-05-20 00:19:56"
            },
            {
                "BackupType": "Data",
                "EndTime": "2022-05-20 00:06:18",
                "FileName": "cos_xtrabackup+1652976368+20220520+000608+3085680764+xbstream.lz4",
                "FilePath": "cos_backup/tdsql/group_1652793502_8559507/set_1652793754_3/xtrabackup/2022-05-20/cos_xtrabackup+1652976368+20220520+000608+3085680764+xbstream.lz4",
                "FileSize": 174847785,
                "InstanceId": "dcdbt-21dfpcv1",
                "InstanceName": "test-name",
                "InstanceStatus": 2,
                "ManualBackup": 0,
                "ShardId": "shard-5zf65smf",
                "StartTime": "2022-05-20 00:06:08"
            },
            {
                "BackupType": "Binlog",
                "EndTime": "2022-05-20 15:18:04",
                "FileName": "binlog+1652793627+20220517+212027+3085689978+binlog.000002.lz4",
                "FilePath": "cos_backup/tdsql/group_1652793502_8559507/set_1652793624_1/binlog/2022-05-17/binlog+1652793627+20220517+212027+3085689978+binlog.000002.lz4",
                "FileSize": 30809729,
                "InstanceId": "dcdbt-21dfpcv1",
                "InstanceName": "test-name",
                "InstanceStatus": 2,
                "ManualBackup": 0,
                "ShardId": "shard-ngbrea6b",
                "StartTime": "2022-05-17 21:20:27"
            }
        ],
        "RequestId": "d30ef4e8-d99d-4502-a870-196592035794",
        "TotalCount": 5
    }
}
```

