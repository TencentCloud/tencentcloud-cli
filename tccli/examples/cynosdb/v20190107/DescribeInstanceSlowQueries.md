**Example 1: 查询实例慢日志详情**



Input: 

```
tccli cynosdb DescribeInstanceSlowQueries --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-xxxxxxxx \
    --StartTime 2022-06-22 00:00:00 \
    --EndTime 2022-06-24 23:59:59
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SlowQueries": [
            {
                "Database": "information_schema",
                "LockTime": 0,
                "QueryTime": 11.00011,
                "RowsExamined": 0,
                "RowsSent": 0,
                "SqlMd5": "267171214708E27C",
                "SqlTemplate": "select sleep(?) limit ? offset ?;",
                "SqlText": "SELECT sleep(11) LIMIT 11 offset 0",
                "Timestamp": 1655891555,
                "UserHost": "11.186.190.10",
                "UserName": "root"
            }
        ],
        "RequestId": "9e56617c-c7cc-44e1-a967-6beb418ad5e7"
    }
}
```

