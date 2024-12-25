**Example 1: 查询备份文件解密密钥**

查询备份文件解密密钥

Input: 

```
tccli cdb DescribeBackupDecryptionKey --cli-unfold-argument  \
    --InstanceId cdb-fybaegd8 \
    --BackupId 12445233
```

Output: 
```
{
    "Response": {
        "DecryptionKey": "your_key",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

