**Example 1: 查询备份库信息**



Input: 

```
tccli bdrc DescribeBackupVaults --cli-unfold-argument  \
    --VaultIds vault-qjhn63ku
```

Output: 
```
{
    "Response": {
        "BackupVaultSet": [
            {
                "BackupPolicySet": [],
                "BackupSet": [],
                "CreateTime": "2026-03-26T17:38:17+08:00",
                "Description": "brctest",
                "EncryptType": "NONE",
                "KmsKeyId": "",
                "Region": "gz",
                "Status": "READ_WRITE",
                "VaultId": "vault-qjhn63ku",
                "VaultName": "112233",
                "VaultType": "COMMON"
            }
        ],
        "RequestId": "9f209ef5-1add-4ca4-8260-bcb6902ddf85",
        "TotalCount": 1
    }
}
```

