**Example 1: 开启备份加密**



Input: 

```
tccli redis ModifyBackupEncrypt --cli-unfold-argument  \
    --InstanceId crs-h09vd2w3 \
    --BackupEncrypt True \
    --EncryptKeyType 0 \
    --KmsRegion ap-region
```

Output: 
```
{
    "Response": {
        "RequestId": "8f555a58-c415-48d0-babb-90f3bd17a2e6"
    }
}
```

