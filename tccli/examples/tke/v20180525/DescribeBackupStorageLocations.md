**Example 1: 查询备份仓库**

查询备份仓库信息

Input: 

```
tccli tke DescribeBackupStorageLocations --cli-unfold-argument  \
    --Names tke-backup
```

Output: 
```
{
    "Response": {
        "BackupStorageLocationSet": [
            {
                "Name": "tke-backup-1",
                "StorageRegion": "ap-guangzhou",
                "Provider": "tencentcloud",
                "Bucket": "tke-backup-2wds9k9p",
                "Path": "/data",
                "State": "Available",
                "Message": "success",
                "LastValidationTime": "2023-04-07T03:18:10Z"
            }
        ],
        "RequestId": "05670c78-3fa8-42c8-87ac-e6b06d0f1f96"
    }
}
```

