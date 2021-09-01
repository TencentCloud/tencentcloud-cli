**Example 1: 查询迁移数据库列表**



Input: 

```
tccli sqlserver DescribeMigrationDatabases --cli-unfold-argument  \
    --InstanceId mssql-si2823jyl \
    --UserName sqlserver_admin \
    --Password 123456
```

Output: 
```
{
    "Response": {
        "RequestId": "4be5990d-a4b5-49dc-b2b4-e713b6aa7ba3",
        "Amount": 3,
        "MigrateDBSet": [
            "Biz-test1",
            "Biz-test2",
            "Biz-test3"
        ]
    }
}
```

