**Example 1: 获取任务详情**



Input: 

```
tccli wedata GetTaskInstance --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --InstanceKey 20250714200130106_2025-10-01 00:00:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "CostTime": 3000,
            "CurRunDate": "2025-10-01 00:00:00",
            "CycleType": "MONTH_CYCLE",
            "EndTime": "2025-08-27 22:24:40",
            "ExecutorGroupId": "20240222212719833743",
            "ExecutorGroupName": "qfh_test",
            "FolderId": "a1eb11e9-6f1a-11ed-8909-bc97e105ba60",
            "FolderName": "u9ed8u8ba4u6587u4ef6u5939",
            "InstanceKey": "20250714200130106_2025-10-01 00:00:00",
            "InstanceState": "COMPLETED",
            "InstanceType": 0,
            "JobErrorMsg": "",
            "LastUpdateTime": "2025-08-27 22:24:44",
            "OwnerUinList": [
                "100039182306"
            ],
            "ProjectId": "1460947878944567296",
            "SchedulerTime": "2025-10-01 00:00:00",
            "StartTime": "2025-08-27 22:24:37",
            "TaskId": "20250714200130106",
            "TaskName": "u8c03u5ea6u53c2u6570u6d4bu8bd51",
            "TaskType": "Shell",
            "TaskTypeId": 35,
            "TotalRunNum": 10,
            "Tries": 1,
            "TryLimit": 5,
            "WorkflowId": "1f0911b9-032e-4e4f-a564-69e4b871d7e2",
            "WorkflowName": "u8c03u5ea6u53c2u6570u6d4bu8bd5"
        },
        "RequestId": "546eed85-388d-4e81-ad3f-28db7a619d18"
    }
}
```

