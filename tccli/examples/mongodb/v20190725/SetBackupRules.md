**Example 1: 设置实例的自动备份规则**



Input: 

```
tccli mongodb SetBackupRules --cli-unfold-argument  \
    --InstanceId cmgo-abcede \
    --BackupTime 22 \
    --BackupMethod 1 \
    --BackupRetentionPeriod 7 \
    --Notify True
```

Output: 
```
{
    "Response": {
        "RequestId": "58f3a6a0-2330-11ef-ad75-7139c2c3f68c"
    }
}
```

