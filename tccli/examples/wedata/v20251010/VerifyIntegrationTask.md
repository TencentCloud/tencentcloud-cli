**Example 1: 校验集成任务**



Input: 

```
tccli wedata VerifyIntegrationTask --cli-unfold-argument  \
    --WorkspaceId test-project-001 \
    --TaskId 314a06b9-19ea-459c-b613-871ab5b606ed \
    --CheckType 9 \
    --TaskMode 1 \
    --Env production
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": "{\"MUST_CHECK\":{\"Status\":1,\"Result\":{}}}"
        },
        "RequestId": "dae20ee2-8d06-4a34-bd93-e46a95ae9c6d"
    }
}
```

