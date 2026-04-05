**Example 1: 成功示例**



Input: 

```
tccli wedata GetMyWorkflowMaxPermission --cli-unfold-argument  \
    --WorkspaceId 17622177773248536 \
    --WorkflowId 8ef0c2ab-a437-458b-a393-dd91a67181db
```

Output: 
```
{
    "Response": {
        "Data": {
            "Permission": "PERMISSION_TYPE_UNSPECIFIED"
        },
        "RequestId": "5fb9464f-f6dc-49bb-9212-a4e82334b0bf"
    }
}
```

