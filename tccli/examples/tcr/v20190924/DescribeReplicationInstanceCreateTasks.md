**Example 1: 查询创建从实例任务状态**



Input: 

```
tccli tcr DescribeReplicationInstanceCreateTasks --cli-unfold-argument  \
    --ReplicationRegistryId tcr-dg284imq-5-os5gcu \
    --ReplicationRegionId 5
```

Output: 
```
{
    "Response": {
        "RequestId": "72c8900b-f23e-42b3-9281-828a42d590a4",
        "Status": "SUCCESS",
        "TaskDetail": [
            {
                "CreatedTime": "2025-01-02T15:10:06+08:00",
                "FinishedTime": "2025-01-02T15:10:12+08:00",
                "TaskMessage": "",
                "TaskName": "SyncDBTask",
                "TaskStatus": "SUCCESS",
                "TaskUUID": "tcr-task-tcr-dg284imq-5-os5gcu-a152a2ca-2aee-4356-8bd9-09eea73c5c0a"
            },
            {
                "CreatedTime": "2025-01-02T15:10:06+08:00",
                "FinishedTime": "2025-01-02T15:10:12+08:00",
                "TaskMessage": "",
                "TaskName": "CreateTcrCrdTask",
                "TaskStatus": "SUCCESS",
                "TaskUUID": "tcr-task-tcr-dg284imq-5-os5gcu-d2c2b630-9417-44ea-b056-992de3289f90"
            }
        ]
    }
}
```

