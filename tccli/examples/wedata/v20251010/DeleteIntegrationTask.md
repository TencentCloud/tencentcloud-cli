**Example 1: 删除集成任务**



Input: 

```
tccli wedata DeleteIntegrationTask --cli-unfold-argument  \
    --TaskId 314a06b9-19ea-459c-b613-871ab5b606ed \
    --WorkspaceId test-project-001
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
        "RequestId": "a500c5ce-21b5-4e54-bdcb-d9a44366d7c9"
    }
}
```

