**Example 1: 删除手动的备份**



Input: 

```
tccli sqlserver RemoveBackups --cli-unfold-argument  \
    --InstanceId mssql-6upluvd5\
    --BackupNames manual_instance_58001_20180702010430.bak.tar
```

Output: 
```
{
    "Response": {
        "RequestId": "55e283aa-0001-4b22-8b60-b208f08cf580"
    }
}
```

