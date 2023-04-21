**Example 1: 创建TKE存储仓库**

创建TKE存储仓库

Input: 

```
tccli tke CreateBackupStorageLocation --cli-unfold-argument  \
    --StorageRegion ap-guangzhou \
    --Provider tencentcloud \
    --Bucket tke-backup-xxx \
    --Path  \
    --Name test-registry-1
```

Output: 
```
{
    "Response": {
        "RequestId": "4bef4bc7-edf2-4de6-a2e1-684bfc37185f"
    }
}
```

