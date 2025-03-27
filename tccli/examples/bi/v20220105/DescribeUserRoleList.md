**Example 1: 用户信息列表**

用户信息列表

Input: 

```
tccli bi DescribeUserRoleList --cli-unfold-argument  \
    --PageNo 1982493789748932 \
    --PageSize 1982493789748932 \
    --AllPage False \
    --UserType UserType \
    --Keyword Keyword \
    --ProjectId ProjectId \
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
                            "ProjectId": 0,
                            "ProjectName": "测试项目",
                            "ScopeType": 0,
                            "ModuleCollection": "datasource"
                        }
                    ],
                    "RoleIdList": [
                        1
                    ],
                    "UserId": "10210",
                    "UserName": "zhangsan",
                    "CorpId": "30310",
                    "Email": "123***@qq.com",
                    "CreatedUser": "zhangsan",
                    "CreatedAt": "2020-09-22 00:00:00",
                    "UpdatedUser": "zhangsan",
                    "UpdatedAt": "2020-09-22 00:00:00",
                    "LastLogin": "2020-09-22T00:00:00+00:00",
                    "Status": 0,
                    "PhoneNumber": "86312***212",
                    "AreaCode": "086",
                    "RootAccount": true,
                    "CorpAdmin": true,
                    "AppUserId": "2102",
                    "AppUserAliasName": "zhangsan",
                    "AppUserName": "zhangsan",
                    "InValidateAppRange": true
                }
            ]
        },
        "Msg": "成功",
        "RequestId": ""
    }
}
```

