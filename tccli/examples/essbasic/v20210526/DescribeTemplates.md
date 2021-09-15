**Example 1: 查询有效模板列表**



Input: 

```
tccli essbasic DescribeTemplates --cli-unfold-argument  \
    --Agent.ProxyAppId xx \
    --Agent.ProxyOrganizationId xx \
    --Agent.ProxyOperator.OpenId xx \
    --Agent.ProxyOperator.ClientIp xx \
    --Agent.ProxyOperator.CustomUserId xx \
    --Agent.ProxyOperator.ProxyIp xx \
    --Agent.ProxyOperator.Channel xx \
    --Agent.AppId xx
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "Description": "xx",
                "Creator": "xx",
                "CreatedOn": 1234567890,
                "TemplateName": "xx",
                "SignComponents": [
                    {
                        "ComponentValue": "xx",
                        "GenerateMode": "xx",
                        "ComponentWidth": 1.1,
                        "FileIndex": 0,
                        "ComponentName": "xx",
                        "ComponentDateFontSize": 0,
                        "ComponentExtra": "xx",
                        "ComponentType": "xx",
                        "ComponentPage": 1,
                        "ComponentDescription": "xx",
                        "ComponentRequired": true,
                        "ComponentPosX": 1241.15,
                        "ComponentPosY": 125.12,
                        "ComponentId": "xx",
                        "DocumentId": "xx",
                        "ComponentHeight": 12.142
                    }
                ],
                "Components": [
                    {
                        "ComponentValue": "xx",
                        "GenerateMode": "xx",
                        "ComponentWidth": 1.1,
                        "FileIndex": 0,
                        "ComponentName": "xx",
                        "ComponentDateFontSize": 0,
                        "ComponentExtra": "xx",
                        "ComponentType": "xx",
                        "ComponentPage": 1,
                        "ComponentDescription": "xx",
                        "ComponentRequired": true,
                        "ComponentPosX": 1241.15,
                        "ComponentPosY": 125.12,
                        "ComponentId": "xx",
                        "DocumentId": "xx",
                        "ComponentHeight": 12.142
                    }
                ],
                "TemplateId": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

