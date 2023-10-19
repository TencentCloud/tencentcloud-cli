**Example 1: 项目内-用户角色列表**

项目内-用户角色列表

Input: 

```
tccli bi DescribeUserRoleProjectList --cli-unfold-argument  \
    --ProjectId 1 \
    --PageNo 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Extra": "abc",
        "Data": {
            "Total": 0,
            "TotalPages": 0,
            "List": [
                {
                    "Id": 1,
                    "RoleList": [
                        {
                            "RoleName": "abc",
                            "RoleId": 0,
                            "ProjectId": 0,
                            "ProjectName": "abc",
                            "ScopeType": 0,
                            "ModuleCollection": "abc"
                        }
                    ],
                    "RoleIdList": [
                        1
                    ],
                    "UserId": "abc",
                    "UserName": "abc",
                    "CorpId": "abc",
                    "Email": "abc",
                    "CreatedUser": "abc",
                    "CreatedAt": "abc",
                    "UpdatedUser": "abc",
                    "UpdatedAt": "abc",
                    "LastLogin": "2020-09-22T00:00:00+00:00",
                    "Status": 0,
                    "PhoneNumber": "abc",
                    "AreaCode": "abc",
                    "RootAccount": true,
                    "CorpAdmin": true
                }
            ]
        },
        "Msg": "abc",
        "RequestId": "abc"
    }
}
```

