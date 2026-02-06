**Example 1: 重跑工作流**



Input: 

```
tccli wedata RerunTriggerWorkflowRunAsync --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId 0fae8078-a7a7-4b67-afd1-8bf18e068dda \
    --WorkflowExecutionId 001e2f39-a71d-4588-9a9a-9f244d32c96c \
    --ExecuteType 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AsyncId": "60a7f0f5-cea2-40fe-b607-a164d9615689"
        },
        "RequestId": "4a20bd2d-8053-4f9f-86b6-bda857e7fcf6"
    }
}
```

