**Example 1: ListCatalogWorkspaces**

ListCatalogWorkspaces

Input: 

```
tccli wedata ListCatalogWorkspaces --cli-unfold-argument  \
    --CatalogID tccatalog.v1.uid1876356801930330423
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
                    "CreatedTime": "1767114565",
                    "PermissionLevel": "1",
                    "UpdatedTime": "1767114565",
                    "WorkspaceID": "17624147441995300",
                    "WorkspaceName": "bs_1106_1"
                }
            ]
        },
        "RequestId": "cc6f55e6-11cc-42e2-a3ea-5396bed79992"
    }
}
```

