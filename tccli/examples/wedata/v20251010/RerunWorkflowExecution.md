**Example 1: 重跑工作流**



Input: 

```
tccli wedata RerunWorkflowExecution --cli-unfold-argument  \
    --WorkflowId 7c8c0980e938da59e7db9258bbbed6df \
    --WorkflowExecutionId test_execution_20251024_172242 \
    --ExecuteType 1 \
    --WorkspaceId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "404149a2-5d30-4cd3-9554-c855d49303f7",
        "Data": {
            "ErrorMessage": null,
            "ExecutionActionId": "23b50c21-eb37-3aed-982b-e042da0cbcc8",
            "ItemId": "test_execution_20251024_172242",
            "ItemName": null,
            "OpStatus": true
        }
    }
}
```

