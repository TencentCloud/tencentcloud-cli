**Example 1: 调整保险箱备份保存时间将会删除多少备份**



Input: 

```
tccli cynosdb CalculateBackupSaveSecExpires --cli-unfold-argument  \
    --VaultId vault-a6ed23f2-f03e-4410-b946-624d1e7d9b5a \
    --BackupSaveSeconds 604800
```

Output: 
```
{
    "Response": {
        "WillDeleteBackupFileCount": 0,
        "WillDeleteBackupFiles": [],
        "WillDeleteBinlogFileCount": 0,
        "WillDeleteBinlogFiles": [],
        "WillDeleteRedoLogFileCount": 0,
        "WillDeleteRedoLogFiles": [],
        "RequestId": "1d7f4916-bd01-4bef-949b-1ee1aef21e7f"
    }
}
```

