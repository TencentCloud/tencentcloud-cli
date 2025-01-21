**Example 1: DescribeDatabaseAuditRecords**

获取数据库审计记录

Input: 

```
tccli cdwdoris DescribeDatabaseAuditRecords --cli-unfold-argument  \
    --InstanceId cdwdoris-akxtck1n \
    --StartTime 2025-01-06 09:36:04 \
    --EndTime 2025-01-06 10:36:04 \
    --PageSize 0 \
    --PageNum 1 \
    --OrderType DESC \
    --Sql 
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "SlowQueryRecords": {
            "OsUser": "str",
            "InitialQueryId": "xasd-qxxc",
            "Sql": "select * from abc",
            "QueryStartTime": "2025-01-06 10:36:04",
            "DurationMs": 0,
            "ReadRows": 0,
            "ResultRows": 0,
            "ResultBytes": 1,
            "MemoryUsage": 0,
            "InitialAddress": "192.168.12.34",
            "DbName": "ab1",
            "SqlType": "INSERT"
        },
        "RequestId": "abc-2xz"
    }
}
```

