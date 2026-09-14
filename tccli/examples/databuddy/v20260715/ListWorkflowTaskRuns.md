**Example 1: 查询工作流任务历史运行列表**



Input: 

```
tccli databuddy ListWorkflowTaskRuns --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --TaskId f2d5ffc0-af32-4584-a315-b106637f1bfe \
    --WorkflowRunId 8e0e3485-2736-4530-92ed-932e019898f1_1786115878097
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "1786115878247",
                    "CreateUserUin": "700002164618",
                    "DependOnList": [],
                    "ErrorCodeString": "",
                    "IsLatestRun": true,
                    "JobId": "",
                    "RerunTimes": 0,
                    "ResourceGroupId": "",
                    "ResourceGroupInfoList": [],
                    "RetryTimes": 0,
                    "RunParams": "",
                    "RunResult": "",
                    "RunState": "CREATE",
                    "RunUserName": "",
                    "RunUserUin": "700002164618",
                    "TaskId": "f2d5ffc0-af32-4584-a315-b106637f1bfe",
                    "TaskName": "py_0807",
                    "TaskTypeExtensions": "",
                    "TaskTypeName": "PYTHON",
                    "TaskVersionId": "2cf47642-f9b8-4b93-a6fa-31a03810c423",
                    "TimeZone": "",
                    "TriggerType": "",
                    "UpdateTime": "1786115878236",
                    "WorkflowId": "8e0e3485-2736-4530-92ed-932e019898f1",
                    "WorkflowName": "",
                    "WorkflowRunId": "8e0e3485-2736-4530-92ed-932e019898f1_1786115878097",
                    "WorkflowTaskRunId": "f2d5ffc0-af32-4584-a315-b106637f1bfe_1786115878097_1",
                    "WorkspaceId": "17697410068842890"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "6e166d32-30fc-49f3-9e01-61ab8af86417"
    }
}
```

