**Example 1: 批量创建并执行SQL任务**

批量创建并执行SQL任务

Input: 

```
tccli dlc CreateTasks --cli-unfold-argument  \
    --Tasks.TaskType SQLTask \
    --Tasks.SQL U0VMRUNUICogRlJPTSBgdGVzdGh5d2AuYHRlc3QxMDBtYCBMSU1JVCAxMDs= \
    --Tasks.Config.0.Key  \
    --Tasks.Config.0.Value  \
    --Tasks.FailureTolerance Proceed \
    --DatabaseName testdb \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "BatchId": "batch-45nyt3ee",
        "RequestId": "b577857e-041f-46c7-b5cf-4b3d3f50bc51",
        "TaskIdSet": [
            "e9663251-3a14-423a-b003-13c77c3fae11"
        ]
    }
}
```

