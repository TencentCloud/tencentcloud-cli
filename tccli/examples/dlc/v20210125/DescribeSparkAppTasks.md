**Example 1: 查询Spark作业的运行任务列表**

查询Spark作业的运行任务列表

Input: 

```
tccli dlc DescribeSparkAppTasks --cli-unfold-argument  \
    --JobId batch_133e005d-6486-4517-8ea7-b6b97b183a6b \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Tasks": {
            "DatabaseName": "my_database",
            "DataAmount": 1000,
            "Id": "task_001",
            "UsedTime": 120,
            "OutputPath": "/data/output/",
            "CreateTime": "2025-01-13T12:00:00Z",
            "State": 1,
            "SQLType": "SELECT",
            "SQL": "SELECT * FROM my_table;",
            "ResultExpired": false,
            "RowAffectInfo": "100 rows affected",
            "DataSet": "my_data_set",
            "Error": "",
            "Percentage": 75,
            "OutputMessage": "Task completed",
            "TaskType": "DataProcessing",
            "ProgressDetail": "75% complete",
            "UpdateTime": "2025-01-13T13:00:00Z",
            "DataEngineId": "engine_01",
            "OperateUin": "user_123",
            "DataEngineName": "Spark Engine",
            "InputType": "CSV",
            "InputConf": "/config/input.csv",
            "DataNumber": 5000,
            "CanDownload": true,
            "UserAlias": "john_doe",
            "SparkJobName": "data_processing_job",
            "SparkJobId": "job_001",
            "SparkJobFile": "/jobs/job_001.jar",
            "UiUrl": "https://mydashboard.com/job_001",
            "TotalTime": 150,
            "CmdArgs": "--input /data/input.csv --output /data/output/",
            "ImageVersion": "1.0.0",
            "DriverSize": "large",
            "ExecutorSize": "medium",
            "ExecutorNums": 4,
            "ExecutorMaxNumbers": 10,
            "CommonMetrics": {
                "CreateTaskTime": 5,
                "ProcessTime": 100,
                "QueueTime": 10,
                "ExecutionTime": 120,
                "IsResultCacheHit": true,
                "MatchedMVBytes": 2048,
                "MatchedMVs": "2",
                "AffectedBytes": "11",
                "AffectedRows": 1000,
                "ProcessedBytes": 314572800,
                "ProcessedRows": 1000
            },
            "SparkMonitorMetrics": {
                "ShuffleWriteBytesCos": 500000,
                "ShuffleWriteBytesTotal": 1000000
            },
            "PrestoMonitorMetrics": {
                "LocalCacheHitRate": 95,
                "FragmentCacheHitRate": 90
            }
        },
        "TotalCount": 1,
        "SparkAppTasks": [
            {
                "DatabaseName": "my_database",
                "DataAmount": 1000,
                "Id": "task_001",
                "UsedTime": 120,
                "OutputPath": "/data/output/",
                "CreateTime": "2025-01-13T12:00:00Z",
                "State": 1,
                "SQLType": "SELECT",
                "SQL": "SELECT * FROM my_table;",
                "ResultExpired": false,
                "RowAffectInfo": "100 rows affected",
                "DataSet": "my_data_set",
                "Error": "",
                "Percentage": 75,
                "OutputMessage": "Task completed",
                "TaskType": "DataProcessing",
                "ProgressDetail": "75% complete",
                "UpdateTime": "2025-01-13T13:00:00Z",
                "DataEngineId": "engine_01",
                "OperateUin": "user_123",
                "DataEngineName": "Spark Engine",
                "InputType": "CSV",
                "InputConf": "/config/input.csv",
                "DataNumber": 5000,
                "CanDownload": true,
                "UserAlias": "john_doe",
                "SparkJobName": "data_processing_job",
                "SparkJobId": "job_001",
                "SparkJobFile": "/jobs/job_001.jar",
                "UiUrl": "https://mydashboard.com/job_001",
                "TotalTime": 150,
                "CmdArgs": "--input /data/input.csv --output /data/output/",
                "ImageVersion": "1.0.0",
                "DriverSize": "large",
                "ExecutorSize": "medium",
                "ExecutorNums": 4,
                "ExecutorMaxNumbers": 10,
                "CommonMetrics": {
                    "CreateTaskTime": 5,
                    "ProcessTime": 100,
                    "QueueTime": 10,
                    "ExecutionTime": 120,
                    "IsResultCacheHit": true,
                    "MatchedMVBytes": 2048,
                    "MatchedMVs": "2",
                    "AffectedBytes": "11",
                    "AffectedRows": 1000,
                    "ProcessedBytes": 314572800,
                    "ProcessedRows": 1000
                },
                "SparkMonitorMetrics": {
                    "ShuffleWriteBytesCos": 500000,
                    "ShuffleWriteBytesTotal": 1000000
                },
                "PrestoMonitorMetrics": {
                    "LocalCacheHitRate": 95,
                    "FragmentCacheHitRate": 90
                }
            }
        ],
        "RequestId": "dbb4e0d5-d07a-4c63-8af2-7ccd00b4ab90"
    }
}
```

