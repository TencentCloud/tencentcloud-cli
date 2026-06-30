**Example 1: DescribeTaskDetail接口示例**



Input: 

```
tccli dlc DescribeTaskDetail --cli-unfold-argument  \
    --TaskInstanceId da2334b3fe7211ef852f5254007d4e2c
```

Output: 
```
{
    "Response": {
        "RequestId": "c20fc817-3e5b-46e4-91d3-3f43db345a38",
        "TaskDetail": {
            "AnalysisStatusType": 0,
            "CanDownload": false,
            "CmdArgs": "",
            "CommonMetrics": {
                "AffectedBytes": "1049893",
                "AffectedRows": 10,
                "CreateTaskTime": 105,
                "ExecutionTime": 1579,
                "IsResultCacheHit": false,
                "MatchedMVBytes": null,
                "MatchedMVs": null,
                "ProcessTime": 107,
                "ProcessedBytes": 0,
                "ProcessedRows": 0,
                "QueueTime": 0
            },
            "CreateTime": "1741695471200",
            "CreatorAlias": "100017140401",
            "CreatorUin": "100017140401",
            "CustomizedConf": "",
            "DataAmount": 0,
            "DataEngineId": "DataEngine-iwcrcjq1",
            "DataEngineName": "super_spark",
            "DataNumber": 0,
            "DataSet": "",
            "DatabaseName": "",
            "DriverSize": "",
            "EngineHasListenerConfig": true,
            "EngineType": "spark",
            "EngineTypeDetail": "SparkSQL",
            "Error": "",
            "ExecutorMaxNumbers": 0,
            "ExecutorNums": 0,
            "ExecutorSize": "",
            "Id": "da2334b3fe7211ef852f5254007d4e2c",
            "ImageVersion": "SuperSQL-S 3.5",
            "InputConf": "",
            "InputRecordsSum": 0,
            "InputType": "",
            "OperateUin": "100017140401",
            "OutputBytesSum": 1049893,
            "OutputFilesNum": 1,
            "OutputMessage": "",
            "OutputPath": "lakefs://6000000186bb9b4e5d6a01f0bab6dc05c73b2c64995d45690e45cbc6ec2e36703bafdc3a@dlca10f-100017140401-1739416252-100040138245-1333670961/1304581893/.system/result/20250311/da2334b3fe7211ef852f5254007d4e2c/",
            "OutputRecordsSum": 10,
            "OutputSmallFilesNum": 1,
            "Percentage": 100,
            "PrestoMonitorMetrics": null,
            "ProgressDetail": "[{\"jobId\":\"1\",\"stages\":[{\"stageId\":\"1\",\"schedule\":1},{\"stageId\":\"2\",\"schedule\":1}],\"jobState\":\"SUCCEEDED\",\"totalTime\":217,\"firstLaunchTime\":1741695471813},{\"jobId\":\"0\",\"stages\":[{\"stageId\":\"0\",\"schedule\":1}],\"jobState\":\"SUCCEEDED\",\"totalTime\":88,\"firstLaunchTime\":1741695471753}]",
            "ResourceGroupId": "",
            "ResourceGroupName": "",
            "ResultExpired": false,
            "ResultFormat": "csv",
            "RowAffectInfo": "10 rows affected (1.579000 seconds)",
            "SQL": "INSERT INTO `f284_database_thea`.`optimize_iceberg_native_table_1` VALUES (int(current_timestamp())+1,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+2,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+3,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+4,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+5,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+6,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+7,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+8,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+9,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+10,'optimize_iceberg_native_table_1数据写入',current_timestamp())",
            "SQLType": "DML",
            "ShuffleReadBytesSum": 1230,
            "ShuffleReadRecordsSum": 10,
            "Source": "dataExploration",
            "SourceExtra": "",
            "SparkAppId": "",
            "SparkJobFile": "",
            "SparkJobId": "",
            "SparkJobName": "",
            "SparkMonitorMetrics": null,
            "StageStartTime": 1741695471753,
            "State": 2,
            "TaskCategory": "SQL",
            "TaskName": "sql_query_20250311201751_1fc9dd4a",
            "TaskTimeSum": 0,
            "TaskType": "SparkSQLTask",
            "TotalTime": 2667,
            "UiUrl": "http://11.142.253.112/history/spark-5d3e75773a2d4d979e8ac93f5b590ba0/none/10/SQL/?group=10",
            "UpdateTime": "1741695473867",
            "UsedTime": 281,
            "UserAlias": "100017140401"
        }
    }
}
```

