**Example 1: 查询备份文件列表**



Input: 

```
tccli lighthousedb DescribeBackupList --cli-unfold-argument  \
    --Limit 10 \
    --ClusterId lhdbmysql-ilgo90hu \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BackupList": [
            {
                "SnapshotId": 10000,
                "SnapshotTime": "20200204",
                "FileName": "snap",
                "FileSize": 20190215,
                "StartTime": "2019-01-20 01:10:12",
                "FinishTime": "2019-01-20 02:10:12",
                "BackupType": "snapshot",
                "BackupMethod": "auto",
                "BackupStatus": "success",
                "SnapShotType": "full",
                "BackupName": "desc123",
                "BackupId": 100
            }
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

