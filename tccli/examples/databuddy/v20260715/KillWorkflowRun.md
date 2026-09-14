**Example 1: 终止工作流的运行**



Input: 

```
tccli databuddy KillWorkflowRun --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --WorkflowId 8e0e3485-2736-4530-92ed-932e019898f1 \
    --WorkflowRunIds 8e0e3485-2736-4530-92ed-932e019898f1_1786115878097
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
                    "RunActionId": "cmd_20260807235246_000001",
                    "WorkflowId": "8e0e3485-2736-4530-92ed-932e019898f1_1786115878097",
                    "WorkflowName": "",
                    "WorkflowRunId": ""
                }
            ]
        },
        "RequestId": "43957900-50db-43be-9cb2-9af3b1f278c0"
    }
}
```

