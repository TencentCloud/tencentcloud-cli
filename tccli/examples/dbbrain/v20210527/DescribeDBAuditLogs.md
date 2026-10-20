**Example 1: 查询 mariadb Proxy 审计日志**

查询 mariadb 实例的 Proxy 审计日志示例。MultiSql 使用 JSON 字符串承载二维数组。

Input: 

```
tccli dbbrain DescribeDBAuditLogs --cli-unfold-argument  \
    --Product mariadb \
    --InstanceId tdsql-1zsrqfdkh4 \
    --LogType Proxy \
    --StartTime 2026-10-10 11:05:06 \
    --EndTime 2026-10-10 12:05:06 \
    --Limit 20 \
    --Offset 0 \
    --Filter.SqlType SELECT INSERT \
    --Filter.ExecTime 100 200 \
    --Filter.ErrCode 0 \
    --Filter.MultiSql [["a","b"]] \
    --Filter.DBName da \
    --Filter.User dfg \
    --Filter.Host 123.1.1.1 \
    --Filter.ThreadId 12301
```

Output: 
```
{
    "Response": {
        "RequestId": "ed279d8b-a9d9-48d6-9429-e0fde000994a",
        "TotalCount": 1,
        "FilteredRecords": 0,
        "ProxyLogs": [
            {
                "Timestamp": "2026-10-10 18:19:39",
                "ClusterId": "tdsql-1zsrqfdkh4",
                "User": "shine",
                "Host": "11.161.84.21",
                "DBName": "",
                "Sql": "/*p=dmc,o=100047808302,i=121ea724*/ CREATE DATABASE `test` DEFAULT CHARACTER SET = utf8mb4 DEFAULT COLLATE = utf8mb4_0900_ai_ci;",
                "SqlType": "Create",
                "SqlTemplate": "Create",
                "SqlTemplateId": "2026540316",
                "ComType": "COM_QUERY",
                "ExecTime": 255,
                "SqlStartTime": 1791627579927,
                "SqlStartTimeUs": 927490,
                "ThreadId": "513208377",
                "ProxyHost": "30.122.175.73:24717",
                "ProxyThread": "57875",
                "Autocommit": "1",
                "HoldConns": "1",
                "NewConnNum": 0,
                "AffectRows": 0,
                "SentRows": 0,
                "ErrCode": "1044",
                "ErrInfo": "Access denied for user 'shine'@'%' to database 'test'",
                "BusinessCode": "i=121ea724,o=100047808302,p=dmc",
                "BusinessTag": ""
            }
        ]
    }
}
```

