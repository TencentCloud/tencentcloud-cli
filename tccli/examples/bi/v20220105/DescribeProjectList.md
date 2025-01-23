**Example 1: 项目列表数据接口**

项目列表数据接口

Input: 

```
tccli bi DescribeProjectList --cli-unfold-argument  \
    --PageSize 1 \
    --PageNo 1 \
    --Keyword demo \
    --AllPage True
```

Output: 
```
{
    "Response": {
        "ErrorInfo": {
            "ErrorTip": "",
            "ErrorLevel": "INFO",
            "DocLink": "数据不存在",
            "FAQ": "",
            "ReservedField": ""
        },
        "Extra": "",
        "Msg": "成功",
        "Data": {
            "List": [
                {
                    "Id": 1,
                    "Logo": "http://www.cloud.com***/logo.png",
                    "Name": "bi项目",
                    "ColorCode": "#666",
                    "CreatedUser": "张三",
                    "CreatedAt": "张三",
                    "MemberCount": 0,
                    "PageCount": 0,
                    "LastModifyName": "张三",
                    "Source": "",
                    "Apply": true,
                    "UpdatedUser": "张三",
                    "UpdatedAt": "张三",
                    "CorpId": "10010101",
                    "Mark": "说明备注",
                    "Seed": "",
                    "AuthList": [
                        "10101"
                    ],
                    "PanelScope": "scope",
                    "IsExternalManage": true,
                    "ManagePlatform": "saas",
                    "ConfigList": [
                        {
                            "ModuleGroup": "project",
                            "Components": [
                                {
                                    "ModuleId": "10101",
                                    "IncludeType": "useable",
                                    "Params": ""
                                }
                            ]
                        }
                    ]
                }
            ],
            "Total": 1,
            "TotalPages": 1
        },
        "RequestId": "dfjksak10w1qdsk2312"
    }
}
```

