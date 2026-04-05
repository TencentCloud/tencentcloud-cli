**Example 1: RevokeCatalogToWorkspacePermissions**

RevokeCatalogToWorkspacePermissions

Input: 

```
tccli wedata RevokeCatalogToWorkspacePermissions --cli-unfold-argument  \
    --PermissionEntries.0.CatalogID tccatalog.v1.uid1876356801930330423 \
    --PermissionEntries.0.CatalogName c4 \
    --PermissionEntries.0.WorkspaceID 17624147441995300 \
    --PermissionEntries.0.WorkspaceName bs_1106_1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Failures": [],
            "Success": true
        },
        "RequestId": "5e29752a-8f44-462d-8277-b19267c5d781"
    }
}
```

