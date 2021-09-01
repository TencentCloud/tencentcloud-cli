**Example 1: 修改备份名称**



Input: 

```
tccli sqlserver ModifyBackupName --cli-unfold-argument  \
    --InstanceId mssql-6upluvd5 \
    --BackupId 1234568 \
    --BackupName backup_name
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0b5780-d2fa-11ea-ba72-1f709d38ab3e"
    }
}
```

