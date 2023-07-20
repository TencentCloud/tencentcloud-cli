**Example 1: 查询任务列表**

查询任务列表

Input: 

```
tccli dlc DescribeTasks --cli-unfold-argument  \
    --Limit 0 \
    --Offset 0 \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --SortBy abc \
    --Sorting abc \
    --StartTime abc \
    --EndTime abc \
    --DataEngineName abc
```

Output: 
```
{
    "Response": {
        "TaskList": [
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
        "TotalCount": 1,
        "TasksOverview": {
            "TaskQueuedCount": 0,
            "TaskInitCount": 0,
            "TaskRunningCount": 0,
            "TotalTaskCount": 0
        },
        "RequestId": "abc"
    }
}
```

