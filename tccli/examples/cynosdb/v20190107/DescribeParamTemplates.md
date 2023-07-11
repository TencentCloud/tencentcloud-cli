**Example 1: 参数板列表**

参数板列表

Input: 

```
tccli cynosdb DescribeParamTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "fc791b35-d5e5-4e08-859d-1c095e783199",
        "Items": [
            {
                "TemplateDescription": "API测试",
                "TemplateName": "API测试",
                "Id": 27,
                "EngineVersion": "5.7",
                "ParamInfoSet": [
                    {
                        "CurrentValue": "12",
                        "Description": "API测试",
                        "Min": "10",
                        "Default": "10",
                        "Max": "10000",
                        "ParamType": "integer",
                        "EnumValue": [
                            "test"
                        ],
                        "ParamName": "param1",
                        "NeedReboot": 0
                    }
                ],
                "DbMode": "NORMAL"
            },
            {
                "TemplateName": "API测试",
                "TemplateDescription": "API测试",
                "Id": 28,
                "EngineVersion": "5.7",
                "ParamInfoSet": [
                    {
                        "CurrentValue": "12",
                        "Description": "API测试",
                        "Min": "10",
                        "Default": "10",
                        "Max": "10000",
                        "ParamType": "integer",
                        "EnumValue": [
                            "tste",
                            "test2"
                        ],
                        "ParamName": "param2",
                        "NeedReboot": 0
                    }
                ],
                "DbMode": "NORMAL"
            }
        ]
    }
}
```

