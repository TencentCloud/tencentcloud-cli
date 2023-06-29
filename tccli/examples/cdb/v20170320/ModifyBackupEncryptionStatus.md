**Example 1: 开启实例备份加密**

开启实例备份加密

Input: 

```
tccli cdb ModifyBackupEncryptionStatus --cli-unfold-argument  \
    --InstanceId cdb-XXXX \
    --EncryptionStatus on
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

