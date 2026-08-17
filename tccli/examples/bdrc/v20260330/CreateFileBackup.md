**Example 1: 创建文件备份点**



Input: 

```
tccli bdrc CreateFileBackup --cli-unfold-argument  \
    --ResourceId ins-0dl6ai18 \
    --BackupPaths /var/log \
    --ExcludeSystemDirectories True \
    --BackupStorageId vault-ivsapm9k
```

Output: 
```
{
    "Response": {
        "BackupId": "fb-hjyz84u8",
        "RequestId": "4fcb2255-91b4-466b-98a1-1169ede37e8f"
    }
}
```

