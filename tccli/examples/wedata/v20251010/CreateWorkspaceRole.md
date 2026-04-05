**Example 1: demo**



Input: 

```
tccli wedata CreateWorkspaceRole --cli-unfold-argument  \
    --WorkspaceId 1 \
    --BasicInfo.Name abe1 \
    --BasicInfo.Description abe1 \
    --BasicInfo.DisplayName abe1 \
    --BasicInfo.RoleType workspace_custom
```

Output: 
```
{
    "Response": {
        "Data": {
            "RoleId": "784451512981327872"
        },
        "RequestId": "37f1109f-454a-4276-964f-ded8f5752541"
    }
}
```

