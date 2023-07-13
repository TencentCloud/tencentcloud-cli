**Example 1: 查询审计日志**

查询审计日志

Input: 

```
tccli cynosdb DescribeAuditLogs --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-qwerasdf \
    --StartTime 2017-07-12 10:29:20 \
    --EndTime 2017-07-13 10:29:20
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": "1",
        "Items": [
            {
                "PolicyName": "sys_default",
                "ExecTime": 0,
                "Timestamp": "2023-06-26 10:32:36.000",
                "AffectRows": 0,
                "ThreadId": 0,
                "TableName": "",
                "ErrCode": 0,
                "Host": "10.0.0.1",
                "SentRows": 0,
                "User": "test",
                "Sql": "SELECT * FROM test LIMIT 1;",
                "SqlType": "SELECT",
                "InstanceName": "test",
                "DBName": "test_db"
            }
        ]
    }
}
```

