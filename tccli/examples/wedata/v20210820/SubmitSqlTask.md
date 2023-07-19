**Example 1: 请求demo**



Input: 

```
tccli wedata SubmitSqlTask --cli-unfold-argument  \
    --ScriptContent select 1 \
    --ResourceQueue default \
    --DatabaseName default \
    --ProjectId 1 \
    --DatabaseType HIVE \
    --DatasourceType HIVE \
    --DatasourceId 6 \
    --GroupId default \
    --EngineId default \
    --ScriptId 100 \
    --RunParams {"name":"Tom", "age":123}
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "Record": {
            "Id": 858,
            "InstanceId": "20220218112409315_2022-03-02T17:07:37+08:00",
            "ScriptContent": "select name from student where name='ccc';",
            "CreateTime": "2022-03-02T17:07:36+08:00",
            "Status": null
        },
        "Details": [
            {
                "Id": 858,
                "ScriptContent": "select name from student where name='ccc';",
                "StartTime": "2022-03-02T17:07:36+08:00",
                "EndTime": "2022-03-02T17:07:36+08:00",
                "Status": "CREATED",
                "RecordId": 858
            }
        ]
    }
}
```

