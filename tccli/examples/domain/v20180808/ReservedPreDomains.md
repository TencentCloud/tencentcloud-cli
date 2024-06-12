**Example 1: 成功示例**



Input: 

```
tccli domain ReservedPreDomains --cli-unfold-argument  \
    --DomainList aksdwe1.cn aksdwe2.cn \
    --TemplateId tmpl-abxxxxxx
```

Output: 
```
{
    "Response": {
        "SucDomainList": [
            "aksdwe1.cn"
        ],
        "FailDomainList": [
            {
                "Domain": "aksdwe2.cn",
                "FailReason": "域名下架"
            }
        ],
        "RequestId": "xxxx-xxx-xxx-xxxx"
    }
}
```

