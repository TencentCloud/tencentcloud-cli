**Example 1: 查询有效模板列表**



Input: 

```
tccli essbasic DescribeTemplates --cli-unfold-argument  \
    --Agent.ProxyAppId d2b****b66f954d7cc \
    --Agent.ProxyOrganizationId yDxAyUyK****cb7u0jQn0Zh7f7 \
    --Agent.ProxyOperator.OpenId 732aaef****541b89c49e0cc \
    --Agent.ProxyOperator.ClientIp 8.8.8.8 \
    --Agent.ProxyOperator.ProxyIp 8.8.8.8 \
    --Agent.AppId ed68bc6***********0214e4e \
    --TemplateId templated_test_id \
    --ContentType 1 \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "Description": "测试模板",
                "Recipients": [
                    {
                        "RecipientType": "INDIVIDUAL",
                        "Description": "签署人信息",
                        "RoutingOrder": 0,
                        "SignType": 0,
                        "RecipientId": "yDxlTUyK***********LrHa7uB",
                        "RequireSign": true,
                        "RequireValidation": true,
                        "RoleName": "个人签署方"
                    }
                ],
                "Creator": "鹅鹅子",
                "CreatedOn": 1234567890,
                "TemplateName": "测试模板",
                "SignComponents": [
                    {
                        "ComponentValue": "",
                        "GenerateMode": "xx",
                        "ComponentWidth": 1.1,
                        "FileIndex": 0,
                        "ComponentName": "文本",
                        "ComponentDateFontSize": 0,
                        "ComponentExtra": "",
                        "ComponentType": "SIGN_SIGNATURE",
                        "ComponentPage": 1,
                        "ComponentDescription": "xx",
                        "ComponentRequired": true,
                        "ComponentPosX": 1241.15,
                        "ComponentPosY": 125.12,
                        "ComponentId": "componentId_1",
                        "DocumentId": "",
                        "ComponentHeight": 12.142
                    }
                ],
                "TemplateType": 0,
                "IsPromoter": true,
                "Components": [
                    {
                        "ComponentValue": "yDxlTUyK***********xe8mbiVR",
                        "GenerateMode": "",
                        "ComponentWidth": 1.1,
                        "FileIndex": 0,
                        "ComponentName": "盖章",
                        "ComponentDateFontSize": 0,
                        "ComponentExtra": "",
                        "ComponentType": "SIGN_SEAL",
                        "ComponentPage": 1,
                        "ComponentDescription": "xx",
                        "ComponentRequired": true,
                        "ComponentPosX": 1241.15,
                        "ComponentPosY": 125.12,
                        "ComponentId": "componentId_2",
                        "DocumentId": "",
                        "ComponentHeight": 12.142
                    }
                ],
                "TemplateId": "yDxlTUyK***********8bbdrxhT5th"
            }
        ],
        "RequestId": "s1631799397530469887",
        "TotalCount": 1,
        "Limit": 1,
        "Offset": 0
    }
}
```

