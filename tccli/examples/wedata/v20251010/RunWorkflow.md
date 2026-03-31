**Example 1: 运行工作流**

成功运行一个工作流

Input: 

```
tccli wedata RunWorkflow --cli-unfold-argument  \
    --WorkflowId a2147f80-dc35-49cd-916c-eb40a8fdde71 \
    --ExecuteType 1 \
    --WorkspaceId 17663856806379896
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorMessage": "",
            "ExecutionActionId": "",
            "ItemId": "a5197e15-15f4-40ff-87a3-3911e55338e3",
            "ItemName": "lk_test_alarm",
            "OpStatus": true
        },
        "RequestId": "0c25ddb4-beb1-4304-83b1-840baf2e2b97"
    }
}
```

