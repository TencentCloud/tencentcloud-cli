**Example 1: 项目内用户接口示例**

项目内用户接口示例

Input: 

```
tccli bi DescribeUserProjectList --cli-unfold-argument  \
    --ProjectId 1982493789748932 \
    --AllPage False \
    --PageNo 1982493789748932 \
    --PageSize 1982493789748932 \
    --Keyword zhangsan
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
        "Data": {
            "List": [
                {
                    "UserId": "1101",
                    "UserName": "zhangsan",
                    "CorpId": "1012",
                    "Email": "123***@qq.com",
                    "LastLogin": "2020-09-22T00:00:00+00:00",
                    "Status": 0,
                    "FirstModify": 0,
                    "PhoneNumber": "86212***21",
                    "AreaCode": "086",
                    "CreatedUser": "zhangsan",
                    "CreatedAt": "2020-09-22T00:00:00+00:00",
                    "UpdatedUser": "zhangsan",
                    "UpdatedAt": "2020-09-22T00:00:00+00:00",
                    "GlobalUserName": "zhangsan",
                    "Mobile": "153****798",
                    "AppId": "101",
                    "AppUserId": "zhangsan",
                    "AppUserAliasName": "zhangsan",
                    "AppUserName": "zhangsan",
                    "InValidateAppRange": true
                }
            ],
            "Total": 0,
            "TotalPages": 0
        },
        "Extra": "",
        "Msg": "成功",
        "RequestId": "RequestId-123"
    }
}
```

