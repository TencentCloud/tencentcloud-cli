**Example 1: DescribeSlowQueryRecords**

慢查询

Input: 

```
tccli cdwdoris DescribeSlowQueryRecords --cli-unfold-argument  \
    --InstanceId cdwdoris-3lnbut3w \
    --QueryDurationMs 3000 \
    --EndTime 2025-01-03 15:13:48 \
    --StartTime 2025-01-03 14:58:48 \
    --PageSize 10 \
    --PageNum 1 \
    --IsQuery -1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "SlowQueryRecords": [
            {
                "OsUser": "user",
                "InitialQueryId": "xadfa-2xasdfa-a74rax",
                "Sql": "select * from test",
                "QueryStartTime": "2025-01-02 12:23:12",
                "DurationMs": 12,
                "ReadRows": 1234,
                "ResultRows": 364,
                "ResultBytes": 1,
                "MemoryUsage": 0,
                "InitialAddress": "192.168.13.24"
            }
        ],
        "RequestId": "asdfas-xadsfa-adssfad-1sdsa"
    }
}
```

