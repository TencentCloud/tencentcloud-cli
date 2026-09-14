**Example 1: 运行工作流**



Input: 

```
tccli databuddy RunWorkflow --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --WorkflowId 8e0e3485-2736-4530-92ed-932e019898f1 \
    --RunType 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ActionResults": [
                {
                    "ErrorMessage": "",
                    "OpStatus": true,
                    "RunActionId": "cmd_20260807195442_000001",
                    "WorkflowId": "8e0e3485-2736-4530-92ed-932e019898f1_1786103682348",
                    "WorkflowName": "new_workflow_20260807_190451",
                    "WorkflowRunId": ""
                }
            ]
        },
        "RequestId": "5e78212a-8c5b-444f-a493-f64b563d707c"
    }
}
```

