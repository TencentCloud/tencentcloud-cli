**Example 1: 项目内-用户角色列表**

项目内-用户角色列表

Input: 

```
tccli bi DescribeUserRoleProjectList --cli-unfold-argument  \
    --PageNo 1982493789748932 \
    --PageSize 1982493789748932 \
    --ProjectId 1982493789748932 \
    --IsOnlyBindAppUser False
```

Output: 
```
{
    "Response": {
        "ErrorInfo": {
            "ErrorTip": "",
            "ErrorLevel": "INFO",
            "DocLink": "",
            "FAQ": "",
            "ReservedField": ""
        },
        "Extra": "",
        "Data": {
            "Total": 0,
            "TotalPages": 0,
            "List": [
                {
                    "Id": 1,
                    "RoleList": [
                        {
                            "RoleName": "企业管理员",
                            "RoleId": 0,
                            "ProjectId": 210210,
                            "ProjectName": "测试项目",
                            "ScopeType": 0,
                            "ModuleCollection": "project"
                        }
                    ],
                    "RoleIdList": [
                        1
                    ],
                    "UserId": "21021",
                    "UserName": "zhangsan",
                    "CorpId": "1202101",
                    "Email": "123***@qq.com",
                    "CreatedUser": "zhangsan",
                    "CreatedAt": "zhangsan",
                    "UpdatedUser": "zhangsan",
                    "UpdatedAt": "2020-09-22 00:00:00",
                    "LastLogin": "2020-09-22T00:00:00+00:00",
                    "Status": 0,
                    "PhoneNumber": "152****423",
                    "AreaCode": "086",
                    "RootAccount": true,
                    "CorpAdmin": true,
                    "AppUserId": "2103",
                    "AppUserAliasName": "zhangsan",
                    "AppUserName": "zhangsan",
                    "InValidateAppRange": true
                }
            ]
        },
        "Msg": "成功",
        "RequestId": "3211dfZ12-2331"
    }
}
```

