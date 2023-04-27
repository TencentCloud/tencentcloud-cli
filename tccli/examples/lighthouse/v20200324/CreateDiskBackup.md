**Example 1: 创建云硬盘备份点**

创建云硬盘备份点

Input: 

```
tccli lighthouse CreateDiskBackup --cli-unfold-argument  \
    --DiskBackupName disk-backup-01 \
    --DiskId lhdisk-qtovvuzq
```

Output: 
```
{
    "Response": {
        "DiskBackupId": "lhbak-6068cwhv",
        "RequestId": "ef009de9-1bf7-44b3-a30e-adfb328aff8c"
    }
}
```

