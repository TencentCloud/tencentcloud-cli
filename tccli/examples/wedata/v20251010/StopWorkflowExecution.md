**Example 1: 停止工作流运行示例**



Input: 

```
tccli wedata StopWorkflowExecution --cli-unfold-argument  \
    --WorkflowId wf_01 \
    --WorkflowExecutionIdList exec_1001 \
    --WorkspaceId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ActionResults": [
                {
                    "ErrorMessage": "",
                    "ExecutionActionId": "",
                    "ItemId": "exec_1001",
                    "ItemName": "",
                    "OpStatus": true
                }
            ]
        },
        "RequestId": "ccacd6a6-2a80-4ed8-9299-c5c0e2dd2749"
    }
}
```

