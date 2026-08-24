**Example 1: 查询备份点禁止操作列表**



Input: 

```
tccli bdrc DescribeFileBackupsDeniedActions --cli-unfold-argument  \
    --BackupIds fb-nwb6txnq
```

Output: 
```
{
    "Response": {
        "BackupDeniedActionSet": [
            {
                "BackupId": "fb-nwb6txnq",
                "DeniedActions": [
                    {
                        "Action": "DeleteFileBackups",
                        "Code": "UnsupportedOperation.FileBackupStateError",
                        "Message": "FileBackup(fb-nwb6txnq) status is creating, not support"
                    },
                    {
                        "Action": "CreateFileRestoreTask",
                        "Code": "UnsupportedOperation.FileBackupStateError",
                        "Message": "FileBackup(fb-nwb6txnq) status is creating, not support"
                    }
                ]
            }
        ],
        "RequestId": "cd7cf6d1-71f8-476b-95e6-ae8e2021c8ef"
    }
}
```

