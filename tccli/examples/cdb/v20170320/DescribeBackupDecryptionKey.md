**Example 1: 查询备份文件解密密钥**

查询备份文件解密密钥

Input: 

```
tccli cdb DescribeBackupDecryptionKey --cli-unfold-argument  \
    --InstanceId cdb-XXXX \
    --BackupId 12345
```

Output: 
```
{
    "Response": {
        "DecryptionKey": "XXXXXXXXXXX",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

