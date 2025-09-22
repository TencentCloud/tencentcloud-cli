**Example 1: 成功示例**



Input: 

```
tccli wedata ListUpstreamTasks --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --TaskId 20250723102549746 \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CrontabExpression": "0 0 0 * * ?",
                    "CycleType": "C",
                    "DelayTime": null,
                    "EndTime": "2100-01-01 03:59:59",
                    "InitStrategy": "T+0",
                    "OwnerUin": "100028578753",
                    "ProjectId": "1464962169590902784",
                    "ScheduleDesc": null,
                    "StartTime": "2025-07-25 04:00:00",
                    "Status": "O",
                    "TaskAction": "",
                    "TaskId": "20250724155107573",
                    "TaskName": "test_shell_0723_copy_copy",
                    "TaskTypeDesc": "Shell",
                    "TaskTypeId": 35,
                    "WorkflowId": "6754d9ac-caf9-4278-a339-0d0f0d2e9dbd",
                    "WorkflowName": "test_0799"
                }
            ],
            "PageNumber": 1,
            "PageSize": 20,
            "TotalCount": 2,
            "TotalPageNumber": 1
        },
        "RequestId": "4f60a917-a570-496e-b618-1f21323d172d"
    }
}
```

