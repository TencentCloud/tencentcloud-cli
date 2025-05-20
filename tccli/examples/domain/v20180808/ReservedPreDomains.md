**Example 1: 成功示例**



Input: 

```
tccli domain ReservedPreDomains --cli-unfold-argument  \
    --DomainList aksdwe1.cn aksdwe2.cn \
    --TemplateId tmpl-qdpjnfe8 \
    --IsAutoPay 0 \
    --IsBidAutoPay 0
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
        "SucDomains": [
            {
                "Domain": "aksdwe1.cn",
                "BusinessId": "P00117****"
            }
        ],
        "RequestId": "sdwewx-sdowe-***"
    }
}
```

