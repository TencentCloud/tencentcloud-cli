**Example 1: 重跑工作流**

重跑工作流

Input: 

```
tccli databuddy RerunWorkflowRun --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --WorkflowId 1b185f10-151d-42e5-886d-f8c4eb2fcae5 \
    --WorkflowRunId 1b185f10-151d-42e5-886d-f8c4eb2fcae5_1787110336358_p550ec615a5cdfee0 \
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
                    "RunActionId": "cmd_20260819135346_000001",
                    "WorkflowId": "1b185f10-151d-42e5-886d-f8c4eb2fcae5",
                    "WorkflowName": "zl_wf_260813_142851",
                    "WorkflowRunId": "1b185f10-151d-42e5-886d-f8c4eb2fcae5_1787110336358_p550ec615a5cdfee0"
                }
            ]
        },
        "RequestId": "5503d42a-692f-4b40-a974-ef33dad110f9"
    }
}
```

