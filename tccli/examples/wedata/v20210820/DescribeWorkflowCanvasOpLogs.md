**Example 1: 示例1**

demo

Input: 

```
tccli wedata DescribeWorkflowCanvasOpLogs --cli-unfold-argument  \
    --Filter.OperatorIds 100028578851 \
    --WorkflowId f5d1b42f-ed67-11ed-8909-bc97e105ba60 \
    --ProjectId 1460947878944567296 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "CurrentPage": 1,
            "CurrentPageItems": 4,
            "Items": [
                {
                    "Content": "更新任务：hive_task_jayden_1",
                    "CreateTimestamp": 1683528191,
                    "OperatorId": 100028578851,
                    "OperatorName": "jaydenjhu",
                    "WorkflowId": "f5d1b42f-ed67-11ed-8909-bc97e105ba60"
                },
                {
                    "Content": "创建任务：hive_task_jayden_1",
                    "CreateTimestamp": 1683528186,
                    "OperatorId": 100028578851,
                    "OperatorName": "jaydenjhu",
                    "WorkflowId": "f5d1b42f-ed67-11ed-8909-bc97e105ba60"
                },
                {
                    "Content": "更新工作流：workflow_1",
                    "CreateTimestamp": 1683526649,
                    "OperatorId": 100028578851,
                    "OperatorName": "jaydenjhu",
                    "WorkflowId": "f5d1b42f-ed67-11ed-8909-bc97e105ba60"
                },
                {
                    "Content": "创建工作流：workflow_1",
                    "CreateTimestamp": 1683526628,
                    "OperatorId": 100028578851,
                    "OperatorName": "jaydenjhu",
                    "WorkflowId": "f5d1b42f-ed67-11ed-8909-bc97e105ba60"
                }
            ],
            "PageSize": 10,
            "TotalItems": 4,
            "TotalPages": 1
        },
        "RequestId": "9b9b85b8-aaa1-406b-9298-e37bc3771013"
    }
}
```

