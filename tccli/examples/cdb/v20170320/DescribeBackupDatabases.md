**Example 1: 查询备份数据库列表**



Input: 

```
tccli cdb DescribeBackupDatabases --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --StartTime 2017-07-12 10:29:20
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": "2",
        "Items": [
            {
                "DatabaseName": "mysql"
            },
            {
                "DatabaseName": "test"
            }
        ]
    }
}
```

