**Example 1: 按照Sql模板查询指定时间段内的慢日志统计结果**

按照Sql模板查询指定时间段内的慢日志统计结果。

Input: 

```
tccli dbbrain DescribeSlowLogTopSqls --cli-unfold-argument  \
    --InstanceId test \
    --SortBy QueryTime \
    --OrderBy ASC \
    --Limit 10 \
    --Offset 0 \
    --StartTime '2019-01-01 00:00:00' \
    --EndTime '2019-01-01 01:00:00' \
    --SchemaList.0.Schema dbName
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "TotalCount": 1,
        "Rows": [
            {
                "RowsExaminedMax": 0,
                "ExecTimes": 2,
                "RowsSentMax": 0,
                "QueryTimeRatio": 100,
                "LockTimeRatio": 0,
                "LockTimeMin": 0,
                "RowsExaminedRatio": 0,
                "Schema": "dbName",
                "SqlText": "select test from test",
                "QueryTime": 28.17341,
                "SqlTemplate": "select ? from ?",
                "QueryTimeMax": 14.086705,
                "LockTime": 0,
                "RowsSent": 0,
                "RowsSentMin": 0,
                "LockTimeMax": 0,
                "RowsSentRatio": 0,
                "RowsExamined": 0,
                "RowsExaminedMin": 0,
                "QueryTimeMin": 0,
                "RowsSentAvg": 0,
                "LockTimeAvg": 0,
                "RowsExaminedAvg": 0,
                "QueryTimeAvg": 0
            }
        ]
    }
}
```

