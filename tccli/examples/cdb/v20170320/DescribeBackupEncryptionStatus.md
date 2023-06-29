**Example 1: 查询实例的备份加密状态**

查询实例的备份加密状态

Input: 

```
tccli cdb DescribeBackupEncryptionStatus --cli-unfold-argument  \
    --InstanceId cdb-XXXX
```

Output: 
```
{
    "Response": {
        "EncryptionStatus": "on",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

