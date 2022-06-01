**Example 1: 模板查询接口**



Input: 

```
tccli ess DescribeFlowTemplates --cli-unfold-argument  \
    --Operator.UserId string \
    --Operator.ClientIp string \
    --Operator.Channel string \
    --Operator.OpenId  \
    --Operator.ProxyIp string \
    --Offset 0 \
    --Limit 20 \
    --ContentType 0 \
    --Filters.0.Key template-id \
    --Filters.0.Values 162509089e82f9479cb4cb1949e047d8
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "TemplateId": "162509089e82f9479cb4cb1949e047d8",
                "TemplateName": "string",
                "Description": "XXXXX",
                "DocumentResourceIds": [
                    "12345678123456781234567812345678"
                ],
                "FileInfos": [
                    {
                        "CreatedOn": 1234567890,
                        "FileId": "04100497d78304b5a0dd9d02494f43bb",
                        "FileName": "7530fbd040cc79b9784c7922f1c26aaf-verify.pdf",
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
                        "FileIndex": 0
                    }
                ],
                "Status": 0
            }
        ],
        "TotalCount": 10,
        "RequestId": "xx"
    }
}
```

