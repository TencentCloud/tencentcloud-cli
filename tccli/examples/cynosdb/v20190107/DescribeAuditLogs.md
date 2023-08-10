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

**Example 2: 查询xx时间范围内，sql中包含select和test_db，并且来源IP不等于10.0.0.1并且不等100.0.0.1的记录**



Input: 

```
tccli cynosdb DescribeAuditLogs --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-qwerasdf \
    --StartTime 2023-08-01 00:00:00 \
    --EndTime 2023-08-07 00:00:00 \
    --Limit 20 \
    --LogFilter.0.Type sql \
    --LogFilter.0.Compare WINC \
    --LogFilter.0.Value select \
    --LogFilter.1.Type sql \
    --LogFilter.1.Compare WINC \
    --LogFilter.1.Value test_db \
    --LogFilter.2.Type host \
    --LogFilter.2.Compare NEQ \
    --LogFilter.2.Value 10.0.0.1 100.0.0.1
```

Output: 
```
{
    "Response": {
        "Items": null,
        "RequestId": "90d90456-2a5b-4015-81b8-9e2fca52012b",
        "TotalCount": 0
    }
}
```

**Example 3: 查询xx时间范围内，sql中包含selec或者upda，并且来源IP包含10.0.的记录**

sql样例：select * from test_db limit 1;
sql  INC selec 能搜索到;
sql  WINC selec 搜索不到样例;

Input: 

```
tccli cynosdb DescribeAuditLogs --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-qwerasdf \
    --StartTime 2023-08-01 00:00:00 \
    --EndTime 2023-08-07 00:00:00 \
    --Limit 20 \
    --LogFilter.0.Type sql \
    --LogFilter.0.Compare INC \
    --LogFilter.0.Value selec up \
    --LogFilter.1.Type host \
    --LogFilter.1.Compare INC \
    --LogFilter.1.Value 10.0.
```

Output: 
```
{
    "Response": {
        "Items": null,
        "RequestId": "90d90456-2a5b-4015-81b8-9e2fca52012b",
        "TotalCount": 0
    }
}
```

