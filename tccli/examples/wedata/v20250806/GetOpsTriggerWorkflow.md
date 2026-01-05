**Example 1: 查询工作流详情**

工作流相关任务DAG

Input: 

```
tccli wedata GetOpsTriggerWorkflow --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId f5959d18-330a-4467-b3b9-55e24eff14bd
```

Output: 
```
{
    "Response": {
        "Data": {
            "TriggerTaskLinks": [
                {
                    "DownstreamTaskId": "20251111162552321",
                    "LinkId": "4c586283-7d80-48cd-a3a8-8c82e1b81215",
                    "UpstreamTaskId": "20251111160411927",
                    "WorkflowId": "f5959d18-330a-4467-b3b9-55e24eff14bd",
                    "WorkflowVersionId": null
                }
            ],
            "TriggerTasks": [
                {
                    "FolderId": "a1eb11e9-6f1a-11ed-8909-bc97e105ba60",
                    "FolderName": "默认文件夹",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "us_dev",
                    "TaskId": "20251111160411927",
                    "TaskName": "vvvvvv",
                    "TaskType": "NOTEBOOK",
                    "TaskTypeId": 132,
                    "UserNameInCharge": "erinhong",
                    "UserUinInCharge": "100044422498",
                    "WorkflowId": "f5959d18-330a-4467-b3b9-55e24eff14bd",
                    "WorkflowName": "erin332333"
                },
                {
                    "FolderId": "a1eb11e9-6f1a-11ed-8909-bc97e105ba60",
                    "FolderName": "默认文件夹",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "us_dev",
                    "TaskId": "20251111162552321",
                    "TaskName": "erin_1_copy",
                    "TaskType": "RUN_WORKFLOW",
                    "TaskTypeId": 140,
                    "UserNameInCharge": "erinhong",
                    "UserUinInCharge": "100044422498",
                    "WorkflowId": "f5959d18-330a-4467-b3b9-55e24eff14bd",
                    "WorkflowName": "erin332333"
                },
                {
                    "FolderId": "a1eb11e9-6f1a-11ed-8909-bc97e105ba60",
                    "FolderName": "默认文件夹",
                    "ProjectId": "1460947878944567296",
                    "ProjectName": "us_dev",
                    "TaskId": "20251120115002421",
                    "TaskName": "23123213",
                    "TaskType": "SHELL",
                    "TaskTypeId": 35,
                    "UserNameInCharge": "erinhong",
                    "UserUinInCharge": "100044422498",
                    "WorkflowId": "f5959d18-330a-4467-b3b9-55e24eff14bd",
                    "WorkflowName": "erin332333"
                }
            ]
        },
        "RequestId": "5012bd86-61e8-42b5-8513-26ff88569e84"
    }
}
```

