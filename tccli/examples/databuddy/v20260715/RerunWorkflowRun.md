**Example 1: 重跑工作流**

重跑工作流

Input: 

```
tccli databuddy RerunWorkflowRun --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --WorkflowId 18b1a42e-951d-4b31-98a0-b404dac2c324 \
    --WorkflowRunId 18b1a42e-951d-4b31-98a0-b404dac2c324_1786024800000 \
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
                    "RunActionId": "cmd_20260807233141_000001",
                    "WorkflowId": "18b1a42e-951d-4b31-98a0-b404dac2c324_1786024800000",
                    "WorkflowName": "",
                    "WorkflowRunId": ""
                }
            ]
        },
        "RequestId": "fa65efd3-dd08-4f9d-9b94-acdba94366ca"
    }
}
```

