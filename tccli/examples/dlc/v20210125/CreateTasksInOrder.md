**Example 1: 按顺序创建任务**

按顺序创建任务

Input: 

```
tccli dlc CreateTasksInOrder --cli-unfold-argument  \
    --Tasks.TaskType SQLTask \
    --Tasks.SQL U0VMRUNUICogRlJPTSBgdGVzdGh5d2AuYHRlc3QxMDBtYCBMSU1JVCAxMDs= \
    --Tasks.Config.0.Key  \
    --Tasks.Config.0.Value  \
    --Tasks.FailureTolerance Proceed \
    --DatabaseName testdb \
    --DatasourceConnectionName COSDataCatalog
```

Output: 
```
{
    "Response": {
        "BatchId": "batch-8n7l3qny",
        "RequestId": "6a61ed18-e2ee-496b-8c04-f65b4edd9721",
        "TaskIdSet": [
            "640ae8ea-5189-4603-9c57-abad74fba93c"
        ]
    }
}
```

