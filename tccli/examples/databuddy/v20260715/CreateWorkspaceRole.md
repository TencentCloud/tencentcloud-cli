**Example 1: CreateWorkspaceRole**

创建工作空间角色

Input: 

```
tccli databuddy CreateWorkspaceRole --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --BasicInfo.Description zjy_role_name \
    --BasicInfo.DisplayName zjy_role_name \
    --BasicInfo.RoleType role \
    --Permissions.0.ModuleId 104 \
    --Permissions.0.Permissions RWD
```

Output: 
```
{
    "Response": {
        "Data": {
            "RoleId": "869986134523174912",
            "Status": true
        },
        "RequestId": "2cdc9c5e-c2d6-4e14-8a30-18514ba0a4ce"
    }
}
```

