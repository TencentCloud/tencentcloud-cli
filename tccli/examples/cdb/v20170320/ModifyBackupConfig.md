**Example 1: 修改数据库备份配置**

修改数据库备份配置

Input: 

```
tccli cdb ModifyBackupConfig --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --ExpireDays 10 \
    --BinlogExpireDays 8 \
    --BackupMethod logical \
    --StartTime 02:00-06:00
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

