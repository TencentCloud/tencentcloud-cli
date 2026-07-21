**Example 1: MCP 任务示例**



Input: 

```
tccli dlc DescribeMCPTask --cli-unfold-argument  \
    --TaskId **
```

Output: 
```
{
    "Response": {
        "TaskInfo": {
            "BatchId": "batch-1234567890",
            "CreateTime": "2026-07-16 10:00:00",
            "DataEngineId": "DataEngine-mock-001",
            "DataSet": "[[\"col1\",\"col2\"],[\"value1\",\"value2\"]]",
            "DatabaseName": "mock_database",
            "EndTime": "2026-07-16 10:00:10",
            "EngineTypeDetail": "SparkSQL",
            "Id": "11",
            "IsSQLCutOff": false,
            "OperateUin": "100000000001",
            "OutputMessage": "Mock task completed successfully",
            "Progress": 100,
            "ResourceGroupName": "mock_resource_group",
            "SQL": "SELECT * FROM db.table LIMIT 10",
            "SQLType": "DQL",
            "SparkJobId": "spark-job-mock-001",
            "SparkJobName": "mock_spark_job",
            "StartTime": "2026-07-16 10:00:01",
            "State": 2,
            "TaskKind": "SQLTask",
            "TaskType": "SQLTask",
            "TotalTime": 9500,
            "UpdateTime": "2026-07-16 10:00:10",
            "UsedTime": 9000
        },
        "RequestId": "88d52c8f-5baf-4d42-afa7-73bbe0aa7198"
    }
}
```

