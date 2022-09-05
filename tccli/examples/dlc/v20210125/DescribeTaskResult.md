**Example 1: 查询任务结果**

查询任务结果，每次返回1000行数据

Input: 

```
tccli dlc DescribeTaskResult --cli-unfold-argument  \
    --TaskId 9e20f9c021cb11ec835f5254006c64af \
    --NextToken 
```

Output: 
```
{
    "Response": {
        "RequestId": "9328049f-30bc-4feb-aecf-e3b4ff2d1b00",
        "TaskInfo": {
            "TaskId": "9e20f9c021cb11ec835f5254006c64af",
            "DatasourceConnectionName": "CosDataCatalog",
            "DatabaseName": "auth_test",
            "SQL": "SELECT * FROM `auth_test`.`hive_test` LIMIT 10",
            "SQLType": "DQL",
            "State": 2,
            "DataAmount": 850363,
            "UsedTime": 1761,
            "TotalTime": 2000,
            "OutputPath": "cosn://dlc-nj-1258469122/test/DLCQueryResults/2021/09/30/9e20f9c021cb11ec835f5254006c64af/",
            "CreateTime": "1632991895728",
            "OutputMessage": "success",
            "RowAffectInfo": "59378 rows affected (1.761000 seconds)",
            "ResultSchema": [
                {
                    "Name": "a",
                    "Type": "integer",
                    "Comment": "",
                    "Precision": 0,
                    "Scale": 0,
                    "Nullable": "NULLABLE"
                },
                {
                    "Name": "b",
                    "Type": "varchar",
                    "Comment": "",
                    "Precision": 0,
                    "Scale": 0,
                    "Nullable": "NULLABLE"
                }
            ],
            "ResultSet": "[[\"3\",\"kk\"],[\"3\",\"kk\"],[\"9143\",\" \\\"28992\\\"\"],[\"19048\",\" \\\"11266\\\"\"],[\"16711\",\" \\\"17422\\\"\"],[\"3816\",\" \\\"18501\\\"\"],[\"16428\",\" \\\"13774\\\"\"],[\"30190\",\" \\\"5177\\\"\"],[\"24824\",\" \\\"19479\\\"\"],[\"9709\",\" \\\"5532\\\"\"]]",
            "NextToken": "",
            "Percentage": 100,
            "ProgressDetail": "[{\"jobId\":\"0\",\"stages\":[{\"stageId\":\"0\",\"schedule\":1},{\"stageId\":\"1\",\"schedule\":1},{\"stageId\":\"2\",\"schedule\":1},{\"stageId\":\"3\",\"schedule\":1}],\"jobState\":\"\"}]",
            "DisplayFormat": "table"
        }
    }
}
```

