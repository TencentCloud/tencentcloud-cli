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
            "DatabaseName": "abc",
            "DataAmount": 0,
            "Id": "abc",
            "UsedTime": 0,
            "OutputPath": "abc",
            "CreateTime": "abc",
            "State": 0,
            "SQLType": "abc",
            "SQL": "abc",
            "ResultExpired": true,
            "RowAffectInfo": "abc",
            "DataSet": "abc",
            "Error": "abc",
            "Percentage": 0,
            "OutputMessage": "abc",
            "TaskType": "abc",
            "ProgressDetail": "abc",
            "UpdateTime": "abc",
            "DataEngineId": "abc",
            "OperateUin": "abc",
            "DataEngineName": "abc",
            "InputType": "abc",
            "InputConf": "abc",
            "DataNumber": 0,
            "CanDownload": true,
            "UserAlias": "abc",
            "SparkJobName": "abc",
            "SparkJobId": "abc",
            "SparkJobFile": "abc",
            "UiUrl": "abc",
            "TotalTime": 0,
            "CmdArgs": "abc",
            "ImageVersion": "abc",
            "DriverSize": "abc",
            "ExecutorSize": "abc",
            "ExecutorNums": 1,
            "ExecutorMaxNumbers": 1,
            "CommonMetrics": {
                "CreateTaskTime": 0,
                "ProcessTime": 0,
                "QueueTime": 0,
                "ExecutionTime": 0,
                "IsResultCacheHit": true,
                "MatchedMVBytes": 0,
                "MatchedMVs": "abc",
                "AffectedBytes": "abc",
                "AffectedRows": 0,
                "ProcessedBytes": 0,
                "ProcessedRows": 0
            },
            "SparkMonitorMetrics": {
                "ShuffleWriteBytesCos": 0,
                "ShuffleWriteBytesTotal": 0
            },
            "PrestoMonitorMetrics": {
                "LocalCacheHitRate": 0,
                "FragmentCacheHitRate": 0
            }
        },
        "TotalCount": 0,
        "SparkAppTasks": [
            {
                "DatabaseName": "abc",
                "DataAmount": 0,
                "Id": "abc",
                "UsedTime": 0,
                "OutputPath": "abc",
                "CreateTime": "abc",
                "State": 0,
                "SQLType": "abc",
                "SQL": "abc",
                "ResultExpired": true,
                "RowAffectInfo": "abc",
                "DataSet": "abc",
                "Error": "abc",
                "Percentage": 0,
                "OutputMessage": "abc",
                "TaskType": "abc",
                "ProgressDetail": "abc",
                "UpdateTime": "abc",
                "DataEngineId": "abc",
                "OperateUin": "abc",
                "DataEngineName": "abc",
                "InputType": "abc",
                "InputConf": "abc",
                "DataNumber": 0,
                "CanDownload": true,
                "UserAlias": "abc",
                "SparkJobName": "abc",
                "SparkJobId": "abc",
                "SparkJobFile": "abc",
                "UiUrl": "abc",
                "TotalTime": 0,
                "CmdArgs": "abc",
                "ImageVersion": "abc",
                "DriverSize": "abc",
                "ExecutorSize": "abc",
                "ExecutorNums": 1,
                "ExecutorMaxNumbers": 1,
                "CommonMetrics": {
                    "CreateTaskTime": 0,
                    "ProcessTime": 0,
                    "QueueTime": 0,
                    "ExecutionTime": 0,
                    "IsResultCacheHit": true,
                    "MatchedMVBytes": 0,
                    "MatchedMVs": "abc",
                    "AffectedBytes": "abc",
                    "AffectedRows": 0,
                    "ProcessedBytes": 0,
                    "ProcessedRows": 0
                },
                "SparkMonitorMetrics": {
                    "ShuffleWriteBytesCos": 0,
                    "ShuffleWriteBytesTotal": 0
                },
                "PrestoMonitorMetrics": {
                    "LocalCacheHitRate": 0,
                    "FragmentCacheHitRate": 0
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

