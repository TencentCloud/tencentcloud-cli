**Example 1: 终止运行**



Input: 

```
tccli wedata KillTriggerWorkflowRuns --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId 36f56792-1b9f-4bae-aa20-c80359f69c9c \
    --WorkflowExecutionIdList 0045ce2f-02e3-4091-8b31-3dd084ebfdb6 \
    --All False \
    --Pending False
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ErrorMessage": null,
                "ExecutionActionId": null,
                "ItemId": "0045ce2f-02e3-4091-8b31-3dd084ebfdb6",
                "ItemName": "ives_test1",
                "OpStatus": true
            }
        ],
        "RequestId": "5b0e289c-7f77-46e6-9297-7e1a3399f993"
    }
}
```

