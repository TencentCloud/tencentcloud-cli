**Example 1: 查询有效模板列表**



Input: 

```
tccli essbasic DescribeTemplates --cli-unfold-argument  \
    --Agent.ProxyAppId d2b7b02fd1178f7c63f2db66f954d7cc \
    --Agent.ProxyOrganizationId yDxAyUyKQWXJ5BUupHcb7u0jQn0Zh7f7 \
    --Agent.ProxyOperator.OpenId 732aaefa78c439d726f541b89c49e0cc \
    --Agent.ProxyOperator.ClientIp 8.8.8.8 \
    --Agent.ProxyOperator.ProxyIp 8.8.8.8 \
    --Agent.AppId ed68bc6904fbd4795b4658c480214e4e \
    --TemplateId templated_test_id
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "Description": "测试模版",
                "Recipients": [
                    {
                        "RecipientType": "INDIVIDUAL",
                        "Description": "签署人信息",
                        "RoutingOrder": 0,
                        "SignType": 0,
                        "RecipientId": "yDxlTUyKQWX7hrUupHcb7Cfz0LrHa7uB",
                        "RequireSign": true,
                        "RequireValidation": true,
                        "RoleName": "个人签署方"
                    }
                ],
                "Creator": "鹅鹅子",
                "CreatedOn": 1234567890,
                "TemplateName": "测试模版",
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
                "Components": [
                    {
                        "ComponentValue": "yDxlTUyKQWX76SUupHcb7uS5xe8mbiVR",
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
                "TemplateId": "yDxlTUyKQWX7hOUupHcb78bbdrxhT5th"
            }
        ],
        "RequestId": "s1631799397530469887"
    }
}
```

