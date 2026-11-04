**Example 1: 查询角色详情**



Input: 

```
tccli tione DescribeRole --cli-unfold-argument  \
    --TiProjectId 1889353273052233728 \
    --RoleId admin
```

Output: 
```
{
    "Response": {
        "AccessRules": [
            {
                "ActionType": [
                    "ModifyWorkspace",
                    "DeleteWorkspace"
                ],
                "ActionTypeName": [],
                "DataActionType": [],
                "Module": "Workspace"
            }
        ],
        "CreateTime": "2025-11-24T18:32:39+08",
        "Description": "",
        "RequestId": "410a1ff4-99f6-44b5-ae98-01a8950f5907",
        "RoleId": "admin",
        "RoleName": "管理员",
        "RoleType": "SYSTEM"
    }
}
```

