**Example 1: 查询任务列表**

查询任务列表

Input: 

```
tccli dlc DescribeTasks --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --Filters.0.Name task-type \
    --Filters.0.Values GovernSparkSQLTask GovernSparkBatchTask StandardGovernSparkSQLTask \
    --SortBy create-time  \
    --Sorting desc  \
    --StartTime 2024-01-15 00:00:00 \
    --EndTime 2025-01-16 23:59:59 \
    --DataEngineName  \
    --ResourceGroupName 
```

Output: 
```
{
    "Response": {
        "RequestId": "3a392e14-0f96-4069-8426-8ee75c4fcb1a",
        "TaskList": [
            {
                "Id": "Autotask-xxxx",
                "DatabaseName": "dlc-db",
                "SQLType": "OTHER",
                "SQL": "{\n \"Catalog\": \"DataLakeCatalog\",\n \"Database\": \"dlc-db\",\n \"Table\": \"term\",\n \"Arguments\": [\n {\n \"Key\": \"age\",\n \"Value\": \"18\"\n },\n {\n \"Key\": \"max\",\n \"Value\": \"30\"\n }\n ]\n}",
                "DataAmount": 0,
                "UsedTime": 0,
                "TotalTime": 0,
                "OutputPath": "",
                "RowAffectInfo": "",
                "ResultExpired": false,
                "State": 0,
                "CreateTime": "1736997039696",
                "UpdateTime": "1736997039696",
                "DataSet": "",
                "Error": "",
                "OutputMessage": "",
                "Percentage": 0,
                "TaskType": "GovernSparkBatchTask",
                "ProgressDetail": "",
                "OperateUin": "100015157500",
                "DataEngineId": "DataEngine-6****9",
                "DataEngineName": "dlc-db",
                "ResourceGroupName": "",
                "ImageVersion": "Spark 3.2",
                "InputType": "",
                "InputConf": "",
                "DataNumber": 0,
                "CanDownload": false,
                "UserAlias": "xiaoming",
                "SparkJobName": "",
                "SparkJobId": "",
                "SparkJobFile": "",
                "UiUrl": "",
                "CmdArgs": "",
                "CommonMetrics": null,
                "SparkMonitorMetrics": null,
                "PrestoMonitorMetrics": null,
                "DriverSize": "",
                "ExecutorSize": "",
                "ExecutorNums": 0,
                "ExecutorMaxNumbers": 0,
                "ResultFormat": "",
                "EngineTypeDetail": "SparkBatch"
            }
        ],
        "TasksOverview": {
            "TaskQueuedCount": 0,
            "TaskInitCount": 0,
            "TaskRunningCount": 0,
            "TotalTaskCount": 0
        },
        "TotalCount": 118429
    }
}
```

