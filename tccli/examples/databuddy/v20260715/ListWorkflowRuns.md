**Example 1: 工作流运行列表**



Input: 

```
tccli databuddy ListWorkflowRuns --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --PageNumber 1 \
    --PageSize 10 \
    --WorkflowId 8e8a8cd9-633f-4fae-b5fa-f376a4d31da7
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 125,
            "TotalPageNumber": 13,
            "Items": [
                {
                    "AppId": "260073493",
                    "WorkflowName": "www1",
                    "WorkflowId": "8e8a8cd9-633f-4fae-b5fa-f376a4d31da7",
                    "WorkflowRunId": "8e8a8cd9-633f-4fae-b5fa-f376a4d31da7_1789995691987",
                    "WorkspaceId": "17678671667189298",
                    "TriggerType": "",
                    "RunStartTime": "0",
                    "PendingStartTime": "0",
                    "QueueStartTime": "0",
                    "RunEndTime": "0",
                    "EndTime": "0",
                    "RunCostTime": "0",
                    "QueueCostTime": "0",
                    "PendingCostTime": "1",
                    "RunState": "QUEUED",
                    "ResourceGroupIds": [],
                    "RunUserUin": "700002164619",
                    "RunUserName": "",
                    "ErrorCodeString": "",
                    "WorkflowParams": "",
                    "WorkflowVersionId": "381cae4e-d8af-40d6-9b0d-79d0fad8b21f",
                    "SupportRerun": false,
                    "CreateTime": "1789995692013",
                    "RerunTimes": 0,
                    "SelectedTaskIds": [
                        "9aa66a88-9a88-4a98-9d7f-1b92e3aedbff"
                    ],
                    "ResourceGroupInfoList": [],
                    "LabelList": [],
                    "ParentWorkflowRunId": "",
                    "ParentWorkflowTaskRunId": "",
                    "ParentWorkflowTaskRunName": "",
                    "Permission": "MANAGE",
                    "AdvancedParameters": [],
                    "ScheduledTime": "1789995691987"
                }
            ],
            "BizStateEnumInfos": [
                {
                    "LabelKey": "SUCCESS",
                    "LabelValue": "成功",
                    "Count": 78
                }
            ],
            "BizErrorCodeEnumInfos": [
                {
                    "LabelKey": "ExecutionFailed",
                    "LabelValue": "ExecutionFailed",
                    "Count": 11
                }
            ]
        },
        "RequestId": "d088d842-0a4f-4141-af82-50dde96919c4"
    }
}
```

**Example 2: 按默认分页查询工作空间下工作流运行列表**

按默认分页查询工作空间下工作流运行列表

Input: 

```
tccli databuddy ListWorkflowRuns --cli-unfold-argument  \
    --WorkspaceId 17697410068842890
```

Output: 
```
{
    "Response": {
        "Data": {
            "BizErrorCodeEnumInfos": [
                {
                    "Count": 12576,
                    "LabelKey": "",
                    "LabelValue": ""
                }
            ],
            "BizStateEnumInfos": [
                {
                    "Count": 12091,
                    "LabelKey": "SUCCESS",
                    "LabelValue": "成功"
                }
            ],
            "Items": [
                {
                    "AdvancedParameters": [],
                    "AppId": "251436191",
                    "CreateTime": "1786115878109",
                    "EndTime": "0",
                    "ErrorCodeString": "",
                    "LabelList": [],
                    "ParentWorkflowRunId": "",
                    "ParentWorkflowTaskRunId": "",
                    "ParentWorkflowTaskRunName": "",
                    "PendingCostTime": "37",
                    "PendingStartTime": "0",
                    "Permission": "MANAGE",
                    "QueueCostTime": "0",
                    "QueueStartTime": "0",
                    "RerunTimes": 0,
                    "ResourceGroupIds": [],
                    "ResourceGroupInfoList": [],
                    "RunCostTime": "0",
                    "RunEndTime": "0",
                    "RunStartTime": "0",
                    "RunState": "QUEUED",
                    "RunUserName": "",
                    "RunUserUin": "700002164618",
                    "SelectedTaskIds": [
                        "40d34e5c-12d9-4ac3-88ed-2f879713d4e4"
                    ],
                    "SupportRerun": false,
                    "TriggerType": "",
                    "WorkflowId": "8e0e3485-2736-4530-92ed-932e019898f1",
                    "WorkflowName": "new_workflow_20260807_190451",
                    "WorkflowParams": "{\"pppp1\":\"vvvv1\"}",
                    "WorkflowRunId": "8e0e3485-2736-4530-92ed-932e019898f1_1786115878097",
                    "WorkflowVersionId": "bcac4a2c-a47a-453b-8e31-34282e556db2",
                    "WorkspaceId": "17697410068842890"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 106670,
            "TotalPageNumber": 10667
        },
        "RequestId": "5f543f6f-7fae-47e9-8add-eb9d045d1bea"
    }
}
```

