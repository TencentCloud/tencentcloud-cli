**Example 1: 设置备份规则**



Input: 

```
tccli mongodb SetBackupRules --cli-unfold-argument  \
    --InstanceId cmgo-xxxxxx \
    --BackupMethod 0 \
    --BackupFrequency 12 \
    --BackupRetentionPeriod 7 \
    --BackupVersion 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1e9c4e16-f7a5-4db1-8978-3f92e8ca4790"
    }
}
```

