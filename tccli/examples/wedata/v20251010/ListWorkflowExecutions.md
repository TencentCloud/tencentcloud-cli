**Example 1: 查询运维工作流执行信息**



Input: 

```
tccli wedata ListWorkflowExecutions --cli-unfold-argument  \
    --WorkspaceId 1 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 1,
            "PageSize": 10,
            "Items": [
                {
                    "AppId": "1300055887",
                    "CreateTime": "1761297763564",
                    "ErrorCodeStr": "NotFound",
                    "ExecutionCostTime": "15",
                    "ExecutionEndTime": "1761297763564",
                    "ExecutionId": "test_execution_20251024_172242",
                    "ExecutionStartTime": "1761297763564",
                    "ExecutionState": "STOP",
                    "PendingCostTime": "16",
                    "QueueCostTime": "18",
                    "RerunTimes": 0,
                    "ResourceGroupIds": null,
                    "ExecuteUserUin": "100031753986",
                    "ExecuteUserName": "zhangsan",
                    "SelectedTaskIds": [
                        "task1",
                        "task2"
                    ],
                    "SupportRerun": false,
                    "TriggerType": "ManualTrigger",
                    "WorkflowId": "7c8c0980e938da59e7db9258bbbed6df",
                    "WorkflowName": null,
                    "WorkflowParams": "{\"customer_id\":\"123123\",\"customer_name\":\"jayden\"}",
                    "WorkflowVersionId": "5b7e4c6b9e753f647bd43356b3bc1fa2",
                    "WorkspaceId": "1"
                }
            ],
            "TotalCount": "1",
            "TotalPageNumber": "1"
        },
        "RequestId": "4e94a8cd-88c9-40c8-970b-4bad9a14e50d"
    }
}
```

