**Example 1: 查询工作流运行数量变化趋势图**



Input: 

```
tccli wedata GetWorkflowTaskExecutionHistogram --cli-unfold-argument  \
    --WorkflowId 98a029b598f604cde7fb1f0091c83ca320251031 \
    --WorkspaceId 1 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "TaskExecutions": [
                        {
                            "CreateTime": "1761650601562",
                            "CreateUin": "",
                            "DependOnList": [],
                            "ErrorCodeStr": "",
                            "ExecuteUserName": "",
                            "ExecuteUserUin": "",
                            "ExecutionId": "task_exec120251031",
                            "ExecutionState": "SUCCESS",
                            "IsLatestExecution": true,
                            "JobId": "120251031",
                            "RerunTimes": 0,
                            "ResourceGroupId": "1",
                            "ResourceGroupInfoList": [],
                            "RetryTimes": 0,
                            "RunParams": "",
                            "TaskId": "2d9edebc-f797-4d5d-bff9-2721a96b3829251031",
                            "TaskName": "task_nameA",
                            "TaskTypeExtensions": "",
                            "TaskTypeName": "",
                            "TaskVersionId": "4bc3c156-027e-4286-8d32-0a802e13f96420251031",
                            "TimeZone": "",
                            "TriggerType": "Manual",
                            "UpdateTime": "1761650601562",
                            "WorkflowExecutionId": "f9bae178ebb2a061f1ecc7d9ec9ce79520251031",
                            "WorkflowId": "98a029b598f604cde7fb1f0091c83ca320251031",
                            "WorkflowName": "",
                            "WorkspaceId": "1"
                        },
                        {
                            "CreateTime": "1761650601562",
                            "CreateUin": "",
                            "DependOnList": [],
                            "ErrorCodeStr": "",
                            "ExecuteUserName": "",
                            "ExecuteUserUin": "",
                            "ExecutionId": "task_exec220251031",
                            "ExecutionState": "SUCCESS",
                            "IsLatestExecution": true,
                            "JobId": "220251031",
                            "RerunTimes": 0,
                            "ResourceGroupId": "1",
                            "ResourceGroupInfoList": [],
                            "RetryTimes": 0,
                            "RunParams": "",
                            "TaskId": "c5e572e2-81e5-42b6-ba78-2973b1e69bf1251031",
                            "TaskName": "task_nameB",
                            "TaskTypeExtensions": "",
                            "TaskTypeName": "",
                            "TaskVersionId": "9b596b27-4f0f-44f5-a7f8-c695e80a9db720251031",
                            "TimeZone": "",
                            "TriggerType": "Manual",
                            "UpdateTime": "1761650601562",
                            "WorkflowExecutionId": "f9bae178ebb2a061f1ecc7d9ec9ce79520251031",
                            "WorkflowId": "98a029b598f604cde7fb1f0091c83ca320251031",
                            "WorkflowName": "",
                            "WorkspaceId": "1"
                        }
                    ],
                    "WorkflowExecution": {
                        "AppId": "1300055887",
                        "CreateTime": "1761605100005",
                        "EndTime": "1761747006000",
                        "ErrorCodeStr": "ActiveRunLimitExceeded",
                        "ExecuteUserName": "",
                        "ExecuteUserUin": "700002164618",
                        "ExecutionCostTime": "278",
                        "ExecutionEndTime": "1761657486000",
                        "ExecutionId": "f9bae178ebb2a061f1ecc7d9ec9ce79520251031",
                        "ExecutionStartTime": "1761653886456",
                        "ExecutionState": "FAILED",
                        "PendingCostTime": "390",
                        "PendingStartTime": "1761625086000",
                        "QueueCostTime": "501",
                        "QueueStartTime": "1761617886000",
                        "RerunTimes": 0,
                        "ResourceGroupIds": [],
                        "ResourceGroupInfoList": [],
                        "SelectedTaskIds": [],
                        "SupportRerun": false,
                        "TriggerType": "Scheduler",
                        "WorkflowId": "98a029b598f604cde7fb1f0091c83ca320251031",
                        "WorkflowName": "",
                        "WorkflowParams": "",
                        "WorkflowVersionId": "d9ce86112fb7d35aee14458e01ca2da420251031",
                        "WorkspaceId": "1"
                    }
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "0abde70a-766b-4fe2-a552-70326ec93bb0"
    }
}
```

