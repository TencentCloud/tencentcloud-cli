**Example 1: 查询数据库审计日志**

查询审计日志成功

Input: 

```
tccli cdb DescribeAuditLogs --cli-unfold-argument  \
    --InstanceId cdb-qwer1234 \
    --StartTime '2023-06-18 00:00:00' \
    --EndTime '2023-06-19 00:00:00' \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "AffectRows": 1,
                "CheckRows": 0,
                "CpuTime": 375.786,
                "DBName": "wyang",
                "ErrCode": 0,
                "ExecTime": 1503,
                "Host": "100.122.76.176",
                "IoWaitTime": 7,
                "LockWaitTime": 1140,
                "NsTime": 104188594,
                "PolicyName": "sys_default",
                "SentRows": 0,
                "Sql": "INSERT INTO `test_db` values('张三',0)",
                "SqlType": "INSERT",
                "ThreadId": 162,
                "Timestamp": "2023-06-07 17:50:05.104",
                "TrxLivingTime": 1475,
                "User": "root"
            }
        ],
        "RequestId": "b3951c71-1da4-4b8f-9de5-ad71ab1e2917-0"
    }
}
```

