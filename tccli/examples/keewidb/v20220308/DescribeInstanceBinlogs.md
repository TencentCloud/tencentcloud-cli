**Example 1: 示例1**



Input: 

```
tccli keewidb DescribeInstanceBinlogs --cli-unfold-argument  \
    --InstanceId kee-lagg27el \
    --Limit 5 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "BackupSet": [
            {
                "BackupId": "211331",
                "EndTime": "2022-06-29 20:48:28",
                "FileSize": 606208,
                "Filename": "pmedis_backup_binlog.1-1655902375-shard-1-thread-2.tgz",
                "StartTime": "2022-06-29 20:48:28"
            },
            {
                "BackupId": "211321",
                "EndTime": "2022-06-29 20:48:28",
                "FileSize": 606208,
                "Filename": "pmedis_backup_binlog.1-1655902375-shard-0-thread-3.tgz",
                "StartTime": "2022-06-29 20:48:28"
            },
            {
                "BackupId": "211320",
                "EndTime": "2022-06-29 20:48:12",
                "FileSize": 606208,
                "Filename": "pmedis_backup_binlog.1-1655902375-shard-3-thread-0.tgz",
                "StartTime": "2022-06-29 20:48:12"
            },
            {
                "BackupId": "211319",
                "EndTime": "2022-06-29 20:48:28",
                "FileSize": 606208,
                "Filename": "pmedis_backup_binlog.1-1655902375-shard-0-thread-2.tgz",
                "StartTime": "2022-06-29 20:48:28"
            },
            {
                "BackupId": "211318",
                "EndTime": "2022-06-29 20:48:12",
                "FileSize": 606208,
                "Filename": "pmedis_backup_binlog.1-1655902375-shard-5-thread-3.tgz",
                "StartTime": "2022-06-29 20:48:12"
            }
        ],
        "RequestId": "342e23c5-fbfe-407f-9acf-8bb890fca8b2",
        "TotalCount": 24
    }
}
```

