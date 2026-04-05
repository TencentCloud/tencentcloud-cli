**Example 1: BatchCheckCatalogWorkspacePermission**

BatchCheckCatalogWorkspacePermission

Input: 

```
tccli wedata BatchCheckCatalogWorkspacePermission --cli-unfold-argument  \
    --Items.0.CatalogID tccatalog.v1.uid1876356801930330423 \
    --Items.0.WorkspaceID 17624147441995300 \
    --Items.0.PermissionLevel 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Results": [
                {
                    "CatalogID": "tccatalog.v1.uid1876356801930330423",
                    "HasPermission": false,
                    "PermissionLevel": "1",
                    "WorkspaceID": "17624147441995300"
                }
            ]
        },
        "RequestId": "d92f0e24-0178-4f4b-878f-fd00a6fefe14"
    }
}
```

