**Example 1: dev_test**



Input: 

```
tccli wedata GetTaskExecution --cli-unfold-argument  \
    --WorkspaceId 1 \
    --TaskExecutionId t_exec_1001_1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "1700000001100",
            "CreateUin": "creator_1",
            "DependenceFinishedTime": "1700000001300",
            "ErrorCodeStr": "ManualTerminated",
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
            "RetryTimes": 0,
            "RunParams": "{\"param1\":\"A\"}",
            "TaskId": "task1",
            "TaskName": "Task One",
            "TaskTypeExtensions": "{\"param1\":\"A\"}",
            "TaskTypeName": "Shell",
            "TaskVersionId": "ver_t1",
            "TriggerType": "Scheduler",
            "UpdateTime": "1764734794605",
            "WaitTime": "0",
            "WorkflowExecutionId": "exec_1001",
            "WorkflowId": "wf_01",
            "WorkflowName": "maxxx_205517",
            "WorkspaceId": "1"
        },
        "RequestId": "f51d205a-34d4-49e3-b846-4c3521d49d0c"
    }
}
```

