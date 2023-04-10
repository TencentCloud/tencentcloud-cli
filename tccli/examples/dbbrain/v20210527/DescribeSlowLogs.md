**Example 1: 按照Sql模板查询指定时间段内的慢日志详细信息**

按照Sql模板查询指定时间段内的慢日志详细信息

Input: 

```
tccli dbbrain DescribeSlowLogs --cli-unfold-argument  \
    --Product mysql \
    --InstanceId test \
    --Md5 12323242323 \
    --Limit 10 \
    --Offset 0 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "ea7afb20-cf8d-11ed-9231-5be1865f5f0a",
        "Rows": [
            {
                "LockTime": 0,
                "UserHost": "169.254.128.9",
                "RowsSent": 1,
                "UserName": "root",
                "Database": "information_schema",
                "SqlText": "/* dbbrain user mark */select SLEEP(10)",
                "QueryTime": 10,
                "RowsExamined": 0,
                "Timestamp": "2023-03-31 10:47:35"
            },
            {
                "LockTime": 0,
                "UserHost": "169.254.128.9",
                "RowsSent": 1,
                "UserName": "root",
                "Database": "information_schema",
                "SqlText": "/* dbbrain user mark */select SLEEP(8)",
                "QueryTime": 8,
                "RowsExamined": 0,
                "Timestamp": "2023-03-31 10:47:45"
            }
        ]
    }
}
```

