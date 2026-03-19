**Example 1: 手动备份投递到保险箱**



Input: 

```
tccli cynosdb CopyBackupToVault --cli-unfold-argument  \
    --VaultId vault-a6ed23f2-f03e-4410-b946-624d1e7d9b5a \
    --BackupIds 126511
```

Output: 
```
{
    "Response": {
        "TaskId": 4295131269,
        "RequestId": "43fcda86-c0c8-4115-a298-702fd26868e0"
    }
}
```

