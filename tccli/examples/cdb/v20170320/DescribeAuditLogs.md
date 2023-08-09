**Example 1: 查询数据库审计日志**



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

**Example 2: 查询xx时间范围内，sql中包含select和test_db，并且来源IP不等于10.0.0.1和100.0.0.1的记录**



Input: 

```
tccli cdb DescribeAuditLogs --cli-unfold-argument  \
    --InstanceId cdb-0ei6rgrp \
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
tccli cdb DescribeAuditLogs --cli-unfold-argument  \
    --InstanceId cdb-0ei6rgrp \
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

