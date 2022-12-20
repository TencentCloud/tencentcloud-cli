**Example 1: 查看云硬盘备份点操作限制列表**



Input: 

```
tccli lighthouse DescribeDiskBackupsDeniedActions --cli-unfold-argument  \
    --DiskBackupIds lhbak-nuen5foj
```

Output: 
```
{
    "Response": {
        "DiskBackupDeniedActionSet": [
            {
                "DiskBackupId": "lhbak-nuen5foj",
                "DeniedActions": [
                    {
                        "Action": "ApplyDiskBackup",
                        "Code": "UnsupportedOperation.InvalidDiskBackupState",
                        "Message": "The disk backup `lhbak-nuen5foj` is in `ROLLBACKING` state and does not support this operation."
                    },
                    {
                        "Action": "DeleteDiskBackups",
                        "Code": "UnsupportedOperation.InvalidDiskBackupState",
                        "Message": "The disk backup `lhbak-nuen5foj` is in `ROLLBACKING` state and does not support this operation."
                    }
                ]
            }
        ],
        "RequestId": "64f1ba69-db43-47c6-b1f1-584b172e3f8a"
    }
}
```

