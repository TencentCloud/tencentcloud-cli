**Example 1: 查询工作流运行详情**



Input: 

```
tccli databuddy GetWorkflowRun --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --WorkflowRunId 8e0e3485-2736-4530-92ed-932e019898f1_1786115878097
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkflowRun": {
                "AdvancedParameters": [],
                "AppId": "251436191",
                "CreateTime": "1786115878109",
                "EndTime": "0",
                "ErrorCodeString": "",
                "LabelList": [],
                "ParentWorkflowRunId": "",
                "ParentWorkflowTaskRunId": "",
                "ParentWorkflowTaskRunName": "",
                "PendingCostTime": "297",
                "PendingStartTime": "0",
                "Permission": "",
                "QueueCostTime": "0",
                "QueueStartTime": "0",
                "RerunTimes": 0,
                "ResourceGroupIds": [],
                "ResourceGroupInfoList": [],
                "RunCostTime": "0",
                "RunEndTime": "0",
                "RunStartTime": "0",
                "RunState": "QUEUED",
                "RunUserName": "we********e************m",
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
        },
        "RequestId": "c97a0eca-6267-49ef-8525-76d38d2e18ab"
    }
}
```

