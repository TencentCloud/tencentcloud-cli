**Example 1: 获取备份下载链接**

获取备份下载链接

Input: 

```
tccli postgres DescribeBackupDownloadURL --cli-unfold-argument  \
    --DBInstanceId postgres-oamgybor \
    --BackupType LogBackup \
    --BackupId f9509fc2-2281-551c-b937-86d38cf79f3b \
    --URLExpireTime 12
```

Output: 
```
{
    "Response": {
        "BackupDownloadURL": "******",
        "RequestId": "7c4e788e-5ec9-4125-bb80-7baabe2744dc"
    }
}
```

