**Example 1: 获取迁移任务列表**



Input: 

```
tccli trocket DescribeSmoothMigrationTaskList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "TotalCount": 10,
        "Data": [
            {
                "TaskId": "28deebbb-d489-471e-bb21-69fab50aed36",
                "TaskName": "test-task",
                "SourceClusterName": "source-cluster",
                "InstanceId": "rmq-1gabcde",
                "ConnectionType": "VPC",
                "SourceNameServer": "1.1.1.1:9876",
                "TaskStatus": "ServiceMigration",
                "InstanceVersion": "5"
            }
        ],
        "RequestId": "9b299610-7402-47d3-91d1-f012faf13929"
    }
}
```

