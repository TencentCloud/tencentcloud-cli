**Example 1: 按照Sql模板查询指定时间段内的慢日志统计结果**



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
                "QueryTimeMin": 0.0,
                "LockTimeMin": 0.0,
                "QueryTimeMax": 14.086705,
                "QueryTimeRatio": 0.0,
                "RowsSentRatio": 0.0,
                "RowsSentMax": 0,
                "RowsExaminedMin": 0,
                "RowsSentMin": 0,
                "SqlText": "xx",
                "Schema": "xx",
                "LockTimeMax": 0.0,
                "LockTimeRatio": 0.0,
                "ExecTimes": 2,
                "LockTimeAvg": 0.0,
                "RowsExamined": 0,
                "RowsSentAvg": 0.0,
                "QueryTime": 28.17341,
                "RowsExaminedAvg": 0.0,
                "RowsExaminedMax": 0,
                "RowsSent": 0,
                "RowsExaminedRatio": 0.0,
                "QueryTimeAvg": 0.0,
                "SqlTemplate": "xx",
                "LockTime": 0.0
            }
        ]
    }
}
```

