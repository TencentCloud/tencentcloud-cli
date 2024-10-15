**Example 1: 洞察分析列表**



Input: 

```
tccli dlc DescribeTasksAnalysis --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TaskList": [
            {
                "Id": "abc",
                "InstanceStartTime": 0,
                "InstanceCompleteTime": 0,
                "State": 0,
                "SQL": "abc",
                "IsSQLCutOff": true,
                "DataEngineId": "abc",
                "DataEngineName": "abc",
                "OperateUin": "abc",
                "UserAlias": "abc",
                "UiUrl": "abc",
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
                    "ProcessedRows": 0,
                    "QueryResultTime": 0
                },
                "SparkAppId": "abc",
                "SparkGroupId": "abc",
                "StageStartTime": 0,
                "StageEndTime": 0,
                "JobTimeSum": 0,
                "TaskTimeSum": 0,
                "InputRecordsSum": 0,
                "InputBytesSum": 0,
                "OutputRecordsSum": 0,
                "OutputBytesSum": 0,
                "ShuffleReadBytesSum": 0,
                "ShuffleReadRecordsSum": 0,
                "Suggestions": "abc",
                "SuggestionsEng": "abc",
                "AnalysisStatus": "abc",
                "AnalysisStatusType": 0,
                "TaskType": "abc",
                "SQLStartTime": 0,
                "WaitExecuteTime": 0,
                "WaitTime": 0,
                "QueryResultTime": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

