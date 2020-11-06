**Example 1: 修改实例mssql-j8kv137v的备份策略**



Input: 

```
tccli sqlserver ModifyBackupStrategy --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v \
    --BackupType daily \
    --BackupTime 14 \
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

