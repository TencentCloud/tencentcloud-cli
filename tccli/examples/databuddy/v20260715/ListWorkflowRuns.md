**Example 1: 工作流运行列表**



Input: 

```
tccli databuddy ListWorkflowRuns --cli-unfold-argument  \
    --WorkspaceId 17622177773248536 \
    --PageNumber 1 \
    --PageSize 10 \
    --WorkflowId f4ec3e79-7368-44c9-8b04-031fad7f1a76 \
    --WorkflowNameKeyword demo \
    --CreateStartTime 1773244800000 \
    --CreateEndTime 1773244800000 \
    --RunStates ACTIVE \
    --ErrorCodeStrings demo \
    --RunUserUins 100044134096 \
    --LabelKeyIds f4ec3e79-7368-44c9-8b04-031fad7f1a76 \
    --LabelValueIds f4ec3e79-7368-44c9-8b04-031fad7f1a76
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 1,
            "Items": [],
            "BizStateEnumInfos": [],
            "BizErrorCodeEnumInfos": []
        },
        "RequestId": "43144820-519a-4b91-b2b3-4835ed5b35f5"
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

