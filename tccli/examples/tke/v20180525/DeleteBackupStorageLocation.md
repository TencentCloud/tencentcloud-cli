**Example 1: 删除备份仓库**

删除备份仓库，注意，此接口不会清理备份仓库底层存储数据

Input: 

```
tccli tke DeleteBackupStorageLocation --cli-unfold-argument  \
    --Name tke-storage-backup
```

Output: 
```
{
    "Response": {
        "RequestId": "ebc80be1-c6a7-4c1f-870e-74eba8471969"
    }
}
```

