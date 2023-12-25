**Example 1: DescribeSlowQueryRecords**

慢查询

Input: 

```
tccli cdwdoris DescribeSlowQueryRecords --cli-unfold-argument  \
    --InstanceId abc \
    --QueryDurationMs 0 \
    --StartTime abc \
    --EndTime abc \
    --PageSize 0 \
    --PageNum 0 \
    --DurationMs abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "SlowQueryRecords": [
            {
                "OsUser": "abc",
                "InitialQueryId": "abc",
                "Sql": "abc",
                "QueryStartTime": "abc",
                "DurationMs": 0,
                "ReadRows": 0,
                "ResultRows": 0,
                "ResultBytes": 1,
                "MemoryUsage": 0,
                "InitialAddress": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

