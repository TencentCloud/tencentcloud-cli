**Example 1: 查询权限**



Input: 

```
tccli wedata ListResourcePermissions --cli-unfold-argument  \
    --Resource.ResourceType CATALOG \
    --Resource.ResourceUri DataLakeCatalog \
    --Filters.0.Name None \
    --Filters.0.Values None \
    --OrderFields.0.Name None \
    --OrderFields.0.Direction None \
    --Page.PageSize 1 \
    --Page.PageNumber 200
```

Output: 
```
{
    "Response": {
        "Data": {
            "Details": [],
            "TotalCount": 0
        },
        "RequestId": "2e4b3e8b-f0d1-4bd4-a172-d06fdb6812b7"
    }
}
```

