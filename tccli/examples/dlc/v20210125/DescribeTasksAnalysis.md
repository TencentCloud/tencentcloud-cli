**Example 1: 洞察分析列表**



Input: 

```
tccli dlc DescribeTasksAnalysis --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "580668d5-d47c-44a1-86ea-273843d94778",
        "TaskList": [
            {
                "Id": "67ea3d234006dc901",
                "SparkAppId": "spark-79d96185704bf75631fbaefxxxx",
                "SparkGroupId": "85",
                "TaskType": "SparkSQLTask",
                "State": 2,
                "OperateUin": "1000****1923",
                "SQL": "select * from tpcds_sql_orc.store_sales limit 100000",
                "IsSQLCutOff": false,
                "UserAlias": "user1",
                "UiUrl": "https://dlc-spark-ui.chongqing.cloud.tencent.com/history/spark-*/none/xx/SQL/?group=xx",
                "DataEngineId": "DataEngine-12341",
                "DataEngineName": "super_spark_270",
                "InstanceStartTime": 1733842361290,
                "InstanceCompleteTime": 1733842401892,
                "SQLStartTime": 1733842364672,
                "StageStartTime": 1733842364683,
                "StageEndTime": 1733842400272,
                "JobTimeSum": 35589,
                "TaskTimeSum": 403,
                "WaitExecuteTime": 4118,
                "WaitTime": 3393,
                "QueryResultTime": 141,
                "InputRecordsSum": 49049600,
                "InputBytesSum": 20648020108,
                "OutputRecordsSum": 100000,
                "OutputBytesSum": 14638477,
                "ShuffleReadBytesSum": 0,
                "ShuffleReadRecordsSum": 0,
                "Suggestions": "[]",
                "SuggestionsEng": "[]",
                "AnalysisStatus": "[\"SPARK-OutputSmallFile\"]",
                "AnalysisStatusType": 1,
                "OutputFilesNum": 0,
                "OutputSmallFilesNum": 0,
                "CommonMetrics": {
                    "CreateTaskTime": null,
                    "ProcessTime": 95,
                    "QueueTime": 0,
                    "ExecutionTime": 39707,
                    "IsResultCacheHit": false,
                    "MatchedMVBytes": null,
                    "MatchedMVs": null,
                    "AffectedBytes": "14638477",
                    "AffectedRows": 100000,
                    "ProcessedBytes": 20648020108,
                    "ProcessedRows": 49049600,
                    "QueryResultTime": 141
                }
            }
        ],
        "TotalCount": 1
    }
}
```

