**Example 1: 工作流任务运行详情列表**



Input: 

```
tccli wedata ListTriggerTaskRuns --cli-unfold-argument  \
    --ProjectId 3149092944204222464 \
    --Filters.0.Name Keyword \
    --Filters.0.Values 20260206114443865 \
    --OrderFields.0.Name ScheduleTime \
    --OrderFields.0.Direction DESC \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "ErrorCodeStr": "runner exec wedata err",
                    "ExecuteUserUin": "700001893691",
                    "ExecutionEndTime": "1771987842000",
                    "ExecutionId": "f68e0637-6b3d-48a7-8326-dd456009c5da",
                    "ExecutionStartTime": "1771987841000",
                    "ExecutionTime": "1000",
                    "IsLatestExecution": false,
                    "RerunTimes": 0,
                    "RetryTimes": 0,
                    "ScheduleTime": "1771987837144",
                    "TaskExecutionState": "FAILED",
                    "TaskId": "20260206114443865",
                    "TaskName": "t_wf_skip_A_tnsd",
                    "TriggerType": "Manual",
                    "WaitTime": "3839",
                    "WorkflowExecutionId": "16752a77-f4fa-4107-bf15-eb4f35537d0c",
                    "WorkflowId": "7483e714-6607-47c5-887a-1f40996051c6",
                    "WorkflowName": "t_wf_skip_8szRR2"
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalCount": 8,
            "TotalPageNumber": 8
        },
        "RequestId": "54561345-8717-488d-b325-991be2c2f083"
    }
}
```

