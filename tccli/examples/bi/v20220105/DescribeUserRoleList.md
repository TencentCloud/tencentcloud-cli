**Example 1: 用户信息列表**

用户信息列表

Input: 

```
tccli bi DescribeUserRoleList --cli-unfold-argument  \
    --PageNo 0 \
    --PageSize 0 \
    --AllPage True \
    --UserType 1 \
    --Keyword  \
    --ProjectId 1101 \
    --IsOnlyBindAppUser True
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
                    "UserName": "zhangsna",
                    "CorpId": "30310",
                    "Email": "232***12@qq.com",
                    "CreatedUser": "zhangsna",
                    "CreatedAt": "2020-09-22 00:00:00",
                    "UpdatedUser": "zhangsna",
                    "UpdatedAt": "2020-09-22 00:00:00",
                    "LastLogin": "2020-09-22T00:00:00+00:00",
                    "Status": 0,
                    "PhoneNumber": "86312***212",
                    "AreaCode": "086",
                    "RootAccount": true,
                    "CorpAdmin": true,
                    "AppUserId": "2102",
                    "AppUserAliasName": "zhangsn",
                    "AppUserName": "zhangsn",
                    "InValidateAppRange": true
                }
            ]
        },
        "Msg": "成功",
        "RequestId": ""
    }
}
```

