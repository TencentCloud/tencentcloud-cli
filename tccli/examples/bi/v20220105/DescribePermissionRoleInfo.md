**Example 1: 项目内角色列表接口示例**

项目内角色列表接口示例

Input: 

```
tccli bi DescribePermissionRoleInfo --cli-unfold-argument  \
    --ProjectId 1 \
    --PageNo 0 \
    --PageSize 10 \
    --AllPage true
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 1,
                "RoleName": "abc",
                "CorpId": "abc",
                "RoleType": "abc",
                "Scope": "abc",
                "Description": "abc",
                "CreatedAt": "abc",
                "CreatedUser": "abc",
                "UpdatedAt": "abc",
                "UpdatedUser": "abc",
                "ScopeType": 0,
                "CanChoose": true,
                "ModuleCollection": "abc"
            }
        ],
        "Msg": "abc",
        "Extra": "abc",
        "RequestId": "abc"
    }
}
```

