**Example 1: 展示项目详情接口示例**

展示项目详情接口示例

Input: 

```
tccli bi DescribeProjectInfo --cli-unfold-argument  \
    --Id 1982493789748932 \
    --DefaultPanelType 1982493789748932
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
        "Extra": "ext",
        "Msg": "成功",
        "Data": {
            "Id": 1,
            "Logo": "https://cloud.tencetn****/logo.png",
            "Name": "测试项目",
            "ColorCode": "#fff",
            "CreatedUser": "zhangsan",
            "CreatedAt": "zhangsan",
            "MemberCount": 0,
            "PageCount": 0,
            "LastModifyName": "zhangsan",
            "Source": "sas",
            "Apply": true,
            "UpdatedUser": "zhangsan",
            "UpdatedAt": "zhangsan",
            "CorpId": "1010",
            "Mark": "Mark",
            "Seed": "Seed",
            "AuthList": [
                "110101"
            ],
            "PanelScope": "page",
            "IsExternalManage": true,
            "ManagePlatform": "saas",
            "ConfigList": [
                {
                    "ModuleGroup": "page",
                    "Components": [
                        {
                            "ModuleId": "1101",
                            "IncludeType": "usable",
                            "Params": ""
                        }
                    ]
                }
            ]
        },
        "RequestId": "RequestId-123"
    }
}
```

