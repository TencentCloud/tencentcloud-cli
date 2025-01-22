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
            "CreatedUser": "zhangsna",
            "CreatedAt": "zhangsan",
            "MemberCount": 0,
            "PageCount": 0,
            "LastModifyName": "zhangsna",
            "Source": "sas",
            "Apply": true,
            "UpdatedUser": "zhangsna",
            "UpdatedAt": "zhangsna",
            "CorpId": "1010",
            "Mark": "beiz",
            "Seed": "safd",
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
        "RequestId": "sasfsfd21dssfasdsf-fdsdad"
    }
}
```

