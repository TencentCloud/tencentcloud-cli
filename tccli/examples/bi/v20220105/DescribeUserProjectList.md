**Example 1: 项目内用户接口示例**

项目内用户接口示例

Input: 

```
tccli bi DescribeUserProjectList --cli-unfold-argument  \
    --ProjectId 0 \
    --AllPage True \
    --PageNo 0 \
    --PageSize 0
```

Output: 
```
{
    "Response": {
        "ErrorInfo": {
            "ErrorTip": "abc",
            "ErrorLevel": "abc",
            "DocLink": "abc",
            "FAQ": "abc",
            "ReservedField": "abc"
        },
        "Data": {
            "List": [
                {
                    "UserId": "abc",
                    "UserName": "abc",
                    "CorpId": "abc",
                    "Email": "abc",
                    "LastLogin": "2020-09-22T00:00:00+00:00",
                    "Status": 0,
                    "FirstModify": 0,
                    "PhoneNumber": "abc",
                    "AreaCode": "abc",
                    "CreatedUser": "abc",
                    "CreatedAt": "2020-09-22T00:00:00+00:00",
                    "UpdatedUser": "abc",
                    "UpdatedAt": "2020-09-22T00:00:00+00:00",
                    "GlobalUserName": "abc",
                    "Mobile": "abc",
                    "AppId": "abc",
                    "AppUserId": "abc",
                    "AppUserAliasName": "abc",
                    "AppUserName": "abc",
                    "InValidateAppRange": true
                }
            ],
            "Total": 0,
            "TotalPages": 0
        },
        "Extra": "abc",
        "Msg": "abc",
        "RequestId": "abc"
    }
}
```

