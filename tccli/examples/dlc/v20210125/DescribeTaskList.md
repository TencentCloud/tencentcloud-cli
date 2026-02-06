**Example 1: DescribleTasks接口示例**



Input: 

```
tccli dlc DescribeTaskList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 10 \
    --Filters.0.Name task-id \
    --Filters.0.Values 3434747dfe5911efadef76cfa258de8c
```

Output: 
```
{
    "Response": {
        "RequestId": "f337202f-4b7a-4ae6-a976-64196f1b818e",
        "TaskList": [
            {
                "AnalysisStatusType": 0,
                "CanDownload": false,
                "CmdArgs": "",
                "CommonMetrics": null,
                "CreateTime": "1741694628056",
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
                "EngineHasListenerConfig": false,
                "EngineType": "",
                "EngineTypeDetail": "SparkSQL",
                "Error": "",
                "ExecutorMaxNumbers": 0,
                "ExecutorNums": 0,
                "ExecutorSize": "",
                "Id": "e39b2b73fe7011ef852f5254007d4e2c",
                "ImageVersion": "SuperSQL-S 3.5",
                "InputConf": "",
                "InputRecordsSum": 0,
                "InputType": "",
                "OperateUin": "100017140401",
                "OutputBytesSum": 1049893,
                "OutputFilesNum": 1,
                "OutputMessage": "",
                "OutputPath": "lakefs://6000000186bb9b4e5d6a01f0bab6dc05c73b2c64995d45690e45cbc6ec2e36703bafdc3a@dlca10f-100017140401-1739416252-100040138245-1333670961/1304581893/.system/result/20250311/e39b2b73fe7011ef852f5254007d4e2c/",
                "OutputRecordsSum": 10,
                "OutputSmallFilesNum": 1,
                "Percentage": 100,
                "PrestoMonitorMetrics": null,
                "ProgressDetail": "[{\"jobId\":\"1\",\"stages\":[{\"stageId\":\"1\",\"schedule\":1},{\"stageId\":\"2\",\"schedule\":1}],\"jobState\":\"SUCCEEDED\",\"totalTime\":2728,\"firstLaunchTime\":1741694751313},{\"jobId\":\"0\",\"stages\":[{\"stageId\":\"0\",\"schedule\":1}],\"jobState\":\"SUCCEEDED\",\"totalTime\":5934,\"firstLaunchTime\":1741694749494}]",
                "ResourceGroupId": "",
                "ResourceGroupName": "",
                "ResultExpired": false,
                "ResultFormat": "csv",
                "RowAffectInfo": "10 rows affected (11.542000 seconds)",
                "SQL": "INSERT INTO `f284_database_thea`.`optimize_iceberg_native_table_1` VALUES (int(current_timestamp())+1,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+2,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+3,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+4,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+5,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+6,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+7,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+8,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+9,'optimize_iceberg_native_table_1数据写入',current_timestamp()),(int(current_timestamp())+10,'optimize_iceberg_native_table_1数据写入',current_timestamp())",
                "SQLType": "DML",
                "ShuffleReadBytesSum": 1021,
                "ShuffleReadRecordsSum": 10,
                "Source": "dataExploration",
                "SourceExtra": "",
                "SparkAppId": "",
                "SparkJobFile": "",
                "SparkJobId": "",
                "SparkJobName": "",
                "SparkMonitorMetrics": null,
                "StageStartTime": 1741694749494,
                "State": 2,
                "TaskCategory": "SQL",
                "TaskName": "sql_query_20250311200348_c806d895",
                "TaskTimeSum": 8,
                "TaskType": "SparkSQLTask",
                "TotalTime": 128454,
                "UiUrl": "http://11.142.253.112/history/spark-5d3e75773a2d4d979e8ac93f5b590ba0/none/0/SQL/?group=0",
                "UpdateTime": "1741694756510",
                "UsedTime": 4541,
                "UserAlias": "100017140401"
            }
        ],
        "TotalCount": 1420
    }
}
```

