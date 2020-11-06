**Example 1: Querying slow log statistics in specified time period by SQL template**



Input: 

```
tccli dbbrain DescribeSlowLogTopSqls --cli-unfold-argument  \
    --InstanceId test \
    --SortBy QueryTime \
    --OrderBy ASC \
    --Limit 10 \
    --Offset 0 \
    --StartTime '2019-01-01 00:00:00' \
    --EndTime '2019-01-01 01:00:00'
```

Output: 
```
{
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
            "Schema": "",
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
            "QueryTimeMin": 0
        }
    ]
}
```

