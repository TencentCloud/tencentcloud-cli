**Example 1: demo**



Input: 

```
tccli wedata ListEntityPermissionScopes --cli-unfold-argument  \
    --WorkspaceId aa-zz \
    --EntityType FILE
```

Output: 
```
{
    "Response": {
        "Data": {
            "Permissions": [
                "MANAGE"
            ]
        },
        "RequestId": "d0ddedab-991b-4d4c-b9b7-079dee9af298"
    }
}
```

