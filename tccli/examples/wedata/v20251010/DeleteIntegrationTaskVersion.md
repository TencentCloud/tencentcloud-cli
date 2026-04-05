**Example 1: 删除集成任务版本**



Input: 

```
tccli wedata DeleteIntegrationTaskVersion --cli-unfold-argument  \
    --WorkspaceId test-project-001 \
    --TaskId 314a06b9-19ea-459c-b613-871ab5b606ed \
    --TaskVersion 20251219163217
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": true,
            "DeleteErrInfo": "",
            "DeleteFlag": "1"
        },
        "RequestId": "20c29848-3f39-4f6d-94fe-d3a97f933c7e"
    }
}
```

