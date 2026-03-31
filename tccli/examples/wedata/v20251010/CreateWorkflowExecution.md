**Example 1: 运行工作流**



Input: 

```
tccli wedata CreateWorkflowExecution --cli-unfold-argument  \
    --WorkflowId 02b789442dcf92505741eb33f55162d6 \
    --ExecuteType 1 \
    --WorkspaceId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorMessage": null,
            "ExecutionActionId": "23b50c21-eb37-3aed-982b-e042da0cbcc8",
            "ItemId": "02b789442dcf92505741eb33f55162d6",
            "ItemName": "new_workflow_20251025_100729",
            "OpStatus": true
        },
        "RequestId": "039e2422-5fdf-4736-8a01-931239321d03"
    }
}
```

