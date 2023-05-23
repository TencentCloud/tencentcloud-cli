**Example 1: 获取慢SQL模板列表 **

按照Sql模板+schema的聚合方式，统计排序指定时间段内的top慢sql。

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
        "RequestId": "ed279d8b-a9d9-48d6-9429-e0fde000994a",
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
                "SqlText": "select * from user where name='sz'",
                "Schema": "test",
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
                "SqlTemplate": "select * from user where name=?",
                "LockTime": 0.0,
                "Md5": "2323847233"
            }
        ]
    }
}
```

