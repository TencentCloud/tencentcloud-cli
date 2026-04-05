**Example 1: GrantCatalogToWorkspacePermissions**

GrantCatalogToWorkspacePermissions

Input: 

```
tccli wedata GrantCatalogToWorkspacePermissions --cli-unfold-argument  \
    --PermissionEntries.0.CatalogName c4 \
    --PermissionEntries.0.WorkspaceID 17624149598811176 \
    --PermissionEntries.0.WorkspaceName bs_1106_2 \
    --PermissionEntries.0.PermissionLevel 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Failures": [],
            "Success": true
        },
        "RequestId": "b1702373-2144-47ed-9286-a657f8aa8dab"
    }
}
```

