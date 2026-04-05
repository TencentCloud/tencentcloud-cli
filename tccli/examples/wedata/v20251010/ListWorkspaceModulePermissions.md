**Example 1: demo**



Input: 

```
tccli wedata ListWorkspaceModulePermissions --cli-unfold-argument  \
    --WorkspaceId 102 \
    --SubjectType workspace
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
        "RequestId": "105a78f3-108f-4867-8037-1e2064d94f06"
    }
}
```

