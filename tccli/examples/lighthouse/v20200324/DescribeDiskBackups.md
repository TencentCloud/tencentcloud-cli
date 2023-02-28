**Example 1: 查看云硬盘备份点列表**

查看云硬盘备份点列表

Input: 

```
tccli lighthouse DescribeDiskBackups --cli-unfold-argument  \
    --DiskBackupIds lhbak-nuen5foj
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DiskBackupSet": [
            {
                "DiskBackupId": "lhbak-nuen5foj",
                "DiskUsage": "DATA_DISK",
                "DiskId": "lhdisk-nbebddz8",
                "DiskSize": 200,
                "DiskBackupName": "lhdisk-nbebddz8-data-disk-062317",
                "DiskBackupState": "ROLLBACKING",
                "Percent": 100,
                "LatestOperation": "ApplyDiskBackup",
                "LatestOperationState": "OPERATING",
                "LatestOperationRequestId": "41c963ec-5e49-4454-8f98-b3f008958eb9",
                "CreatedTime": "2022-06-23T09:19:05Z"
            }
        ],
        "RequestId": "67a6539c-c9b3-453d-9ba4-9024e0e05f31"
    }
}
```

