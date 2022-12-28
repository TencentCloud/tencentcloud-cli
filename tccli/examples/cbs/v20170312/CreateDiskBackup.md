**Example 1: 创建云硬盘备份点**

为拥有备份点配额的云硬盘手动创建一个云硬盘备份点。

Input: 

```
tccli cbs CreateDiskBackup --cli-unfold-argument  \
    --DiskId disk-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "DiskBackupId": "dbp-xxxxxxxx",
        "RequestId": "a79a4333-ac8e-426c-8cfe-2923c4010d64"
    }
}
```

