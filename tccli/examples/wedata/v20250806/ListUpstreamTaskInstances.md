**Example 1: 获取任务实例的直接上游**



Input: 

```
tccli wedata ListUpstreamTaskInstances --cli-unfold-argument  \
    --ProjectId 2428908825624145920 \
    --InstanceKey 20250828163920570_2025-08-28 16:40:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CostTime": 0,
                    "CurRunDate": "2025-08-28 16:40:00",
                    "CycleType": "MINUTE_CYCLE",
                    "EndTime": null,
                    "ExecutorGroupId": "20240227210859451466",
                    "ExecutorGroupName": "u6267u884cu5e73u53f0u6d4bu8bd5u4e13u7528-worker",
                    "FolderId": "6067bd9d-83ea-11f0-8c70-043f72d4907c",
                    "FolderName": "yukittzhang",
                    "InstanceKey": "20250828163904071_2025-08-28 16:40:00",
                    "InstanceState": "WAIT_RUN",
                    "InstanceType": 1,
                    "LastUpdateTime": "2025-08-28 16:40:02",
                    "OwnerUinList": [],
                    "ProjectId": "2428908825624145920",
                    "SchedulerTime": "2025-08-28 16:40:00",
                    "StartTime": null,
                    "TaskId": "20250828163904071",
                    "TaskName": "openapi_up",
                    "TaskType": "Shell",
                    "TaskTypeId": 35,
                    "TotalRunNum": 0,
                    "Tries": 0,
                    "TryLimit": 5,
                    "WorkflowId": "15b26760-b03d-43d8-be63-60a32e64fa01",
                    "WorkflowName": "2321R3"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 0
        },
        "RequestId": "70473087-7555-4f96-9404-ef8532211cc4"
    }
}
```

