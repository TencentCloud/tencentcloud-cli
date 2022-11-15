**Example 1: 修改实例mssql-j8kv137v的备份策略**



Input: 

```
tccli sqlserver ModifyBackupStrategy --cli-unfold-argument  \
    --BackupTime 14 \
    --InstanceId mssql-j8kv137v \
    --RegularBackupCounts 1 \
    --BackupSaveDays 7 \
    --BackupDay 1 \
    --RegularBackupSaveDays 365 \
    --BackupType daily \
    --RegularBackupEnable enable \
    --RegularBackupStrategy month \
    --RegularBackupStartTime 2022-10-10
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

