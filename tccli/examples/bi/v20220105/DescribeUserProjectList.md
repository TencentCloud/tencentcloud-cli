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
                    "UserName": "zhangsn",
                    "CorpId": "1012",
                    "Email": "242***@qq.com",
                    "LastLogin": "2020-09-22T00:00:00+00:00",
                    "Status": 0,
                    "FirstModify": 0,
                    "PhoneNumber": "86212***21",
                    "AreaCode": "086",
                    "CreatedUser": "zhangsna",
                    "CreatedAt": "2020-09-22T00:00:00+00:00",
                    "UpdatedUser": "zhangsn",
                    "UpdatedAt": "2020-09-22T00:00:00+00:00",
                    "GlobalUserName": "zhangsn",
                    "Mobile": "153****798",
                    "AppId": "101",
                    "AppUserId": "zhangsn",
                    "AppUserAliasName": "zhangsa",
                    "AppUserName": "zjang",
                    "InValidateAppRange": true
                }
            ],
            "Total": 0,
            "TotalPages": 0
        },
        "Extra": "",
        "Msg": "成功",
        "RequestId": "sddfsdf212ffdf-dsdas"
    }
}
```

