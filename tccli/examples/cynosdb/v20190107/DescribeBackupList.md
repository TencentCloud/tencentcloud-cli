**Example 1: 查询备份文件列表**

查询备份文件列表

Input: 

```
tccli cynosdb DescribeBackupList --cli-unfold-argument  \
    --Limit 10 \
    --ClusterId cynosdbpg-ilgo90hu \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "BackupList": [
            {
                "SnapshotId": 1,
                "FileName": "abc",
                "FileSize": 1,
                "StartTime": "abc",
                "FinishTime": "abc",
                "BackupType": "abc",
                "BackupMethod": "abc",
                "BackupStatus": "abc",
                "SnapshotTime": "abc",
                "BackupId": 0,
                "SnapShotType": "abc",
                "BackupName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

