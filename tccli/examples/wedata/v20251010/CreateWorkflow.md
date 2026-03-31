**Example 1: 成功**

创建工作流成功

Input: 

```
tccli wedata CreateWorkflow --cli-unfold-argument  \
    --WorkspaceId 1346 \
    --BaseInfo.WorkflowName dasdqwe
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkflowId": "697a4c92-30f0-4479-bb6a-066d50690cee"
        },
        "RequestId": "2fc7fec0-840b-416f-b4f8-c84fd6a138e8"
    }
}
```

