**Example 1: 删除保险箱内备份**



Input: 

```
tccli cynosdb DeleteBackupVault --cli-unfold-argument  \
    --VaultId vault-a6ed23f2-f03e-4410-b946-624d1e7d9b5a \
    --BackupIds 631
```

Output: 
```
{
    "Response": {
        "TaskId": 4295131366,
        "RequestId": "24db1d68-f25f-4da7-a8f7-f9a8bd2a0307"
    }
}
```

