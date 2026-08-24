**Example 1: 查询备份库操作掩码**



Input: 

```
tccli bdrc DescribeBackupVaultsDeniedActions --cli-unfold-argument  \
    --VaultIds vault-qjhn63ku
```

Output: 
```
{
    "Response": {
        "BackupVaultDeniedActionSet": [
            {
                "DeniedActions": [],
                "VaultId": "vault-qjhn63ku"
            }
        ],
        "RequestId": "0d86eaa9-1aac-4cab-98e1-8e25c9e7f5b0"
    }
}
```

