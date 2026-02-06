**Example 1: 查看调度工作流上游任务列表**

查看调度工作流上游任务列表

Input: 

```
tccli wedata ListUpstreamTriggerTasks --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20251124113217312
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "OwnerUin": "100028579606",
                    "ProjectId": "1460947878944567296",
                    "Status": "N",
                    "TaskId": "20251121163138956",
                    "TaskName": "gallop_workflow_task_test",
                    "TaskTypeDesc": "Shell",
                    "TaskTypeId": 35,
                    "WorkflowId": "d3e40dcc-bf42-4fb9-b081-b00408d478ec",
                    "WorkflowName": "gallopcai_workflow"
                },
                {
                    "OwnerUin": "100028660434",
                    "ProjectId": "1460947878944567296",
                    "Status": "N",
                    "TaskId": "20251124172632837",
                    "TaskName": "gallop_workflow_task_test_up2",
                    "TaskTypeDesc": "Shell",
                    "TaskTypeId": 35,
                    "WorkflowId": "d3e40dcc-bf42-4fb9-b081-b00408d478ec",
                    "WorkflowName": "gallopcai_workflow"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 2,
            "TotalPageNumber": 1
        },
        "RequestId": "ba62a9be-c23a-47c6-bb3c-7f2ecb3ce771"
    }
}
```

