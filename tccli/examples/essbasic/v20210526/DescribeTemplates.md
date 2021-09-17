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
                "Description": "xx",
                "Recipients": [
                    {
                        "RecipientType": "xx",
                        "Description": "xx",
                        "RoutingOrder": 0,
                        "SignType": 0,
                        "RecipientId": "xx",
                        "RequireSign": true,
                        "RequireValidation": true,
                        "RoleName": "xx"
                    }
                ],
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
                "TemplateType": 0,
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

