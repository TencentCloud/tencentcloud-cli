**Example 1: 查询安全策略配置模板列表**

查询安全策略配置模板列表

Input: 

```
tccli teo DescribeWebSecurityTemplates --cli-unfold-argument  \
    --ZoneIds zone-2bu6nf2gwsax zone-6wkpkd5gzvms
```

Output: 
```
{
    "Response": {
        "RequestId": "e56b198e-e7ca-4fa6-904d-2b81927e5663",
        "TotalCount": 2,
        "SecurityPolicyTemplates": [
            {
                "ZoneId": "zone-2wkpkd5gzvms",
                "TemplateId": "temp-1m9la413",
                "TemplateName": "CC防护模板",
                "BindDomains": [
                    {
                        "Domain": "t.teo-secdev01.top",
                        "ZoneId": "zone-2wkpkd5gzvms",
                        "Status": "online"
                    },
                    {
                        "Domain": "a.teo-secdev02.top",
                        "ZoneId": "zone-9ac5swm0293l",
                        "Status": "fail"
                    }
                ]
            },
            {
                "ZoneId": "zone-8bu6nf2gwsax",
                "TemplateId": "temp-ws139la4",
                "TemplateName": "Bot防护模板",
                "BindDomains": [
                    {
                        "Domain": "a.teo-secdev03.top",
                        "ZoneId": "zone-8bu6nf2gwsax",
                        "Status": "process"
                    }
                ]
            }
        ]
    }
}
```

