**Example 1: 查询备份文件列表**

查询备份文件列表

Input: 

```
tccli cynosdb DescribeBackupList --cli-unfold-argument  \
    --Limit 2 \
    --ClusterId cynosdbmysql-ck8fmktd \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "BackupList": [
            {
                "BackupId": 1880312,
                "BackupMethod": "auto",
                "BackupName": "",
                "BackupStatus": "success",
                "BackupType": "snapshot",
                "FileName": "jia_20241028040005",
                "FileSize": 10426,
                "FinishTime": "2024-10-28 04:02:34",
                "SnapShotType": "increment",
                "SnapshotId": 1880312,
                "SnapshotTime": "2024-10-28 04:00:04",
                "StartTime": "2024-10-28 04:02:14"
            },
            {
                "BackupId": 1879681,
                "BackupMethod": "auto",
                "BackupName": "",
                "BackupStatus": "success",
                "BackupType": "logic",
                "FileName": "jia_20241028022147",
                "FileSize": 1684666,
                "FinishTime": "2024-10-28 02:22:24",
                "SnapShotType": "full",
                "SnapshotId": 1879681,
                "SnapshotTime": "2024-10-28 02:21:47",
                "StartTime": "2024-10-28 02:21:47"
            }
        ],
        "RequestId": "1f2f4b1e-424d-4740-9b26-d947e957780e",
        "TotalCount": 40
    }
}
```

