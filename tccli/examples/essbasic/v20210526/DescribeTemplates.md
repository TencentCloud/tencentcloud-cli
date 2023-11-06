**Example 1: 模板查询接口-指定模板Id查询模板信息**

指定查询条件为TemplateId,  只返回此模板的信息

Input: 

```
tccli essbasic DescribeTemplates --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --TemplateIds yDSLVUUckpo3pub6UE5dPdv8pkDsrbEn
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "TemplateId": "yDSLVUUckpo3pub6UE5dPdv8pkDsrbEn",
                "TemplateName": "西红柿买卖合同模板",
                "Description": "南山农批西红柿买卖合同模板",
                "Components": [],
                "Recipients": [
                    {
                        "RecipientId": "yDSLVUUckpo3nocjUEnf33ki7GtMQC2L",
                        "RecipientType": "INDIVIDUAL",
                        "Description": "",
                        "RoleName": "买房-自然人",
                        "RequireValidation": false,
                        "RequireSign": false,
                        "SignType": 0,
                        "RoutingOrder": -1,
                        "IsPromoter": false
                    },
                    {
                        "RecipientId": "yDSLVUUckpo3noc8UEnf33kxKp7Waeq1",
                        "RecipientType": "ENTERPRISE",
                        "Description": "",
                        "RoleName": "卖方-菜市场",
                        "RequireValidation": false,
                        "RequireSign": false,
                        "SignType": 0,
                        "RoutingOrder": -1,
                        "IsPromoter": false
                    }
                ],
                "SignComponents": [
                    {
                        "ComponentId": "ComponentId_2",
                        "ComponentType": "SIGN_SEAL",
                        "ComponentName": "企业印章",
                        "ComponentRequired": true,
                        "ComponentRecipientId": "yDSLVUUckpo3noc8UEnf33kxKp7Waeq1",
                        "FileIndex": 0,
                        "GenerateMode": "",
                        "ComponentWidth": 119,
                        "ComponentHeight": 119,
                        "ComponentPage": 1,
                        "ComponentPosX": 32.640625,
                        "ComponentPosY": 0,
                        "ComponentExtra": "{\"Date\":true,\"isAfterCut\":false,\"PageRanges\":[]}",
                        "ComponentValue": "",
                        "ComponentDateFontSize": 0,
                        "DocumentId": "",
                        "ComponentDescription": "",
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ChannelComponentId": "",
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "RelativeLocation": "",
                        "KeywordIndexes": [],
                        "Placeholder": ""
                    },
                    {
                        "ComponentId": "ComponentId_5",
                        "ComponentType": "SIGN_SIGNATURE",
                        "ComponentName": "个人签名/印章",
                        "ComponentRequired": true,
                        "ComponentRecipientId": "yDSLVUUckpo3nocjUEnf33ki7GtMQC2L",
                        "FileIndex": 0,
                        "GenerateMode": "",
                        "ComponentWidth": 119,
                        "ComponentHeight": 43,
                        "ComponentPage": 1,
                        "ComponentPosX": 397.640625,
                        "ComponentPosY": 14,
                        "ComponentExtra": "{\"Date\":true,\"isAfterCut\":false}",
                        "ComponentValue": "",
                        "ComponentDateFontSize": 0,
                        "DocumentId": "",
                        "ComponentDescription": "",
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ChannelComponentId": "",
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "RelativeLocation": "",
                        "KeywordIndexes": [],
                        "Placeholder": ""
                    },
                    {
                        "ComponentId": "ComponentId_6",
                        "ComponentType": "SIGN_DATE",
                        "ComponentName": "签署日期1",
                        "ComponentRequired": true,
                        "ComponentRecipientId": "yDSLVUUckpo3nocjUEnf33ki7GtMQC2L",
                        "FileIndex": 0,
                        "GenerateMode": "",
                        "ComponentWidth": 119,
                        "ComponentHeight": 20,
                        "ComponentPage": 1,
                        "ComponentPosX": 397.640625,
                        "ComponentPosY": 57,
                        "ComponentExtra": "{\"Format\":\"yyyy年m月d日\",\"Gaps\":\"2,2\",\"FontSize\":12,\"FontAlign\":\"Center\",\"Font\":\"黑体\",\"isAfterCut\":false}",
                        "ComponentValue": "",
                        "ComponentDateFontSize": 0,
                        "DocumentId": "",
                        "ComponentDescription": "",
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ChannelComponentId": "",
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "RelativeLocation": "",
                        "KeywordIndexes": [],
                        "Placeholder": ""
                    },
                    {
                        "ComponentId": "ComponentId_3",
                        "ComponentType": "SIGN_DATE",
                        "ComponentName": "签署日期",
                        "ComponentRequired": true,
                        "ComponentRecipientId": "yDSLVUUckpo3noc8UEnf33kxKp7Waeq1",
                        "FileIndex": 0,
                        "GenerateMode": "",
                        "ComponentWidth": 119,
                        "ComponentHeight": 20,
                        "ComponentPage": 1,
                        "ComponentPosX": 32.640625,
                        "ComponentPosY": 119,
                        "ComponentExtra": "{\"Format\":\"yyyy年m月d日\",\"Gaps\":\"2,2\",\"FontSize\":12,\"FontAlign\":\"Center\",\"Font\":\"黑体\",\"isAfterCut\":false}",
                        "ComponentValue": "",
                        "ComponentDateFontSize": 0,
                        "DocumentId": "",
                        "ComponentDescription": "",
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ChannelComponentId": "",
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "RelativeLocation": "",
                        "KeywordIndexes": [],
                        "Placeholder": ""
                    }
                ],
                "TemplateType": 3,
                "IsPromoter": false,
                "Creator": "张三",
                "CreatedOn": 1699259970,
                "PreviewUrl": "",
                "PdfUrl": "",
                "ChannelTemplateId": "",
                "ChannelTemplateName": "",
                "ChannelAutoSave": 0,
                "TemplateVersion": "20231106002",
                "Available": 1
            }
        ],
        "TotalCount": 1,
        "Limit": 0,
        "Offset": 0,
        "RequestId": "072c42c3-8ec2-43f3-b872-bc28594b0597"
    }
}
```

**Example 2: 模板查询接口-模糊搜索模板名**

1.指定查询条件为TemplateName
2.指定QueryAllComponents为true，返回所有参与方(创建方+签署方)的填写控件列表Components

Input: 

```
tccli essbasic DescribeTemplates --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --TemplateName 西红柿 \
    --QueryAllComponents True
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "TemplateId": "yDSLVUUckpo3pub6UE5dPdv8pkDsrbEn",
                "TemplateName": "西红柿买卖合同模板",
                "Description": "南山农批西红柿买卖合同模板",
                "Components": [
                    {
                        "ComponentId": "ComponentId_11",
                        "ComponentType": "TEXT",
                        "ComponentName": "西红柿的价格",
                        "ComponentRequired": true,
                        "ComponentRecipientId": "yDSLVUUckpo3nwi1UEnf33kBMNXjdB2c",
                        "FileIndex": 0,
                        "GenerateMode": "",
                        "ComponentWidth": 144,
                        "ComponentHeight": 20,
                        "ComponentPage": 1,
                        "ComponentPosX": 336.640625,
                        "ComponentPosY": 205,
                        "ComponentExtra": "{\"FontSize\":12,\"FontAlign\":\"Left\",\"Font\":\"黑体\",\"SubType\":\"TEXT\",\"MaxLength\":12}",
                        "ComponentValue": "",
                        "ComponentDateFontSize": 0,
                        "DocumentId": "",
                        "ComponentDescription": "",
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ChannelComponentId": "",
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "RelativeLocation": "",
                        "KeywordIndexes": [],
                        "Placeholder": ""
                    },
                    {
                        "ComponentId": "ComponentId_12",
                        "ComponentType": "TEXT",
                        "ComponentName": "西红柿的交接时间",
                        "ComponentRequired": true,
                        "ComponentRecipientId": "yDSLVUUckpo3nwi1UEnf33kBMNXjdB2c",
                        "FileIndex": 0,
                        "GenerateMode": "",
                        "ComponentWidth": 144,
                        "ComponentHeight": 20,
                        "ComponentPage": 1,
                        "ComponentPosX": 341.640625,
                        "ComponentPosY": 270,
                        "ComponentExtra": "{\"FontSize\":12,\"FontAlign\":\"Left\",\"Font\":\"黑体\",\"SubType\":\"TEXT\",\"MaxLength\":12}",
                        "ComponentValue": "",
                        "ComponentDateFontSize": 0,
                        "DocumentId": "",
                        "ComponentDescription": "",
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ChannelComponentId": "",
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "RelativeLocation": "",
                        "KeywordIndexes": [],
                        "Placeholder": ""
                    }
                ],
                "Recipients": [
                    {
                        "RecipientId": "yDSLVUUckpo3nwi3UEnf33kxdJyaybFb",
                        "RecipientType": "INDIVIDUAL",
                        "Description": "",
                        "RoleName": "买房-自然人",
                        "RequireValidation": false,
                        "RequireSign": false,
                        "SignType": 0,
                        "RoutingOrder": -1,
                        "IsPromoter": false
                    },
                    {
                        "RecipientId": "yDSLVUUckpo3nwi1UEnf33kBMNXjdB2c",
                        "RecipientType": "ENTERPRISE",
                        "Description": "",
                        "RoleName": "卖方-菜市场",
                        "RequireValidation": false,
                        "RequireSign": false,
                        "SignType": 0,
                        "RoutingOrder": -1,
                        "IsPromoter": false
                    }
                ],
                "SignComponents": [
                    {
                        "ComponentId": "ComponentId_2",
                        "ComponentType": "SIGN_SEAL",
                        "ComponentName": "企业印章",
                        "ComponentRequired": true,
                        "ComponentRecipientId": "yDSLVUUckpo3nwi1UEnf33kBMNXjdB2c",
                        "FileIndex": 0,
                        "GenerateMode": "",
                        "ComponentWidth": 119,
                        "ComponentHeight": 119,
                        "ComponentPage": 1,
                        "ComponentPosX": 32.640625,
                        "ComponentPosY": 0,
                        "ComponentExtra": "{\"Date\":true,\"isAfterCut\":false,\"PageRanges\":[]}",
                        "ComponentValue": "",
                        "ComponentDateFontSize": 0,
                        "DocumentId": "",
                        "ComponentDescription": "",
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ChannelComponentId": "",
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "RelativeLocation": "",
                        "KeywordIndexes": [],
                        "Placeholder": ""
                    },
                    {
                        "ComponentId": "ComponentId_5",
                        "ComponentType": "SIGN_SIGNATURE",
                        "ComponentName": "个人签名/印章",
                        "ComponentRequired": true,
                        "ComponentRecipientId": "yDSLVUUckpo3nwi3UEnf33kxdJyaybFb",
                        "FileIndex": 0,
                        "GenerateMode": "",
                        "ComponentWidth": 119,
                        "ComponentHeight": 43,
                        "ComponentPage": 1,
                        "ComponentPosX": 397.640625,
                        "ComponentPosY": 14,
                        "ComponentExtra": "{\"Date\":true,\"isAfterCut\":false}",
                        "ComponentValue": "",
                        "ComponentDateFontSize": 0,
                        "DocumentId": "",
                        "ComponentDescription": "",
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ChannelComponentId": "",
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "RelativeLocation": "",
                        "KeywordIndexes": [],
                        "Placeholder": ""
                    },
                    {
                        "ComponentId": "ComponentId_6",
                        "ComponentType": "SIGN_DATE",
                        "ComponentName": "签署日期1",
                        "ComponentRequired": true,
                        "ComponentRecipientId": "yDSLVUUckpo3nwi3UEnf33kxdJyaybFb",
                        "FileIndex": 0,
                        "GenerateMode": "",
                        "ComponentWidth": 119,
                        "ComponentHeight": 20,
                        "ComponentPage": 1,
                        "ComponentPosX": 397.640625,
                        "ComponentPosY": 57,
                        "ComponentExtra": "{\"Format\":\"yyyy年m月d日\",\"Gaps\":\"2,2\",\"FontSize\":12,\"FontAlign\":\"Center\",\"Font\":\"黑体\",\"isAfterCut\":false,\"PageRanges\":[]}",
                        "ComponentValue": "",
                        "ComponentDateFontSize": 0,
                        "DocumentId": "",
                        "ComponentDescription": "",
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ChannelComponentId": "",
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "RelativeLocation": "",
                        "KeywordIndexes": [],
                        "Placeholder": ""
                    },
                    {
                        "ComponentId": "ComponentId_3",
                        "ComponentType": "SIGN_DATE",
                        "ComponentName": "签署日期",
                        "ComponentRequired": true,
                        "ComponentRecipientId": "yDSLVUUckpo3nwi1UEnf33kBMNXjdB2c",
                        "FileIndex": 0,
                        "GenerateMode": "",
                        "ComponentWidth": 119,
                        "ComponentHeight": 20,
                        "ComponentPage": 1,
                        "ComponentPosX": 32.640625,
                        "ComponentPosY": 119,
                        "ComponentExtra": "{\"Format\":\"yyyy年m月d日\",\"Gaps\":\"2,2\",\"FontSize\":12,\"FontAlign\":\"Center\",\"Font\":\"黑体\",\"isAfterCut\":false,\"PageRanges\":[]}",
                        "ComponentValue": "",
                        "ComponentDateFontSize": 0,
                        "DocumentId": "",
                        "ComponentDescription": "",
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "ChannelComponentId": "",
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "RelativeLocation": "",
                        "KeywordIndexes": [],
                        "Placeholder": ""
                    }
                ],
                "TemplateType": 3,
                "IsPromoter": false,
                "Creator": "张三",
                "CreatedOn": 1699259970,
                "PreviewUrl": "",
                "PdfUrl": "",
                "ChannelTemplateId": "",
                "ChannelTemplateName": "",
                "ChannelAutoSave": 0,
                "TemplateVersion": "20231106004",
                "Available": 1
            }
        ],
        "TotalCount": 1,
        "Limit": 20,
        "Offset": 0,
        "RequestId": "8fb09e62-9642-44c8-992b-ddd6e5086293"
    }
}
```

**Example 3: 模板查询接口-通过不存在的模板Id查询模板信息**

1.指定一个不存在的模板ID进行查询

Input: 

```
tccli essbasic DescribeTemplates --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --TemplateIds yDRSRUUgygj6qnwfUuO4zjEwc193c2hH
```

Output: 
```
{
    "Response": {
        "RequestId": "8fb09e62-9642-44c8-992b-ddd6e5086293",
        "Templates": [],
        "Offset": 0,
        "Limit": 20,
        "TotalCount": 0
    }
}
```

