**Example 1: dev_test**



Input: 

```
tccli wedata DeleteWorkflowExecution --cli-unfold-argument  \
    --WorkspaceId 1 \
    --WorkflowExecutionIdList exec_1002 \
    --WorkflowId wf_02
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
                    "ItemId": "exec_1002",
                    "ItemName": "",
                    "OpStatus": true
                }
            ]
        },
        "RequestId": "79f04ea7-3821-4525-aa0d-a13dc1747a85"
    }
}
```

