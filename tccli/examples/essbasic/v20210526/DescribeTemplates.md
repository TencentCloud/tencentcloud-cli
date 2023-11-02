**Example 1: 模板查询接口-指定模板Id查询模板信息**

1.指定查询条件为TemplateId
2.指定Limit为最多返回20条数据

Input: 

```
tccli essbasic DescribeTemplates --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId yDxAyUyK****cb7u0jQn0Zh7f7 \
    --Agent.ProxyOperator.OpenId 732aaef****541b89c49e0cc \
    --Agent.AppId ed68bc6***********0214e4e \
    --TemplateId yDRS4UUgygqdcjjhUuO4zjEBpXdcsHWX \
    --ContentType 1 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "ChannelAutoSave": 0,
                "PdfUrl": "test",
                "Description": "test",
                "Recipients": [
                    {
                        "RecipientType": "test",
                        "Description": "test",
                        "RoutingOrder": 0,
                        "SignType": 0,
                        "RecipientId": "test",
                        "IsPromoter": true,
                        "RequireValidation": true,
                        "RoleName": "test",
                        "RequireSign": true
                    }
                ],
                "TemplateName": "test",
                "CreatedOn": 1234567890,
                "Creator": "test",
                "ChannelTemplateName": "test",
                "Available": 2,
                "SignComponents": [
                    {
                        "ComponentValue": "test",
                        "FileIndex": 0,
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ComponentType": "test",
                        "ComponentPosX": 1241.15,
                        "ComponentPosY": 125.12,
                        "GenerateMode": "test",
                        "KeywordIndexes": [
                            0
                        ],
                        "ComponentDateFontSize": 0,
                        "RelativeLocation": "test",
                        "ComponentHeight": 12.142,
                        "ComponentDescription": "test",
                        "ComponentRequired": true,
                        "ComponentId": "test",
                        "ComponentRecipientId": "test",
                        "KeywordPage": 0,
                        "ComponentWidth": 1.1,
                        "ComponentName": "test",
                        "ChannelComponentId": "test",
                        "ComponentExtra": "test",
                        "ComponentPage": 1,
                        "KeywordOrder": "test",
                        "Placeholder": "",
                        "DocumentId": "test"
                    }
                ],
                "TemplateType": 0,
                "IsPromoter": true,
                "PreviewUrl": "test",
                "Components": [
                    {
                        "ComponentValue": "test",
                        "FileIndex": 0,
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ComponentType": "test",
                        "ComponentPosX": 1241.15,
                        "ComponentPosY": 125.12,
                        "GenerateMode": "test",
                        "KeywordIndexes": [
                            0
                        ],
                        "ComponentDateFontSize": 0,
                        "RelativeLocation": "test",
                        "ComponentHeight": 12.142,
                        "ComponentDescription": "test",
                        "ComponentRequired": true,
                        "ComponentId": "test",
                        "ComponentRecipientId": "test",
                        "KeywordPage": 0,
                        "ComponentWidth": 1.1,
                        "ComponentName": "test",
                        "ChannelComponentId": "test",
                        "ComponentExtra": "test",
                        "ComponentPage": 1,
                        "KeywordOrder": "test",
                        "Placeholder": "",
                        "DocumentId": "test"
                    }
                ],
                "TemplateId": "test",
                "TemplateVersion": "test",
                "ChannelTemplateId": "test"
            }
        ],
        "TotalCount": 1,
        "Limit": 1,
        "RequestId": "test",
        "Offset": 1
    }
}
```

**Example 2: 模板查询接口-模糊搜索模板名**

1.指定查询条件为TemplateName
2.指定Limit为最多返回20条数据
3.指定QueryAllComponents为true，返回所有component

Input: 

```
tccli essbasic DescribeTemplates --cli-unfold-argument  \
    --TemplateName 顺序签署 \
    --QueryAllComponents true \
    --Agent.ProxyOperator.OpenId test1xxxa_test1 \
    --Agent.AppId 7f3497f015xxxxe0984a9657b0ec \
    --Agent.ProxyOrganizationOpenId test1_claraxxxanization1 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "TemplateId": "test",
                "TemplateName": "test",
                "Description": "test",
                "Available": 2,
                "Components": [
                    {
                        "ComponentId": "test",
                        "ComponentType": "test",
                        "ComponentName": "test",
                        "ComponentRequired": true,
                        "ComponentRecipientId": "test",
                        "FileIndex": 0,
                        "GenerateMode": "test",
                        "ComponentWidth": 0,
                        "ComponentHeight": 0,
                        "ComponentPage": 0,
                        "ComponentPosX": 0,
                        "ComponentPosY": 0,
                        "ComponentExtra": "test",
                        "ComponentValue": "test",
                        "ComponentDateFontSize": 0,
                        "DocumentId": "test",
                        "ComponentDescription": "test",
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ChannelComponentId": "test",
                        "KeywordOrder": "test",
                        "KeywordPage": 0,
                        "RelativeLocation": "test",
                        "Placeholder": "",
                        "KeywordIndexes": [
                            0
                        ]
                    }
                ],
                "Recipients": [
                    {
                        "RecipientId": "test",
                        "RecipientType": "test",
                        "Description": "test",
                        "RoleName": "test",
                        "RequireValidation": true,
                        "RequireSign": true,
                        "SignType": 0,
                        "RoutingOrder": 0,
                        "IsPromoter": true
                    }
                ],
                "SignComponents": [
                    {
                        "ComponentId": "test",
                        "ComponentType": "test",
                        "ComponentName": "test",
                        "ComponentRequired": true,
                        "ComponentRecipientId": "test",
                        "FileIndex": 0,
                        "GenerateMode": "test",
                        "ComponentWidth": 0,
                        "ComponentHeight": 0,
                        "ComponentPage": 0,
                        "ComponentPosX": 0,
                        "ComponentPosY": 0,
                        "ComponentExtra": "test",
                        "ComponentValue": "test",
                        "ComponentDateFontSize": 0,
                        "DocumentId": "test",
                        "ComponentDescription": "test",
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ChannelComponentId": "test",
                        "KeywordOrder": "test",
                        "KeywordPage": 0,
                        "RelativeLocation": "test",
                        "Placeholder": "",
                        "KeywordIndexes": [
                            0
                        ]
                    }
                ],
                "TemplateType": 0,
                "IsPromoter": true,
                "Creator": "test",
                "CreatedOn": 0,
                "PreviewUrl": "test",
                "PdfUrl": "test",
                "ChannelTemplateId": "test",
                "ChannelTemplateName": "test",
                "ChannelAutoSave": 0,
                "TemplateVersion": "test"
            }
        ],
        "TotalCount": 0,
        "Limit": 1,
        "Offset": 1,
        "RequestId": "test"
    }
}
```

**Example 3: 模板查询接口-通过不存在的模板Id查询模板信息**

1.指定一个不存在的模板ID进行查询

Input: 

```
tccli essbasic DescribeTemplates --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId yDxAyUyK****cb7u0jQn0Zh7f7 \
    --Agent.ProxyOperator.OpenId 732aaef****541b89c49e0cc \
    --Agent.AppId ed68bc6***********0214e4e \
    --TemplateId yDRS4UUxxxxxxxjEBpXdcsHWX \
    --ContentType 1 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "s1695125479063466836",
        "Templates": [],
        "Offset": 0,
        "Limit": 20,
        "TotalCount": 0
    }
}
```

