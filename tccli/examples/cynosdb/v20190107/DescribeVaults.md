**Example 1: 查询保险箱列表**



Input: 

```
tccli cynosdb DescribeVaults --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 229,
        "Vaults": [
            {
                "AutoCopyConfigs": [
                    {
                        "ClusterId": "cynosdbmysql-03e2xlyd",
                        "CopyType": "binlog",
                        "VaultId": "vault-a6ed23f2-f03e-4410-b946-624d1e7d9b5a",
                        "VaultRegion": "ap-guangzhou"
                    }
                ],
                "BackupFileCount": 1,
                "BackupFileSize": 4183356,
                "BackupSaveSeconds": 604800,
                "BinlogFileCount": 9,
                "BinlogFileSize": 1320651467,
                "RedoLogFileCount": 3,
                "RedoLogFileSize": 1123284320,
                "Status": "running",
                "Tasks": [],
                "VaultId": "vault-a6ed23f2-f03e-4410-b946-624d1e7d9b5a",
                "VaultName": "testtttt",
                "VaultRegion": "ap-guangzhou"
            }
        ],
        "RequestId": "af30455b-61bd-495c-b751-e43a47978c1d"
    }
}
```

