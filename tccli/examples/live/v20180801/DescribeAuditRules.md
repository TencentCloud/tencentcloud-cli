**Example 1: 请求示例**

请求示例。

Input: 

```
tccli live DescribeAuditRules --cli-unfold-argument  \
    --DomainName 5000.livepush.myqcloud.com \
    --TemplateId 1016 \
    --AppName live \
    --StreamName test1
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "AppName": "live",
                "CreateTime": "2025-09-24T13:23:43+08:00",
                "DomainName": "5000.livepush.myqcloud.com",
                "StreamName": "test1",
                "TemplateId": 1016,
                "UpdateTime": "2025-09-24T13:23:43+08:00"
            }
        ],
        "RequestId": "b4ec9307-0916-4daf-b1b7-74631f7f89fe"
    }
}
```

