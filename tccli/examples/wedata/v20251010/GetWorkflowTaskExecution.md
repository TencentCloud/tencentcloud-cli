**Example 1: 查询工作流运行详情**



Input: 

```
tccli wedata GetWorkflowTaskExecution --cli-unfold-argument  \
    --WorkspaceId 1 \
    --WorkflowExecutionId exec_1001
```

Output: 
```
{
    "Response": {
        "Data": {
            "BizStateEnumInfos": [
                {
                    "Count": 1,
                    "LabelKey": "TERMINATING",
                    "LabelValue": "正在终止"
                }
            ],
            "TaskExecutions": [
                {
                    "CreateTime": "1700000001100",
                    "CreateUin": "creator_1",
                    "DependOnList": [],
                    "DependenceFinishedTime": "1700000001300",
                    "ErrorCodeStr": "ManualTerminated",
                    "ExecuteUserName": "",
                    "ExecuteUserUin": "user1",
                    "ExecutionEndTime": "1700000001600",
                    "ExecutionId": "t_exec_1001_1",
                    "ExecutionStartTime": "1700000001500",
                    "ExecutionState": "TERMINATING",
                    "ExecutionTime": "1300",
                    "IsLatestExecution": true,
                    "IssueTime": "1700000001400",
                    "JobId": "job_exec_1001_task1",
                    "RerunTimes": 0,
                    "ResourceGroupId": "rg_01",
                    "ResourceGroupInfoList": [],
                    "RetryTimes": 0,
                    "RunParams": "{\"param1\":\"A\"}",
                    "TaskId": "task1",
                    "TaskName": "Task One",
                    "TaskTypeExtensions": "{\"param1\":\"A\"}",
                    "TaskTypeName": "Shell",
                    "TaskVersionId": "ver_t1",
                    "TimeZone": "",
                    "TriggerType": "Scheduler",
                    "UpdateTime": "1764734794605",
                    "WaitTime": "0",
                    "WorkflowExecutionId": "exec_1001",
                    "WorkflowId": "wf_01",
                    "WorkflowName": "",
                    "WorkspaceId": "1"
                }
            ],
            "WorkflowExecution": {
                "AppId": "1300055887",
                "CreateTime": "1761743406000",
                "EndTime": "1761747006000",
                "ErrorCodeStr": "",
                "ExecuteUserName": "",
                "ExecuteUserUin": "700002164618",
                "ExecutionCostTime": "1500",
                "ExecutionEndTime": "1700000005000",
                "ExecutionId": "exec_1001",
                "ExecutionStartTime": "1700000002000",
                "ExecutionState": "SUCCESS",
                "PendingCostTime": "3",
                "PendingStartTime": "1700000007000",
                "QueueCostTime": "13",
                "QueueStartTime": "1700000006500",
                "RerunTimes": 0,
                "ResourceGroupIds": [
                    "rg_01"
                ],
                "ResourceGroupInfoList": [],
                "SelectedTaskIds": [
                    "task1",
                    "task2"
                ],
                "SupportRerun": true,
                "TriggerType": "Scheduler",
                "WorkflowId": "wf_01",
                "WorkflowName": "maxxx_205517",
                "WorkflowParams": "{\"customer_id\":\"A1\",\"priority\":\"high\"}",
                "WorkflowVersionId": "ver_01",
                "WorkspaceId": "1"
            }
        },
        "RequestId": "0007ed3a-4688-4588-ac71-1ba1429ac09c"
    }
}
```

