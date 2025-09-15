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
                "RoleName": "testdata",
                "CorpId": "testdata",
                "RoleType": "testdata",
                "Scope": "testdata",
                "Description": "testdata",
                "CreatedAt": "testdata",
                "CreatedUser": "testdata",
                "UpdatedAt": "testdata",
                "UpdatedUser": "testdata",
                "ScopeType": 0,
                "CanChoose": true,
                "ModuleCollection": "testdata"
            }
        ],
        "Msg": "testdata",
        "Extra": "testdata",
        "RequestId": "testdata"
    }
}
```

