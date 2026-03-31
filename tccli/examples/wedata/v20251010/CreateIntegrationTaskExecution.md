**Example 1: 调试数据接入任务**



Input: 

```
tccli wedata CreateIntegrationTaskExecution --cli-unfold-argument  \
    --WorkspaceId test_workspace_01 \
    --TaskId 4313be0b-742d-4dd9-afa8-08281047188e \
    --TaskVersion 20251226161431 \
    --ResourceGroupId resource_1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorMessage": "",
            "JobId": "6820251229231645008",
            "OpStatus": true,
            "TaskId": "4313be0b-742d-4dd9-afa8-08281047188e"
        },
        "RequestId": "b2c5b7b1-8f64-428f-804b-1c2766763e10"
    }
}
```

