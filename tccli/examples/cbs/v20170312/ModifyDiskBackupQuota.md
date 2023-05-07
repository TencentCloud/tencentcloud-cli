**Example 1: 调整云硬盘备份点配额**

调整云硬盘备份点配额

Input: 

```
tccli cbs ModifyDiskBackupQuota --cli-unfold-argument  \
    --DiskId disk-xxxxxxxx \
    --DiskBackupQuota 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5d41fd68-372a-4c90-81c6-a6f982328058"
    }
}
```

