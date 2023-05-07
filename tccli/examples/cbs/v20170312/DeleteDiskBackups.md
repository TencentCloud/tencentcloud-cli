**Example 1: 删除云硬盘备份点**

删除备份点ID为dbp-xxxxxxxx的备份点。

Input: 

```
tccli cbs DeleteDiskBackups --cli-unfold-argument  \
    --DiskBackupIds dbp-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "a79a4333-ac8e-426c-8cfe-2923c4010d64"
    }
}
```

