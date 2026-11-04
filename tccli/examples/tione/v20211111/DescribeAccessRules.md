**Example 1: 查询当前用户权限**



Input: 

```
tccli tione DescribeAccessRules --cli-unfold-argument  \
    --TiProjectId 1889353273052233728
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
                "ActionTypeName": [
                    "编辑工作空间",
                    "删除工作空间"
                ],
                "DataActionType": [],
                "Module": "Workspace"
            }
        ],
        "RequestId": "30ddd0f0-89e9-43ea-a176-60c4cefae586"
    }
}
```

