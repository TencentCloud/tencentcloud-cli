**Example 1: ListCatalogWorkspaces**

catalog工作空间列表

Input: 

```
tccli wedata ListCatalogWorkspaces --cli-unfold-argument  \
    --CatalogName c4 \
    --WorkspaceID 17623497097012366
```

Output: 
```
{
    "Response": {
        "Data": {
            "PermissionEntries": [
                {
                    "CatalogID": "tccatalog.v1.uid1876356801930330423",
                    "CatalogName": "c4",
                    "CreatedTime": "1773903972",
                    "PermissionLevel": "2",
                    "UpdatedTime": "1773903972",
                    "WorkspaceID": "17676920188276733",
                    "WorkspaceName": "workflow_z2"
                }
            ]
        },
        "RequestId": "a1fd7e1b-e0c7-4d2d-9c64-e559c9b16905"
    }
}
```

