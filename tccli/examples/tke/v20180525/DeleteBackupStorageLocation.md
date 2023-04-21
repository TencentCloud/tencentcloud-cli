**Example 1: 删除备份仓库**

删除备份仓库，注意，此接口不会清理备份仓库底层存储数据

Input: 

```
tccli tke DeleteBackupStorageLocation --cli-unfold-argument  \
    --Name abc
```

Output: 
```
{
    "Response": {
        "RequestId": "0878bad3-d0aa-4886-beac-7f4d450d55fa"
    }
}
```

