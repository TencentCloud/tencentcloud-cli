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

**Example 2: 返回所有component**



Input: 

```
tccli essbasic DescribeTemplates --cli-unfold-argument  \
    --QueryAllComponents true \
    --Agent.ProxyOperator.OpenId test1_clara_test1 \
    --Agent.AppId 7f3497f015042c9a35e0984a9657b0ec \
    --Agent.ProxyOrganizationOpenId test1_clara_open_organization1 \
    --Agent.ProxyOrganizationId yDxHwUyKQDHmEPUuO4zjEBNLMLjthsmk \
    --TemplateId yDR0JUUgygspbi8uUuO4zjESIpKDSkE9
```

Output: 
```
{
    "Response": {
        "Limit": 20,
        "Offset": 0,
        "RequestId": "90ceffe5-94b1-45ac-b256-5cd54829065c",
        "Templates": [
            {
                "Components": [
                    {
                        "ComponentDateFontSize": 0,
                        "ComponentDescription": "测试",
                        "ComponentExtra": "{\"Font\":\"黑体\",\"FontAlign\":\"Left\",\"FontSize\":12,\"MaxLength\":6}",
                        "ComponentHeight": 18,
                        "ComponentId": "componentId_3",
                        "ComponentName": "test",
                        "ComponentPage": 3,
                        "ComponentPosX": 453.49572753906,
                        "ComponentPosY": 312.78833580017,
                        "ComponentRequired": true,
                        "ComponentType": "TEXT",
                        "ComponentValue": "",
                        "ComponentWidth": 80,
                        "DocumentId": "",
                        "FileIndex": 0,
                        "GenerateMode": ""
                    },
                    {
                        "ComponentDateFontSize": 0,
                        "ComponentDescription": "测试",
                        "ComponentExtra": "{\"Font\":\"黑体\",\"FontAlign\":\"Left\",\"FontSize\":12,\"MaxLength\":6}",
                        "ComponentHeight": 18,
                        "ComponentId": "componentId_3",
                        "ComponentName": "test",
                        "ComponentPage": 3,
                        "ComponentPosX": 453.49572753906,
                        "ComponentPosY": 312.78833580017,
                        "ComponentRequired": true,
                        "ComponentType": "TEXT",
                        "ComponentValue": "",
                        "ComponentWidth": 80,
                        "DocumentId": "",
                        "FileIndex": 0,
                        "GenerateMode": ""
                    }
                ],
                "CreatedOn": 1661503344,
                "Creator": "张倩",
                "Description": "",
                "IsPromoter": false,
                "Recipients": [
                    {
                        "Description": "",
                        "IsPromoter": true,
                        "RecipientId": "yDR0JUUgygspbzduUuO4zjECvKyhk7jT",
                        "RecipientType": "ENTERPRISE",
                        "RequireSign": true,
                        "RequireValidation": false,
                        "RoleName": "测试环境_自动化测试",
                        "RoutingOrder": -1,
                        "SignType": 0
                    },
                    {
                        "Description": "",
                        "IsPromoter": false,
                        "RecipientId": "yDR0JUUgygspbzdaUuO4zjERyDQZICyF",
                        "RecipientType": "INDIVIDUAL",
                        "RequireSign": true,
                        "RequireValidation": false,
                        "RoleName": "个人签署方1",
                        "RoutingOrder": -1,
                        "SignType": 0
                    }
                ],
                "SignComponents": [
                    {
                        "ComponentDateFontSize": 0,
                        "ComponentDescription": "",
                        "ComponentExtra": "",
                        "ComponentHeight": 113.33,
                        "ComponentId": "componentId_4",
                        "ComponentName": "测试环境_自动化测试盖章1",
                        "ComponentPage": 3,
                        "ComponentPosX": 327.49572753906,
                        "ComponentPosY": 552.09656333923,
                        "ComponentRequired": true,
                        "ComponentType": "SIGN_SEAL",
                        "ComponentValue": "",
                        "ComponentWidth": 113.33,
                        "DocumentId": "",
                        "FileIndex": 0,
                        "GenerateMode": ""
                    },
                    {
                        "ComponentDateFontSize": 0,
                        "ComponentDescription": "",
                        "ComponentExtra": "",
                        "ComponentHeight": 40,
                        "ComponentId": "componentId_5",
                        "ComponentName": "个人签署方1签名1",
                        "ComponentPage": 3,
                        "ComponentPosX": 386.49572753906,
                        "ComponentPosY": 730.18323326111,
                        "ComponentRequired": true,
                        "ComponentType": "SIGN_SIGNATURE",
                        "ComponentValue": "",
                        "ComponentWidth": 112,
                        "DocumentId": "",
                        "FileIndex": 0,
                        "GenerateMode": ""
                    }
                ],
                "TemplateId": "yDR0JUUgygspbi8uUuO4zjESIpKDSkE9",
                "TemplateName": "无序签署&发起方有填写控件的b2c模板",
                "TemplateType": 3
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 3: 模糊搜索模版名**



Input: 

```
tccli essbasic DescribeTemplates --cli-unfold-argument  \
    --TemplateName 顺序签署 \
    --QueryAllComponents true \
    --Agent.ProxyOperator.OpenId test1_clara_test1 \
    --Agent.AppId 7f3497f015042c9a35e0984a9657b0ec \
    --Agent.ProxyOrganizationOpenId test1_clara_open_organization1 \
    --Agent.ProxyOrganizationId yDxHwUyKQDHmEPUuO4zjEBNLMLjthsmk \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "Limit": 2,
        "Offset": 0,
        "RequestId": "3842c68d-d272-4196-9ef5-9fc63bcddbf8",
        "Templates": [
            {
                "Components": [],
                "CreatedOn": 1661503792,
                "Creator": "张倩",
                "Description": "",
                "IsPromoter": false,
                "Recipients": [
                    {
                        "Description": "",
                        "IsPromoter": true,
                        "RecipientId": "yDR0JUUgygspuac2UuO4zjERwT0dL9xs",
                        "RecipientType": "ENTERPRISE",
                        "RequireSign": true,
                        "RequireValidation": false,
                        "RoleName": "测试环境_自动化测试",
                        "RoutingOrder": 0,
                        "SignType": 0
                    },
                    {
                        "Description": "",
                        "IsPromoter": false,
                        "RecipientId": "yDR0JUUgygspuaclUuO4zjEyDHvECsDZ",
                        "RecipientType": "INDIVIDUAL",
                        "RequireSign": true,
                        "RequireValidation": false,
                        "RoleName": "个人签署方1",
                        "RoutingOrder": 1,
                        "SignType": 0
                    }
                ],
                "SignComponents": [
                    {
                        "ComponentDateFontSize": 0,
                        "ComponentDescription": "",
                        "ComponentExtra": "",
                        "ComponentHeight": 113.33,
                        "ComponentId": "componentId_13",
                        "ComponentName": "测试环境_自动化测试盖章1",
                        "ComponentPage": 3,
                        "ComponentPosX": 330.49572753906,
                        "ComponentPosY": 384.09656333923,
                        "ComponentRequired": true,
                        "ComponentType": "SIGN_SEAL",
                        "ComponentValue": "",
                        "ComponentWidth": 113.33,
                        "DocumentId": "",
                        "FileIndex": 0,
                        "GenerateMode": ""
                    },
                    {
                        "ComponentDateFontSize": 0,
                        "ComponentDescription": "",
                        "ComponentExtra": "",
                        "ComponentHeight": 40,
                        "ComponentId": "componentId_14",
                        "ComponentName": "个人签署方1签名1",
                        "ComponentPage": 3,
                        "ComponentPosX": 252.49572753906,
                        "ComponentPosY": 632.18323326111,
                        "ComponentRequired": true,
                        "ComponentType": "SIGN_SIGNATURE",
                        "ComponentValue": "",
                        "ComponentWidth": 112,
                        "DocumentId": "",
                        "FileIndex": 0,
                        "GenerateMode": ""
                    }
                ],
                "TemplateId": "yDR0JUUgygspuacjUuO4zjEEauW70uGG",
                "TemplateName": "顺序签署时B是首位签署的b2c模板",
                "TemplateType": 3
            },
            {
                "Components": [],
                "CreatedOn": 1661503695,
                "Creator": "张倩",
                "Description": "",
                "IsPromoter": false,
                "Recipients": [
                    {
                        "Description": "",
                        "IsPromoter": false,
                        "RecipientId": "yDR0JUUgygspuwurUuO4zjETakC1TTWY",
                        "RecipientType": "INDIVIDUAL",
                        "RequireSign": true,
                        "RequireValidation": false,
                        "RoleName": "个人签署方1",
                        "RoutingOrder": 0,
                        "SignType": 0
                    },
                    {
                        "Description": "",
                        "IsPromoter": true,
                        "RecipientId": "yDR0JUUgygspuwu5UuO4zjESF9B8DCsK",
                        "RecipientType": "ENTERPRISE",
                        "RequireSign": true,
                        "RequireValidation": false,
                        "RoleName": "测试环境_自动化测试",
                        "RoutingOrder": 1,
                        "SignType": 0
                    }
                ],
                "SignComponents": [
                    {
                        "ComponentDateFontSize": 0,
                        "ComponentDescription": "",
                        "ComponentExtra": "",
                        "ComponentHeight": 40,
                        "ComponentId": "componentId_11",
                        "ComponentName": "个人签署方1签名1",
                        "ComponentPage": 3,
                        "ComponentPosX": 413.49572753906,
                        "ComponentPosY": 348.75421714783,
                        "ComponentRequired": true,
                        "ComponentType": "SIGN_SIGNATURE",
                        "ComponentValue": "",
                        "ComponentWidth": 112,
                        "DocumentId": "",
                        "FileIndex": 0,
                        "GenerateMode": ""
                    },
                    {
                        "ComponentDateFontSize": 0,
                        "ComponentDescription": "",
                        "ComponentExtra": "",
                        "ComponentHeight": 113.33,
                        "ComponentId": "componentId_12",
                        "ComponentName": "测试环境_自动化测试盖章1",
                        "ComponentPage": 3,
                        "ComponentPosX": 318.49572753906,
                        "ComponentPosY": 497.16193199158,
                        "ComponentRequired": true,
                        "ComponentType": "SIGN_SEAL",
                        "ComponentValue": "",
                        "ComponentWidth": 113.33,
                        "DocumentId": "",
                        "FileIndex": 0,
                        "GenerateMode": ""
                    }
                ],
                "TemplateId": "yDR0JUUgygspuactUuO4zjE8v6DE0hRC",
                "TemplateName": "顺序签署时B非首位签署的b2c模板",
                "TemplateType": 3
            }
        ],
        "TotalCount": 4
    }
}
```

