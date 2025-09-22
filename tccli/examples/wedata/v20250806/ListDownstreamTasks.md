**Example 1: 成功示例**



Input: 

```
tccli wedata ListDownstreamTasks --cli-unfold-argument  \
    --TaskId 20250723102628422 \
    --ProjectId 1464962169590902784 \
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
                    "EndTime": "2100-01-01 23:59:59",
                    "InitStrategy": "T+0",
                    "OwnerUin": "100028578753",
                    "ProjectId": "1464962169590902784",
                    "ScheduleDesc": "0 0 0 * * ?",
                    "StartTime": "2025-07-25 00:00:00",
                    "Status": "Y",
                    "TaskAction": "",
                    "TaskId": "20250723102549746",
                    "TaskName": "test_shell_0723",
                    "TaskTypeDesc": "Shell",
                    "TaskTypeId": 35,
                    "WorkflowId": "6754d9ac-caf9-4278-a339-0d0f0d2e9dbd",
                    "WorkflowName": "test_0799"
                }
            ],
            "PageNumber": 1,
            "PageSize": 20,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "c6a00c6d-b3e7-48aa-9a08-7d3264fd1aa0"
    }
}
```

