**Example 1: 授予集成任务权限**



Input: 

```
tccli wedata GrantIntegrationTaskPermission --cli-unfold-argument  \
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
        "RequestId": "268ccd1d-8416-4918-923f-8d329e609ec3"
    }
}
```

