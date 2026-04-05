**Example 1: demo**



Input: 

```
tccli wedata UpdateWorkspaceRole --cli-unfold-argument  \
    --WorkspaceId 1 \
    --BasicInfo.Id 784448714810134528 \
    --BasicInfo.Name ab \
    --BasicInfo.Description ab \
    --BasicInfo.DisplayName abe \
    --BasicInfo.RoleType workspace_custom
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "e3150e02-35fc-4d98-92ed-d81b748fbba4"
    }
}
```

