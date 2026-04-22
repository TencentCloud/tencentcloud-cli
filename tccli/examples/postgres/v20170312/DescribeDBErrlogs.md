**Example 1: 查询错误日志**



Input: 

```
tccli postgres DescribeDBErrlogs --cli-unfold-argument  \
    --DBInstanceId postgres-nykju5pj \
    --StartTime 2026-04-15 17:54:50 \
    --EndTime 2026-04-17 17:54:50 \
    --LogFilters.0.Type ApplicationName \
    --LogFilters.0.Compare INC \
    --LogFilters.0.Value slow_log_test
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "ApplicationName": "slow_log_test",
                "ClientAddr": "10.15.255.3:59834",
                "Database": "postgres",
                "ErrMsg": "canceling statement due to user request,,,,0,,SET application_name='slow_log_test'; select pg_sleep(3);",
                "ErrTime": "2026-04-17 11:00:38",
                "ProcessId": 58892,
                "SessionId": "69e1a253.e60c",
                "SessionStartTime": "2026-04-17 11:00:35",
                "SqlStateCode": "57014",
                "UserName": "root",
                "VirtualTransactionId": "1125/307"
            }
        ],
        "TotalCount": 1,
        "RequestId": "fd225dcd-1f80-4db7-bd28-577a498631a7"
    }
}
```

