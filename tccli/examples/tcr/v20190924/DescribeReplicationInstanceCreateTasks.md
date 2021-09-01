**Example 1: 查询创建从实例任务状态**



Input: 

```
tccli tcr DescribeReplicationInstanceCreateTasks --cli-unfold-argument  \
    --ReplicationRegistryId tcr-ak9876-5 \
    --ReplicationRegionId 5
```

Output: 
```
{
    "Response": {
        "TaskDetail": [
            {
                "TaskName": "SyncMasterDBTask",
                "TaskUUID": "tcr-task-3765025c-b063-4d38-be45-52e47b2c5795",
                "TaskStatus": "SUCCESS",
                "TaskMessage": "",
                "CreatedTime": "xx",
                "FinishedTime": "xx"
            },
            {
                "TaskName": "SyncMasterBucketTask",
                "TaskUUID": "tcr-task-d008eec3-c6a0-41b1-b171-409e06fff024",
                "TaskStatus": "SUCCESS",
                "TaskMessage": "",
                "CreatedTime": "xx",
                "FinishedTime": "xx"
            },
            {
                "TaskName": "CreateTcrCrdTask",
                "TaskUUID": "tcr-task-335e5a7b-b3e4-49ff-b4c3-9f81a6afac0d",
                "TaskStatus": "SUCCESS",
                "TaskMessage": "",
                "CreatedTime": "xx",
                "FinishedTime": "xx"
            }
        ],
        "Status": "SUCCESS",
        "RequestId": "5c497866-b88c-48c8-895d-0aba37109640"
    }
}
```

