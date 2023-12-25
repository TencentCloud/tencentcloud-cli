**Example 1: DescribeDatabaseAuditRecords**

获取数据库审计记录

Input: 

```
tccli cdwdoris DescribeDatabaseAuditRecords --cli-unfold-argument  \
    --InstanceId abc \
    --StartTime abc \
    --EndTime abc \
    --PageSize 0 \
    --PageNum 0 \
    --OrderType abc \
    --User abc \
    --DbName abc \
    --SqlType abc \
    --Sql abc \
    --Users abc \
    --DbNames abc \
    --SqlTypes abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "SlowQueryRecords": {
            "OsUser": "abc",
            "InitialQueryId": "abc",
            "Sql": "abc",
            "QueryStartTime": "abc",
            "DurationMs": 0,
            "ReadRows": 0,
            "ResultRows": 0,
            "ResultBytes": 1,
            "MemoryUsage": 0,
            "InitialAddress": "abc",
            "DbName": "abc",
            "SqlType": "abc"
        },
        "RequestId": "abc"
    }
}
```

