**Example 1: 展示项目详情接口示例**

展示项目详情接口示例

Input: 

```
tccli bi DescribeProjectInfo --cli-unfold-argument  \
    --Id 43
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
        "Extra": "abc",
        "Msg": "abc",
        "Data": {
            "Id": 1,
            "Logo": "abc",
            "Name": "abc",
            "ColorCode": "abc",
            "CreatedUser": "abc",
            "CreatedAt": "abc",
            "MemberCount": 0,
            "PageCount": 0,
            "LastModifyName": "abc",
            "Source": "abc",
            "Apply": true,
            "UpdatedUser": "abc",
            "UpdatedAt": "abc",
            "CorpId": "abc",
            "Mark": "abc",
            "Seed": "abc",
            "AuthList": [
                "abc"
            ],
            "PanelScope": "abc",
            "IsExternalManage": true,
            "ManagePlatform": "abc",
            "ConfigList": [
                {
                    "ModuleGroup": "abc",
                    "Components": [
                        {
                            "ModuleId": "abc",
                            "IncludeType": "abc",
                            "Params": "abc"
                        }
                    ]
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

