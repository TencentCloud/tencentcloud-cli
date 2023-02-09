**Example 1: 创建数据库备份**



Input: 

```
tccli cdb CreateBackup --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --BackupDBTableList.0.Table tb1 \
    --BackupDBTableList.0.Db db1 \
    --BackupMethod logical
```

Output: 
```
{
    "Response": {
        "BackupId": 102996666,
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

