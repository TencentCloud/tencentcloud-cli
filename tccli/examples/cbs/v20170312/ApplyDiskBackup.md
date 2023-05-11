**Example 1: 回滚备份点到原云硬盘**

回滚备份点到原云硬盘

Input: 

```
tccli cbs ApplyDiskBackup --cli-unfold-argument  \
    --DiskId disk-xxxxxxxx \
    --DiskBackupId dbp-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "5d41fd68-372a-4c90-81c6-a6f982328058"
    }
}
```

