**Example 1: 创建迁移任务**



Input: 

```
tccli sqlserver CreateMigration --cli-unfold-argument  \
    --MigrateName 测试接口 \
    --MigrateType 2 \
    --SourceType 5 \
    --Source.Url http://gz-oncvm-1254065710.cosgz.myqcloud.com/testdb.bak \
    --Target.InstanceId mssql-si2823jyl
```

Output: 
```
{
    "Response": {
        "RequestId": "4be5990d-a4b5-49dc-b2b4-e713b6aa7ba3",
        "MigrateId": 2728
    }
}
```

