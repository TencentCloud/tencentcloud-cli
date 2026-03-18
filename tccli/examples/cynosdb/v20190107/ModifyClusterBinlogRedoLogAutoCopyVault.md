**Example 1: 设置binlog和redoLog自动投递**



Input: 

```
tccli cynosdb ModifyClusterBinlogRedoLogAutoCopyVault --cli-unfold-argument  \
    --ClusterId cynosdbmysql-03e2xlyd \
    --AutoCopyVaults.0.VaultId vault-a6ed23f2-f03e-4410-b946-624d1e7d9b5a \
    --AutoCopyVaults.0.VaultRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "TaskId": 4295131272,
        "RequestId": "448df343-49af-4fea-a79a-82580248996c"
    }
}
```

