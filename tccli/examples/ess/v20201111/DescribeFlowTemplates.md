**Example 1: 模板查询接口-指定模板Id查询模板信息**

1.指定Filters中的Key通过template-id过滤
2.指定Filter中的Value为yDRS4UUgygqdcjjhUuO4zjEBpXdcsHWX
3.指定Limit为最多返回20条数据

Input: 

```
tccli ess DescribeFlowTemplates --cli-unfold-argument  \
    --Operator.Channel YUFU \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.OpenId  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --Offset 0 \
    --Limit 20 \
    --ApplicationId  \
    --Filters.0.Key template-id \
    --Filters.0.Values yDRS4UUgygqdcjjhUuO4zjEBpXdcsHWX
```

Output: 
```
{
    "Response": {
        "RequestId": "s16951208061xxxx3957",
        "Templates": [
            {
                "AttachmentResourceIds": [],
                "Available": 2,
                "Components": [],
                "CreatedOn": 1693967458,
                "Creator": "测试人",
                "Description": "",
                "DocumentResourceIds": [
                    "yDwJ0UUckpk2079mUxgm9jJ8EZp3aAc0"
                ],
                "FileInfos": [
                    {
                        "CreatedOn": 1693967456,
                        "FileId": "yDwJ0UUckpk2079mUxgm9jJ8EZp3aAc0",
                        "FileName": "test.pdf",
                        "FileSize": 65259
                    }
                ],
                "OrganizationId": "yDxbNUyKQDx3oAUuO4zjEBQGidlGe4hP",
                "PreviewUrl": "",
                "Promoter": {
                    "DeliveryMethod": "EMAIL",
                    "Description": "",
                    "Email": "",
                    "Mobile": "",
                    "RecipientExtra": "",
                    "RecipientId": "yDwJBUUckpk5469kUu9cFsf1x6ZYgfu5",
                    "RecipientType": "PROMOTER",
                    "RequireDelivery": false,
                    "RequireSign": false,
                    "RequireValidation": false,
                    "RoleName": "发起人",
                    "RoutingOrder": 0,
                    "UserId": ""
                },
                "Published": true,
                "Recipients": [
                    {
                        "DeliveryMethod": "EMAIL",
                        "Description": "",
                        "Email": "",
                        "Mobile": "",
                        "RecipientExtra": "{\"RecipientEnterpriseType\":1,\"SameWithPromoter\":true}",
                        "RecipientId": "yDwJ0UUckpk2077lUxgm9jJ9eZgZChJe",
                        "RecipientType": "ENTERPRISE",
                        "RequireDelivery": false,
                        "RequireSign": false,
                        "RequireValidation": false,
                        "RoleName": "张三示例企业",
                        "RoutingOrder": 1,
                        "UserId": ""
                    },
                    {
                        "DeliveryMethod": "EMAIL",
                        "Description": "",
                        "Email": "",
                        "Mobile": "",
                        "RecipientExtra": "{}",
                        "RecipientId": "yDxZzUyKQDKuihUuO4zjEy09jfapyHjn",
                        "RecipientType": "INDIVIDUAL",
                        "RequireDelivery": false,
                        "RequireSign": false,
                        "RequireValidation": false,
                        "RoleName": "乙方",
                        "RoutingOrder": 2,
                        "UserId": ""
                    }
                ],
                "Seals": [],
                "ShareTemplateId": "",
                "SignComponents": [
                    {
                        "ChannelComponentId": "",
                        "ChannelComponentSource": 0,
                        "ComponentDateFontSize": 0,
                        "ComponentExtra": "{\"Date\":true,\"isAfterCut\":false}",
                        "ComponentHeight": 43,
                        "ComponentId": "ComponentId_4",
                        "ComponentName": "个人签名/印章",
                        "ComponentPage": 1,
                        "ComponentPosX": 10.5,
                        "ComponentPosY": 27,
                        "ComponentRecipientId": "yDxZzUyKQDKuihUuO4zjEy09jfapyHjn",
                        "ComponentRequired": true,
                        "ComponentType": "SIGN_SIGNATURE",
                        "ComponentValue": "",
                        "ComponentWidth": 119,
                        "FileIndex": 0,
                        "ForbidMoveAndDelete": false,
                        "GenerateMode": "",
                        "KeywordIndexes": [],
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "LockComponentValue": false,
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "RelativeLocation": "",
                        "IsFormType": false
                    },
                    {
                        "ChannelComponentId": "",
                        "ChannelComponentSource": 0,
                        "ComponentDateFontSize": 0,
                        "ComponentExtra": "{\"Format\":\"yyyy年m月d日\",\"Gaps\":\"2,2\",\"FontSize\":12,\"FontAlign\":\"Center\",\"Font\":\"黑体\",\"isAfterCut\":false}",
                        "ComponentHeight": 20,
                        "ComponentId": "ComponentId_5",
                        "ComponentName": "签署日期",
                        "ComponentPage": 1,
                        "ComponentPosX": 10.5,
                        "ComponentPosY": 70,
                        "ComponentRecipientId": "yDxZzUyKQDKuihUuO4zjEy09jfapyHjn",
                        "ComponentRequired": true,
                        "ComponentType": "SIGN_DATE",
                        "ComponentValue": "",
                        "ComponentWidth": 119,
                        "FileIndex": 0,
                        "ForbidMoveAndDelete": false,
                        "GenerateMode": "",
                        "KeywordIndexes": [],
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "LockComponentValue": false,
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "RelativeLocation": "",
                        "IsFormType": false
                    },
                    {
                        "ChannelComponentId": "",
                        "ChannelComponentSource": 0,
                        "ComponentDateFontSize": 0,
                        "ComponentExtra": "{\"Date\":true,\"isAfterCut\":false,\"PageRanges\":[]}",
                        "ComponentHeight": 119,
                        "ComponentId": "ComponentId_7",
                        "ComponentName": "企业印章",
                        "ComponentPage": 1,
                        "ComponentPosX": 140.5,
                        "ComponentPosY": 27,
                        "ComponentRecipientId": "yDwJ0UUckpk2077lUxgm9jJ9eZgZChJe",
                        "ComponentRequired": true,
                        "ComponentType": "SIGN_SEAL",
                        "ComponentValue": "",
                        "ComponentWidth": 119,
                        "FileIndex": 0,
                        "ForbidMoveAndDelete": false,
                        "GenerateMode": "",
                        "KeywordIndexes": [],
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "LockComponentValue": false,
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "RelativeLocation": "",
                        "IsFormType": false
                    },
                    {
                        "ChannelComponentId": "",
                        "ChannelComponentSource": 0,
                        "ComponentDateFontSize": 0,
                        "ComponentExtra": "{\"Format\":\"yyyy年m月d日\",\"Gaps\":\"2,2\",\"FontSize\":12,\"FontAlign\":\"Center\",\"Font\":\"黑体\",\"isAfterCut\":false}",
                        "ComponentHeight": 20,
                        "ComponentId": "ComponentId_8",
                        "ComponentName": "签署日期1",
                        "ComponentPage": 1,
                        "ComponentPosX": 140.5,
                        "ComponentPosY": 146,
                        "ComponentRecipientId": "yDwJ0UUckpk2077lUxgm9jJ9eZgZChJe",
                        "ComponentRequired": true,
                        "ComponentType": "SIGN_DATE",
                        "ComponentValue": "",
                        "ComponentWidth": 119,
                        "FileIndex": 0,
                        "ForbidMoveAndDelete": false,
                        "GenerateMode": "",
                        "KeywordIndexes": [],
                        "KeywordOrder": "",
                        "KeywordPage": 0,
                        "LockComponentValue": false,
                        "OffsetX": 0,
                        "OffsetY": 0,
                        "RelativeLocation": "",
                        "IsFormType": false
                    }
                ],
                "SignOrder": [
                    -1
                ],
                "Status": 1,
                "TemplateId": "yDRS4UUgygqdcjjhUuO4zjEBpXdcsHWX",
                "TemplateName": "e2eTest-启停用模板_88433",
                "TemplateSeals": [],
                "TemplateType": 3,
                "TemplateVersion": "20230906002"
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 2: 魔板查询接口-通过不存在的模板Id查询模板信息**

1.指定一个不存在的模板ID进行查询

Input: 

```
tccli ess DescribeFlowTemplates --cli-unfold-argument  \
    --Operator.Channel YUFU \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.OpenId  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --Offset 0 \
    --Limit 20 \
    --ApplicationId  \
    --Filters.0.Key template-id \
    --Filters.0.Values yDRS4UUgygqdcjjhUuO4zjEBpXdcsHWw
```

Output: 
```
{
    "Response": {
        "RequestId": "s1695125479063466836",
        "Templates": [],
        "TotalCount": 0
    }
}
```

