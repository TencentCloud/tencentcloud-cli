**Example 1: Modifying a migration task**



Input: 

```
tccli sqlserver ModifyMigration --cli-unfold-argument  \
    --MigrateId 2728 \
    --MigrateName 'Test API' \
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

