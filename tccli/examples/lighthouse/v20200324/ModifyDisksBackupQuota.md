**Example 1: 调整云硬盘备份点配额**



Input: 

```
tccli lighthouse ModifyDisksBackupQuota --cli-unfold-argument  \
    --DiskIds lhdisk-guzg7nsa \
    --DiskBackupQuota 0
```

Output: 
```
{
    "Response": {
        "RequestId": "822edbc4-5d4a-4e19-9d61-2a243f04d06e"
    }
}
```

