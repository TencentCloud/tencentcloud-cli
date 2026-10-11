**Example 1: 查询作业详情**



Input: 

```
tccli dlc DescribeJobDetail --cli-unfold-argument  \
    --JobId job-9f3a2b1c
```

Output: 
```
{
    "Response": {
        "JobDetail": {
            "JobId": "job-9f3a2b1c",
            "JobName": "spark-sql-demo",
            "CreatorSubUin": "700281534962",
            "State": "SUCCEEDED",
            "MajorType": "SPARK",
            "MinorType": "SPARK_SQL",
            "RunMode": "WAREHOUSE",
            "WarehouseId": "wh-8f21c3",
            "PartitionCode": "dlc-p-nwruuglc",
            "PartitionName": "spark-demo-partition",
            "QueueName": "root.default",
            "CheckpointLocation": "cosn://demo-bucket/checkpoints/demo_stream",
            "CreateTime": 1767256876123,
            "SubmitTime": 1767256876123,
            "FinishTime": 1767256876123,
            "RunningTimeMs": 900000,
            "WarehouseName": "spark-warehouse",
            "FlowId": "flow-2a9c4e",
            "ExecutionId": "exec-6f1b83",
            "JobSource": "手动触发",
            "WaitingTimeMs": 900000,
            "HistoryUrl": "https://spark-history.demo/job-9f3a2b1c",
            "ErrorMessage": "详见作业日志",
            "CustomProperties": "{\"spark.executor.memory\":\"4g\"}",
            "EnvVars": [
                {
                    "Key": "spark.executor.memory",
                    "Value": "4g"
                }
            ],
            "RuntimeCode": "spark-3.5.5",
            "RuntimeName": "Spark 3.5.5",
            "SysCatalogVersion": "TCCATALOG"
        },
        "RequestId": "f4a1c9b2-7d3e-4a58-9c62-1e8b5d7a2f43"
    }
}
```

