**Example 1: 获取模板列表**



Input: 

```
tccli ses ListEmailTemplates --cli-unfold-argument  \
    --Limit 0 \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "TotalCount": 1,
        "TemplatesMetadata": [
            {
                "TemplateID": 10091,
                "CreatedTimestamp": 1607512575,
                "TemplateName": "Test Template",
                "ReviewReason": "通过",
                "TemplateStatus": 0
            }
        ]
    }
}
```

