**Example 1: 查询参数模板详情**

查询参数模板详情

Input: 

```
tccli cynosdb DescribeParamTemplateDetail --cli-unfold-argument  \
    --TemplateId 4837003
```

Output: 
```
{
    "Response": {
        "DbMode": "NORMAL",
        "EngineVersion": "5.7",
        "Items": [
            {
                "CurrentValue": "1000",
                "Default": "0",
                "Description": "The maximum permitted number of simultaneous client connections per user.",
                "EnumValue": [],
                "Func": "",
                "IsFunc": false,
                "IsGlobal": 0,
                "MatchType": "",
                "MatchValue": "",
                "Max": "10240",
                "Min": "0",
                "ModifiableInfo": {
                    "IsModifiable": 1
                },
                "NeedReboot": 0,
                "ParamName": "max_user_connections",
                "ParamType": "integer",
                "SupportFunc": false
            }
        ],
        "RequestId": "ca8481bf-ba79-42ba-b90b-bd47df104add",
        "TemplateDescription": "测试模板",
        "TemplateId": 4837003,
        "TemplateName": "测试模板",
        "TotalCount": 1
    }
}
```

