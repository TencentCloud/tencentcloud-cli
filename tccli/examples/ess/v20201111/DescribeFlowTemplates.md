**Example 1: 模板查询接口**

查询企业模板列表

Input: 

```
tccli ess DescribeFlowTemplates --cli-unfold-argument  \
    --Operator.UserId string \
    --Offset 0 \
    --Limit 20 \
    --ContentType 0 \
    --Filters.0.Key template-id \
    --Filters.0.Values 16250***********49e047d8
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "TemplateId": "162509******b1949e047d8",
                "TemplateName": "string",
                "Description": "test",
                "CreatedOn": 1690438900,
                "Published": true,
                "Creator": "yD****id",
                "TemplateType": 3,
                "TemplateVersion": "0",
                "OrganizationId": "yD***Id",
                "PreviewUrl": "",
                "TemplateSeals": [],
                "Available": 1,
                "DocumentResourceIds": [
                    "123456******7812345678"
                ],
                "FileInfos": [
                    {
                        "CreatedOn": 1234567890,
                        "FileId": "0410049******2494f43bb",
                        "FileName": "7530fbd040c*********26aaf-verify.pdf",
                        "FileSize": 45435
                    }
                ],
                "AttachmentResourceIds": [
                    "string"
                ],
                "Promoter": {
                    "RecipientId": "0",
                    "RecipientType": "PROMOTER",
                    "Description": "发起人角色",
                    "RoleName": "发起人",
                    "RequireValidation": "False",
                    "RequireSign": "False",
                    "RoutingOrder": 0,
                    "RequireDelivery": "False",
                    "Email": "123@tencent.com",
                    "Mobile": "12332112345",
                    "UserId": "",
                    "DeliveryMethod": "email",
                    "RecipientExtra": ""
                },
                "SignOrder": [
                    0,
                    1
                ],
                "Recipients": [
                    {
                        "RecipientId": "1",
                        "RecipientType": "enterprise",
                        "Description": "",
                        "RoleName": "企业",
                        "RequireValidation": "False",
                        "RequireSign": "True",
                        "RoutingOrder": 0,
                        "RequireDelivery": "True",
                        "Email": "123@tencent.com",
                        "Mobile": "12332112345",
                        "UserId": "",
                        "DeliveryMethod": "email",
                        "RecipientExtra": ""
                    },
                    {
                        "RecipientId": "2",
                        "RecipientType": "enterprise",
                        "Description": "",
                        "RoleName": "企业HR",
                        "RequireValidation": "False",
                        "RequireSign": "True",
                        "RoutingOrder": 0,
                        "RequireDelivery": "True",
                        "Email": "123@tencent.com",
                        "Mobile": "12332112345",
                        "UserId": "",
                        "DeliveryMethod": "email",
                        "RecipientExtra": ""
                    }
                ],
                "Components": [
                    {
                        "ComponentRecipientId": "1",
                        "ComponentId": "string",
                        "ComponentName": "string",
                        "ComponentType": "string",
                        "ComponentRequired": true,
                        "ComponentWidth": 1.1,
                        "ComponentHeight": 12.142,
                        "ComponentPage": 1,
                        "ComponentPosX": 1241.15,
                        "ComponentPosY": 125.12,
                        "ComponentExtra": "string",
                        "ComponentValue": "value",
                        "IsFormType": true,
                        "KeywordPage": 0,
                        "ChannelComponentId": "yD***id",
                        "GenerateMode": "KEYWORD",
                        "ComponentDateFontSize": 12,
                        "OffsetY": 0,
                        "OffsetX": 0,
                        "RelativeLocation": "",
                        "KeywordOrder": "",
                        "KeywordIndexes": [],
                        "ChannelComponentSource": 0,
                        "FileIndex": 0
                    }
                ],
                "SignComponents": [
                    {
                        "ComponentRecipientId": "1",
                        "ComponentId": "string",
                        "ComponentName": "string",
                        "ComponentType": "string",
                        "ComponentRequired": true,
                        "ComponentWidth": 1.1,
                        "ComponentHeight": 12.142,
                        "ComponentPage": 1,
                        "ComponentPosX": 1241.15,
                        "ComponentPosY": 125.12,
                        "ComponentExtra": "string",
                        "ComponentValue": "value",
                        "IsFormType": true,
                        "KeywordPage": 0,
                        "ChannelComponentId": "yD***id",
                        "GenerateMode": "KEYWORD",
                        "ComponentDateFontSize": 12,
                        "OffsetY": 0,
                        "OffsetX": 0,
                        "RelativeLocation": "",
                        "KeywordOrder": "",
                        "KeywordIndexes": [],
                        "ChannelComponentSource": 0,
                        "FileIndex": 0
                    }
                ],
                "Status": 0
            }
        ],
        "TotalCount": 10,
        "RequestId": "test"
    }
}
```

