**Example 1: Modifying the backup policy of the "mssql-j8kv137v" instance**



Input: 

```
tccli sqlserver ModifyBackupStrategy --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v\
    --BackupType daily\
    --BackupTime 14\
    --BackupDay 1
```

Output: 
```
{
    "Response": {
        "RequestId": "780339f6-30d7-419a-a30c-c2dc0933af1c",
        "Errno": 0,
        "Msg": ""
    }
}
```

