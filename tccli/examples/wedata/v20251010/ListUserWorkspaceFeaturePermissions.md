**Example 1: demo**



Input: 

```
tccli wedata ListUserWorkspaceFeaturePermissions --cli-unfold-argument  \
    --WorkspaceId 102
```

Output: 
```
{
    "Response": {
        "Data": {
            "Permissions": [
                {
                    "ModuleMeta": {
                        "DisplayName": "快速开始",
                        "Leaf": "Y",
                        "ModuleId": "101",
                        "ParentId": "1",
                        "SortId": "101"
                    }
                }
            ]
        },
        "RequestId": "362d20f3-05ec-43de-b4de-ae3ed24530e2"
    }
}
```

