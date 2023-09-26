**Example 1: demo**

用户信息列表

Input: 

```
tccli bi DescribeUserRoleList --cli-unfold-argument  \
    --UserType  \
    --Keyword  \
    --PageNo 0 \
    --PageSize 20
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

