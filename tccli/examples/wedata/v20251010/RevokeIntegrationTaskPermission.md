**Example 1: 撤销集成任务权限**



Input: 

```
tccli wedata RevokeIntegrationTaskPermission --cli-unfold-argument  \
    --WorkspaceId test-project-001 \
    --TaskId 314a06b9-19ea-459c-b613-871ab5b606ed \
    --Permission EDIT \
    --UinList 700002164618
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": true
        },
        "RequestId": "da324db0-9ca9-45bd-8a11-97505d2746c5"
    }
}
```

