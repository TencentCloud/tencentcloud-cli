**Example 1: 查询备份仓库**

查询备份仓库信息

Input: 

```
tccli tke DescribeBackupStorageLocations --cli-unfold-argument  \
    --Names abc
```

Output: 
```
{
    "Response": {
        "BackupStorageLocationSet": [
            {
                "Name": "abc",
                "StorageRegion": "ap-guangzhou",
                "Provider": "tencentcloud",
                "Bucket": "tke-backup-xx",
                "Path": "",
                "State": "Available",
                "Message": "",
                "LastValidationTime": "2023-04-07T03:18:10Z"
            }
        ],
        "RequestId": "05670c78-3fa8-42c8-87ac-e6b06d0f1f96"
    }
}
```

