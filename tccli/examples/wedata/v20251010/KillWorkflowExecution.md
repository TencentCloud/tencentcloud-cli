**Example 1: 停止工作流运行**

成功停止工作流运行

Input: 

```
tccli wedata KillWorkflowExecution --cli-unfold-argument  \
    --WorkflowId wf_01 \
    --WorkspaceId 1 \
    --WorkflowExecutionIdList exec_1001
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
        "RequestId": "9f8205dd-1fa4-4e30-9546-fe13e978b56c"
    }
}
```

