**Example 1: 通过任务 ID 查询表血缘**

通过任务 ID 查询表血缘

Input: 

```
tccli wedata DescribeTaskLineage --cli-unfold-argument  \
    --TaskId 20240610151527396
```

Output: 
```
{
    "Response": {
        "RequestId": "5b52cec2-f76f-4e38-9855-1577b139ce9b",
        "TaskLineageInfos": [
            {
                "SourceTable": {
                    "TaskId": "20240610151527396",
                    "TaskName": "chanchu",
                    "DataSourceId": 29547,
                    "DataSourceType": "HIVE",
                    "DatabaseName": "a_saski_test",
                    "SchemaName": "",
                    "TableName": "tb1554",
                    "TableUri": "a_saski_test.tb1554",
                    "Type": 0
                },
                "TargetTable": {
                    "TaskId": "20240610151527396",
                    "TaskName": "chanchu",
                    "DataSourceId": 29547,
                    "DataSourceType": "HIVE",
                    "DatabaseName": "a_saski_test",
                    "SchemaName": "",
                    "TableName": "tb1552",
                    "TableUri": "a_saski_test.tb1552",
                    "Type": 1
                }
            }
        ]
    }
}
```

