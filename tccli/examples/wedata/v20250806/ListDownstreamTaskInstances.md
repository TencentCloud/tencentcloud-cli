**Example 1: 获取任务的直接下游**



Input: 

```
tccli wedata ListDownstreamTaskInstances --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --InstanceKey 20250708114505208_2025-08-26 00:00:00 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CostTime": 0,
                    "CurRunDate": "2025-08-27 01:00:00",
                    "CycleType": "HOUR_CYCLE",
                    "EndTime": "2025-08-27 02:00:12",
                    "ExecutorGroupId": "20240222212719833743",
                    "ExecutorGroupName": "qfh_test",
                    "FolderId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                    "FolderName": "carlshi",
                    "InstanceKey": "20250708114842380_2025-08-27 01:00:00",
                    "InstanceState": "EXPIRED",
                    "InstanceType": 1,
                    "LastUpdateTime": "2025-08-27 02:00:15",
                    "OwnerUinList": [],
                    "ProjectId": "1460947878944567296",
                    "SchedulerTime": "2025-08-27 01:00:00",
                    "StartTime": null,
                    "TaskId": "20250708114842380",
                    "TaskName": "son_hour",
                    "TaskType": "Shell",
                    "TaskTypeId": 35,
                    "TotalRunNum": 0,
                    "Tries": 0,
                    "TryLimit": 5,
                    "WorkflowId": "b8f62e8b-5484-4810-aff7-3815e5abcb0c",
                    "WorkflowName": "zd10"
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalCount": 24,
            "TotalPageNumber": 24
        },
        "RequestId": "be421bc2-c9cd-4abd-94ed-4069df5708f7"
    }
}
```

