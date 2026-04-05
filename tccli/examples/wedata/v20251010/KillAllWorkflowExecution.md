**Example 1: 停止工作流下全部运行**



Input: 

```
tccli wedata KillAllWorkflowExecution --cli-unfold-argument  \
    --WorkflowId wf_01 \
    --WorkspaceId 1 \
    --All True
```

Output: 
```
{
    "Response": {
        "Data": {
            "ActionResults": [
                {
                    "ErrorMessage": "没有工作流运行需要操作.",
                    "ExecutionActionId": "",
                    "ItemId": "",
                    "ItemName": "",
                    "OpStatus": false
                }
            ]
        },
        "RequestId": "c5518b79-65d9-45f3-a3e7-5989f838753a"
    }
}
```

