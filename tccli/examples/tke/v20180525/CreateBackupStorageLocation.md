**Example 1: 创建TKE存储仓库**

创建TKE存储仓库

Input: 

```
tccli tke CreateBackupStorageLocation --cli-unfold-argument  \
    --StorageRegion ap-guangzhou \
    --Bucket tke-backup-test \
    --Name tke-storage-backup \
    --Provider tencentcloud \
    --Path tke
```

Output: 
```
{
    "Response": {
        "RequestId": "6b4cf747-ecfb-42ae-a1fb-a0132353c80b"
    }
}
```

